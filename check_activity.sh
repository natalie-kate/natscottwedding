#!/bin/bash
x=$((10*60))   
date=$(date -I)
currentTime=$(date +"%H:%M" | awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }')

if (test -f logs/localhost_extended_access_log.$date.txt); then
    last=$(tail -n1 logs/localhost_extended_access_log.$date.txt)
    lastTime=$(grep -Po '\d{2}:\d{2}:\d{2}(?= )' <<< $last)
    seconds=$(echo $lastTime | awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }')
    sum=$(($seconds + $x))

    if (($sum >= $currentTime)); then

        echo "Active"
        exit 75
    else
        echo "No activity, fine to update"
    fi
   
else  
    echo "No activity, fine to update"
fi