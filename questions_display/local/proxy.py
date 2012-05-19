#!/usr/bin/env python
# encoding: utf-8
"""
proxy.py

Created by Luís Leao and Sam Carecho on 2012-05-18.
"""

TEMPO = 3.0

import sys
import os

from Pubnub import Pubnub
import threading
import serial
import facebook


question_data = None
ser = serial.Serial("/dev/tty.usbmodem411", 9600) #621
t = None
data = False


def callback_timer():
    global ser, question_data, data, t
    t = None
    if question_data and "access_token" in question_data: 
        graph = facebook.GraphAPI(question_data["access_token"])
        question = graph.get_object("/%s" % question_data["question"])
        if "options" in question:
            option_0 = 0;
            option_1 = 0;
            for option in question["options"]["data"]:
                if option["id"] == question_data["option_0"]:
                    option_0 = float(option["votes"])
                if option["id"] == question_data["option_1"]:
                    option_1 = float(option["votes"])
            
            print "Received data!"
            perc = 50
            if int(option_0 + option_1) > 0:
                perc = int((option_1 / (option_0 + option_1) * 100))
            print question["question"]
            print "%04d;%04d;%04d\n" % (option_0, option_1, perc)
            ser.write("%04d;%04d;%04d\n" % (option_0, option_1, perc))
    
    t = threading.Timer(TEMPO, callback_timer)
    t.start()
    
    



def receive(message):
    global question_data, t
    print "received new PubNub message"
    question_data = message
    if t:
        t.cancel()
    callback_timer()

    return True


# if you need to send a message
#	history = pubnub.history({
#	    'channel' : 'hello_world',
#	    'limit'   : 1
#	})
#	print(history)



def main():
	print "started"
	global t
	t = threading.Timer(TEMPO, callback_timer)
	t.start()
	
	
	pubnub = Pubnub(
	    "pub-e10385fe-9f9f-46a4-b969-f3c8ba11ff59",  ## PUBLISH_KEY
	    "sub-f8f2ff3a-a176-11e1-bbc1-f151a023fb9a",  ## SUBSCRIBE_KEY
	    "sec-OGY5MTk3Y2QtMDY2OS00NThiLTlmZjItNWFkZGM3NDgxMmZi",
	    False
	)
	
	print("subscribing...")
	pubnub.subscribe({
	    'channel'  : 'fbhackaton_newquestion',
	    'callback' : receive 
	})


if __name__ == '__main__':
	main()



