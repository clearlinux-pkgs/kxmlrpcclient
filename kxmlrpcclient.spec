#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kxmlrpcclient
Version  : 5.87.0
Release  : 38
URL      : https://download.kde.org/stable/frameworks/5.87/portingAids/kxmlrpcclient-5.87.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.87/portingAids/kxmlrpcclient-5.87.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.87/portingAids/kxmlrpcclient-5.87.0.tar.xz.sig
Summary  : XML-RPC client library for KDE
Group    : Development/Tools
License  : BSD-2-Clause LGPL-2.0
Requires: kxmlrpcclient-data = %{version}-%{release}
Requires: kxmlrpcclient-lib = %{version}-%{release}
Requires: kxmlrpcclient-license = %{version}-%{release}
Requires: kxmlrpcclient-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : qtbase-dev

%description
# KXmlRpcClient
XML-RPC client
## Introduction
This library contains simple XML-RPC Client support. It is a complete
client and is quite easy to use. Only one interface is exposed to the
world, kxmlrpcclient/client.h and of that interface, you only need to
use 3 methods: setUrl, setUserAgent and call.

%package data
Summary: data components for the kxmlrpcclient package.
Group: Data

%description data
data components for the kxmlrpcclient package.


%package dev
Summary: dev components for the kxmlrpcclient package.
Group: Development
Requires: kxmlrpcclient-lib = %{version}-%{release}
Requires: kxmlrpcclient-data = %{version}-%{release}
Provides: kxmlrpcclient-devel = %{version}-%{release}
Requires: kxmlrpcclient = %{version}-%{release}

%description dev
dev components for the kxmlrpcclient package.


%package lib
Summary: lib components for the kxmlrpcclient package.
Group: Libraries
Requires: kxmlrpcclient-data = %{version}-%{release}
Requires: kxmlrpcclient-license = %{version}-%{release}

%description lib
lib components for the kxmlrpcclient package.


%package license
Summary: license components for the kxmlrpcclient package.
Group: Default

%description license
license components for the kxmlrpcclient package.


%package locales
Summary: locales components for the kxmlrpcclient package.
Group: Default

%description locales
locales components for the kxmlrpcclient package.


%prep
%setup -q -n kxmlrpcclient-5.87.0
cd %{_builddir}/kxmlrpcclient-5.87.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634485177
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1634485177
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kxmlrpcclient
cp %{_builddir}/kxmlrpcclient-5.87.0/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kxmlrpcclient/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
cp %{_builddir}/kxmlrpcclient-5.87.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kxmlrpcclient/20079e8f79713dce80ab09774505773c926afa2a
pushd clr-build
%make_install
popd
%find_lang libkxmlrpcclient5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kxmlrpcclient.categories
/usr/share/qlogging-categories5/kxmlrpcclient.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KXmlRpcClient/KXmlRpcClient/Client
/usr/include/KF5/KXmlRpcClient/kxmlrpcclient/client.h
/usr/include/KF5/KXmlRpcClient/kxmlrpcclient/kxmlrpcclient_export.h
/usr/include/KF5/kxmlrpcclient_version.h
/usr/lib64/cmake/KF5XmlRpcClient/KF5XmlRpcClientConfig.cmake
/usr/lib64/cmake/KF5XmlRpcClient/KF5XmlRpcClientConfigVersion.cmake
/usr/lib64/cmake/KF5XmlRpcClient/KF5XmlRpcClientTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5XmlRpcClient/KF5XmlRpcClientTargets.cmake
/usr/lib64/libKF5XmlRpcClient.so
/usr/lib64/qt5/mkspecs/modules/qt_KXmlRpcClient.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5XmlRpcClient.so.5
/usr/lib64/libKF5XmlRpcClient.so.5.87.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kxmlrpcclient/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kxmlrpcclient/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e

%files locales -f libkxmlrpcclient5.lang
%defattr(-,root,root,-)

