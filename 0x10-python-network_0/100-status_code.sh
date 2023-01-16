#!/bin/bash
# Display the status of a HTTP response
curl -sI "$1" |grep HTTP | cut -d' ' -f2
