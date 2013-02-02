#!/usr/bin/env python
"""A simple messaging app.

Accepts argument to the URL of: http://.../?m=chat%20message. You can also do a
POST.

A way to cheat and send a message to this app using the Javascript console.

var sendMessage = function(m) {
    // Fix the URL.
    document.createElement('img').src = 'http://.../?m=' + encodeURIComponent(m);
};

// Sample usage.
sendMessage('I am a message.');
"""

import json

import webapp2

class BaseHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(self.execute()))

    def post(self):
        self.get()

    def execute(self):
        return {
            'success': False,
            'error': 'Not implemeted.'
        }

class MessageHandler(BaseHandler):
    def execute(self):
        message = self.request.get('m', '')
        if message:
            # Put calls to glass with message here.
            return {'success': True}
        else:
            return {
                'success': False,
                'error': 'No message given.'
            }

class LocationHandler(BaseHandler):
    def execute(self):
        lat = self.request.get('lat', '')
        lng = self.request.get('lng', '')
        if lat and lng:
            # Put calls to glass with message here.
            return {'success': True}
        else:
            return {
                'success': False,
                'error': 'Missing location data.'
            }

class ImageHandler(BaseHandler):
    def execute(self):
        src = self.request.get('src', '')
        if src:
            # Put calls to glass with message here.
            return {'success': True}
        else:
            return {
                'success': False,
                'error': 'No image source given.'
            }

app = webapp2.WSGIApplication([
    ('/', MessageHandler),
    ('/message', MessageHandler),
    ('/location', LocationHandler),
    ('/image', ImageHandler)
])
