#!/bin/bash
#request with a modified header
curl -sX GET -H 'X-HolbertonSchool-User-Id: 98' "$1"
