#!/bin/bash
# Takes in a URL and displays the size of the HTTP response body
curl -sI "$1" | grep 'Content-Length' | cut -d ' ' -f 2
