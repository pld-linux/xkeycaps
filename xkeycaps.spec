Summary:	xkeycaps - a keymap editor for the X Window System
Summary(pl):	xkeycaps - edytor mapy klawiatury dla X Window System
Name:		xkeycaps
Version:	2.46
Release:	2
License:	BSD
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://www.jwz.org/xkeycaps/%{name}-%{version}.tar.Z
Source1:	%{name}.desktop
URL:		http://www.jwz.org/xkeycaps/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
xkeycaps is a graphical front-end to xmodmap.It opens a window that
looks like a keyboard; moving the mouse over a key shows what KeySyms
and Modifier bits that key generates. Clicking on a key simulates
KeyPress/KeyRelease events on the window of your choice. It is
possible to change the KeySyms and Modifiers generated by a key
through a mouse-based interface. This program can also write an input
file for xmodmap to recreate your changes in future sessions.

%description -l pl
xkeycaps jest graficzn� nak�adk� na xmodmap. xkeycaps otwiera okno,
kt�re wygl�da jak klawiatura; przesuwaj�c mysz� ponad klawiszami
uzyskujemy informacj� na temat KeySyms oraz bit�w Modifier jakie ten
klawisz generuje. Klikni�cie na klawiszu symuluje zdarzenia
KeyPress/KeyRelease dla okna, kt�re wybierzesz. Mo�na zmieni� KeySyms
i Modifiers wygenerowane przez klawisz przy u�yciu bazuj�cego na myszy
interfejsu. Ten program mo�e tak�e zapisywa� plik konfiguracyjny dla
xmodmapa.

%prep
%setup -q

%build
xmkmf -a
%{__make} DEFAULT_KBD_NAME="L101" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
        MANDIR=%{_mandir}/man1 \
        BINDIR=%{_bindir} 

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities

gzip -9nf README defining.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_applnkdir}/Utilities/xkeycaps.desktop
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
