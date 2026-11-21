from src.core.wot_offsets import CURRENT, WotOffsets


def test_offsets_are_aligned():
    assert isinstance(CURRENT, WotOffsets)
    assert CURRENT.entity_list % 4 == 0
    assert CURRENT.view_matrix > CURRENT.entity_list  # rough sanity