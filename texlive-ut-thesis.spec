# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ut-thesis
# catalog-date 2008-10-05 10:59:55 +0200
# catalog-license lppl
# catalog-version 1.8
Name:		texlive-ut-thesis
Version:	1.8
Release:	1
Summary:	University of Toronto thesis style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ut-thesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ut-thesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ut-thesis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This not described as an 'official' class, just one distributed
"in the hope that it will be useful". A skeleton file, using
the class, is provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ut-thesis/ut-thesis.cls
%doc %{_texmfdistdir}/doc/latex/ut-thesis/README
%doc %{_texmfdistdir}/doc/latex/ut-thesis/ut-thesis.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
