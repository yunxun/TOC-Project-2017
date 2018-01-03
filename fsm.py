from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'go to state1'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'go to state2'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == ('feed','hug','play')

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == ('wake','wakeup','...','sorry')

    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == ('vegetable','no')

    def on_enter_state1(self, update):
        update.message.reply_text("Hello~I'm Capoo.I like to eat meat!!Lots of meat.state1")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text(("Hungry~QQ state2")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')
       
    def on_enter_state3(self, update):
        update.message.reply_text("Mew~ Mew~ Happy <3~ state3")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')
    
    def on_enter_state4(self, update):
        update.message.reply_text("so Boring.Play with me.  state4")
        self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state4')
    
    def on_enter_state5(self, update):
        update.message.reply_text("Angry...  state5")
        self.go_back(update)

    def on_exit_state5(self, update):
        print('Leaving state5')
