# -*- coding=utf-8 -*-
import requests
import itchat
import random
from itchat.content import *

KEY = '04f44290d4cf462aae8ac563ea7aac16'


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return


# @itchat.msg_register([TEXT, PICTURE, RECORDING, ATTACHMENT, VIDEO])
# def greeting(msg):
#     itchat.send_msg('nice to meet you', msg['FromUserName'])


@itchat.msg_register([PICTURE, ATTACHMENT, VIDEO, TEXT])
def download_files(msg):
    if msg['Type'] == 'Text':
        return
    else:
        msg.download(msg['FileName'])
    # msg['Text'](msg['FileName'])      #下载文件
    itchat.send('@%s@%s' % (
        'img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']),
                msg['FromUserName'])
    defaultReply = '复习中，有事请留言。'
    itchat.send_image(msg['FileName'])
    # reply = get_response(msg['Text'])+random.choice(robots)
    return defaultReply


@itchat.msg_register([TEXT])
def tuling_reply(msg):
    # robots = ['——By小飞侠', '——By小王子', '——By某某某']
    defaultReply = '复习中，有事请留言。\n我已经收到消息: ' + msg['Text']
    # reply = get_response(msg['Text'])+random.choice(robots)
    return defaultReply


# 群聊消息功能，慎用
# 使用 isGroupChat=True 指定消息来自于群聊，这个参数默认为 False
# @itchat.msg_register(TEXT, isGroupChat=True)
# def text_reply(msg):
#    if(msg.isAt):  # 判断是否有人@自己 #  如果有人@自己，就发一个消息告诉对方我已经收到了信息
#      itchat.send_msg("我已经收到了来自{0}的消息，实际内容为{1}".format(msg['ActualNickName'],msg['Text']),toUserName=msg['FromUserName'])


# 添加好友
# @itchat.msg_register(itchat.content.CARD,isFriendChat=True)
# def simply(msg):
#     printmsg['Text']
#     print(msg['Content'])
#     itchat.add_friend(userName=msg['Text']['UserName'])  #添加推荐的好友
#     print(msg['RecommendInfo'])
#     print(msg['RecommendInfo']['UserName'])


itchat.auto_login(hotReload=True)
# itchat.auto_login(enableCmdQR=True)这个只能在命令行生成二维码，not suggested，不能生成图片
itchat.run()
