import os
from flask import request

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, ButtonsTemplate


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"



# def send_image_url(id, img_url):
#     url = request.url_root + img_url
#     # print("URL: ", url)
#     # url = img_url
#     # app.logger.info("url=" + url)
#     line_bot_api = LineBotApi(channel_access_token)
#     line_bot_api.reply_message(id, ImageSendMessage(url, url))

#     return "OK"


"""
elif text == 'buttons':
        buttons_template = ButtonsTemplate(
            title='My buttons sample', text='Hello, my buttons', actions=[
                URIAction(label='Go to line.me', uri='https://line.me'),
                PostbackAction(label='ping', data='ping'),
                PostbackAction(label='ping with text', data='ping', text='ping'),
                MessageAction(label='Translate Rice', text='米')
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
"""


"""
def send_button_message(id, text, buttons):
    pass
"""
