#!/bin/bash

# this script lets you feed a penguin (Pingu)
# if Pingu does not like your food, Pingu will
# say so...

if [ $1 == fish ]; then
	echo "Hmmm fish...Pingu likes it!"
elif [ $1 == 'cake' ]; then
	echo "Hmmm CAKE...Pingu loves it!"
else
	echo "This is garbage..."
fi
