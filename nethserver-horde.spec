Summary: NethServer configuration for Horde groupware
Name: nethserver-horde
Version: 0.0.1
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: nethserver-devtools

Requires: nethserver-httpd, nethserver-mysql, nethserver-mail-server
Requires: php-mysql php-pecl-imagick aspell-en
Requires: php-horde-horde php-horde-ingo php-horde-kronolith php-horde-imp php-horde-turba

%description
NethServer configuration for Horde groupware

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{version}-%{release}-filelist

%files -f %{version}-%{release}-filelist
%defattr(-,root,root)
%config(noreplace) %attr(0660, apache, apache) /etc/horde/imp/conf.php
%config(noreplace) %attr(0660, apache, apache) /etc/horde/ingo/conf.php
%config(noreplace) %attr(0660, apache, apache) /etc/horde/kronolith/conf.php
%config(noreplace) %attr(0660, apache, apache) /etc/horde/nag/conf.php
%config(noreplace) %attr(0660, apache, apache) /etc/horde/turba/conf.php
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
