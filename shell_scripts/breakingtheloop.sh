#!/bin/bash

for NUM in {1..100}
do
   if [ $NUM -eq 42 ]
   then
      echo "Found the number: "  $NUM !!!
      break
   fi
   echo "Not looking for this - Discarding " $NUM
done