Summary:	A vr micro-Kernel
Name:		Maverik
Version:	5.1
Release:	1
Copyright:	GPL
Group:		Development/Libraries
Vendor:		Advanced Interfaces Group
Source0:	ftp://aig.cs.man.ac.uk/pub/aig/Maverik/%{name}-%{version}.tar.gz
Source1:	ftp://aig.cs.man.ac.uk/pub/aig/Maverik/%{name}Demos-%{version}.tar.gz
Source2:	Maverik-5.1-1.rpm-extras.tgz
Patch:		Maverik-5.1-1-linux.patch
URL:		http://hegel.cs.man.ac.uk/systems/Maverik/
Buildroot:	/tmp/%{name}-%{version}-root

%description
GNU Maverik is a framework and library for developing VR applications (it is
not an end-user application). It provides optimised management of graphics
and peripheral driving capabilities for a single user. A novel feature of
GNU MAVERIK is its direct use of the applications own data structures. This
means significant performance benefits can be achieved through application
specific optmisations.

Under GNU/Linux, GNU MAVERIK can use 3DFx VOODOO cards in pairs to drive stereo
headsets. See the web pages (http://aig.cs.man.ac.uk) for more detail, and
examples of applications written using GNU MAVERIK.


%package demos
Summary:	Maverik Demos
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description demos
Maverik demos. AIGLab, EscapeCity and LegibleCity.

%prep
%setup -q
%setup -q -T -D -b 1
%setup -q -T -D -a 2
%patch -p 1

for i in doc/MFS/man3/*; do
	if [ -L $i ]; then
		echo ".so `ls -l $i | awk '{print $11}'; rm -f $i`" > $i
	fi
done

%build
#export OS_TYPE="Linux"
#export MAV_HOME=`pwd`
#source setup_env
( ./setup --VRML97 --MESAPATH=/usr/X11R6 ; make ; make clean)

#export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${RPM_BUILD_DIR}/Maverik-3.0b4/lib/Linux
#(cd examples; make)

# dont make examples they need incl and lib paths setting, and those
# are different between our build and the installed build. Fix that
# one day. For now a useful test for the user to try.
#(cd examples ; make ; make clean)

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_prefix}/src/examples/%{name}-%{version}
install -d $RPM_BUILD_ROOT/{%{_libdir},%{_includedir}/Maverik,%{_mandir}/man3}

install -s lib/*.so $RPM_BUILD_ROOT/%{_libdir}/
install incl/* $RPM_BUILD_ROOT/%{_includedir}/Maverik/

cp -a examples/* $RPM_BUILD_ROOT/%{_prefix}/src/examples/%{name}-%{version}/
cp -a demos $RPM_BUILD_ROOT/%{_prefix}/src/examples/%{name}-%{version}/

find $RPM_BUILD_ROOT/%{_prefix}/src/examples/%{name}-%{version} -type f \
	-exec strip --strip-unneeded {} \; || :

# manual
install doc/MFS/man3/* $RPM_BUILD_ROOT/%{_mandir}/man3/



gzip -9nf $RPM_BUILD_ROOT/%{_mandir}/man3/* README.rpm README FAQ VERSIONS \
	doc/MPG/ps/mpg.ps doc/MFS/ps/mfs.ps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc {README.rpm,README,FAQ,VERSIONS}.gz
%doc doc/MPG/ps/mpg.ps.gz doc/MFS/ps/mfs.ps.gz doc/MFS/html
%attr(755, root, root) %{_libdir}/*.so
%dir %{_includedir}/Maverik
%attr(644, root, root) %{_includedir}/Maverik/*
%attr(644, root, root) %{_mandir}/man3/*
%dir %{_prefix}/src/examples/%{name}-%{version}
%{_prefix}/src/examples/%{name}-%{version}/MPG
%{_prefix}/src/examples/%{name}-%{version}/kernel
%{_prefix}/src/examples/%{name}-%{version}/misc
%{_prefix}/src/examples/%{name}-%{version}/Makefile
%{_prefix}/src/examples/%{name}-%{version}/README

%files demos
%defattr(-,root,root,755)
%{_prefix}/src/examples/%{name}-%{version}/demos
