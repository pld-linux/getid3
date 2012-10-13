%define		release_date 20111213
Summary:	getID3() - The PHP media file parser
Summary(pl.UTF-8):	getID3() - parser plików multimedialnych dla PHP
Name:		getid3
Version:	1.9.3
Release:	1
License:	GPL
Group:		Applications
Source0:	http://downloads.sourceforge.net/getid3/%{name}-%{version}-%{release_date}.zip
# Source0-md5:	00990e23f4035c29974d025cc5f3eeb7
URL:		http://getid3.sourceforge.net/
BuildRequires:	unzip
Requires:	php(core) >= 5.3.0
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
%doc changelog.txt dependencies.txt readme.txt structure.txt license.commercial.txt
%{_appdir}
%{_examplesdir}/*
