#!/usr/bin/python
import os
#print("Running capasityflash!\n")
os.system('vdq -q > /tmp/capacity.tmp')
f=open("/tmp/capacity.tmp")
o=open("/store/.capacityflash.json","w+")
line=f.readline()
start=0
while line:
	if len(line) > 1:
		if start == 1:
			if "}" in line:
				o.write(oldline[:-2] + "\n")
			elif "]" in line:
				o.write(oldline[:-2] + "\n")
			else:
				o.write(oldline)

		oldline=line
	line = f.readline()
	start=1

o.write(oldline)
o.close()
f.close()
#o=open("/store/.capacityflash.json")
#print(o.read())
#os.system('ls -la /')
#os.system('ls -la /store/')
