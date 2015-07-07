#!/usr/bin/env python
"""Script to get Facebook info using Graph API"""
import requests


def create_post_url(graph_url, app_id, app_secret):
    """to make the URL"""
    post_args = "/?key=value&access_token=" + app_id + "|" + app_secret
    post_url = graph_url + post_args

    return post_url


# def connect_db():
#     """connecting to DB"""
#     connection = mysql.connector.connect(user='rr', password='rr',
#                                          database='facebook_data')
#     return connection


def main():
    """The main function"""
    list_companies = ["walmart", "cisco", "pepsi", "facebook"]
    graph_url = "https://graph.facebook.com/"
    app_id = "342918142392056"
    app_secret = "b52b21c24c870c5c139cca42f03ada7b"

    # Show company list
    print "Companies in our list:"
    for company in list_companies:
        print "> ", company
    print

    for company in list_companies:
        # make graph api url with company username
        current_page = graph_url + \
                       create_post_url(company, app_id, app_secret)

        # open public page in facebook graph api
        # take response from the url
        web_response = requests.get(current_page)
        # conversion to human readable format
        json_fbpage = web_response.json()

        # print page data to console
        print company, "page"
        print "Page ID: ", json_fbpage["id"]
        print "Total likes: ", json_fbpage["likes"]
        print "People talking about it: ", json_fbpage["talking_about_count"]
        print "Link to Facebook Page: ", json_fbpage["link"]
        print "Facebook username: ", json_fbpage["username"]
        print "Website: ", json_fbpage["website"]
        print ""

        # gather JSON Data
        # page_data = (json_fbpage["id"], json_fbpage["likes"],
        #              json_fbpage["talking_about_count"],
        #              json_fbpage["username"])

if __name__ == '__main__':
    main()
