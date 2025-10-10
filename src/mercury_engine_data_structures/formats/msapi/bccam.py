from __future__ import annotations

from typing import TYPE_CHECKING

import construct
from construct.core import (
    Const,
    Construct,
    Int32sl,
    Int32ul,
    Int64ul,
    Pointer,
    Struct,
)

from mercury_engine_data_structures.base_resource import BaseResource
from mercury_engine_data_structures.common_types import CVectorConstruct, Float, StrId
from mercury_engine_data_structures.formats.msapi.common_msapi import LinkedList
from mercury_engine_data_structures.formats.msapi.msapi import MsapiPointer, StandardModelMsapi

if TYPE_CHECKING:
    from mercury_engine_data_structures.game_check import Game

CameraAnimation = Struct(
    "_name" / Int64ul,
    "name" / Pointer(construct.this._name, StrId),
    "unk1" / Int32ul,
    "frames" / Float,  # num frames, always int, at 30fps
    "pos" / CVectorConstruct(3),
    "rot" / CVectorConstruct(3),
    "scale" / CVectorConstruct(3),
    "_pad" / Const(-1, Int32sl),
    "_pUnk2" / Int64ul,
    "pVec1" / Pointer(construct.this._pUnk2, CVectorConstruct(3)),
    "vec2" / CVectorConstruct(3),
    "unk2" / Const(1.0, Float),
    "unk3" / Const(1000.0, Float),
    "_pad2" / Const(-1, Int32sl),
    "ptr1" / Int64ul,  # size 0x18 (ptr, ptr?, ptr?)
    "ptr2" / Int64ul,  # size 0x18 (ptr, ptr, ptr)
    "ptr3" / Int64ul,  # size 0x20, req?, (int32, int32, int32, unk32, float, pad32, ptr)
    "ptr4" / Int64ul,  # size 0x20, req?, (int32, int32, int32, unk32, float, pad32, ptr)
    "ptr5" / Int64ul,
    "ptr6" / Int64ul,
    "ptr7" / Int64ul,
)


CameraAnims = Struct("anims" / MsapiPointer(LinkedList(CameraAnimation)))

BCCAM = StandardModelMsapi(b"MCAN", "1.4.0", CameraAnims)


class Bccam(BaseResource):
    @classmethod
    def construct_class(cls, target_game: Game) -> Construct:
        return BCCAM
