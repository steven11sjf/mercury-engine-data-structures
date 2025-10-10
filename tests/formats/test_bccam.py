from __future__ import annotations

import pytest

from mercury_engine_data_structures import dread_data
from mercury_engine_data_structures.formats.bccam import Bccam


@pytest.mark.parametrize("bccam_path", dread_data.all_files_ending_with(".bccam"))
def test_bapd_100(dread_tree_100, bccam_path):
    construct_class = Bccam.construct_class(dread_tree_100.target_game)
    raw = dread_tree_100.get_raw_asset(bccam_path)

    data = construct_class.parse(raw, target_game=dread_tree_100.target_game)
    assert data == 0
