#!/bin/bash
# Sends a custom header to the URL passed as argument
curl -H "X-School-User-Id: 98" "$1"
