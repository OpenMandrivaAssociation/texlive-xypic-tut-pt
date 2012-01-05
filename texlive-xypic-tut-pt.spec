# revision 15878
# category Package
# catalog-ctan /info/portuguese/xypic-tutorial
# catalog-date 2007-03-01 23:46:20 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-xypic-tut-pt
Version:	20070301
Release:	2
Summary:	A tutorial for XY-pic, in Portuguese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/portuguese/xypic-tutorial
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xypic-tut-pt.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xypic-tut-pt.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
