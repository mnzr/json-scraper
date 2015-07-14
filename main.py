#!/usr/bin/env python
"""Script to get Facebook info using Graph API"""
import requests
from sys import argv
import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError

SCRAP_DB = "fbscrap"


def create_post_url(graph_url, app_id, app_secret):
    """to make the URL"""
    post_args = "/?key=value&access_token=" + app_id + "|" + app_secret
    post_url = graph_url + post_args

    return post_url


def connect_db():
    """connecting to rethinkDB"""
    r.connect('localhost', 28015).repl()
    connection = r.connect(host='localhost',
                           port=28015,
                           db='fbscrap')
    return connection


# Setting up the app database
# Creating a table `fbscrap` in the database named in `TODO_DB` variable.
# We'll create the database and table here using
# [`db_create`](http://www.rethinkdb.com/api/python/db_create/)
# and
# [`table_create`](http://www.rethinkdb.com/api/python/table_create/) commands.
def setup_db():
    """to setup a DB"""
    connection = r.connect(host='localhost',
                           port=28015)
    try:
        r.db_create(SCRAP_DB).run(connection)
        r.db(SCRAP_DB).table_create('fbscrap').run(connection)
        print 'Using newly created database.'
    except RqlRuntimeError:
        print 'Using existing database.'
    finally:
        connection.close()


def insert_db(name, id, likes, talking_about_count, link, username,
              website):
    """ print page data to console"""
    # connection = r.connect(host='localhost',
                           # port=28015,
                           # db='fbscrap')
    r.table('fbscrap').insert(
        {
            'name': name,
            'id': id,
            'likes': likes,
            'talking_about_count': talking_about_count,
            'link': link,
            'username': username,
            'website': website
        }).run(connect_db())


def main():
    """The main function"""
    # list_companies = ["walmart", "cisco", "pepsi", "facebook"]
    list_companies = ["walmart"]
    graph_url = "https://graph.facebook.com/"
    app_id = argv[1]
    app_secret = argv[2]

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

        # insert JSON Data to rethinkDB

        insert_db(company,
                  json_fbpage["id"],
                  json_fbpage["likes"],
                  json_fbpage["talking_about_count"],
                  json_fbpage["link"],
                  json_fbpage["username"],
                  json_fbpage["website"])

        print "So the big bad DB has this info now:"
        for doc in r.db("fbscrap").table("fbscrap").run(connect_db()):
            for key in doc:
                print key, " ", doc[key]
            print ""


r.db("fbscrap").table("fbscrap")

if __name__ == '__main__':
    main()
