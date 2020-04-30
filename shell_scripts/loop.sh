#!/bin/bash
# This generates a file every 5 minutes
while true; do
touch pic−`date +%s`.jpg
sleep 20
done
