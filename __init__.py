#!/usr/bin/env python
import urllib2
import json

def main():
    list_companies = ["walmart", "cisco", "pepsi", "facebook"]

    graph_url = "http://graph.facebook.com/"

    for company in list_companies:
        #make graph api url with company username
        current_page = graph_url + company

        #open public page in facebook graph api
        web_response = urllib2.urlopen(current_page)    #take response from the url
        #print(web_response)
        readable_page = web_response.read()             #conversion to human readable format
        #print(readable_page)
        json_fbpage = json.loads(readable_page)         #

        #print page data to console
        print
        print company, "page"
        print json_fbpage["id"]
        print json_fbpage["likes"]
        print json_fbpage["talking_about_count"]
        print json_fbpage["username"]

if __name__ == '__main__':
    main()