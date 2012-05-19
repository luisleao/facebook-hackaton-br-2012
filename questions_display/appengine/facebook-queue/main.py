#!/usr/bin/env python
# coding=utf-8


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util


import time
import simplejson as json
from urllib import urlencode
import random
import string
import uuid
import base64




class Queue(db.Model):
	#key_name = foursquare_user_id
	active = db.BooleanProperty(required=True, default=False)
	created = db.DateTimeProperty(auto_now_add=True)
	updated = db.DateTimeProperty(auto_now=True)
	question = db.StringProperty(required=True)
	option_a_text = db.StringProperty(required=True)
	option_a_id = db.StringProperty(required=True)
	option_a_votes = db.StringProperty(required=True)
	facebook_user = db.StringProperty(required=True)
	facebook_access_token = db.StringProperty(required=True)


class AddHandler(webapp.RequestHandler):
	

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')





def main():
	handlers = [
		("/", MainHandler),
	]
	
	application = webapp.WSGIApplication(handlers, debug=True)
	util.run_wsgi_app(application)


if __name__ == '__main__':
	main()
