#!/usr/bin/env python3
import base64
import hashlib
import hmac
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from linebot import webhook
import setting


REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
PUSH_ENDPOINT = 'https://api.line.me/v2/bot/message/push'


# 送られてきたrequestの署名を検証する
def signature_check(body, signature):
    b = webhook.SignatureValidator(setting.CHANNEL_SECRET)
    return b.validate(body, signature)


# reply messageを送る
def reply_message(reply_token, text):
    line_bot_api = LineBotApi(setting.ACCESS_TOKEN)
    try:
        line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    except LineBotApiError as e:
        print('error')
        print(e)


# push messageを送る
def push_message(id, text):
    line_bot_api = LineBotApi(setting.ACCESS_TOKEN)

    send_text = list()
    for e in text:
        send_text.append(TextSendMessage(text=e))

    try:
        line_bot_api.push_message(id, send_text)
    except LineBotApiError as e:
        print('error')
        print(e)
