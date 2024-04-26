#!/bin/bash
# Sends a JSON POST request to a URL and displays the body of the response

# Check if the JSON file is valid
if jq . "$2" >/dev/null 2>&1; then
    # Send the POST request with the JSON file as data and display the response
    curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
else
    echo "Not a valid JSON"
fi
