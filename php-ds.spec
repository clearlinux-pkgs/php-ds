#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-ds
Version  : 1.4.0
Release  : 44
URL      : https://pecl.php.net/get/ds-1.4.0.tgz
Source0  : https://pecl.php.net/get/ds-1.4.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: php-ds-lib = %{version}-%{release}
Requires: php-ds-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : pcre2-dev

%description
No detailed description available

%package lib
Summary: lib components for the php-ds package.
Group: Libraries
Requires: php-ds-license = %{version}-%{release}

%description lib
lib components for the php-ds package.


%package license
Summary: license components for the php-ds package.
Group: Default

%description license
license components for the php-ds package.


%prep
%setup -q -n ds-1.4.0
cd %{_builddir}/ds-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-ds
cp %{_builddir}/ds-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-ds/deade8804defd51c80d108c07d80095a4e4344ba
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20220829/ds.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-ds/deade8804defd51c80d108c07d80095a4e4344ba
