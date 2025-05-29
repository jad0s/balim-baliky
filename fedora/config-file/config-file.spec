%global cargo_install_lib 1
%define debug_package %{nil}
%bcond_without check

Name:		rust-config-file
Version:	0.2.3
Release:	%autorelease
Summary:	Read and parse configuration file automatically

License:	BSD-2-Clause
URL:		https://github.com/Keruspe/config-file
Source0:	https://github.com/Keruspe/config-file/archive/refs/tags/v%{version}.tar.gz#/config-file-%{version}.tar.gz
Source1:	LICENSE

BuildRequires:	cargo-rpm-macros >= 26
BuildRequires:	rust-serde-devel
BuildRequires:	rust-thiserror-devel
BuildRequires:	rust-toml-devel >= 0.5.0

%description
`config-file` is a simple Rust library to read and parse configuration files
automatically using Serde. It supports TOML format and is designed for ease of use.

%package devel
Summary:	%{summary}
Provides:	crate-%{name} = %{version}-%{release}
Provides:	crate(config-file) = %{version}
Provides:	crate(config-file/default) = %{version}
Provides:	crate(config-file/std) = %{version}

%description devel
Development files and metadata for the Rust `config-file` crate.

%prep
%autosetup -n config-file-%{version} -p1
%cargo_prep
cp %{SOURCE1} LICENSE #We have to include the LICENSE manually since upstream doesn't include it

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%check
%cargo_test

%files devel
%license LICENSE
%doc README.md
%dir %{_datadir}/cargo
%dir %{_datadir}/cargo/registry
%{_datadir}/cargo/registry/config-file-%{version}

%changelog
* Thu May 29 2025 jados <jados42008@gmail.com> - 0.2.3-1
- Initial package for Fedora
