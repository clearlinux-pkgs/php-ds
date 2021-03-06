#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-ds
Version  : 1.3.0
Release  : 10
URL      : https://pecl.php.net/get/ds-1.3.0.tgz
Source0  : https://pecl.php.net/get/ds-1.3.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: php-ds-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : pcre2-dev

%description
No detailed description available

%package lib
Summary: lib components for the php-ds package.
Group: Libraries

%description lib
lib components for the php-ds package.


%prep
%setup -q -n ds-1.3.0
cd %{_builddir}/ds-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
autoupdate
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20200930/ds.so
