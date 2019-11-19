#!/bin/bash

echo """
____        _   _
|  _ \ _   _| |_| |__   ___  _ __  
| |_) | | | | __| |_ \ / _ \| |_ \ 
|  __/| |_| | |_| | | | (_) | | | |
|_|    \__/ |\__|_| |_|\___/|_| |_|
       |___/ 
#By:N4Br0kEr 
#desec-security
#17/11/2019
#version: 1.0

"""
echo "[1] Dns "
echo ""
echo "[2] Whois "
echo ""
echo "[3] Scan "
echo ""
read -p  "[#] > " var
case $var in
"1")

python test02.py dns 
exit
esac

case $var in
"2")
python test02.py whois
exit

esac
case $var in
"3")
python test02.py scan
exit
esac


