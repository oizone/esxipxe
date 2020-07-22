#!/bin/sh
git clone https://github.com/oizone/esxipxe.git /tftp
mkdir /tftp/cd
7z x -o/tftp/cd /ESXi.iso
dhcpd -4 
/usr/sbin/in.tftpd --listen --address 0.0.0.0:69 --secure --retransmit 1000000 --blocksize 512 -vvv /tftp
nginx
