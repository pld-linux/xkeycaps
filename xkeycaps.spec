Summary:	xkeycaps - a keymap editor for the X Window System
Summary(es):	Un editor de mapas de teclado para X
Summary(pl):	xkeycaps - edytor mapy klawiatury dla X Window System
Summary(pt_BR):	Um editor de mapas de teclado para o X
Name:		xkeycaps
Version:	2.46
Release:	5
License:	BSD
Group:		X11/Applications
Source0:	http://www.jwz.org/xkeycaps/%{name}-%{version}.tar.Z
# Source0-md5:	6792f828db6538f44f7696a8783b44ac
Source1:	%{name}.desktop
Source2:	%{name}.png
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

%description -l es
xkeycaps es una interfaz gr�fica para xmodmap. Abre una ventana que
parece un teclado; mover el rat�n sobre una tecla muestra las KeySyms
y los bits modificadores que la contrase�a genera. Si se hace click en
una tecla simula eventos KeyPress/KeyRelease en la ventana que se
escoja. Se pueden cambiar los KeySyms y bits modificadores generados
por una contrase�a a trav�s de una interfaz que se basa en el rat�n.
Este programa tambi�n puede escribir un archivo para que el xmodmap lo
cargue las pr�ximas veces que se use X. Para obtener m�s detalles se
debe consultar la p�gina del manual.

%description -l pl
xkeycaps jest graficzn� nak�adk� na xmodmap. xkeycaps otwiera okno,
kt�re wygl�da jak klawiatura; przesuwaj�c mysz� ponad klawiszami
uzyskujemy informacj� na temat KeySyms oraz bit�w Modifier jakie ten
klawisz generuje. Klikni�cie na klawiszu symuluje zdarzenia
KeyPress/KeyRelease dla okna, kt�re wybierzesz. Mo�na zmieni� KeySyms
i Modifiers wygenerowane przez klawisz przy u�yciu bazuj�cego na myszy
interfejsu. Ten program mo�e tak�e zapisywa� plik konfiguracyjny dla
xmodmapa.

%description -l pt_BR
xkeycaps � uma interface gr�fica para o xmodmap. Ele abre uma janela
que parece um teclado; mover o mouse sobre uma tecla mostra as KeySyms
e os bits modificadores que a chave gera. Clicando em uma tecla simula
eventos KeyPress/KeyRelease na janela de sua escolha. � poss�vel mudar
os KeySyms e bits modificadores gerados por uma chave atrav�s de uma
interface baseada em mouse. Esse programa pode tamb�m escrever um
arquivo para o xmodmap carregar nas pr�ximas vezes que voc� usar o X.
Veja a p�gina do manual para maiores detalhes.

%prep
%setup -q

%build
xmkmf -a
%{__make} DEFAULT_KBD_NAME="L101" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Settings,%{_pixmapsdir}}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
        MANDIR=%{_mandir}/man1 \
        BINDIR=%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README defining.txt
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Settings/xkeycaps.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man1/*
