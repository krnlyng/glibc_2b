Name:           glibc
Version:        2.25
Release:        1%{?dist}
Summary:        glibc

License: LGPLv2+ and LGPLv2+ with exceptions and GPLv2+
Group: System Environment/Libraries
URL: http://www.gnu.org/software/glibc/
Source0:        %{name}-%{version}.tar.bz2

# Require libgcc in case some program calls pthread_cancel in its %%post
Requires(pre): libgcc
# This is for building auxiliary programs like memusage, nscd
# For initial glibc bootstraps it can be commented out
#BuildRequires: gd-devel libpng-devel zlib-devel texinfo
BuildRequires:  zlib-devel texinfo
BuildRequires: sed >= 3.95, libcap-devel, gettext
#BuildRequires: /bin/ps, /bin/kill, /bin/awk, procps
BuildRequires: gawk,  util-linux, quilt
# This gcc >= 3.2 is to ensure that __frame_state_for is exported by glibc
# will be compatible with egcs 1.x.y
BuildRequires: gcc >= 3.2
%define enablekernel 2.6.32
%ifarch %{ix86}
%ifarch i486
%define _target_cpu	i486
%else
%define _target_cpu	i686
%endif
%endif
%ifarch i386
%define nptl_target_cpu i486
%else
%ifarch i486
%define nptl_target_cpu i686
%else
%define nptl_target_cpu %{_target_cpu}
%endif
%endif

# Need AS_NEEDED directive
# Need --hash-style=* support
BuildRequires: binutils >= 2.19.51.0.10
BuildRequires: gcc >= 3.2.1-5
BuildRequires: elfutils >= 0.72
BuildRequires: rpm >= 4.2-0.56

%description
glibc

%prep
%setup -q


%build
mkdir build
cd build
../configure --prefix=%{_prefix}
make %{?_smp_mflags}


%install
cd build
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)

