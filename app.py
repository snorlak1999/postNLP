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

def sendPre(tipe):
    data= {
            "speech": "",
            "messages": [
              {
                "type": 4,
                "payload": {
                  "line": {
                    "type": "imagemap",
                    "baseUrl": "https://firebasestorage.googleapis.com/v0/b/treat-me-22bff.appspot.com/o/"+tipe+".jpg?alt=media&_ignore=",
                    "altText": "Kuesioner "+tipe,
                    "baseSize": {
                      "width": 1040,
                      "height": 584
                    },
                    "actions": [
                    ]
                  }
                }
              }
            ]
    }
    return data

def sendImg(tipe):
    data={}
    if (tipe=="anxiety-01" or tipe=="anxiety-03" or tipe=="anxiety-06" or tipe=="anxiety-07"):
        data={
            "speech": "",
            "messages": [
              {
                "type": 4,
                "payload": {
                  "line": {
                    "type": "imagemap",
                    "baseUrl": "https://firebasestorage.googleapis.com/v0/b/treat-me-22bff.appspot.com/o/"+tipe+".jpg?alt=media&_ignore=",
                    "altText": "Kuesioner "+tipe,
                    "baseSize": {
                      "width": 1040,
                      "height": 584
                    },
                    "actions": [
                       {
                          "type": "message",
                          "area": {
                            "x": 42,
                            "y": 456,
                            "width": 210,
                            "height": 97
                          },
                          "text": "A"
                        },
                        {
                          "type": "message",
                          "area": {
                            "x": 294,
                            "y": 455,
                            "width": 209,
                            "height": 95
                          },
                          "text": "B"
                        },
                        {
                          "type": "message",
                          "area": {
                            "x": 547,
                            "y": 455,
                            "width": 209,
                            "height": 98
                          },
                          "text": "C"
                        },
                        {
                          "type": "message",
                          "area": {
                            "x": 799,
                            "y": 456,
                            "width": 209,
                            "height": 96
                          },
                          "text": "D"
                        }
                    ]
                  }
                }
              }
            ]
        }
    elif (tipe=="anxiety-02" or tipe=="anxiety-04" or tipe=="anxiety-05"):
        data={
            "speech": "",
            "messages": [
              {
                "type": 4,
                "payload": {
                  "line": {
                    "type": "imagemap",
                    "baseUrl": "https://firebasestorage.googleapis.com/v0/b/treat-me-22bff.appspot.com/o/"+tipe+".jpg?alt=media&_ignore=",
                    "altText": "Kuesioner "+tipe,
                    "baseSize": {
                      "width": 1040,
                      "height": 584
                    },
                    "actions": [   
                        {
                          "type": "message",
                          "area": {
                            "x": 43,
                            "y": 331,
                            "width": 427,
                            "height": 95
                          },
                          "text": "A"
                        },
                        {
                          "type": "message",
                          "area": {
                            "x": 42,
                            "y": 456,
                            "width": 423,
                            "height": 97
                          },
                          "text": "B"
                        },
                        {
                          "type": "message",
                          "area": {
                            "x": 548,
                            "y": 333,
                            "width": 454,
                            "height": 93
                          },
                          "text": "C"
                        },
                        {
                          "type": "message",
                          "area": {
                            "x": 547,
                            "y": 456,
                            "width": 453,
                            "height": 97
                          },
                          "text": "D"
                        }
                    ]
                  }
                }
              }
            ]
        }
    elif (tipe.split("-")[0]=="depression"):
        data={
            "speech": "",
            "messages": [
              {
                "type": 4,
                "payload": {
                  "line": {
                    "type": "imagemap",
                    "baseUrl": "https://firebasestorage.googleapis.com/v0/b/treat-me-22bff.appspot.com/o/"+tipe+".jpg?alt=media&_ignore=",
                    "altText": "Kuesioner "+tipe,
                    "baseSize": {
                      "width": 1040,
                      "height": 584
                    },
                    "actions": [    
                        {
                          "type": "message",
                          "area": {
                            "x": 358,
                            "y": 323,
                            "width": 158,
                            "height": 192
                          },
                          "text": "A"
                        },
                        {
                          "type": "message",
                          "area": {
                            "x": 516,
                            "y": 321,
                            "width": 150,
                            "height": 195
                          },
                          "text": "B"
                        },
                        {
                          "type": "message",
                          "area": {
                            "x": 666,
                            "y": 319,
                            "width": 150,
                            "height": 199
                          },
                          "text": "C"
                        },
                        {
                          "type": "message",
                          "area": {
                            "x": 816,
                            "y": 326,
                            "width": 152,
                            "height": 192
                          },
                          "text": "D"
                        }
                    ]
                    }
                }
              }
            ]
        }
    return data

