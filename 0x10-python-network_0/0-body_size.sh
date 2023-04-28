#!/bin/env bash
# Takes in a URL, sends a request to that URL then and displays the size of the body of the response
curl -Is "$1" | grep Content-Length | cut --delimiter=' ' --fields=2
