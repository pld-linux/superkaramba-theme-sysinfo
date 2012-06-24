
%define		theme	sysinfo

Summary:	superkaramba - Stylus Sysinfo theme
Summary(pl.UTF-8):	superkaramba - motyw Stylus Sysinfo
Name:		superkaramba-theme-%{theme}
Version:	0.1
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/22618-%{theme}.tar.gz
# Source0-md5:	caaf97a549b319790d8e3fcb1ba2f5e5
URL:		http://www.kde-look.org/content/show.php?content=22618
BuildRequires:	sed >= 4.0
Requires:	perl-libnet
Requires:	superkaramba >= 0.36
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_sysinfodir 	%{_datadir}/themes/superkaramba/sysinfo

%description
kstatus theme for superkaramba. Features :
 - User@hostname Output
 - Kernel Version Output
 - KDE Version Output
 - CPU Usage Stats with progress bar indicator
 - CPU Clockspeed / Cache Detection
 - RAM / Swapfile Usage with progress bar indicator
 - Hard Disk Drive Monitor
 - Network Traffic Monitor
 - IP Address Output
 - Uptime / Time / Date Output

%description -l pl.UTF-8
Motyw Stylus Theme dla superkaramby. Wyświetlane informacje :
 - User@hostname
 - Wersja jądra
 - Wersja KDE
 - Obciążenie procesora
 - Częstotliwość / cache procesora
 - Wykorzystanie pamięci RAM i pliku wymiany
 - Monitor dysków
 - Monitor sieci
 - Uptime, czas, data
 - Powiadamianie o nowej poczcie

%prep
%setup -q -n %{theme}

# theme modified to use proper path (mail_pop3.pl) and prepare for email clients
%{__sed} -i 's,/path/to,%{_sysinfodir}/scripts,g' sysinfo.theme
cp sysinfo.theme sysinfo_kmail.theme
%{__sed} -i 's/kmail/mozilla-thunderbird/g' sysinfo.theme
mv sysinfo.theme sysinfo_thunderbird.theme

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysinfodir}{,/images,/scripts}

install *.theme $RPM_BUILD_ROOT%{_sysinfodir}
install images/*.png $RPM_BUILD_ROOT%{_sysinfodir}/images
install scripts/*.pl $RPM_BUILD_ROOT%{_sysinfodir}/scripts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysinfodir}
%{_sysinfodir}/*.theme
%{_sysinfodir}/images
%attr(755,root,root) %{_sysinfodir}/scripts
