%define name    dt
%define version 15.14
%define release 7

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:	Hardware performances test
URL:		http://home.comcast.net/~SCSIguy/SCSI_FAQ/RMiller_Tools/dt.html
License:	GPL
Group:		System/Kernel and hardware
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 15.14-6mdv2011.0
+ Revision: 617904
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 15.14-5mdv2010.0
+ Revision: 428391
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 15.14-4mdv2009.0
+ Revision: 244554
- rebuild
- fix no-buildroot-tag

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 15.14-2mdv2008.1
+ Revision: 130054
- BuildRequires: ed
- kill re-definition of %%buildroot on Pixel's request

  + Anne Nicolas <ennael@mandriva.org>
    - rebuild for 2008.0
    - Import dt



* Tue May 9 2006 Anne Nicolas <anne.nicolas@mandriva.com> 15.14-1mdk
- initial release
