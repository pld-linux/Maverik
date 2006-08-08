Summary:	A VR micro-Kernel
Summary(pl):	Mikroj±dro VR
Name:		Maverik
Version:	6.2
Release:	1
License:	GPL
Group:		Development/Libraries
#Source0Download: http://aig.cs.man.ac.uk/maverik/download.php
Source0:	http://aig.cs.man.ac.uk/maverik/maverik-%{version}.tar.gz
# Source0-md5:	b15b290f5a0c8c6c21a2f5c47ad8be37
Source1:	http://aig.cs.man.ac.uk/maverik/maverik-demos-%{version}.tar.gz
# Source1-md5:	cb31b5e61c6c390edb564c61a96e3eaf
Source2:	%{name}-5.1-1.rpm-extras.tgz
# Source2-md5:	c6bd7b4fa670c32a545939d080862803
Patch0:		%{name}-5.1-1-linux.patch
URL:		http://aig.cs.man.ac.uk/maverik/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Maverik is a framework and library for developing VR applications
(it is not an end-user application). It provides optimised management
of graphics and peripheral driving capabilities for a single user. A
novel feature of GNU MAVERIK is its direct use of the applications own
data structures. This means significant performance benefits can be
achieved through application specific optmisations.

%description -l pl
GNU Maverik jest ¶rodowiskiem przeznaczonym do rozwoju aplikacji VR.
Dostarcza zoptymalizowane zarz±dzanie grafik± itp. Nowo¶ci± w GNU
Mavericu jest bezpo¶rednie u¿ywanie struktur danych aplikacji przez co
mo¿liwe jest znaczne przyspieszenie dzia³ania przez optymalizacjê
aplikacji u¿ywaj±cej Maverika.

%package demos
Summary:	Maverik Demos
Summary(pl):	Dema Maverika
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description demos
Maverik demos. AIGLab, EscapeCity and LegibleCity.

%description demos -l pl
Dema Maverika: AIGLab, EscapeCity i LegibleCity.

%prep
%setup -q -n maverik-%{version} -b1 -a2
%patch0 -p 1

for i in doc/MFS/man3/*; do
	if [ -L $i ]; then
		echo ".so `ls -l $i | awk '{print $11}'; rm -f $i`" > $i
	fi
done

%build
#export OS_TYPE="Linux"
#export MAV_HOME=`pwd`
#source setup_env
./setup \
	--VRML97 \
	--MESAPATH=%{_prefix}/X11R6
%{__make}
%{__make} clean

#export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${RPM_BUILD_DIR}/Maverik-3.0b4/lib/Linux
#%{__make} -C examples

# dont make examples they need incl and lib paths setting, and those
# are different between our build and the installed build. Fix that
# one day. For now a useful test for the user to try.
#%{__make} -C examples ; %{__make} -C examples clean

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/Maverik,%{_mandir}/man3}

install lib/*.so $RPM_BUILD_ROOT%{_libdir}
install incl/* $RPM_BUILD_ROOT%{_includedir}/Maverik

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# manual
install doc/MFS/man3/* $RPM_BUILD_ROOT%{_mandir}/man3/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rpm README FAQ VERSIONS
%doc doc/MPG/ps/mpg.ps doc/MFS/ps/mfs.ps doc/MFS/html
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/Maverik
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/MPG
%{_examplesdir}/%{name}-%{version}/kernel
%{_examplesdir}/%{name}-%{version}/misc
%{_examplesdir}/%{name}-%{version}/Makefile
%{_examplesdir}/%{name}-%{version}/README

%files demos
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}/demos
