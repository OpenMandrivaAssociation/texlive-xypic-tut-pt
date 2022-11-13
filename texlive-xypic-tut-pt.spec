Name:		texlive-xypic-tut-pt
Version:	15878
Release:	1
Summary:	A tutorial for XY-pic, in Portuguese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/portuguese/xypic-tutorial
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xypic-tut-pt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xypic-tut-pt.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive xypic-tut-pt package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/xypic-tut-pt/README
%doc %{_texmfdistdir}/doc/generic/xypic-tut-pt/grafico.eps
%doc %{_texmfdistdir}/doc/generic/xypic-tut-pt/xypic-tutorial.pdf
%doc %{_texmfdistdir}/doc/generic/xypic-tut-pt/xypictutorial.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
