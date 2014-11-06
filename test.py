#!/usr/bin/env python
import urllib2
import json

def main():
    graph_url = "http://graph.facebook.com/"
    list_companies = ["walmart", "cisco", "pepsi", "facebook"]
    #list_companies =  ["MozillaBD"]

    #Show company list
    print "Companies in our list:"
    for company in list_companies:
        print "> ", company
    print

    current = raw_input("Which company do you want to know about? \n> ")

    #make graph api url with company username
    current_page = graph_url + current
        #open public page in facebook graph api
    web_response = urllib2.urlopen(current_page)    #take response from the url
    #print(web_response)
    readable_page = web_response.read()             #conversion to human readable format
    #print(readable_page)
    json_fbpage = json.loads(readable_page)         #

    print current + " page has these properties:"
    for property in json_fbpage:
        print "> ", property
    print

    prop = raw_input("Which property about " + current + " do you want to know about? \n> ")
    print json_fbpage[prop]

if __name__ == '__main__':
    main()