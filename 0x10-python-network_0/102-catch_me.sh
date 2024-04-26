#!/bin/bash
# Makes a request to cause the server to respond with a specific message

# Send the request and display only the necessary output
curl -sX PUT -d "user_id=98" -L "$1" -w "%{size_download}\n" -o /dev/null
