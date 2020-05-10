import signal
import os
import daemon as dm
from HW8.master_worker import run_server


def receive_signal(signalNumber, frame):
    print('Received:', signalNumber)
    raise SystemExit('Exiting')
    return


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 10001
    signal.signal(signal.SIGUSR1, receive_signal)
    print('My PID is:', os.getpid())
    with dm.DaemonContext():
        run_server(host, port)
