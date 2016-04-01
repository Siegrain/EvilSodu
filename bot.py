import socket
import time
from utils import translate
from db import get, get_card, get_rune


class Bot(object):

    def __init__(self, host, port, chan, nick, ident, realname):
        self.host = host
        self.port = port
        self.chan = chan
        self.nick = nick
        self.ident = ident
        self.realname = realname
        self.recv_buffer = ''
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))
        self.send('NICK {}\r\n'.format(self.nick))
        self.send('USER {} {} bla :{}\r\n'.format(self.ident, self.host, self.realname))
        time.sleep(3)
        self.send('JOIN {}\r\n'.format(self.chan))

    def send(self, msg):
        self.socket.send(bytes('{}\r\n'.format(msg), 'UTF-8'))
        print('send: ' + msg)

    def recv(self):
        self.recv_buffer = self.socket.recv(1024).decode('UTF-8')
        temp = str.split(self.recv_buffer, '\n')

        for line in temp:
            try:
                line = str.rstrip(line)
                line = str.split(line)

                if (line[0] == 'PING'):
                    self.send('PONG {}'.format(line[1]))
            except:
                pass
        print('recv: ' + self.recv_buffer)

    def message(self, chan, msg):
        self.send('PRIVMSG {} : {}'.format(chan, msg))

    def main(self):
        msg = translate(self.recv_buffer)

        if msg['command'] == 'PRIVMSG':
            time.sleep(0.5)
            sender = msg['nick']
            channel = msg['params'][0].lower()
            message = msg['params'][1].lower()

            if self.nick.lower() in message:

                if 'hello' in message or 'hey' in message or 'hi' in message:
                    output = '\'sup?'

                elif 'rw' in message:
                    output = get_card('rw', 'single')
                    if 'spread' in message:
                        output = get_card('rw', 'spread')

                elif 'rune' in message:
                    output = get_rune('single')
                    if 'spread' in message:
                        output = get_rune('spread')

                elif 'spread' in message:
                    output = get_card('thoth', 'spread')

                elif 'y/n' in message:
                    output = get('yesno')

                elif 'when' in message:
                    output = get('when')

                elif 'necro' in message or 'necronomicon' in message:
                    output = get('necro')

                elif 'quote' in message:
                    output = get('quote')

                elif 'bane' in message:
                    output = get('bane')

                elif 'joke' in message:
                    output = get('joke')

                elif 'cat' in message:
                    output = get('cat')

                elif 'doge' in message:
                    output = get('doge')

                elif 'book' in message:
                    output = get('book')

                elif 'song' in message:
                    output = get('song')

                elif 'crowley' in message:
                    output = get('crowley')

                elif 'tranny' in message or 'trannies' in message:
                    output = get('thoth')

                else:
                    output = get_card('thoth', 'single')

                self.message(channel, '{}: {}'.format(sender, output))

        print('msg: ' + str(msg))

bot = Bot(host='eu.sorcery.net', port=9000, chan='#Siegrain',
          nick='EvilSodu', ident='EvilSodu', realname='EvilSodu')
bot.connect()

while 1:
    bot.recv()
    bot.main()
