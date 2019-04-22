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
    'databaseURL' : 'https://minabot-aceess.firebaseio.com/'
})


# Flask app should start in global layout
app = Flask(__name__)

line_bot_api = LineBotApi('PsfUIymdd+yNhdBGMnctoWVNt6p+n2rX2yVq4OSN1qQeS/gAgxmJqtAiGVDuizXAm5xTKkBohwNmgUDSnOEJw+nb6HTq4WPyh4wiKiWyo21hd6tQ+jGLYsEX1YSbqlaqrnWoMunmTFABnww21+IChwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c6d548e7e5a4bf201d4de8fb1c6fe726')

@app.route('/call', methods=['GET'])


def call():
    database = db.reference()
    user = database.child("user")

    #membaca apakah ada data pada firebase

    snapshot = user.order_by_key().get()
    #key = userId Line
    for key, val in snapshot.items():
        try:
            lMessage= val["lastMessage"]
            #push message jika User memiliki lastMessage
            if lMessage!=None:
                lMessage = str(lMessage).split(" ");
                line_bot_api.push_message(key, TextSendMessage(text="Jumlah Kata dalam 5 Menit terkahir : "+len(lMessage))
			else:
				line_bot_api.push_message(key, TextSendMessage(text="Test Error")
        except Exception as res:
            print("Action jika Error")
    return "Success"



        
    
    
    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 4040))

    print ("Starting app on port %d" %(port))

    app.run(debug=False, port=port, host='0.0.0.0')