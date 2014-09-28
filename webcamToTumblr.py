'''webcamToTumblr project
Epic Jefferson 

A Raspberry Pi project.

Using Tumblr's instructions for registering an app at https://www.tumblr.com/docs/en/api/v2
and to get your consumer key,consumer secret, token key, and token secret.

and adafruit's motion sensing lesson https://learn.adafruit.com/adafruits-raspberry-pi-lesson-12-sensing-movement
'''

#!/usr/bin/env python
import sys
import os
import pytumblr
import time
import RPi.GPIO as io
from tumblr_keys import *		#import your keys, you should save them in a separate tumblr_keys.py
								#consumer_key = 'consumer key'
								#consumer_secret = 'consumer secret'
								#token_key = 'oauth token key' 
								#token_secret = 'oauth token secret'

io.setmode(io.BCM)
pir_pin = 18					#connect the PIR sensor to pin 18 on the Pi's GPIO
io.setup(pir_pin, io.IN)         # activate input

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
	consumer_key,
	consumer_secret,
	token_key,
	token_secret
)

while True:
    print(io.input(pir_pin))	#print to check sensor state
    if io.input(pir_pin):
		os.system('sudo fswebcam -r 640x480 -S 20 webcam.jpg')

		#Posts an image to your tumblr.
		#Make sure you point an image in your hard drive. Here, 'webcam.jpg' must be in the 
		#same folder where the script is saved.
		#From yourBlogName.tumblr.com should just use 'yourBlogName'
		#The default state is set to "queue", to publish use "published"
		client.create_photo('yourBlogName', state="published", tags=["testing", "ok"], data="webcam.jpg")
		time.sleep(5)
    time.sleep(0.25)