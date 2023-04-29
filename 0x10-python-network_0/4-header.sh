#!/bin/bash
# Sends a custom header to the URL passed as argument
curl -sX "GET" -H "X-School-User-Id: 98" "$1"
