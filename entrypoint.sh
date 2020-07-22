#!/bin/sh
dhcpd -4 
/usr/sbin/in.tftpd --listen --address 0.0.0.0:69 --secure --retransmit 1000000 --blocksize 512 -vvv --foreground /tftp
