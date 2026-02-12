import pytest
from backend.services.ton_mile_engine import TonMileEngine

def test_calculate_round_trip_basic():
    # Example values:
    # Depth = 10000 ft
    # Stand length = 90 ft
    # Pipe weight in mud = 20 lbs/ft (nominal + buoyancy)
    # Block weight = 15000 lbs
    # Collar weight in mud = 100 lbs/ft
    # Collar length = 600 ft
    
    # C = 600 * (100 - 20) = 48000
    # Numerator = 10000 * (90 + 10000) * 20 + 4 * 10000 * (15000 + 0.5 * 48000)
    # Numerator = 10000 * 10090 * 20 + 40000 * (15000 + 24000)
    # Numerator = 2018000000 + 40000 * 39000
    # Numerator = 2018000000 + 1560000000 = 3578000000 ft-lbs
    
    # Ton-Miles = 3578000000 / (5280 * 2000) = 3578000000 / 10560000 = 338.8257...
    
    tm = TonMileEngine.calculate_round_trip(10000, 90, 20, 15000, 100, 600)
    assert round(tm, 1) == 338.8
