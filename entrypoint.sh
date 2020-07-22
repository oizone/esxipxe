#!/bin/sh
7z x -o/tftp/cd /tftp/ESXi.iso
dhcpd -4 
/usr/sbin/in.tftpd --listen --address 0.0.0.0:69 --secure --retransmit 1000000 --blocksize 512 -vvv /tftp
