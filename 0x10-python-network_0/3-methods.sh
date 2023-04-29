#!/bin/bash
# Displays all methods the server will acccept
curl -siX "$1" "OPTIONS" | grep "Allow" | cut -d=' ' -f2-
