#!/bin/bash
# Sends a JSON file through HTTP
curl -s -X POST --header "Content-Type: application/json" --data "$(cat "$2")" "$1"
