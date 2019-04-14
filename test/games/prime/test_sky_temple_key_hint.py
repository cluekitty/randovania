from randovania.game_description.resources.pickup_index import PickupIndex
from randovania.games.prime import echoes_items
from randovania.games.prime.patcher_file_lib import sky_temple_key_hint
from randovania.resolver.item_pool import pickup_creator


def test_create_hints_all_placed(empty_patches, echoes_game_description):
    # Setup
    patches = empty_patches.assign_new_pickups([
        (PickupIndex(17 + key), pickup_creator.create_sky_temple_key(key, echoes_game_description.resource_database))
        for key in range(9)
    ])
    expected = [
        {"asset_id": 0xD97685FE,
         "strings": ["The 1st Sky Temple Key is located in Temple Grounds - Profane Path"]},
        {"asset_id": 0x32413EFD,
         "strings": ["The 2nd Sky Temple Key is located in Temple Grounds - Phazon Grounds"]},
        {"asset_id": 0xDD8355C3,
         "strings": ["The 3rd Sky Temple Key is located in Temple Grounds - Ing Reliquary"]},
        {"asset_id": 0x3F5F4EBA,
         "strings": ["The 4th Sky Temple Key is located in Great Temple - Transport A Access"]},
        {"asset_id": 0xD09D2584,
         "strings": ["The 5th Sky Temple Key is located in Great Temple - Temple Sanctuary"]},
        {"asset_id": 0x3BAA9E87,
         "strings": ["The 6th Sky Temple Key is located in Great Temple - Transport B Access"]},
        {"asset_id": 0xD468F5B9,
         "strings": ["The 7th Sky Temple Key is located in Great Temple - Main Energy Controller"]},
        {"asset_id": 0x2563AE34,
         "strings": ["The 8th Sky Temple Key is located in Great Temple - Main Energy Controller"]},
        {"asset_id": 0xCAA1C50A,
         "strings": ["The 9th Sky Temple Key is located in Agon Wastes - Mining Plaza"]},
    ]

    # Run
    result = sky_temple_key_hint.create_hints(patches, echoes_game_description.world_list)

    # Assert
    assert result == expected


def test_create_hints_all_starting(empty_patches, echoes_game_description):
    # Setup
    patches = empty_patches.assign_extra_initial_items({
        echoes_game_description.resource_database.get_item(echoes_items.SKY_TEMPLE_KEY_ITEMS[key]): 1
        for key in range(9)
    })
    expected = [
        {"asset_id": 0xD97685FE,
         "strings": ["The 1st Sky Temple Key has no need to be located."]},
        {"asset_id": 0x32413EFD,
         "strings": ["The 2nd Sky Temple Key has no need to be located."]},
        {"asset_id": 0xDD8355C3,
         "strings": ["The 3rd Sky Temple Key has no need to be located."]},
        {"asset_id": 0x3F5F4EBA,
         "strings": ["The 4th Sky Temple Key has no need to be located."]},
        {"asset_id": 0xD09D2584,
         "strings": ["The 5th Sky Temple Key has no need to be located."]},
        {"asset_id": 0x3BAA9E87,
         "strings": ["The 6th Sky Temple Key has no need to be located."]},
        {"asset_id": 0xD468F5B9,
         "strings": ["The 7th Sky Temple Key has no need to be located."]},
        {"asset_id": 0x2563AE34,
         "strings": ["The 8th Sky Temple Key has no need to be located."]},
        {"asset_id": 0xCAA1C50A,
         "strings": ["The 9th Sky Temple Key has no need to be located."]},
    ]

    # Run
    result = sky_temple_key_hint.create_hints(patches, echoes_game_description.world_list)

    # Assert
    assert result == expected
