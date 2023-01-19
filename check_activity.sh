#!/bin/bash

# if [[  ]]; then
#     echo "There is activity"
#     exit 75
# else
#     echo "No activity, fine to update"
# fi

x=$((10*60))   #here we take 5 mins as example
logFile=$("/logs/localhost_extended_access_log." + date -I + "txt")
currentDateTime=$(date +"%Y-%m-%d %T")
currentTime=$(date +"%s")

if [-f logFile=$logFile ]; then
    
    # logs=$(grep)

    # # last=$(tail -n1 logFile=$logFile|awk -F'[][]' '{ gsub(/\//," ",$2); sub(/:/," ",$2); "date +%s -d \""$2"\""|getline d; print d;}' )

    # if [(last + x) >= currentTime]

    echo "Active"
    exit 75
   
else  
    echo "No activity, fine to update"

