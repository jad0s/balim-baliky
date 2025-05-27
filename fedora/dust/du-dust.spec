Name:           du-dust
Version:        1.2.0
Release:        %autorelease
Summary:        More intuitive version of du written in Rust

License:        Apache-2.0
URL:            https://github.com/bootandy/dust
Source0:        https://github.com/bootandy/dust/archive/refs/tags/v%{version}.tar.gz#/du-dust-%{version}.tar.gz
Source1:        du-dust-vendor-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  gcc

%description
dust is a more intuitive version of du written in Rust. It provides:
- Visual disk usage representation
- Colored output
- Fast parallel scanning
- Intuitive interface

%prep
%autosetup -n dust-%{version}
tar xzf %{SOURCE1} -C .  

%build
export CARGO_HOME=$(pwd)/.cargo
cargo build --release --offline --locked

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 target/release/dust %{buildroot}%{_bindir}/dust

%files
%license LICENSE
%doc README.md
%{_bindir}/dust

%changelog
* Tue May 27 2025 jados <jados42008@gmail.com> - 1.2.0-1
- Initial Fedora package
