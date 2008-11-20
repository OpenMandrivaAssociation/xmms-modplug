%define	name	xmms-modplug
%define oname modplugxmms
%define version 2.05
%define release %mkrel 9

Name:		%{name}
Summary:	Modplug Plugin for XMMS
Version:	%{version}
Release:	%{release}
License:	Public Domain
Group:		Sound
URL:		http://modplug-xmms.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/modplug-xmms/%oname-%{version}.tar.bz2
Patch: modplugxmms-2.05-fix-includes.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}
Requires:	xmms >= 1.0.0
Provides: modplug-xmms
Obsoletes: modplug-xmms
BuildRequires:	libxmms-devel
BuildRequires:  libmodplug-devel >= 1:0.7

%description
Modplug-XMMS is a fully featured, complete input plugin for XMMS which
plays mod-like music formats. It is based on the mod rendering code from
ModPlug, a popular windows mod player written by Olivier Lapicque,
found at http://www.modplug.com

%prep
%setup -q -n %oname-%{version}
%patch -p1

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/xmms/Input/libmodplugxmms.la
install -d -m 755 $RPM_BUILD_ROOT%{_menudir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO
%_bindir/modplugplay
%{_libdir}/xmms/Input/libmodplugxmms.so


