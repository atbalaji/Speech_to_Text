#!/bin/bash
echo 
: | cat $( ls | grep -i $1".c" )
echo 