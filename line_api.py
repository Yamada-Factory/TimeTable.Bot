#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from linebot import webhook
import setting


REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
PUSH_ENDPOINT = 'https://api.line.me/v2/bot/message/push'


# 送られてきたrequestの署名を検証する
def signature_check(body, signature):
    # # channel_secret = ... # Channel secret string
    # # body = ... # Request body string
    # hash = hmac.new(body.encode('utf-8'), hashlib.sha256).digest()
    # signature = base64.b64encode(hash)
    # # Compare X-Line-Signature request header and the signature
    # if signature == signature1:
    #     return True
    # return False
    b = webhook.SignatureValidator(setting.CHANNEL_SECRET)
    return b.validate(body, signature)


# reply messageを送る
def reply_message(reply_token, text):
    line_bot_api = LineBotApi(setting.ACCESS_TOKEN)
    # print(text)
    try:
        if not isinstance(text, (list, tuple)):
            text = [text]
        line_bot_api.reply_message(reply_token, [TextSendMessage(text=t) for t in text])
    except LineBotApiError as e:
        print('error')
        print(e)


# push messageを送る
def push_message(id, text):
    line_bot_api = LineBotApi(setting.ACCESS_TOKEN)
    # print(text)
    try:
        if not isinstance(text, (list, tuple)):
            text = [text]
        line_bot_api.push_message(id, [TextSendMessage(text=t) for t in text])
    except LineBotApiError as e:
        print('error')
        print(e)
