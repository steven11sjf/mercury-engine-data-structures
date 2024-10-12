import pytest
from tests.test_lib import parse_build_compare_editor

from mercury_engine_data_structures import dread_data
from mercury_engine_data_structures.formats.brfld import ActorLayer, Brfld

bossrush_assets = [
    "maps/levels/c10_samus/s201_bossrush_scorpius/s201_bossrush_scorpius.brfld",
    "maps/levels/c10_samus/s202_bossrush_kraid/s202_bossrush_kraid.brfld",
    "maps/levels/c10_samus/s203_bossrush_cu_artaria/s203_bossrush_cu_artaria.brfld",
    "maps/levels/c10_samus/s204_bossrush_drogyga/s204_bossrush_drogyga.brfld",
    "maps/levels/c10_samus/s205_bossrush_strong_rcs/s205_bossrush_strong_rcs.brfld",
    "maps/levels/c10_samus/s206_bossrush_escue/s206_bossrush_escue.brfld",
    "maps/levels/c10_samus/s207_bossrush_cooldownx/s207_bossrush_cooldownx.brfld",
    "maps/levels/c10_samus/s208_bossrush_strong_rcs_x2/s208_bossrush_strong_rcs_x2.brfld",
    "maps/levels/c10_samus/s209_bossrush_golzuna/s209_bossrush_golzuna.brfld",
    "maps/levels/c10_samus/s210_bossrush_elite_cwx/s210_bossrush_elite_cwx.brfld",
    "maps/levels/c10_samus/s211_bossrush_cu_ferenia/s211_bossrush_cu_ferenia.brfld",
    "maps/levels/c10_samus/s212_bossrush_commander/s212_bossrush_commander.brfld",
]


@pytest.mark.parametrize("brfld_path", dread_data.all_files_ending_with(".brfld", bossrush_assets))
def test_dread_brfld_100(dread_tree_100, brfld_path):
    parse_build_compare_editor(Brfld, dread_tree_100, brfld_path)


@pytest.mark.parametrize("brfld_path", bossrush_assets)
def test_dread_brfld_210(dread_tree_210, brfld_path):
    parse_build_compare_editor(Brfld, dread_tree_210, brfld_path)


def test_add_actor_to_actor_groups(dread_tree_100):
    scenario = dread_tree_100.get_file("maps/levels/c10_samus/s010_cave/s010_cave.brfld", Brfld)

    scenario.add_actor_to_actor_groups("eg_collision_camera_000", "breakabletilegroup_000", "breakables")
    assert scenario.is_actor_in_group("eg_collision_camera_000_Default", "breakabletilegroup_000", "breakables")

    scenario.add_actor_to_actor_groups(
        "ssg_collision_camera_000", "Pos_C_LavaWindow_06", actor_layer=ActorLayer.SOUNDS
    )
    assert scenario.is_actor_in_group(
        "ssg_collision_camera_000_Default", "Pos_C_LavaWindow_06", actor_layer=ActorLayer.SOUNDS
    )

    scenario.add_actor_to_actor_groups(
        "lg_collision_camera_000", "cubemap_006_1_bake", "emmy_006_light", ActorLayer.LIGHTS
    )
    assert scenario.is_actor_in_group(
        "lg_collision_camera_000", "cubemap_006_1_bake", "emmy_006_light", ActorLayer.LIGHTS
    )
