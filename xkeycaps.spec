Summary:	xkeycaps - a keymap editor for the X window system
Summary(pl):	xkeycaps - edytor mapy klawiatury dla X window
Name:		xkeycaps
Version:	2.44
Release:	1
Copyright:	BSD
Group:		X11/Applications
Source0:	http://www.jwz.org/xkeycaps/%{name}-%{version}.tar.Z
Source1:	xkeycaps.wmconfig
URL:		http://www.jwz.org/xkeycaps/
BuildPrereq:	XFree86-devel
Buildroot:	/tmp/%{name}-%{version}-root

%description
xkeycaps is a graphical front-end to xmodmap.It opens a window that looks
like a keyboard; moving the mouse over a key shows what KeySyms and Modifier
bits that key generates. Clicking on a key simulates KeyPress/KeyRelease
events on the window of your choice. It is possible to change the KeySyms
and Modifiers generated by a key through a mouse-based interface. This
program can also write an input file for xmodmap to recreate your changes in
future sessions.

%description -l pl
xkeycaps jest graficzn� nak�adk� na xmodmap. xkeycaps otwiera okno, kt�re
wygl�da jak klawiatura; przesuwaj�c mysz� ponad klawiszami uzyskujemy
informacj� na temat KeySyms oraz bit�w Modifier jakie ten klawisz generuje.
Klikni�cie na klawiszu symuluje zdarzenia KeyPress/KeyRelease dla okna, kt�re
wybierzesz. Mo�na zmieni� KeySyms i Modifiers wygenerowane przez klawisz przy
u�yciu bazuj�cego na myszy interfejsu. Ten program mo�e tak�e zapisywa� plik
konfiguracyjny dla xmodmapa.

%prep
%setup -q

%build
xmkmf -a
make DEFAULT_KBD_NAME="L101" CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make install DESTDIR=$RPM_BUILD_ROOT
make install.man DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/xkeycaps

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man1/* \
	README defining.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
/etc/X11/wmconfig/xkeycaps
%attr(755,root,root) /usr/X11R6/bin/xkeycaps
/usr/X11R6/man/man1/*

%changelog
* Mon Jan 11 1999 Arkadiusz Mi�kiewicz <misiek@misiek.eu.org>
- added pl translations

* Thu Sep  8 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.43-1]
- updated URL to http://www.jwz.org/xkeycaps/,
- updated base Source Url to http://www.jwz.org/xkeycaps/

* Sat May  3 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.42-1]
- Copyright statment changed to BSD,
- added %clean section,
- added -q %setup parameter,
- added URL,
- added using $RPM_OPT_FLAGS on compile time,
- removed paching default kbd name (now directly passed as make parameter),
- rewrited Summary and %description,
- removed Packager field from spec (if you want recompile package and
  redistribute this package later put this in your private .rpmrc). 
- changed to regular url,
- added %%{version} to Source url,
- added using %%{name} macro in Buildroot and Source fields,
- added %defattr and %attr macros in %files (allows building package from
  non-root account); %defattr requires rpm >= 2.4.99 on rebuild.

* Fri Aug 22 1997 John A. Martin <jam@jamux.com>
  [2.38-1]
- not commented.

* Fri Jan 17 1997 ??? <root@imp.redhat.com>
  [2.32-1]
- previouse not commented release in rpm package (powercd 4.2).
