import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '404332707:AAEW1JknmPW8ZJHCitPbfrzVOEv4u7By5UE'
WEBHOOK_URL = 'https://e2c4c274.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
    
        'user',     #initial,hello
        'state1',   #nap   
        'state2',   #hungry
	'state3',   #happy
        'state4',   #bored
        'state5'    #angry

    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger':'feed',
            'source':[
                'state2',
                'state4'
                ],
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'reject',
            'source': 'state2',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
        {
            'trigger': 'idle',
            'source': [
                'state1',
                'state5',
                'user',
                'state3'
            ],
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },

        {
            'trigger': 'go_back',
            'source': [  
                'state1',
                'state2',
		'state3', 
		'state4', 
        	'state5' 
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
