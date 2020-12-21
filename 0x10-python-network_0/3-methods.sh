#!/bin/bash
#return the methods available
curl -sI "$1" | grep "Allow:" | cut -d' ' -f2- 
