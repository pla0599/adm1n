#!/bin/bash
#Auth by luoxin0599@gmail.com 2020/10/19
IP=192.168.73.28
touch /var/log/watchdog.log
time=`date +%Y-%m-%d-%H:%M`
echo $time >>/var/log/watchdog.log
cpu=`top -b -n 1 | grep "load" | awk '{printf $10 $11 $12 $13}'`
echo "CPU $cpu">>/var/log/watchdog.log
mem=`free | awk '/Mem/{printf("%.2f\n"), $3/$2*100}' | cut -d "." -f 1`
echo "Memory Usage%  $mem" >>/var/log/watchdog.log
iostat -d -x -k 1 1 >>/var/log/watchdog.log
echo "" >>/var/log/watchdog.log
echo "" >>/var/log/watchdog.log
echo "" >>/var/log/watchdog.log
