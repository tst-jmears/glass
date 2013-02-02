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

class MessageHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        message = self.request.get('m', '')
        if message:
            # Put calls to glass with message here.
            self.response.write(json.dumps({'success': True}))
        else:
            self.response.write(json.dumps({
                'success': False,
                'error': 'No message given.'
            }))

    def post(self):
        self.get()

app = webapp2.WSGIApplication([
    ('/', MessageHandler)
])
