# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device herolte
%define vendor samsung

%define vendor_pretty Samsung
%define device_pretty Galaxy S7

%define installable_zip 1

# As the S7 is a device with Mali GPU
%define android_config \
#define MALI_QUIRKS 1\
%{nil}

%define straggler_files \
/bugreports\
/cache\
/d\
/file_contexts.bin\
/init.baseband.sh\
/property_contexts\
/sdcard\
/selinux_version\
/service_contexts\
/vendor\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

