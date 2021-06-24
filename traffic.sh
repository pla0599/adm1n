#!/bin/bash 
eth="ens192" 
sec=30
echo -ne "date       start_time stop_time average-total(KB) average-in(KB) average-out(KB) \n" 
while true 
do 
local_date=`date "+%Y-%m-%d"` 
start_time=`date "+%H:%M:%S"` 
infirst=$(awk '/'$eth'/{print $2 }' /proc/net/dev) 
outfirst=$(awk '/'$eth'/{print $10 }' /proc/net/dev) 
sumfirst=$(($infirst+$outfirst)) 
sleep $sec"s" 
stop_time=`date "+%H:%M:%S"` 
inend=$(awk '/'$eth'/{print $2 }' /proc/net/dev) 
outend=$(awk '/'$eth'/{print $10 }' /proc/net/dev) 
sumend=$(($inend+$outend)) 

sum=$(($sumend-$sumfirst)) 
aver=$(awk 'BEGIN{printf "%.2f\n",('$sum'/'$sec'/1024)}') 
averin=$(awk 'BEGIN{printf "%.2f\n",(('$inend'-'$infirst')/'$sec'/1024)}')
averout=$(awk 'BEGIN{printf "%.2f\n",(('$outend'-'$outfirst')/'$sec'/1024)}')

echo -ne "$local_date $start_time   $stop_time  $aver                  $averin               $averout\n" 
done
