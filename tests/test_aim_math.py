from src.features.aim_assist.aim_module import AimModule


def test_aim_module_defaults():
    m = AimModule()
    assert m.enabled is True
    assert 0.0 < m.smoothing < 1.0


def test_aim_tick_no_proc_is_noop():
    m = AimModule()
    m.tick(None)  # must not raise
</testing>