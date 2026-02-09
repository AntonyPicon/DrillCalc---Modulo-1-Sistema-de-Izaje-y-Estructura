import pytest
from backend.services.hoisting_engine import HoistingEngine

def test_calculate_efficiency_standard():
    # Test with standard values: N=12, S=15, K=1.04
    eff = HoistingEngine.calculate_efficiency(12, 15, 1.04)
    # Expected theoretical value is ~0.695 based on formula
    assert 0.69 <= eff <= 0.70

def test_calculate_efficiency_invalid_k():
    with pytest.raises(ValueError):
        HoistingEngine.calculate_efficiency(12, 15, 1.0)

def test_calculate_fast_line_tension():
    # W=250000, N=12, eff=0.695
    fast_line = HoistingEngine.calculate_fast_line_tension(250000, 12, 0.69527)
    # 250000 / (12 * 0.69527) = 29964.37...
    assert round(fast_line, 1) == 29964.4

def test_calculate_dead_line_load():
    dead_line = HoistingEngine.calculate_dead_line_load(250000, 12)
    assert round(dead_line, 2) == 20833.33

def test_calculate_derrick_load():
    # W=250000, F_fast=30000, F_dead=21000
    derrick_load = HoistingEngine.calculate_derrick_load(250000, 30000, 21000)
    assert derrick_load == 301000

def test_determine_alert_level():
    assert HoistingEngine.determine_alert_level(4.0) == "SAFE"
    assert HoistingEngine.determine_alert_level(2.5) == "CAUTION"
    assert HoistingEngine.determine_alert_level(1.5) == "DANGER"
