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
#18/11/2019
#version: 1.2

"""
echo "[1] Dns "
echo ""
echo "[2] Whois "
echo ""
echo "[3] Scan "
echo ""
echo "[4] Servidor Tcp "
echo ""
echo "[5] Dns reverso "
echo ""
read -p  "[#] > " var
case $var in
"1")

python script.py dns 
exit
esac

case $var in
"2")
python script.py whois
exit

esac
case $var in
"3")
python script.py scan
exit
esac
case $var in 
"4")
python script.py tcp
esac
case $var in 
"5")
python script.py dnsr
exit
esac




