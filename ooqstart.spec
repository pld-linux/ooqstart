
Summary:	OpenOffice QuickStarter applet
Summary(pl):	Aplet szybkiego startu OpenOffice
Name:		ooqstart
Version:	0.8.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
URL:		http://%{name}.sourceforge.net/
BuildRequires:	gnome-core-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	gnome-core
Provides:	%{name}

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
Aplet s³u¿±cy do szybkiego uruchamiania aplikacji pakietów OpenOffice 
641C+ i StarOffice 6.0+. W za³o¿eniu ma dostarczaæ podobnych funkcji
co ikonki w "menu tray" w innych systemach operacyjnych, w których
dzia³a pakiet OpenOffice.

Program podtrzymuje procesy OpenOffice dzia³aj±ce w tle nawet wtedy,
gdy proces jest zakoñczony przez u¿ytkownika. Cztery aplikacje: Writer,
Calc, Draw i Impress moga byæ uruchomione bezposrednio z menu kontekstowego
apletu. 


%define		_sysconfdir	/etc/X11/GNOME

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} ROOT=$RPM_BUILD_ROOT PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	ETC=$RPM_BUILD_ROOT%{_sysconfdir} install-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/CORBA/servers/*
%{_datadir}/applets/Utility/*
%{_datadir}/pixmaps/*
%{_datadir}/gnome/help/ooqstart_applet/C/*
