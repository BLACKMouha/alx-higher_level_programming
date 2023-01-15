#!/bin/bash
# Sends a HTTP POST request with some data
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
