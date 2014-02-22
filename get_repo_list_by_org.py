#!/usr/bin/env python2

import json
import requests
import sys

try:
	org = sys.argv[1]

except IndexError:
	print "Usage: " + sys.argv[0] + " <GitHub Organization>"
	sys.exit(1)

github_url = "https://api.github.com/orgs/" + org + "/repos"
response = requests.get(github_url)
repos = json.loads(response.content)

for repo in repos:
	print "Found: " + repo['name'] + " - clone URL: " + repo['ssh_url']
