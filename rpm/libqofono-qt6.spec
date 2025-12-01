Name:       libqofono-qt6

Summary:    A library of Qt 6 bindings for ofono
Version:    0.124
Release:    1
License:    LGPLv2
URL:        https://github.com/sailfishos/libqofono
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6Test)

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
This package contains Qt bindings for ofono cellular service
interfaces.

%package declarative
Summary:    Declarative plugin for libqofono
Requires:   %{name} = %{version}-%{release}
Requires:   %{name} = %{version}

%description declarative
This package contains declarative plugin for libofono.

%package devel
Summary:    Development files for ofono Qt bindings
Requires:   %{name} = %{version}-%{release}
Requires:   %{name} = %{version}

%description devel
This package contains the development header files for the ofono Qt bindings.

%package tests
Summary:    qml test app for the ofono Qt bindings
Requires:   %{name} = %{version}-%{release}
Requires:   blts-tools
Requires:   phonesim
Requires:   mce-tools

%description tests
This package contains qml test for ofono Qt bindings.

%package examples
Summary:    Examples for libqofono
Requires:   %{name} = %{version}-%{release}
Requires:   %{name} = %{version}
Requires:   %{name}-declarative = %{version}

%description examples
This package contains examples for declarative plugin for libofono.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_LIBDIR=%{_libdir} -DLIBQOFONO_VERSION=$(sed 's/+.*//' <<<"%{version}") -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/%{name}.so.*
%license COPYING

%files declarative
%defattr(-,root,root,-)
%{_libdir}/qt6/qml/QOfono

%files devel
%defattr(-,root,root,-)
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/qofono-qt6.pc
%{_includedir}/qofono-qt6/*.h
%{_includedir}/qofono-qt6/dbus/ofono*.xml

%files tests
%defattr(-,root,root,-)
/opt/tests/%{name}/*

%files examples
%defattr(-,root,root,-)
/opt/examples/%{name}
