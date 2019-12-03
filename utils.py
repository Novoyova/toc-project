import os
from flask import request
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, ButtonsTemplate, PostbackAction, TemplateSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    return "OK"
    

def send_template_message(replay_token, title, text, image_url):
    line_bot_api = LineBotApi(channel_access_token)
    button_template = ButtonsTemplate(
        title=title, 
        text=text, 
        thumbnail_image_url=image_url,
        actions=
        [
            PostbackAction(label='See details', data='any', text='Detail'),
            PostbackAction(label='Next', data='any', text='Next'),
            PostbackAction(label='Back to main menu', data='any', text='Back')
        ]
    )
    message_template = TemplateSendMessage(alt_text='Your line is not supported' ,template=button_template)
    line_bot_api.reply_message(replay_token, message_template)
    return "OK"
