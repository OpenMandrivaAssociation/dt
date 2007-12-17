%define name    dt
%define version 15.14
%define release %mkrel 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:	Hardware performances test
URL:		http://home.comcast.net/~SCSIguy/SCSI_FAQ/RMiller_Tools/dt.html
License:	GPL
Group:		System/Kernel and hardware
Source0:	intel-%{name}.tar.bz2
Patch0:		makefile.patch.bz2
BuildRequires: ed

%description
'dt' is a generic data test program used to verify proper operation of
peripherals and for obtaining performance information.  Since verification
of data is performed, 'dt' can be thought of as a generic diagnostic tool.

'dt' command lines are similar to the 'dd' program, which is popular on
most UNIX systems.  It contains numerous options to give the user complete
control of the test parameters.

'dt' has been used to successfully test disks, tapes, serial lines,
parallel lines, pipes, and memory mapped files.  In fact, 'dt' can be used
for any device which allows the standard open, read, write, & close system
calls.  Special support is necessary for some devices, such as serial lines,
for setting up the speed, parity, data bits, etc.

%prep
%setup -q -n %{name}.d
%patch0 -p0

%build
%make depend
# avoid static link to libc
%make LDFLAGS=

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%_bindir
cp dt $RPM_BUILD_ROOT%_bindir

install -d $RPM_BUILD_ROOT%_defaultdocdir/%name-%version
cp dt-Abstract dt.examples dt-UsersGuide.* IOT-Example $RPM_BUILD_ROOT%_defaultdocdir/%name-%version
cp LINUX-Notes README.1st ToDoList WhatsNew-* $RPM_BUILD_ROOT%_defaultdocdir/%name-%version
cp -r html $RPM_BUILD_ROOT%_defaultdocdir/%name-%version

%files
%attr(755,root,root)
%_bindir/dt
%_defaultdocdir/%name-%version

%clean
rm -rf $RPM_BUILD_ROOT
