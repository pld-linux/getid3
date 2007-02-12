Summary:	getID3() - The PHP media file parser
Summary(pl.UTF-8):   getID3() - parser plików multimedialnych dla PHP
Name:		getid3
Version:	1.7.5
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/getid3/%{name}-%{version}.zip
# Source0-md5:	defd162488ca015c2392e10d9d1fef2a
URL:		http://getid3.sourceforge.net/
Requires:	php-common >= 3:4.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/php/%{name}

%description
getID3() is a PHP4 script that extracts useful information from MP3s &
other multimedia file formats.

%description -l pl.UTF-8
getID3() to skrypt PHP4 wyciągający przydatne informacje z MP3 i
innych formatów plików multimedialnych.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}
cp -a getid3/*.php $RPM_BUILD_ROOT%{_appdir}
cp -a demos/demo.*.php $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog.txt dependencies.txt readme.txt structure.txt
%{_appdir}
%{_examplesdir}/*
