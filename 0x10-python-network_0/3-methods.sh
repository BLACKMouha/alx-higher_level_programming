#!/bin/bash
# Displays all methods the server will acccept
curl -siX "OPTIONS" "$1" |grep "Allow" | cut -d' ' -f2-
