#!/bin/bash
# Sends a request to a URL and displays only the status code of the response

# Send the request and store the response in a temporary file
curl -s -o tmp_status_code "$1"

# Extract the status code and display it
grep -oP '(?<=HTTP/1\.1 )\d+' tmp_status_code

# Clean up the temporary file
rm tmp_status_code
