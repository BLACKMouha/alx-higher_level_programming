#!/bin/bash
# Sends a custom header to the URL passed as argument
curl -sH "X-School-User-Id: 98" "$1"
