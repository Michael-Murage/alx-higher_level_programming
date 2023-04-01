#!/bin/bash
# takes in a URL, sends a POST request to the passed URL,
#  and displays the body of the response
# A variable email must be sent with the value test@gmail.com
# A variable subject must be sent with the value I will
#  always be here for PLD
# You have to use curl
curl -s "$1" -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
