#!/bin/bash
# Sends a POST request with the content of a JSON file
curl -sX POST -H "Content-Type: application/json; charset=utf-8" -d "@$2" "$1"
