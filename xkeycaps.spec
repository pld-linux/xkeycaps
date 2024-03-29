Summary:	xkeycaps - a keymap editor for the X Window System
Summary(es.UTF-8):	Un editor de mapas de teclado para X
Summary(pl.UTF-8):	xkeycaps - edytor mapy klawiatury dla X Window System
Summary(pt_BR.UTF-8):	Um editor de mapas de teclado para o X
Name:		xkeycaps
Version:	2.46
Release:	9
License:	BSD
Group:		X11/Applications
Source0:	http://www.jwz.org/xkeycaps/%{name}-%{version}.tar.Z
# Source0-md5:	6792f828db6538f44f7696a8783b44ac
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.jwz.org/xkeycaps/
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-util-gccmakedep
BuildRequires:	xorg-util-imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xkeycaps is a graphical front-end to xmodmap.It opens a window that
looks like a keyboard; moving the mouse over a key shows what KeySyms
and Modifier bits that key generates. Clicking on a key simulates
KeyPress/KeyRelease events on the window of your choice. It is
possible to change the KeySyms and Modifiers generated by a key
through a mouse-based interface. This program can also write an input
file for xmodmap to recreate your changes in future sessions.

%description -l es.UTF-8
xkeycaps es una interfaz gráfica para xmodmap. Abre una ventana que
parece un teclado; mover el ratón sobre una tecla muestra las KeySyms
y los bits modificadores que la contraseña genera. Si se hace click en
una tecla simula eventos KeyPress/KeyRelease en la ventana que se
escoja. Se pueden cambiar los KeySyms y bits modificadores generados
por una contraseña a través de una interfaz que se basa en el ratón.
Este programa también puede escribir un archivo para que el xmodmap lo
cargue las próximas veces que se use X. Para obtener más detalles se
debe consultar la página del manual.

%description -l pl.UTF-8
xkeycaps jest graficzną nakładką na xmodmap. xkeycaps otwiera okno,
które wygląda jak klawiatura; przesuwając myszą ponad klawiszami
uzyskujemy informację na temat KeySyms oraz bitów Modifier jakie ten
klawisz generuje. Kliknięcie na klawiszu symuluje zdarzenia
KeyPress/KeyRelease dla okna, które wybierzesz. Można zmienić KeySyms
i Modifiers wygenerowane przez klawisz przy użyciu bazującego na myszy
interfejsu. Ten program może także zapisywać plik konfiguracyjny dla
xmodmapa.

%description -l pt_BR.UTF-8
xkeycaps é uma interface gráfica para o xmodmap. Ele abre uma janela
que parece um teclado; mover o mouse sobre uma tecla mostra as KeySyms
e os bits modificadores que a chave gera. Clicando em uma tecla simula
eventos KeyPress/KeyRelease na janela de sua escolha. É possível mudar
os KeySyms e bits modificadores gerados por uma chave através de uma
interface baseada em mouse. Esse programa pode também escrever um
arquivo para o xmodmap carregar nas próximas vezes que você usar o X.
Veja a página do manual para maiores detalhes.

%prep
%setup -q

%build
xmkmf -a
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	EXTRA_LDOPTIONS="%{rpmldflags}" \
	DEFAULT_KBD_NAME="L101"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1 \
	BINDIR=%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README defining.txt
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/xkeycaps.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man1/*
