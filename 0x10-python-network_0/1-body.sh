#!/bin/bash
# Sends a GET request to a URL and displays the body of the response (only for 200 status code)
response=$(curl -sL -w "%{http_code}" -X GET "$1" -o /dev/null)
status_code=$(echo "$response" | tail -n1)
if [ "$status_code" -eq 200 ]; then
    curl -sL "$1"
else
    echo "Error: Non-200 status code received: $status_code"
fi
