import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()

machine = TocMachine(
    states=
    [
        "init", "food", "sate", "nasi_campur", "betutu", "babi_guling", "pisang_goreng",
        "sate_detail", "nasi_detail", "betutu_detail", "babi_detail", "pisang_detail"
    ],
    transitions=
    [
        {
            "trigger": "advance",
            "source": "init",
            "dest": "food",
            "conditions": "is_init",
        },
        {
            "trigger": "advance",
            "source": "food",
            "dest": "sate",
            "conditions": "is_going_to_sate",
        },
        {
            "trigger": "advance",
            "source": "food",
            "dest": "nasi_campur",
            "conditions": "is_going_to_nasi_campur",
        },
        {
            "trigger": "advance",
            "source": "food",
            "dest": "betutu",
            "conditions": "is_going_to_betutu",
        },
        {
            "trigger": "advance",
            "source": "food",
            "dest": "babi_guling",
            "conditions": "is_going_to_babi_guling",
        },
        {
            "trigger": "advance",
            "source": "food",
            "dest": "pisang_goreng",
            "conditions": "is_going_to_pisang_goreng",
        },
        {
            "trigger": "advance",
            "source": "food",
            "dest": "food",
            "conditions": "is_going_to_self",
        },
        {
            "trigger": "advance",
            "source": "sate",
            "dest": "nasi_campur",
            "conditions": "is_next",
        },
        {
            "trigger": "advance",
            "source": "nasi_campur",
            "dest": "betutu",
            "conditions": "is_next",
        },
        {
            "trigger": "advance",
            "source": "betutu",
            "dest": "babi_guling",
            "conditions": "is_next",
        },
        {
            "trigger": "advance",
            "source": "babi_guling",
            "dest": "pisang_goreng",
            "conditions": "is_next",
        },
        {
            "trigger": "advance",
            "source": "pisang_goreng",
            "dest": "sate",
            "conditions": "is_next",
        },
        {
            "trigger": "advance",
            "source": "sate",
            "dest": "sate_detail",
            "conditions": "is_going_to_sate_detail",
        },
        {
            "trigger": "advance",
            "source": "nasi_campur",
            "dest": "nasi_detail",
            "conditions": "is_going_to_nasi_detail",
        },
        {
            "trigger": "advance",
            "source": "betutu",
            "dest": "betutu_detail",
            "conditions": "is_going_to_betutu_detail",
        },
        {
            "trigger": "advance",
            "source": "babi_guling",
            "dest": "babi_detail",
            "conditions": "is_going_to_babi_detail",
        },
        {
            "trigger": "advance",
            "source": "pisang_goreng",
            "dest": "pisang_detail",
            "conditions": "is_going_to_pisang_detail",
        },
        {
            "trigger": "advance",
            "source": "sate_detail",
            "dest": "nasi_campur",
            "conditions": "is_next",
        },
        {
            "trigger": "advance",
            "source": "nasi_detail",
            "dest": "betutu",
            "conditions": "is_next",
        },
        {
            "trigger": "advance",
            "source": "betutu_detail",
            "dest": "babi_guling",
            "conditions": "is_next",
        },
        {
            "trigger": "advance",
            "source": "babi_detail",
            "dest": "pisang_goreng",
            "conditions": "is_next",
        },
        {
            "trigger": "advance",
            "source": "pisang_detail",
            "dest": "sate",
            "conditions": "is_next",
        },
        {
            "trigger": "advance", 
            "source": 
            [
                "sate", "nasi_campur", "betutu", "babi_guling", "pisang_goreng",
                "sate_detail", "nasi_detail", "betutu_detail", "babi_detail", "pisang_detail"
            ], 
            "dest": "food",
            "conditions": "is_going_to_food",
        },
    ],
    initial="init",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Sorry, I can't understand you")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("./img/fsm.png", prog="dot", format="png")
    return send_file("./img/fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
