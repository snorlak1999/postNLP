#!/usr/bin/env python


import json
import os
import requests

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

line_bot_api = LineBotApi('QiRriK22eidlQYKXbPseOKC9VEoRnR4/Jvo1GMxQMZXkzYoI+wtql1HchBjEdAcwSBrkj9RNBrixAyV9C0Rx1/6AXu/DqNwnVOaZ7b+ouBHvLZUM3NNntPFAz4V6O3gjyDElT/8FslyCkuRJVQd3wAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('66102e73c1b74719168a8873e307430b')

def sendImg(tipe):
    data={
        "speech": "",
        "messages": [
          {
            "type": 4,
            "payload": {
              "line": {
                "type": "imagemap",
                "baseUrl": "https://firebasestorage.googleapis.com/v0/b/treat-me-22bff.appspot.com/o/anxiety-01.jpg?alt=media&_ignore=",
                "altText": "Kuesioner",
                "baseSize": {
                    "width": 1040,
                    "height": 940
                },
                "actions": [                
                ]
                }
            }
          }
        ]
    }
    return data


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
        return sendImg("anxiety-01")
    
    #jika parameternya pertanyaan kuesioner
    elif (str(req.get("result").get("action")).split("-")[0] == "anxiety") or (str(req.get("result").get("action")).split("-")[0] == "depression"):
        jenisKuesioner = str(req.get("result").get("action"))

        #push hasil ke firebase sesuai pertanyaan
        userp.update({
            jenisKuesioner : req.get("result").get("resolvedQuery")
        })
        soal = req.get("result").get("action").split("-")[0]+str(int(req.get("result").get("action").split("-")[1])+1)
        return sendImg(soal)
    
    #jika chat biasa
    else:
        lastM  = userp.child("lastMessage").get()
        if lastM!=None:
            userp.update({
                "lastMessage" : lastM+" "+req.get("result").get("resolvedQuery")
            })
        else:
            userp.update({
                "lastMessage" : req.get("result").get("resolvedQuery")
            })
            
    return {
        "speech": "Chat Lagi",
        "displayText": "Chat Lagi",
        #"data": {},
        #"contextOut": [],
        "source": "line"
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 4040))

    print ("Starting app on port %d" %(port))

    app.run(debug=False, port=port, host='0.0.0.0')
