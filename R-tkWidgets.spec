%define		packname	tkWidgets

Summary:	Widgets to provide user interfaces from bioconductor
Name:		R-%{packname}
Version:	1.40.0
Release:	2
License:	Artistic 2.0
Group:		X11/Applications
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	add1b0a90e4203e43fc7dae67a541e3f
URL:		http://bioconductor.org/packages/release/bioc/html/tkWidgets.html
BuildRequires:	R
BuildRequires:	R-DynDoc
BuildRequires:	R-widgetTools
BuildRequires:	tcl-devel
BuildRequires:	texlive-latex
BuildRequires:	tk-devel
Requires:	R
Requires:	R-DynDoc
Requires:	R-widgetTools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Widgets to provide user interfaces. tcltk should have been installed
for the widgets to run.

This package is a part of the bioconductor (bioconductor.org) project

%prep
%setup -c -q -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/testfiles
