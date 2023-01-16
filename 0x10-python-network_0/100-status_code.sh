#!/bin/bash
# Display the status of a HTTP response
curl -s -o /dev/null -w "%{http_code}" "$1"
