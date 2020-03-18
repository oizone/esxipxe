cp cd/boot.cfg boot.cfg
sed -i 's/\///g' boot.cfg
sed -i 's/prefix=/prefix=cd\//' boot.cfg
