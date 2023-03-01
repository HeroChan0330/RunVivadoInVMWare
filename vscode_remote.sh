#!/usr/bin/env bash
curl -X POST -F "addr=$1" -F "line=$2" "http://192.168.65.1:4567/vscode" --connect-timeout 1
if [ "28" -ne "$?" ]; then 
    echo "success"
else
    timeout 1 xterm -fa 'Monospace' -fs 10 -e dialog --msgbox "Listener in windows is closed" 10 40
fi

