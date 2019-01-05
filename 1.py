# -*- coding=utf-8 -*-
import requests
import itchat
import random

KEY = '04f44290d4cf462aae8ac563ea7aac16'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robo                                                                                      t',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = '忙碌中，有事请留言。我已经收到消息: ' + msg['Text']
   # robots=['——By机器人小杨','——By机器人白杨','——By反正不是本人']
   # reply = get_response(msg['Text'])+random.choice(robots)
    return defaultReply

itchat.auto_login(enableCmdQR=True)
itchat.run()