Summary:	A vr micro-Kernel
Name:		Maverik
Version:	5.0
Release:	1
Copyright:	GPL
Group:		Developments/Libraries
Vendor:		Advanced Interfaces Group
Source0:	ftp://aig.cs.man.ac.uk/pub/aig/Maverik/%{name}-%{version}.tar.gz
Source1:	MaverikDemos-5.0.tar.gz
Source2:	Maverik-4.3-1.rpm-extras.tgz
Patch:		Maverik-4.3.1-linux.patch
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

Examples
----------
To run the examples, you will need to set the LD_LIBRARY_PATH to pick up
the MAVERIK library. i.e.

export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:%{_libdir}/Maverik/lib

%package demos
Summary:	Maverik Demos
Group:		Developments/libraries
Requires:	%{name} = %{version}

%description demos
Maverik demos. AIGLab, EscapeCity and LegibleCity.

%prep
%setup -q
%setup -q -T -D -b 1
%setup -q -T -D -a 2
%patch -p 1

%build
echo "building "
#export OS_TYPE="Linux"
#export MAV_HOME=`pwd`
#source setup_env
( ./setup --VRML97 --TIFF ; make ; make clean)

#export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${RPM_BUILD_DIR}/Maverik-3.0b4/lib/Linux
#(cd examples; make)

# dont make examples they need incl and lib paths setting, and those
# are different between our build and the installed build. Fix that
# one day. For now a useful test for the user to try.
#(cd examples ; make ; make clean)

%install
echo "install"

install -d %{_libdir}/Maverik/Maverik-4.3/lib
(cd lib; cp -pr * %{_libdir}/Maverik/Maverik-4.3/lib)

# include
install -d %{_libdir}/Maverik/Maverik-4.3/incl
cp -pr incl %{_libdir}/Maverik/Maverik-4.3

# examples
cp -pr examples %{_libdir}/Maverik/Maverik-4.3

# bin
install -d %{_libdir}/Maverik/Maverik-4.3/bin
install set_mav_vsn %{_libdir}/Maverik/Maverik-4.3/bin

# src
install -d %{_libdir}/Maverik/Maverik-4.3/src
cp -pr src %{_libdir}/Maverik/Maverik-4.3

# demos (stub)
install -d %{_libdir}/Maverik/Maverik-4.3/demos
cp -pr demos %{_libdir}/Maverik/Maverik-4.3

# misc for remake
install setup %{_libdir}/Maverik/Maverik-4.3/setup
install Makefile %{_libdir}/Maverik/Maverik-4.3/Makefile

# manual
install -d %{_libdir}/Maverik/Maverik-4.3/man/man3
#install Maverik.3 %{_libdir}/Maverik/Maverik-4.3/man/man3
cp -pr doc/MFS/man3 %{_libdir}/Maverik/Maverik-4.3/man/
install  set_mav_vsn.3 %{_libdir}/Maverik/Maverik-4.3/man/man3


%post 
%{_libdir}/Maverik/Maverik-4.3/bin/set_mav_vsn -i 4.3
echo ""
echo "Examples"
echo "----------"
echo "To run the examples, you will need to set the LD_LIBRARY_PATH to pick up"
echo "the MAVERIK library. i.e. (using the bash shell)"
echo ""
echo "      export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:%{_libdir}/Maverik/lib"
echo ""
%preun
%{_libdir}/Maverik/Maverik-4.3/bin/set_mav_vsn -e 4.3
cp %{_libdir}/Maverik/Maverik-4.3/bin/set_mav_vsn /tmp

$postun
if [ $1 != 0 ] ;
then
if [ ! -e %{_libdir}/Maverik/incl ];
then
	/tmp/set_mav_vsn -i newest
fi
rm -f /tmp/set_mav_vsn
fi

%files
#%docdir %{_libdir}/Maverik/Maverik-4.3/man
%doc README.rpm README INSTALL FAQ VERSIONS COPYING doc/MPG/ps/mpg.ps

%dir %{_libdir}/Maverik/Maverik-4.3
%{_libdir}/Maverik/Maverik-4.3/bin
%{_libdir}/Maverik/Maverik-4.3/lib
%{_libdir}/Maverik/Maverik-4.3/incl
%{_libdir}/Maverik/Maverik-4.3/man
%{_libdir}/Maverik/Maverik-4.3/examples
%dir %{_libdir}/Maverik/Maverik-4.3/demos
%{_libdir}/Maverik/Maverik-4.3/demos/Makefile
%{_libdir}/Maverik/Maverik-4.3/demos/README

%files demos
%{_libdir}/Maverik/Maverik-4.3/demos/AIGLab
%{_libdir}/Maverik/Maverik-4.3/demos/EscapeCity
%{_libdir}/Maverik/Maverik-4.3/demos/LegibleCity
