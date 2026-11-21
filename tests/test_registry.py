from src.core.registry import build_default_registry


def test_default_registry_has_all_modules():
    reg = build_default_registry()
    names = {m.name for m in reg.modules()}
    assert "aim_assist" in names
    assert "esp_radar" in names


def test_filter_to():
    reg = build_default_registry()
    reg.filter_to(["esp_radar"])
    assert len(reg) == 1
    assert reg.modules()[0].name == "esp_radar"