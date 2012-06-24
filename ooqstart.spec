Summary:	OpenOffice QuickStarter applet
Summary(pl):	Aplet szybkiego startu OpenOffice
Name:		ooqstart
Version:	0.8.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tgz
# Source0-md5:	f3c15a29e8bbd7780972e69f11f564a4
Patch0:		%{name}-opt.patch
URL:		http://ooqstart.sourceforge.net/
BuildRequires:	gnome-core-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
This applet provides a quick launcher for Open Office 641C+ or Star
Office 6.0+. It attempts to mimic the functionality provided by the
quickstarter tray icon on the other operating system supported by Open
Office.

The program attempts to keep a background process alive at all times,
even if that process is terminated by the user. The four main
applications: Writer, Calc, Draw, and Impress can be launched directly
from the context menu of the applet.

%description -l pl
Aplet s�u��cy do szybkiego uruchamiania aplikacji pakiet�w OpenOffice
641C+ i StarOffice 6.0+. W za�o�eniu ma dostarcza� podobnych funkcji
co ikonki w "menu tray" w innych systemach operacyjnych, w kt�rych
dzia�a pakiet OpenOffice.

Program podtrzymuje procesy OpenOffice dzia�aj�ce w tle nawet wtedy,
gdy proces jest zako�czony przez u�ytkownika. Cztery aplikacje:
Writer, Calc, Draw i Impress mog� by� uruchomione bezpo�rednio z menu
kontekstowego apletu.

%prep
%setup -q
%patch -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install-gnome \
	ROOT=$RPM_BUILD_ROOT \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	ETC=$RPM_BUILD_ROOT%{_sysconfdir}

%find_lang ooqstart_applet --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ooqstart_applet.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/CORBA/servers/*
%{_datadir}/applets/Utility/*
%{_pixmapsdir}/*
