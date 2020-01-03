# -D MUST pass in _version and _release, and SHOULD pass in dist.

Summary: Varnish modules for Varnish Cache
Name: vmod-modules
Version: %{_version}
Release: %{_release}%{?dist}
License: BSD
Group: System Environment/Daemons
URL: https://github.com/otto-de/libvmod-modules
Source0: libvmod-modules-%{version}.tar.gz

#Requires: uuid

BuildRequires: varnish-devel >= 4.1
BuildRequires: pkgconfig
BuildRequires: make
BuildRequires: gcc
BuildRequires: python-docutils >= 0.6

# git builds
#BuildRequires: automake
#BuildRequires: autoconf
#BuildRequires: autoconf-archive
#BuildRequires: libtool

Provides: vmod-modules

%description
Varnish Modules

%prep
%setup -q -n varnish-modules-%{version}

%build

sudo rm -rf /usr/bin/automake
sudo ln -s /usr/bin/automake-1.4 /usr/bin/automake
./bootstrap

%configure

make %{?_smp_mflags}

%check

make %{?_smp_mflags} check

%install

make install DESTDIR=%{buildroot}

# Only use the version-specific docdir created by %doc below
rm -rf %{buildroot}%{_docdir}

# None of these for fedora/epel
find %{buildroot}/%{_libdir}/ -name '*.la' -exec rm -f {} ';'
find %{buildroot}/%{_libdir}/ -name '*.a' -exec rm -f {} ';'

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/varnish*/vmods/
%{_mandir}/man3/*.3*
%doc README.rst COPYING LICENSE

%post

/sbin/ldconfig

%changelog.
