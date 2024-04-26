#!/bin/bash
# Sends a GET request to a URL with a specific header and displays the body of the response
curl -sX GET -H "X-School-User-Id: 98" "$1"
