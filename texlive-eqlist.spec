# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/eqlist
# catalog-date 2008-02-29 19:54:55 +0100
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-eqlist
Version:	2.1
Release:	1
Summary:	Description lists with equal indentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eqlist
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqlist.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqlist.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqlist.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package provides a list environment which sets a
description-like list but with the difference that the
indentation corresponds to the longest item of the list.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
