# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import meeting_pb2 as proto_dot_meeting__pb2


class MeetingServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MeetingStream = channel.unary_stream(
                '/meeting.MeetingService/MeetingStream',
                request_serializer=proto_dot_meeting__pb2.SubscriptionRequest.SerializeToString,
                response_deserializer=proto_dot_meeting__pb2.MeetingInfo.FromString,
                )


class MeetingServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def MeetingStream(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MeetingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MeetingStream': grpc.unary_stream_rpc_method_handler(
                    servicer.MeetingStream,
                    request_deserializer=proto_dot_meeting__pb2.SubscriptionRequest.FromString,
                    response_serializer=proto_dot_meeting__pb2.MeetingInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'meeting.MeetingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MeetingService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def MeetingStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/meeting.MeetingService/MeetingStream',
            proto_dot_meeting__pb2.SubscriptionRequest.SerializeToString,
            proto_dot_meeting__pb2.MeetingInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
