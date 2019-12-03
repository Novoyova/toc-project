from transitions.extensions import GraphMachine
from utils import send_text_message, send_template_message
from data import data


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    # is functions
    def is_init(self, event):
        return True

    def is_going_to_food(self, event):
        return True

    def is_going_to_sate(self, event):
        text = event.message.text
        return text.lower() == "sate" or text == "1"

    def is_going_to_nasi_campur(self, event):
        text = event.message.text
        return text.lower() == "nasi campur" or text == "2"

    def is_going_to_betutu(self, event):
        text = event.message.text
        return text.lower() == "betutu" or text == "3"

    def is_going_to_babi_guling(self, event):
        text = event.message.text
        return text.lower() == "babi guling" or text == "4"

    def is_going_to_pisang_goreng(self, event):
        text = event.message.text
        return text.lower() == "pisang goreng" or text == "5"

    def is_going_to_sate_detail(self, event):
        text = event.message.text
        return text.lower() == "detail"

    def is_going_to_nasi_detail(self, event):
        text = event.message.text
        return text.lower() == "detail"

    def is_going_to_betutu_detail(self, event):
        text = event.message.text
        return text.lower() == "detail"

    def is_going_to_babi_detail(self, event):
        text = event.message.text
        return text.lower() == "detail"

    def is_going_to_pisang_detail(self, event):
        text = event.message.text
        return text.lower() == "detail"

    def is_going_to_self(self, event):
        return True

    def is_next(self, event):
        text = event.message.text
        return text.lower() == "next"

    # on functions
    def on_enter_food(self, event):
        print("I'm entering food")
        print("my event: ", event)
        reply_token = event.reply_token
        send_text_message(reply_token, data['intro'])

    def on_enter_sate(self, event):
        print("I'm entering sate")
        reply_token = event.reply_token
        send_template_message(reply_token, data['sate']['title'], data['sate']['description'], data['sate']['image_url'])

    def on_enter_nasi_campur(self, event):
        print("I'm entering nasi campur")
        reply_token = event.reply_token
        send_template_message(reply_token, data['nasi_campur']['title'], data['nasi_campur']['description'], data['nasi_campur']['image_url'])

    def on_enter_betutu(self, event):
        print("I'm entering betutu")
        reply_token = event.reply_token
        send_template_message(reply_token, data['betutu']['title'], data['betutu']['description'], data['betutu']['image_url'])

    def on_enter_babi_guling(self, event):
        print("I'm entering babi guling")
        print("my event: ", event)
        reply_token = event.reply_token
        send_template_message(reply_token, data['babi_guling']['title'], data['babi_guling']['description'], data['babi_guling']['image_url'])

    def on_enter_pisang_goreng(self, event):
        print("I'm entering pisang goreng")
        print("my event: ", event)
        reply_token = event.reply_token
        send_template_message(reply_token, data['pisang_goreng']['title'], data['pisang_goreng']['description'], data['pisang_goreng']['image_url'])

    def on_enter_sate_detail(self, event):
        print("I'm entering sate detail")
        reply_token = event.reply_token
        send_text_message(reply_token, data['sate']['detail'])

    def on_enter_nasi_detail(self, event):
        print("I'm entering nasi campur detail")
        reply_token = event.reply_token
        send_text_message(reply_token, data['nasi_campur']['detail'])

    def on_enter_betutu_detail(self, event):
        print("I'm entering betutu detail")
        reply_token = event.reply_token
        send_text_message(reply_token, data['betutu']['detail'])

    def on_enter_babi_detail(self, event):
        print("I'm entering babi guling detail")
        reply_token = event.reply_token
        send_text_message(reply_token, data['babi_guling']['detail'])

    def on_enter_pisang_detail(self, event):
        print("I'm entering pisang goreng detail")
        reply_token = event.reply_token
        send_text_message(reply_token, data['pisang_goreng']['detail'])
