#!/usr/bin/env python
# encoding: utf-8
"""
proxy.py

Created by Luís Leao and Sam Carecho on 2012-05-18.
"""

import sys
import os

from Pubnub import Pubnub
import threading


question_data = {}
t = None

def callback_timer():
    global question_data    # Needed to modify global copy of globvar
    global t
    
    print "callback timer"
    print question_data
    #TODO: receive facebook question id and access_token, put in a variable and set a timer to get data and send to arduino
    t = threading.Timer(5.0, callback_timer).start()

def receive(message):
    global question_data    # Needed to modify global copy of globvar
    global t
    if t:
        t.cancel()
    
    question_data = message
    callback_timer()
    return True



#	history = pubnub.history({
#	    'channel' : 'hello_world',
#	    'limit'   : 1
#	})
#	print(history)



def main():
	print "started"
	
	pubnub = Pubnub(
	    "pub-e10385fe-9f9f-46a4-b969-f3c8ba11ff59",  ## PUBLISH_KEY
	    "sub-f8f2ff3a-a176-11e1-bbc1-f151a023fb9a",  ## SUBSCRIBE_KEY
	    "sec-OGY5MTk3Y2QtMDY2OS00NThiLTlmZjItNWFkZGM3NDgxMmZi",
	    False
	)
	
#	info = pubnub.publish({
#	    'channel' : 'fbhackaton_newquestion',
#	    'message' : {
#	        'some_text' : 'Hello my World'
#	    }
#	})
#	print(info)

	print("subscribing...")
	pubnub.subscribe({
	    'channel'  : 'fbhackaton_newquestion',
	    'callback' : receive 
	})
#	print(info)
#	print "main complete"


if __name__ == '__main__':
	main()



