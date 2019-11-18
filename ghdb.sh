#!/bin/bash

#adicionar o bing




SEARCH="firefox"
echo """
       _	 _ _
  __ _| |__   __| | |__
 / _\ | |_ \ / _| | |_ \ 
| (_| | | | | (_| | |_) |
 \__  |_| |_|\__|_|_.__/  
 |___/ 
"""
echo ""
echo "[0] Outro Site"
echo ""
echo "[1] pastebin.com"
echo ""
echo "[2] trello.com"
echo ""
echo "[3] Arquivos "
echo ""
echo "[b] Extra: bing " 
echo ""
read -p "[*] > " var
case $var in 
"0")
read -p "[*] Site : " site
read -p "[*] Alvo : " alvo 
$SEARCH "https://google.com/search?q=site:$site+$alvo" 2> /dev/null
esac
case $var in
"1")
read -p "[*] Alvo: " alvo
$SEARCH "https://google.com/search?q=site:pastebin.com+$alvo" 2> /dev/null
esac
case $var in
"2")
read -p "[*] Alvo: " alvo
$SEARCH "https://google.com/search?q=site:trello.com+$alvo" 2> /dev/null
esac
case $var in
"3")
echo "Arquivos :"
echo ""
echo "[1] txt "
echo ""
echo "[2] php"
echo ""
echo "[3] asp"
echo ""
echo "[4] Outros "
echo ""
read -p "[>] " ext
case $ext in
	"1")
	echo ""
	read -p "[*] Alvo : " alvo
	$SEARCH "https://google.com/search?q=site:$alvo+ext:txt" 2> /dev/null
	;;
	"2")
	echo ""
	read -p "[*] Alvo : " alvo
	$SEARCH "https://google.com/search?q=site:$alvo+ext:php" 2> /dev/null
	;;
	"3")
	echo ""
	read -p "[*] Alvo : " alvo
	$SEARCH "https://google.com/search?q=site:$alvo+ext:asp" 2> /dev/null
	;;
	"4")
	echo ""
	read -p "[*] Alvo : " alvo
	read -p "[*] Ext : " ext
	$SEARCH "https://google.com/search?q=site:$alvo+ext:$ext " 2> /dev/null
	esac
esac
case $var in
"b")
echo """
 _     _             
| |__ (_)_ __   __ _ 
|  _ \| |  _ \ / _| |
| |_) | | | | | (_| |
|_.__/|_|_| |_|\__, |
               |___/ 
"""
echo ""
echo "[0] Outro site "
echo ""
echo "[1] pastebin.com"
echo ""
echo "[2] trello.com"
echo ""
echo "[3] Arquivos "
echo ""
read -p  "[B] > " var
case $var in 
"0")
	read -p "Site: " site
	read -p "Alvo: " alvo
	$SEARCH "https://bing.com/search?q=$site+$alvo" 2> /dev/null
	esac
esac
case $var in 
"1")
read -p "Alvo : " alvo
$SEARCH "https://bing.com/search?q=site:pastebin.com+$alvo" 2> /dev/null
esac
case $var in
"2")
$SEARCH "https://bing.com/search?q=site:trello.com+$alvo" 2> /dev/null
esac
case $var in 
"3")
echo ""
echo "arquivos"
echo ""
echo "[1] txt "
echo ""
echo "[2] php "
echo ""
echo "[3] asp "
echo ""
echo "[4] outro "
read -p  "[*] >" tipo
case $tipo in
	"1")
	read -p "Alvo : " alvo
	$SEARCH "https://bing.com/search?q=site:$alvo+ext:txt" 2> /dev/null
	;;
	"2")
	read -p "Alvo : " alvo
	$SEARCH "https://bing.com/search?q=site:$alvo+ext:php" 2> /dev/null
	;;
	"3")
	$SEARCH "https://bing.com/search?q=site:$alvo+ext:asp" 2> /dev/null
	;;
	"4")
	read -p "Alvo : " alvo
	read -p "Ext : " ext
	$SEARCH "https://bing.com/search?q=site:$alvo+$ext" 2> /dev/null
	esac
esac


