#!/bin/sh
/usr/bin/python /vmfs/volumes/remote-install-location/capacityflash.py
/sbin/chkconfig ntpd on
/sbin/chkconfig SSH on
/etc/init.d/ntpd start
/etc/init.d/SSH start
esxcli system settings advanced set -o /UserVars/HostClientCEIPOptIn -i 2
#reboot
