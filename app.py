#!/usr/bin/env python


import json
import os
import requests
import datetime
from datetime import timedelta

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth

from flask import Flask
from flask import request
from flask import make_response

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

# firebase
cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://treat-me-22bff.firebaseio.com/'
})


# Flask app should start in global layout
app = Flask(__name__)

line_bot_api = LineBotApi('PsfUIymdd+yNhdBGMnctoWVNt6p+n2rX2yVq4OSN1qQeS/gAgxmJqtAiGVDuizXAm5xTKkBohwNmgUDSnOEJw+nb6HTq4WPyh4wiKiWyo21hd6tQ+jGLYsEX1YSbqlaqrnWoMunmTFABnww21+IChwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c6d548e7e5a4bf201d4de8fb1c6fe726')

@app.route('/webhook', methods=['POST'])


def webhook():
    req = request.get_json()
    res = makeWebhookResult(req)  
    
    res = json.dumps(res, indent=4)
    
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    
    return r

def makeWebhookResult(req):  
    #push user id to firebase
    userid = req.get("originalRequest").get("data").get("source").get("userId")
    profile = line_bot_api.get_profile(userid)
    database = db.reference()
    userp = database.child("user").child(userid)
    userp.update({
        "name" : profile.display_name
    })

    #jika parameternya mulai kuesioner
    if req.get("result").get("action") == "mulai-kuesioner":
        return "Anxiety1"
    
    #jika parameternya pertanyaan kuesioner
    elif str(req.get("result").get("action")).split("-")[0] == "anxiety" or str(req.get("result").get("action")).split("-")[0] == "depression":
        jenisKuesioner = str(req.get("result").get("action"))

        #push hasil ke firebase sesuai pertanyaan
        userp.update({
            jenisKuesioner : req.get("result").get("resolvedQuery")
        })
        soal = jenisKuesioner+str(int(req.get("result").get("action").split("-")[1])+1)
        return soal
    #jika chat biasa
    else:
        lastM  = userp.child("lastMessage").get()
        userp.update({
            "lastMessage" : lastM+" "+req.get("result").get("resolvedQuery")
        })
    return "Chat Lagi"

if __name__ == '__main__':
    port = int(os.getenv('PORT', 4040))

    print ("Starting app on port %d" %(port))

    app.run(debug=False, port=port, host='0.0.0.0')
