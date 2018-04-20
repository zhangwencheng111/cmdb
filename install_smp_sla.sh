#!/bin/bash
#2017年11月21日11:24:41
#
#install smokeping slave
##############################

DIR="/usr/local/smokeping"
CACHE_DIR="/usr/local/smokeping/htdocs/cache"
SHARE_SECRET="/usr/local/smokeping/etc/secret.txt"
LOGFILE="/usr/local/smokeping/log"
START_UP="/etc/init.d/smokeping"
SLAVE_NMAE=$1

#download and install
if [ ! -e "$DIR" ];then
	yum -y install curl  rrdtool perl perl-Net-Telnet perl-Net-DNS perl-LDAP perl-libwww-perl perl-RadiusPerl perl-IO-Socket-SSL perl-Socket6 perl-CGI-SpeedyCGI perl-devel perl-FCGI.x86_64 perl-CGI.x86_64 rrdtool-perl.x86_64 perl-ExtUtils-MakeMaker
	cd /usr/local/src/
	wget http://ftp.tu-chemnitz.de/pub/linux/dag/redhat/el6/en/x86_64/rpmforge/RPMS/fping-3.6-1.el6.rf.x86_64.rpm
	rpm -ivh fping-3.6-1.el6.rf.x86_64.rpm
	#install smokeping
	wget https://oss.oetiker.ch/smokeping/pub/smokeping-2.6.11.tar.gz
	tar -zxvf smokeping-2.6.11.tar.gz
	cd smokeping-2.6.11
	./configure --prefix=$DIR
	if [ $? -ne 0 ];then
		./setup/build-perl-modules.sh ${DIR}/thirdparty
	fi
	./configure --prefix=$DIR
	make && make install
        if [ $? -ne 0 ];then
        	echo -e "\033[31m install fail, please check \033[0m"
		exit 1
	fi	

	#验证文件
	echo "ppx.com" > $SHARE_SECRET
	chmod 600 $SHARE_SECRET
	#创建文件
	if [ ! -e "$LOGFILE" ];then
		mkdir $LOGFILE
	fi

	if [ ! -e "$CACHE_DIR" ];then
		mkdir $CACHE_DIR 
	fi
fi

#创建启动脚本
cat << "EOF" > $START_UP
#!/bin/bash
#
# chkconfig: 2345 80 05
# Description: Smokeping init.d script
# Hacked by : How2CentOS - http://www.how2centos.com
# Get function from functions library
. /etc/init.d/functions
# Start the service Smokeping
start() {
        echo -n "Starting Smokeping: "
        /usr/local/smokeping/bin/smokeping --master-url=http://112.73.66.35:9001   --cache-dir=/usr/local/smokeping/htdocs/cache/  --shared-secret=/usr/local/smokeping/etc/secret.txt --logfile=/usr/local/smokeping/log/slave.log  --slave-name=sh-ct
        ### Create the lock file ###
        touch /var/lock/subsys/smokeping
        success $"Smokeping startup"
        echo
}
# Restart the service Smokeping
stop() {
        echo -n "Stopping Smokeping: "
        kill -9 `ps ax | grep "/usr/local/smokeping/bin/smokeping" | grep -v grep | awk '{ print $1 }'` >/dev/null 2>&1
        ### Now, delete the lock file ###
        rm -f /var/lock/subsys/smokeping
        success $"Smokeping shutdown"
        echo
}
### main logic ###
case "$1" in
  start)
        start
        ;;
  stop)
        stop
        ;;
  status)
        status smokeping
        ;;
  restart|reload|condrestart)
        stop
        start
        ;;
  *)
        echo $"Usage: $0 {start|stop|restart|reload|status}"
        exit 1
esac
exit 0
EOF

#修改slave-name
if [ -n "$SLAVE_NMAE" ];then
	sed -i "s/sh-ct/$SLAVE_NMAE/" $START_UP
fi
chmod +x $START_UP

echo -e "Install Smokeping_slave:                                        \033[32m[  OK  ]\033[0m"
echo "use the command '/etc/init.d/smokeping start' to run this server"
