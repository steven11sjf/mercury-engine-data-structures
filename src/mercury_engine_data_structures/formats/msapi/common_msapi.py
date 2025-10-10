from __future__ import annotations

from construct.core import Construct, Int64ul, SizeofError, Struct, Subconstruct
from construct.lib.containers import Container, ListContainer

from mercury_engine_data_structures.formats.msapi.msapi import MsapiPointer

# TODO combine this into msapi.py, or bring MsapiPointer over here and rename other file standard_msapi.py or similar


def LinkedListNode(el_type: Construct):
    return Struct("val" / MsapiPointer(el_type), "next" / Int64ul)


class LinkedList(Subconstruct):
    """
    A linked-list of Int64ul pointers that"""

    def __init__(self, element_type):
        super().__init__(LinkedListNode(element_type))
        self.el_type = element_type

    def _parse(self, stream, context, path):
        res = []

        while True:
            node = self.subcon._parse(stream, context, path)
            res.append(node["val"])

            if node["next"] == 0:
                return Container(vals=ListContainer(res))
            elif node["next"] != stream.tell():
                raise ValueError(f"Linked List goes out of order: expected {node[1]}, got {stream.tell()}")

    def _build(self, obj, stream, context, path):
        for val in obj.vals[:-1]:
            node = {"val": val, "next": stream.tell() + 0x10}
            self.subcon._build(node, stream, context, path)

        self.subcon._build({"val": obj.vals[-1], "next": 0}, stream, context, path)

    def _sizeof(self, context, path):
        return SizeofError("LinkedList has a dynamic size!")
