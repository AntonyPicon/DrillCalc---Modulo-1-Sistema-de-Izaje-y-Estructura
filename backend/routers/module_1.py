"""
DrillCalc - Module 1: Hoisting System & Structure
Author: Antony Picon, Mechanical Engineer
Description: Router definitions for Hoisting System calculations.
"""
from fastapi import APIRouter, HTTPException
from backend.schemas import HoistingInput, HoistingOutput
from backend.services.hoisting_engine import HoistingEngine

router = APIRouter(prefix="/module-1", tags=["Module 1: Hoisting & Structure"])

@router.post("/calculate", response_model=HoistingOutput)
async def calculate_hoisting_system(data: HoistingInput):
    """
    Calculates Hoisting System parameters based on API 4F/9B standards.
    """
    try:
        # 1. Calculate Efficiency
        # Note: API 4F usually assumes N lines string-up.
        # N = data.lines
        # S = data.sheaves
        # K = data.friction_factor
         
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
