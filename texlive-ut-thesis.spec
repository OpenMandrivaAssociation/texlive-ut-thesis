# revision 26793
# category Package
# catalog-ctan /macros/latex/contrib/ut-thesis
# catalog-date 2012-06-01 19:19:53 +0200
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-ut-thesis
Version:	2.0
Release:	5
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


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 813171
- Update to latest release.

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.8-2
+ Revision: 757334
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.8-1
+ Revision: 719867
- texlive-ut-thesis
- texlive-ut-thesis
- texlive-ut-thesis

