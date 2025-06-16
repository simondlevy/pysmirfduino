#!/usr/bin/python3
'''
Copyright (C) 2025 Simon D. Levy

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, in version 3.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

import socket
import sys
from time import sleep
import threading
from threading import Thread


ADDRESS = '64:B7:08:94:28:76'

def connect_to_server(port=1):

    while True:

        try:

            print('Connecting to server %s:%d ... ' % (ADDRESS, port), end='')
            sys.stdout.flush()

            # Create a Bluetooth or IP socket depending on address format
            client = (socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM,
                      socket.BTPROTO_RFCOMM)
                      if ':' in ADDRESS
                      else socket.socket(socket.AF_INET, socket.SOCK_STREAM))

            try:
                client.connect((ADDRESS, port))
                print(' connected')
                break

            except Exception as e:
                print(str(e) + ': is server running?')
                sleep(1)

        except KeyboardInterrupt:
            break

    return client


def threadfun(client):

    while True:

        sleep(0)


def main():

    client = connect_to_server()

    thread = Thread(target=threadfun, args=(client, ))
    thread.daemon = True
    thread.start()

    k = 0

    while True:

        try:

            client.send((chr(65+k) + '\n').encode())
            k = (k + 1) % 26
            sleep(.01)

        except KeyboardInterrupt:
            break

main()
