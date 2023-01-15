#!/bin/bash
# Takes an URL and displays all HTTP methods the server will accept
curl -sH "X-School-User-Id: 98" "$1"
