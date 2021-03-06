# revision 32257
# category Package
# catalog-ctan /macros/latex/contrib/eqlist
# catalog-date 2012-01-23 15:27:59 +0100
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-eqlist
Version:	2.1
Release:	12
Summary:	Description lists with equal indentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eqlist
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqlist.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqlist.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqlist.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a list environment which sets a
description-like list in which the indentation corresponds to
the longest item of the list.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/eqlist/eqlist.sty
%doc %{_texmfdistdir}/doc/latex/eqlist/README
%doc %{_texmfdistdir}/doc/latex/eqlist/eqlist.pdf
%doc %{_texmfdistdir}/doc/latex/eqlist/eqlist.tex
#- source
%doc %{_texmfdistdir}/source/latex/eqlist/eqlist.dtx
%doc %{_texmfdistdir}/source/latex/eqlist/eqlist.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
