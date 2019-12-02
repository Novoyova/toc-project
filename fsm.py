from transitions.extensions import GraphMachine
from utils import send_text_message, send_image_url
from data import data


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_init(self, event):
        return True

    def is_going_to_food(self, event):
        text = event.message.text
        return text.lower() == "back"

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

    def on_enter_food(self, event):
        print("I'm entering food")

        reply_token = event.reply_token
        send_text_message(reply_token, data['intro'])
        # self.go_back()

    # def on_exit_state1(self):
    #     print("Leaving state1")

    def on_enter_sate(self, event):
        print("I'm entering sate")

        reply_token = event.reply_token
        send_text_message(reply_token, data['sate']['description'])
        send_image_url(reply_token, data['sate']['image_url'])
        # self.go_back()

    # def on_exit_state2(self):
    #     print("Leaving state2")

    def on_enter_nasi_campur(self, event):
        print("I'm entering nasi campur")

        reply_token = event.reply_token
        send_text_message(reply_token, data['nasi_campur']['description'])
        send_image_url(reply_token, data['nasi_campur']['image_url'])
        # self.go_back()

    def on_enter_betutu(self, event):
        print("I'm entering betutu")

        reply_token = event.reply_token
        send_text_message(reply_token, data['betutu']['description'])
        send_image_url(reply_token, data['betutu']['image_url'])
        # self.go_back()

    def on_enter_babi_guling(self, event):
        print("I'm entering babi guling")

        reply_token = event.reply_token
        send_text_message(reply_token, data['babi_guling']['description'])
        send_image_url(reply_token, data['babi_guling']['image_url'])
        # self.go_back()

    def on_enter_pisang_goreng(self, event):
        print("I'm entering pisang goreng")
        
        reply_token = event.reply_token
        send_text_message(reply_token, data['pisang_goreng']['description'])
        send_image_url(reply_token, data['pisang_goreng']['image_url'])
        # self.go_back()

    def is_next(self, event):
        text = event.message.text
        return text.lower() == "next"
