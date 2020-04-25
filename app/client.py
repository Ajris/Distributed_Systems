from proto import meeting_pb2_grpc, meeting_pb2

from grpc._channel import _MultiThreadedRendezvous
import grpc
import sys
import time
import asyncio
import threading
import time

channel = grpc.insecure_channel('localhost:50051')
stub = meeting_pb2_grpc.MeetingServiceStub(channel)

def run(cities):
    threads = []

    for city in cities[1:]:
        t = threading.Thread(target=connectToOneCity, args = (city,))
        threads.append(t)
        t.start()


def connectToOneCity(city):
    subscriptionRequest = meeting_pb2.SubscriptionRequest(city=city)
    stream = stub.MeetingStream(subscriptionRequest)

    try:
        for f in stream:
            print(f)
    except _MultiThreadedRendezvous:
        print('Cant reach server')
        time.sleep(1)
        connectToOneCity(city)
    except:
        print('Client finishing')

if(len(sys.argv) == 1):
    print('Give at least one argument')
else:
    run(sys.argv)
