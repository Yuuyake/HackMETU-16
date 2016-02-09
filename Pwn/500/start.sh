chmod -R 700 .

for i in `seq 0 $(($1-1))`
do
	gcc team$i/pwn500.c -oteam$i/p500
	useradd -M p500t$i -s/usr/sbin/nologin
	chown -R p500t$i.p500t$i team$i
	chmod 700 -R team$i
	cd team$i
	echo p200 $i
	sudo -u p500t$i ./p500 &
	cd ..
done
