import xlrd
import os

excel=xlrd.open_workbook('esxi-hosts.xlsx')
sheet=excel.sheet_by_index(0)

i = 2

while i < sheet.nrows:
    output=open(sheet.cell(i,0).value,"w+")
    if os.path.exists("pxelinux.cfg/{}".format(sheet.cell(i,7).value)):
      os.remove("pxelinux.cfg/{}".format(sheet.cell(i,7).value))
    pxe=open("pxelinux.cfg/{}".format(sheet.cell(i,7).value),"w+")

    output.write('vmaccepteula\n')
 
    output.write('rootpw {}\n'.format(sheet.cell(i,12).value))
    output.write('clearpart --alldrives --overwritevmfs\n')

    output.write('install --firstdisk=usb --overwritevmfs --novmfsondisk\n')
    output.write('keyboard Finnish\n')

    output.write("network --bootproto=static --device={} --ip={} --netmask={} --gateway={} --nameserver={} --hostname={} --vlanid={} --addvmportgroup=1\n".format(sheet.cell(i,1).value,sheet.cell(i,2).value,sheet.cell(i,3).value,sheet.cell(i,4).value,sheet.cell(i,5).value,sheet.cell(i,0).value,int(sheet.cell(i,6).value)))

    output.write('reboot --noeject\n')

    output.write('%pre --interpreter=busybox\n')
    output.write('cd /vmfs/volumes/remote-install-location/pxelinux.cfg/\n')

    output.write('ln -sf localboot {}\n'.format(sheet.cell(i,7).value))

    output.write('%firstboot --interpreter=busybox\n')

    output.write('esxcli vsan storage tag add -t capacityFlash -d `esxcli storage core device list|grep -B 1 "Display Name:.*{}"|head -n 1`\n'.format(sheet.cell(i,8).value))

    output.write('esxcli network ip dns search add --domain={}\n'.format(sheet.cell(i,11).value))

    output.write('esxcli network vswitch standard portgroup set -v {} -p "VM Network"\n'.format(int(sheet.cell(i,6).value)))

    output.write('echo "server {}" >> /etc/ntp.conf\n'.format(sheet.cell(i,9).value))
    output.write('echo "server {}" >> /etc/ntp.conf\n'.format(sheet.cell(i,10).value))

    output.write('/vmfs/volumes/remote-install-location/post-config.sh\n')
    pxe.write('default vmware\n')
    pxe.write('display grph\n')
    pxe.write('prompt 1\n')
    pxe.write('timeout 10\n')
    pxe.write('\n')
    pxe.write('label vmware\n')
    pxe.write('\tkernel /cd/mboot.c32\n')
    pxe.write('\tappend -c /boot.cfg ks=nfs://{}/{} +++\n'.format(sheet.cell(0,1).value,sheet.cell(i,0).value))
    pxe.write('\tipappend 2\n')
    pxe.close()
    output.close()
    i += 1





 



 
 

