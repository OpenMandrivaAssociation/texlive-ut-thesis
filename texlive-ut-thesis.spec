%global tl_name ut-thesis
%global tl_revision 78431

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1.8
Release:	%{tl_revision}.1
Summary:	University of Toronto thesis style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ut-thesis
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ut-thesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ut-thesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ut-thesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX document class implements the formatting requirements of the
University of Toronto School of Graduate Studies (SGS), as of Fall 2020
( https://www.sgs.utoronto.ca/academic-progress/program-completio
n/formatting). For example usage, see the GitHub repository.

