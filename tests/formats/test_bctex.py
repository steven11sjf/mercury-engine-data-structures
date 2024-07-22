import pytest
from tests.test_lib import parse_build_compare_editor_parsed

from mercury_engine_data_structures import dread_data, samus_returns_data
from mercury_engine_data_structures.formats.bctex import Bctex

sr_missing = [
    "actors/characters/alpha/models/textures/alphab_a.bctex",
    "actors/characters/alpha/models/textures/alphab_d.bctex",
    "actors/characters/alphacredits/models/textures/alphab_a.bctex",
    "actors/characters/alphacredits/models/textures/alphab_d.bctex",
    "actors/characters/gamma/models/textures/coreveins.bctex",
    "actors/characters/gammacredits/models/textures/coreveins.bctex",
    "actors/characters/gammaevolved/models/textures/coreveins.bctex",
    "actors/characters/glowflypuzzle/models/textures/glowfly_d.bctex",
    "actors/characters/metroid/models/textures/coreveins.bctex",
    "actors/characters/moheekwall/models/textures/moheekwall_a.bctex",
    "actors/characters/morphball/models/textures/fusionmorph_a.bctex",
    "actors/characters/morphball/models/textures/fusionmorphgravity_d.bctex",
    "actors/characters/morphball/models/textures/fusionmorphpower_d.bctex",
    "actors/characters/morphball/models/textures/fusionmorphvaria_d.bctex",
    "actors/characters/morphball/models/textures/samuspowermorphnew_a.bctex",
    "actors/characters/morphball/models/textures/samuspowermorphnew_d.bctex",
    "actors/characters/morphball/models/textures/samusvariamorph_a.bctex",
    "actors/characters/morphball/models/textures/samusvariamorph_d.bctex",
    "actors/characters/omega/models/textures/coreveins.bctex",
    "actors/characters/omegacredits/models/textures/coreveins.bctex",
    "actors/characters/omegaevolved/models/textures/coreveins.bctex",
    "actors/characters/queen/models/textures/coreveins.bctex",
    "actors/characters/queen/models/textures/queen01_a.bctex",
    "actors/characters/queen/models/textures/queen01_d.bctex",
    "actors/characters/queen/models/textures/queen02_a.bctex",
    "actors/characters/queen/models/textures/queen02_d.bctex",
    "actors/characters/queen/models/textures/queen03_a.bctex",
    "actors/characters/queen/models/textures/queen03_d.bctex",
    "actors/characters/queen/models/textures/queen04_a.bctex",
    "actors/characters/queen/models/textures/queen04_d.bctex",
    "actors/characters/ridley/models/textures/ridleydeath_d.bctex",
    "actors/characters/ridley/models/textures/ridleyhand_a.bctex",
    "actors/characters/ridley/models/textures/ridleyhand_d.bctex",
    "actors/characters/samus/models/textures/energywave.bctex",
    "actors/characters/samus/models/textures/gradientdif.bctex",
    "actors/characters/samus/models/textures/grid.bctex",
    "actors/characters/samus/models/textures/noise3.bctex",
    "actors/characters/samus/models/textures/samusending_a.bctex",
    "actors/characters/samus/models/textures/samusending_d.bctex",
    "actors/characters/samus/models/textures/samusgravityreward_d.bctex",
    "actors/characters/samus/models/textures/samusweaponreward_d.bctex",
    "actors/characters/samus/models/textures/samuszeroreward_a.bctex",
    "actors/characters/samus/models/textures/samuszeroreward_d.bctex",
    "actors/characters/samus/models/textures/samuszeroweapon_d.bctex",
    "actors/characters/samusfusion/models/textures/droppables00.bctex",
    "actors/characters/samusfusion/models/textures/droppables01.bctex",
    "actors/characters/samusfusion/models/textures/energywave.bctex",
    "actors/characters/samusfusion/models/textures/gradientdif.bctex",
    "actors/characters/samusfusion/models/textures/grid.bctex",
    "actors/characters/samusfusion/models/textures/laser_la.bctex",
    "actors/characters/samusfusion/models/textures/noise3.bctex",
    "actors/characters/samusfusion/models/textures/phasedisplacement.bctex",
    "actors/characters/samusfusion/models/textures/scanningpulse.bctex",
    "actors/characters/samusrewards/models/textures/energywave.bctex",
    "actors/characters/samusrewards/models/textures/gradientdif.bctex",
    "actors/characters/samusrewards/models/textures/grid.bctex",
    "actors/characters/samusrewards/models/textures/laser_la.bctex",
    "actors/characters/samusrewards/models/textures/noise3.bctex",
    "actors/characters/samusrewards/models/textures/phasedisplacement.bctex",
    "actors/characters/samusrewards/models/textures/samusending_a.bctex",
    "actors/characters/samusrewards/models/textures/samusending_d.bctex",
    "actors/characters/samusrewards/models/textures/samuspower_a.bctex",
    "actors/characters/samusrewards/models/textures/samuspower_d.bctex",
    "actors/characters/samusrewards/models/textures/samusvaria_a.bctex",
    "actors/characters/samusrewards/models/textures/samusvaria_d.bctex",
    "actors/characters/samusrewards/models/textures/samuszeroreward_a.bctex",
    "actors/characters/samusrewards/models/textures/samuszeroweapon_d.bctex",
    "actors/characters/samusrewards/models/textures/scanningpulse.bctex",
    "actors/characters/zeta/models/textures/coreveins.bctex",
    "actors/characters/zetacredits/models/textures/coreveins.bctex",
    "actors/characters/zetaevolved/models/textures/coreveins.bctex",
    "actors/items/itemsphere_spenergygaunlet/models/textures/itemspherespenergygaunlet_d.bctex",
    "actors/items/powerup_spinattack/models/textures/itemvariasuit_d.bctex",
    "actors/props/blockingplant/models/textures/blockingplantheavy_d.bctex",
    "actors/props/creditsfx/models/textures/glow_big.bctex",
    "actors/props/creditsfx/models/textures/glowmetroid.bctex",
    "actors/props/creditsfx/models/textures/halowind.bctex",
    "actors/props/creditsfx/models/textures/xflaremetroid.bctex",
    "actors/props/doorcreatureleft/models/textures/doorcreature_d.bctex",
    "actors/props/doorcreatureleft/models/textures/spiderweb_d.bctex",
    "actors/props/dropprop/models/textures/dropprop_d.bctex",
    "actors/props/samusshipinterior/models/textures/samusship_bigpanel2.bctex",
    "actors/props/spenergybestowalstatue/models/textures/spenergybestowalstatue_d.bctex",
    "actors/weapons/manicminerbotlaser/models/textures/target_circle.bctex",
    "actors/weapons/weaponstank/models/textures/tankglow.bctex",
    "actors/weapons/weaponstank/models/textures/weaponstank_d.bctex",
    "cutscenes/postcredits/models/xparasite/textures/cubemetroids.bctex",
    "maps/blocks/weightblock/textures/weightblock_d.bctex",
    "maps/objects/chozohologram/textures/chozohologram_d.bctex",
    "maps/textures/a1wall01.bctex",
    "maps/textures/a2chozocolumn0301_d.bctex",
    "maps/textures/a6chozocolumn01_d.bctex",
    "maps/textures/a6chozocolumn0204_d.bctex",
    "maps/textures/a9chozobg0301_d.bctex",
    "maps/textures/brick_wall00.bctex",
    "maps/textures/chozohologram01_d.bctex",
    "maps/textures/chozointeriortile04.bctex",
    "maps/textures/chozopath0902_d.bctex",
    "maps/textures/chozopath1002_d.bctex",
    "maps/textures/chozotilewall01b_d.bctex",
    "maps/textures/chozotilewall04haz_d.bctex",
    "maps/textures/chozoverticaldeco01_d.bctex",
    "maps/textures/clear_blue_checker.bctex",
    "maps/textures/dark_grey_checker.bctex",
    "maps/textures/debris0301_d.bctex",
    "maps/textures/green_d.bctex",
    "maps/textures/insect0702_d.bctex",
    "maps/textures/lava2.bctex",
    "maps/textures/light_grey_checker.bctex",
    "maps/textures/plant0103_d.bctex",
    "maps/textures/plant0607_d.bctex",
    "maps/textures/ref_rock03.bctex",
    "maps/textures/ref_rock05.bctex",
    "maps/textures/rock_wall01_d.bctex",
    "maps/textures/rock_wall02.bctex",
    "maps/textures/rockadorn0604cut_d.bctex",
    "maps/textures/rockadornchozo0303_d.bctex",
    "maps/textures/rockadornchozo0306_d.bctex",
    "maps/textures/rockadorngold0303_d.bctex",
    "maps/textures/rockadorngold0306_d.bctex",
    "maps/textures/rockbg0601.bctex",
    "maps/textures/rockcolumn0301_d.bctex",
    "maps/textures/rockcolumn04.bctex",
    "maps/textures/rockplatform0101_d.bctex",
    "maps/textures/rockplatform0405b_d.bctex",
    "maps/textures/rockplatform1002c_d.bctex",
    "maps/textures/rockwall0302_d.bctex",
    "maps/textures/rockwall0402b_d.bctex",
    "maps/textures/rockwalltile0604.bctex",
    "maps/textures/rockwalltile0702c_d.bctex",
    "maps/textures/sand02_d.bctex",
    "maps/textures/smoke0002_d.bctex",
    "maps/textures/spaceblackhole_d.bctex",
    "maps/textures/surface_sky.bctex",
    "maps/textures/surfacebray2c_d.bctex",
    "maps/textures/surfacecolumn01.bctex",
    "maps/textures/temp/cubemetroids.bctex",
    "maps/textures/wall06.bctex",
    "maps/textures/water10b_d.bctex",
    "maps/textures/waterfall.bctex",
    "maps/textures/waterfront01_d.bctex",
    "maps/textures/waterop.bctex",
    "system/fx/textures/arc.bctex",
    "system/fx/textures/arrow3.bctex",
    "system/fx/textures/ashes_la.bctex",
    "system/fx/textures/blood_red.bctex",
    "system/fx/textures/energy.bctex",
    "system/fx/textures/energybubble.bctex",
    "system/fx/textures/energyray.bctex",
    "system/fx/textures/energytrail.bctex",
    "system/fx/textures/fireball_l.bctex",
    "system/fx/textures/fireballbounce_l.bctex",
    "system/fx/textures/fireballbounce_rgba.bctex",
    "system/fx/textures/flame.bctex",
    "system/fx/textures/flameline.bctex",
    "system/fx/textures/fleechswarm.bctex",
    "system/fx/textures/laserfalloff_la.bctex",
    "system/fx/textures/lightning_fade.bctex",
    "system/fx/textures/lightningcore_l.bctex",
    "system/fx/textures/noise2.bctex",
    "system/fx/textures/ramp_bwbwb.bctex",
    "system/fx/textures/raypart_l.bctex",
    "system/fx/textures/specialab.bctex",
    "system/fx/textures/swarm.bctex",
    "system/fx/textures/swirl.bctex",
    "system/fx/textures/swirlcircle.bctex",
    "system/fx/textures/swirlexplosion.bctex",
    "system/fx/textures/target_l.bctex",
    "system/fx/textures/threadleak.bctex",
    "system/fx/textures/wind.bctex",
    "system/fx/textures/wind_arc.bctex",
]

@pytest.mark.parametrize("bctex_path", dread_data.all_files_ending_with(".bctex"))
def test_compare_dread(dread_file_tree, bctex_path):
    parse_build_compare_editor_parsed(Bctex, dread_file_tree, bctex_path)

@pytest.mark.parametrize("bctex_path", samus_returns_data.all_files_ending_with(".bctex", sr_missing))
def test_compare_sr(samus_returns_tree, bctex_path):
    parse_build_compare_editor_parsed(Bctex, samus_returns_tree, bctex_path)
