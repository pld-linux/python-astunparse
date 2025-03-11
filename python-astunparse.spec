#
# Conditional build:
%bcond_with	tests	# unit tests (depend on local python installation, failing on python 3.9)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	An AST unparser for Python
Summary(pl.UTF-8):	Odwrotność parsera AST dla Pythona
Name:		python-astunparse
Version:	1.6.3
Release:	6
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/astunparse/
Source0:	https://files.pythonhosted.org/packages/source/a/astunparse/astunparse-%{version}.tar.gz
# Source0-md5:	2cea4d8e49beba7684bac890e73d6a40
Patch0:		%{name}-deps.patch
URL:		https://pypi.org/project/astunparse/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-six >= 1.6.1
BuildRequires:	python-six < 2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-six >= 1.6.1
BuildRequires:	python3-six < 2
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a factored out version of "unparse" found in the Python source
distribution (under Demo/parser in Python 2 and under Tools/parser in
Python 3).

%description -l pl.UTF-8
Ten moduł to zrefaktorowana wersja "unparse" z dystrybucji źródeł
Pythona (w Demo/parser z Pythona 2 lub Tools/parser z Ptyhona 3).

%package -n python3-astunparse
Summary:	An AST unparser for Python
Summary(pl.UTF-8):	Odwrotność parsera AST dla Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-astunparse
This is a factored out version of "unparse" found in the Python source
distribution (under Demo/parser in Python 2 and under Tools/parser in
Python 3).

%description -n python3-astunparse -l pl.UTF-8
Ten moduł to zrefaktorowana wersja "unparse" z dystrybucji źródeł
Pythona (w Demo/parser z Pythona 2 lub Tools/parser z Ptyhona 3).

%prep
%setup -q -n astunparse-%{version}
%patch -P 0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/lib \
%{__python} -m unittest discover -s tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/lib \
%{__python3} -m unittest discover -s tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.rst HISTORY.rst LICENSE README.rst
%{py_sitescriptdir}/astunparse
%{py_sitescriptdir}/astunparse-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-astunparse
%defattr(644,root,root,755)
%doc AUTHORS.rst HISTORY.rst LICENSE README.rst
%{py3_sitescriptdir}/astunparse
%{py3_sitescriptdir}/astunparse-%{version}-py*.egg-info
%endif
