Summary:	Cross-platform curses-based monitoring tool written in Python
Name:		glances
Version:	1.7.4
Release:	1
License:	LGPL v3
Group:		Applications
Source0:	https://github.com/nicolargo/glances/archive/v%{version}.tar.gz
# Source0-md5:	2062e70326f4c2eb9595c53c59d55047
URL:		https://github.com/nicolargo/glances
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-psutil
Requires:	python-setuptools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glances is a cross-platform curses-based monitoring tool written in
Python.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}/glances
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}/glances
%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
#%%doc
%attr(755,root,root) %{_bindir}/glances
%dir %{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}/*.py[co]
%{py_sitescriptdir}/%{name}/data
%{py_sitescriptdir}/*.egg-info
%dir %{_sysconfdir}/glances
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/glances/glances.conf
%{_mandir}/man1/glances.1*

