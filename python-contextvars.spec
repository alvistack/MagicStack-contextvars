# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-contextvars
Epoch: 100
Version: 2.4
Release: 1%{?dist}
BuildArch: noarch
Summary: PEP 567 Backport
License: Apache-2.0
URL: https://github.com/MagicStack/contextvars/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This package implements a backport of Python 3.7 contextvars module (see
PEP 567) for Python 3.6.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-contextvars
Summary: PEP 567 Backport
Requires: python3
Requires: python3-immutables >= 0.9
Provides: python3-contextvars = %{epoch}:%{version}-%{release}
Provides: python3dist(contextvars) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-contextvars = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(contextvars) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-contextvars = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(contextvars) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-contextvars
This package implements a backport of Python 3.7 contextvars module (see
PEP 567) for Python 3.6.

%files -n python%{python3_version_nodots}-contextvars
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-contextvars
Summary: PEP 567 Backport
Requires: python3
Requires: python3-immutables >= 0.9
Provides: python3-contextvars = %{epoch}:%{version}-%{release}
Provides: python3dist(contextvars) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-contextvars = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(contextvars) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-contextvars = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(contextvars) = %{epoch}:%{version}-%{release}

%description -n python3-contextvars
This package implements a backport of Python 3.7 contextvars module (see
PEP 567) for Python 3.6.

%files -n python3-contextvars
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
