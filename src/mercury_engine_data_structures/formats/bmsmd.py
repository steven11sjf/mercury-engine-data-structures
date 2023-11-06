import functools
from construct.core import (
    Array,
    Const,
    Construct,
    Float32l,
    Hex,
    Int32sl,
    Int32ul,
    Struct,
)

from mercury_engine_data_structures.common_types import StrId, make_vector
from mercury_engine_data_structures.formats import BaseResource
from mercury_engine_data_structures.game_check import Game

BMSMD = Struct(
    "_magic" / Const(b"MSMD"),
    "version" / Const(0x000D0001, Hex(Int32ul)),
    "map_data" / make_vector(Struct(
        "icon" / StrId,
        "scenarios" / make_vector(Struct(
            "name" / StrId,
            "unk1" / Hex(Int32ul),
            "unk2" / Hex(Int32ul),
            "unk3" / Hex(Int32ul),
            "unk4" / Hex(Int32ul),
            "unk5" / Hex(Int32ul),
            "unk6" / Hex(Int32ul),
            "number_of_tiles" / Int32ul,
            "unk7" / Hex(Int32ul),
            "unk8" / Hex(Int32ul),
            "coordinates" / Array(2, Int32ul),
            "sub_scenarios" / make_vector(Struct(
                "name" / StrId,
                "unk1" / Float32l,
                "unk2" / Float32l,
                "coordinates" / Array(2, Int32sl),
            )),
        )),
    )),
)

class Bmsmd(BaseResource):
    @classmethod
    @functools.lru_cache
    def construct_class(cls, target_game: Game) -> Construct:
        return BMSMD