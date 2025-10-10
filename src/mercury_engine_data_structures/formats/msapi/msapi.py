from __future__ import annotations

import construct
from construct.core import (
    Const,
    Construct,
    Int64ul,
    Subconstruct,
    stream_size,
)
from construct.lib.containers import Container

from mercury_engine_data_structures.common_types import StrId, VersionAdapter


# construct.setGlobalPrintPrivateEntries(True)
class MsapiPointer(Subconstruct):
    def __init__(self, subcon, nullable=False):
        super().__init__(Int64ul)
        self.nullable = nullable
        self.inner_type = subcon

    def _parse(self, stream, context, path):
        context._root = context._.get("_root", context)
        assert hasattr(context._root, "_structures")
        structures = context._root._structures

        offset = self.subcon._parse(stream, context, path)

        if offset == 0:
            if self.nullable:
                return None
            else:
                raise ValueError(
                    f"MsapiPointer of type {self.inner_type} is not nullable but encountered a null value! {{path}}"
                )

        if offset not in structures.keys():
            structures[offset] = (construct.evaluate(self.inner_type, context), Container())

        return structures[offset][1]

    def _build(self, obj, stream, context, path):
        root = context.get("_root", context)
        assert hasattr(root, "_to_build")
        to_build = root._to_build
        assert hasattr(root, "_pointers")
        pointers = root._pointers

        if obj is None:
            if self.nullable:
                self.subcon._build(0, stream, context, path)
                return
            else:
                raise ValueError(
                    f"MsapiPointer of type {self.inner_type} is not nullable but is building a None value!"
                )

        curr = stream.tell()
        to_build.append((obj, construct.evaluate(self.inner_type, context)))
        pointers[curr] = obj
        self.subcon._build(0, stream, context, path)

        return curr


class StandardModelMsapi(Subconstruct):
    def __init__(self, magic, version: int | str | tuple[int, int, int] | None, root: Construct):
        super().__init__(root)
        self.magic = magic
        self.version = version

    def _parse(self, stream, context, path):
        structures: dict[int, tuple[Construct, Container]] = {}
        context._root = context
        root = context._root
        root._structures = structures

        size = stream_size(stream)

        Const(self.magic)._parse(stream, context, path)
        ver = VersionAdapter(self.version)._parse(stream, context, path)
        root.version = ver

        # when parsing, we will read from the offsets directly
        # so that we can parse valid input in nonstandard order

        root = self.subcon._parse(stream, context, path)
        off = stream.tell()
        remaining = {k: v for k, v in structures.items() if off <= k}

        while remaining:
            if off in structures.keys():
                print(f"Parsing {structures[off][0].__class__.__name__} at {off:X}")
                r = structures[off][0]._parse(stream, context, path)
                if structures[off][0] is StrId:
                    r = Container(val=r)
                structures[off][1].update(r)
                off = stream.tell()
                remaining = {k: v for k, v in structures.items() if off <= k}

            else:
                if off < size:
                    off += 1
                    stream.read(1)
                else:
                    raise ValueError(f"Structures remain, but reached EOF ({off})")

        return Container(version=ver, root=root)

    def _build(self, obj, stream, context, path):
        # TODO fix :)
        context._root = context
        root = context._root

        to_build: list[tuple[Container, Construct]] = []
        root._to_build = to_build
        offsets: dict[int, int] = {}
        root._offsets = offsets
        pointers: dict[int, Container] = {}
        root._pointers = pointers  # dict[int, Container] - all offsets in the file and what they point to

        Const(self.magic)._build(None, stream, context, path)
        VersionAdapter(self.version)._build(obj.version, stream, context, path)

        self.subcon._build(obj.root, stream, context, path)

        while len(to_build) != 0:
            (val, con) = to_build.pop(0)
            # align non-strings
            if con is not StrId and (cur := stream.tell() % 8) != 0:
                Const(b"\xff" * (8 - cur))._build(None, stream, context, path)

            if con is StrId:
                val = val.val

            offsets[id(val)] = stream.tell()
            con._build(val, stream, context, path)

        for off, val in pointers.items():
            stream.seek(off)
            print(val)
            Int64ul._build(offsets[id(val)], stream, context, path)

        return context