def send2Img(tipe):
    data={
        "speech": "",
        "messages": [
         {
            "type": 4,
            "payload": {
              "line": {
                "type": "imagemap",
                "baseUrl": "https://firebasestorage.googleapis.com/v0/b/treat-me-22bff.appspot.com/o/depression-intro.jpg?alt=media&_ignore=",
                "altText": "depression intro",
                "baseSize": {
                  "width": 1040,
                  "height": 584
                },
                "actions": [                
                ]
                }
            }
          }, 
          {
            "type": 4,
            "payload": {
              "line": {
                "type": "imagemap",
                "baseUrl": "https://firebasestorage.googleapis.com/v0/b/treat-me-22bff.appspot.com/o/"+tipe+".jpg?alt=media&_ignore=",
                "altText": "Kuesioner "+tipe,
                "baseSize": {
                  "width": 1040,
                  "height": 584
                },
                "actions": [  
                        {
                          "type": "message",
                          "area": {
                            "x": 358,
                            "y": 323,
                            "width": 158,
                            "height": 192
                          },
                          "text": "A"
                        },
                        {
                          "type": "message",
                          "area": {
                            "x": 516,
                            "y": 321,
                            "width": 150,
                            "height": 195
                          },
                          "text": "B"
                        },
                        {
                          "type": "message",
                          "area": {
                            "x": 666,
                            "y": 319,
                            "width": 150,
                            "height": 199
                          },
                          "text": "C"
                        },
                        {
                          "type": "message",
                          "area": {
                            "x": 816,
                            "y": 326,
                            "width": 152,
                            "height": 192
                          },
                          "text": "D"
                        }
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
    conn = userp.child("connect").get()
    
    #jika parameternya disconnect
    if req.get("result").get("action") == "disconnect":
        us = database.child("user").child(str(conn))
        us.update({
            "lastMessage" : None,
            "connect" : None
        })
        userp.update({
            "lastMessage" : None,
            "connect" : None
        })
        
        usName = str(us.child("name").get())
        myName = str(userp.child("name").get())
        #send ke yang terhubung
        line_bot_api.push_message(str(conn), TextSendMessage(text="Maaf kamu telah terputus dari "+myName))
            
        return {
            "speech": "Kamu telah terputus dari "+usName,
            "displayText": "Kamu telah terputus dari "+usName,
            #"data": {},
            #"contextOut": [],
            "source": "line"
        }
    
    if conn!=None:
        try:
            lastM  = userp.child("lastMessage").get()
            if lastM!=None:
                userp.update({
                    "lastMessage" : lastM+" "+req.get("result").get("resolvedQuery")+"."
                })
            else:
                userp.update({
                    "lastMessage" : req.get("result").get("resolvedQuery")+"."
                })
            line_bot_api.push_message(str(conn), TextSendMessage(text=str(req.get("result").get("resolvedQuery"))))
            return "Sukses"
        except Exception as res:
            return {
                "speech": "Maaf kamu gagal mengirimkan pesan, coba lagi",
                "displayText": "Maaf kamu gagal mengirinkan pesan, coba lagi",
                #"data": {},
                #"contextOut": [],
                "source": "line"
            } 
    
    
    #jika parameternya connect 
    if req.get("result").get("action") == "connect":
        try:
            reqConnect = str(req.get("result").get("resolvedQuery")).split(" ")[1]
          
            us = database.child("user").child(reqConnect)
            
            usName = str(us.child("name").get())
            myName = str(userp.child("name").get())
            
            if(str(userp.child("stat").get())!="2"):
                return {
                    "speech": "Maaf kamu bukan konselor",
                    "displayText": "Maaf kamu bukan konselor",
                    #"data": {},
                    #"contextOut": [],
                    "source": "line"
                } 
                
            #validasi apakah user telah terhubung ke yang lain
            if (us.child("connect").get()!=None):
                return {
                    "speech": "Maaf "+usName+" telah terhubung ke yang lain",
                    "displayText": "Maaf "+usName+" telah terhubung ke yang lain",
                    #"data": {},
                    #"contextOut": [],
                    "source": "line"
                } 
            
            #mengupdate status connect ke konselor
            userp.update({
                "connect" : reqConnect
            })
            us.update({
                "connect" : userid
            })
           
            
            #send ke yang terhubung
            line_bot_api.push_message(reqConnect, TextSendMessage(text="Yeayy , Kamu telah terhubung dengan "+myName+"\nAnda langsung dapat chattingan disini \nReply (#Disconnect) untuk disconnect"))
            
            return {
                "speech": "Yeayy , Kamu telah terhubung ke "+usName+"\nReply (#Disconnect) untuk disconnect",
                "displayText": "Yeayy , Kamu telah terhubung ke "+usName+"\nReply (#Disconnect) untuk disconnect",
                #"data": {},
                #"contextOut": [],
                "source": "line"
            } 
        
        except Exception as res:
            return {
                "speech": "Maaf kamu gagal menghubungkan",
                "displayText": "Maaf kamu gagal menghubungkan",
                #"data": {},
                #"contextOut": [],
                "source": "line"
            } 
        
            
    #jika parameternya mulai kuesioner
    if req.get("result").get("action") == "mulai-kuesioner":
        return {
            "speech": "Usia kamu berapa? ",
            "displayText": "Usia kamu berapa? ",
            #"data": {},
            #"contextOut": [],
            "source": "line"
        } 
    
    #jika parameternya age
    elif req.get("result").get("action") == "age":
        try:
            #validasi umur
            if int(req.get("result").get("resolvedQuery"))<100 and int(req.get("result").get("resolvedQuery"))>1: 
                userp.update({
                    "age" : int(req.get("result").get("resolvedQuery"))
                })
            else:
                userp.update({
                    "age" : "-"
                })
        except Exception as res:
            print("Error")
        return sendImg("anxiety-01")
    
    #jika parameternya pertanyaan kuesioner
    elif (str(req.get("result").get("action")).split("-")[0] == "anxiety") or (str(req.get("result").get("action")).split("-")[0] == "depression"):
        jenisKuesioner = str(req.get("result").get("action"))
        
        #push hasil ke firebase sesuai pertanyaan
        userp.update({
            jenisKuesioner : req.get("result").get("resolvedQuery")
        })
        
        
        #untuk menampilkan yang pre 02
        if(jenisKuesioner=="depression-01"):
            return sendPre("depression-pre-02")
        
        #untuk menampilkan yang pre 04
        if(jenisKuesioner=="depression-03"):
            return sendPre("depression-pre-04")
        
        #untuk menampilkan yang pre 05
        if(jenisKuesioner=="depression-04"):
            return sendPre("depression-pre-05")
        
        #untuk menampilkan yang pre 09
        if(jenisKuesioner=="depression-08"):
            return sendPre("depression-pre-09")
        
        soal = req.get("result").get("action").split("-")[0]+"-0"+str(int(req.get("result").get("action").split("-")[1])+1)
        if jenisKuesioner=="anxiety-07":
            soal="depression-01"
            return send2Img(soal)
        elif jenisKuesioner=="depression-09":
            #read all data
            dataKuesioner = userp.get()
            
            #jumlahAnxienty
            jumlahAnxiety=0
            x=1
            while x<8:
                nilai=0
                if str(dataKuesioner["anxiety-0"+str(x)]).lower()=="a":
                    nilai = 0
                elif str(dataKuesioner["anxiety-0"+str(x)]).lower()=="b":
                    nilai = 1
                elif str(dataKuesioner["anxiety-0"+str(x)]).lower()=="c":
                    nilai = 2
                elif str(dataKuesioner["anxiety-0"+str(x)]).lower()=="d":
                    nilai = 3
                jumlahAnxiety = jumlahAnxiety+nilai
                x=x+1
            
            #jumlah depression
            jumlahDepression=0
            x=1
            while x<9:
                nilai=0
                if str(dataKuesioner["depression-0"+str(x)]).lower()=="a":
                    nilai = 0
                elif str(dataKuesioner["depression-0"+str(x)]).lower()=="b":
                    nilai = 1
                elif str(dataKuesioner["depression-0"+str(x)]).lower()=="c":
                    nilai = 2
                elif str(dataKuesioner["depression-0"+str(x)]).lower()=="d":
                    nilai = 3
                jumlahDepression = jumlahDepression+nilai
                x=x+1
            
            #last data
            nilai=0
            if str(req.get("result").get("resolvedQuery")).lower()=="a":
                nilai = 0
            elif str(req.get("result").get("resolvedQuery")).lower()=="b":
                nilai = 1
            elif str(req.get("result").get("resolvedQuery")).lower()=="c":
                nilai = 2
            elif str(req.get("result").get("resolvedQuery")).lower()=="d":
                nilai = 3
            jumlahDepression=jumlahDepression+nilai
                
            tipeAnxiety=""
            if jumlahAnxiety<=5:
                tipeAnxiety="Mild"
            elif jumlahAnxiety<=10:
                tipeAnxiety="Moderate"
            elif jumlahAnxiety<=15:
                tipeAnxiety="Moderately severe"
            elif jumlahAnxiety<=21:
                tipeAnxiety="Sereve depression"
                
            tipeDepression=""
            if jumlahDepression<=4:
                tipeDepression="Minimal depression"
            elif jumlahDepression<=9:
                tipeDepression="Mild depression"
            elif jumlahDepression<=14:
                tipeDepression="Moderate depression"
            elif jumlahDepression<=19:
                tipeDepression="Moderately severe depression"
            elif jumlahDepression<=27:
                tipeDepression="Severe depression"
            
            
            #mengirimkan data ke semua konselor
            user = database.child("user")
            snapshot = user.order_by_key().get()
            #key = userId Line
            for key, val in snapshot.items():
                try:
                    stat= val["stat"]
                    #push message jika User memiliki lastMessage
                    if str(stat)=="2":
                        line_bot_api.push_message(key, TextSendMessage(text="Calon Pasien : \n"+"Nama : "+str(dataKuesioner["name"])+"\n"+"Umur : "+str(dataKuesioner["age"])+"\n"+"Nilai Kecemasan : "+str(jumlahAnxiety)+"\n"+"Tipe Kecemasan : "+str(tipeAnxiety)+"\n"+"Nilai Depression : "+str(jumlahDepression)+"\n"+"Tipe Depression : "+str(tipeDepression)+"\n\n\nUntuk menghubungkan balas dengan\n"))
                        line_bot_api.push_message(key, TextSendMessage(text="#connect "+str(userid)))
                        
                except Exception as res:
                    print("Error")
            thanks = "Terima kasih udah dengerin cerita Meeta! \nEhh!! Ternyata tahap assessment sudah selesai loh!! Yeay \(’-’ )/ \nSekarang, Meeta mau nyariin kamu ahli kesehatan paling bagus yang ada disekitar kamu\n\n\nNanti.. Meeta kabarin ya kalau udah ketemu, sampai nanti."

            return {
                "speech": thanks,
                "displayText": thanks,
                #"data": {},
                #"contextOut": [],
                "source": "line"
            }
        return sendImg(soal)
    
    #jika chat biasa
    else:    
        return {
            "speech": "Masukan kamu salah silahkan kirim lagi",
            "displayText": "Masukan kamu salah silahkan kirim lagi",
            #"data": {},
            #"contextOut": [],
            "source": "line"
        }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 4040))

    print ("Starting app on port %d" %(port))

    app.run(debug=False, port=port, host='0.0.0.0')
