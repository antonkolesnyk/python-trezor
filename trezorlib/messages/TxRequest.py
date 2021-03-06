# Automatically generated by pb2py
from __future__ import absolute_import
from .. import protobuf as p
from .TxRequestDetailsType import TxRequestDetailsType
from .TxRequestSerializedType import TxRequestSerializedType


class TxRequest(p.MessageType):
    FIELDS = {
        1: ('request_type', p.UVarintType, 0),
        2: ('details', TxRequestDetailsType, 0),
        3: ('serialized', TxRequestSerializedType, 0),
    }
    MESSAGE_WIRE_TYPE = 21
