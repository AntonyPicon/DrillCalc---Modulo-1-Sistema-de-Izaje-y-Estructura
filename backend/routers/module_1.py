"""
DrillCalc - Module 1: Hoisting System & Structure
Author: Antony Picon, Mechanical Engineer
Description: Router definitions for Hoisting System calculations.
"""
from fastapi import APIRouter, HTTPException
from backend.schemas import HoistingInput, HoistingOutput, TonMileInput, TonMileOutput
from backend.services.hoisting_engine import HoistingEngine
from backend.services.ton_mile_engine import TonMileEngine

router = APIRouter(prefix="/module-1", tags=["Module 1: Hoisting & Structure"])

@router.post("/calculate", response_model=HoistingOutput)
async def calculate_hoisting_system(data: HoistingInput):
    """
    Calculates Hoisting System parameters based on API 4F/9B standards.
    """
    try:
        # 1. Calculate Efficiency
        efficiency = HoistingEngine.calculate_efficiency(data.lines, data.sheaves, data.friction_factor)

        # 2. Calculate Fast Line Tension
        fast_line_tension = HoistingEngine.calculate_fast_line_tension(data.hook_load, data.lines, efficiency)

        # 3. Calculate Dead Line Load
        dead_line_load = HoistingEngine.calculate_dead_line_load(data.hook_load, data.lines)

        # 4. Calculate Derrick Load
        derrick_load = HoistingEngine.calculate_derrick_load(data.hook_load, fast_line_tension, dead_line_load)

        # 5. Calculate Safety Factor
        safety_factor = HoistingEngine.calculate_safety_factor(data.wire_strength, fast_line_tension)

        # 6. Determine Alert Level
        alert_level = HoistingEngine.determine_alert_level(safety_factor)

        return HoistingOutput(
            efficiency=efficiency,
            fast_line_tension=fast_line_tension,
            dead_line_load=dead_line_load,
            derrick_load=derrick_load,
            safety_factor=safety_factor,
            alert_level=alert_level
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error during calculation.")

@router.post("/calculate-ton-mile", response_model=TonMileOutput)
async def calculate_ton_mile(data: TonMileInput):
    """
    Calculates Ton-Miles for a Round Trip based on API RP 9B.
    """
    try:
        ton_miles = TonMileEngine.calculate_round_trip(
            depth=data.depth,
            stand_length=data.stand_length,
            pipe_weight_mud=data.pipe_weight_mud,
            block_weight=data.block_weight,
            collar_weight_mud=data.collar_weight_mud,
            collar_length=data.collar_length
        )
        return TonMileOutput(ton_miles=ton_miles)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calculating Ton-Mile: {str(e)}")

