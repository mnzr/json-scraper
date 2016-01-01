#!/usr/bin/env python
"""Script to get Github info using API"""
import requests


# Add any number of usernames here
users = ['google', 'facebook', 'apache']
url = "https://api.github.com/users/"
# Which JSON properties we want to catch
properties = ['login', 'id', 'html_url', 'public_repos', 'created_at']

for user in users:
    # make API url with Github username
    current_page = url + user
    # take response from the url
    response = requests.get(current_page)
    # conversion to human readable format
    json = response.json()
    for prop in properties:
        print(prop, ':', json[prop])
    print('')
