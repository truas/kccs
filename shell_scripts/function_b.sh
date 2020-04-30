#!/bin/bash

# Calling one function from another
func_one () {
   echo I was a simple echo. Now I am  echo-function - $1
   func_two
}

func_two () {
   echo "And I am the echo-echo-Function!"
}

# Calling function one.
func_one Mooncake