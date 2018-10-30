# pylint: disable=W0621, W0105

from __future__ import print_function
import sys
import getopt

# import Checksum
import BasicSender

"""
This is a skeleton sender class. Create a fantastic transport protocol here.
"""

""" TODO
To initiate a connection, send a syn message with any initial sequence number.
After sending the syn message,
    the sender waits for an ack packet to finish a handshake
After the handshake,
    send actual data packets in the same connection using the data
    message type, adjusting the sequence number appropriately.
    the last data in a connection should be transmitted with the fin message
    type to signal the receiver that the connection is complete.

should split the input file into appropriately sized chunks of data,
specify an initial sequence number for the connection,
and append a checksum to each packet. The sequence number
should increment by one for each additional packet in a connection.
Functions for generating and validating packet checksums will be provided
for you (see Checksum.py).

Your sender should provide reliable service under the following network conditions:
- Loss: arbitrary levels; you should be able to handle periods of 100% packet loss.
- Corruption: arbitrary types and frequency.
- Re-ordering: may arrive in any order, and
- Duplication: you could see a packet any number of times.
- Delay: packets may be delayed indefinitely (but in practice, generally not more than
10s).

Your sender should be invoked with the following command:
python Sender.py -f <input file>

The sender should implement a 500ms retransmission timer to automatically
retransmit packets that were never acknowledged (potentially due to ack packets
being lost). We do not expect you to use an adaptive timeout.
Your sender should support a window size of 7 packets (i.e., 7 unacknowledged
packets).
Your sender should roughly meet or exceed the performance (in both time and number
of packets required to complete a transfer) of a properly implemented Go Back N based
BEARS-TP sender.
Your sender should be able to handle arbitrary message data (i.e., it should be able to
send an image file just as easily as a text file).
Any packets received with an invalid checksum should be ignored.
"""


class Sender(BasicSender.BasicSender):
    def __init__(self, dest, port, filename, debug=False, sackMode=False):
        super(Sender, self).__init__(dest, port, filename, debug)
        self.sackMode = sackMode
        self.debug = debug

    # Main sending loop.
    def start(self):
        # add things here
        pass


'''
This will be run if you run this script from the command line. You should not
change any of this; the grader may rely on the behavior here to test your
submission.
'''
if __name__ == "__main__":
    def usage():
        print("BEARS-TP Sender")
        print("-f FILE | --file=FILE The file to transfer; if empty reads from STDIN")
        print("-p PORT | --port=PORT The destination port, defaults to 33122")
        print("-a ADDRESS | --address=ADDRESS The receiver address or hostname, defaults to localhost")
        print("-d | --debug Print debug messages")
        print("-h | --help Print this usage message")
        print("-k | --sack Enable selective acknowledgement mode)")

    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "f:p:a:dk", ["file=", "port=", "address=", "debug=", "sack="])
    except BaseException:
        usage()
        exit()

    port = 33122
    dest = "localhost"
    filename = None
    debug = True
    sackMode = False

    for o, a in opts:
        if o in ("-f", "--file="):
            filename = a
        elif o in ("-p", "--port="):
            port = int(a)
        elif o in ("-a", "--address="):
            dest = a
        elif o in ("-d", "--debug="):
            debug = True
        elif o in ("-k", "--sack="):
            sackMode = True

    s = Sender(dest, port, filename, debug, sackMode)
    try:
        s.start()
    except (KeyboardInterrupt, SystemExit):
        exit()
