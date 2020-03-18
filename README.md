# esxipxe
PXE boot for installing VMware ESXi so that hosts are ready to be taken in by VCF SDDC manager, including vSAN disk config.
Tested with ESXi 6.7U3 and 7.0, using Helios4 as NAS, Juniper SRX300 as router and Dell Embedded PC and NUC for hosts.


Usage instructions:
1. Place files in a folder which shared both through TFTP and NFS - personally currently use openmediavault for this purpose
2. Configure DHCP for PXE boot, personally use Juniper SRX where this is done by adding properies to dhcp pool (x.x.x.x is the TFTP server):
   boot-file pxelinux.0;
   option 150 ip-address x.x.x.x;
3. Update host info in esxi-hosts.xlsx, most fields are self explanatory
   NFS server is fileshare in NFS3 form
   Password can be plain text or sourced has ready encrypted hash to shadow as in example
   GUID is host PXE boot id, can be also mac address or even just default. If default then any host will boot with that.
   capacitydisk field is a name which identifies disk which will be used as capacity disk in vSAN (currently supports only 1+1 disk config, easy to fix but don't needed atm)
4. run create-hosts.py with python3, requires xlrd module installed. Script assumes to be run from the tftp share folder
5. place all files from ESXi image to folder named cd
6. run command fix-boot.cfg.sh which will create a proper boot.cfg file
7. Configure hosts to pxe boot by default
8. Boot hosts

What happens:
1. Host boots from network and installs ESXi
   configures network
   password etc
   changes the PXE boot file to point into a file localboot
2. Second and future boots are done as PXE but OS is loaded from localdisk
3. First boot
   configures NTP
   enables SSH
   tags vSAN disk as capacity disk
   creates /store/.capacityflash.json
