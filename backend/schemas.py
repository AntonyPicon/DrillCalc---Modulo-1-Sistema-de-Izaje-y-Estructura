"""
DrillCalc - Module 1: Hoisting System & Structure
Author: Antony Picon, Mechanical Engineer
Description: Pydantic schemas for the Hoisting System API.
"""
from pydantic import BaseModel, Field
from typing import Literal

class HoistingInput(BaseModel):
    """
    Input model for Hoisting System calculations based on API 4F/9B.
    """
    hook_load: float = Field(..., gt=0, description="Carga en el gancho (W_hook) en libras (lbs).")
    lines: int = Field(..., gt=0, description="Número de líneas guarnidas (N).")
    sheaves: int = Field(..., gt=0, description="Número total de poleas (S) en el sistema (Corona + Viajero).")
    friction_factor: float = Field(1.04, gt=1.0, description="Factor de fricción por polea (K). Típicamente 1.04 para rodamientos de rodillos.")
    wire_strength: float = Field(..., gt=0, description="Resistencia nominal a la ruptura del cable (LB_nom) en libras (lbs).")

class HoistingOutput(BaseModel):
    """
    Output model containing calculated values and safety assessment.
    """
    efficiency: float = Field(..., description="Eficiencia del sistema de izaje (eta).")
    fast_line_tension: float = Field(..., description="Tensión en la línea rápida (F_fast) en libras.")
    dead_line_load: float = Field(..., description="Carga en la línea muerta (F_dead) en libras.")
    derrick_load: float = Field(..., description="Carga total en la torre (F_derrick) en libras.")
    safety_factor: float = Field(..., description="Factor de Diseño o Seguridad (FD).")
    alert_level: Literal["DANGER", "CAUTION", "SAFE"] = Field(..., description="Nivel de alerta basado en el Factor de Seguridad.")

class TonMileInput(BaseModel):
    """
    Input model for Ton-Mile calculations (Round Trip).
    Ref: API RP 9B
    """
    depth: float = Field(..., gt=0, description="Profundidad actual (D) en pies (ft).")
    stand_length: float = Field(..., gt=0, description="Longitud del equipo/parada (L) en pies (ft).")
    pipe_weight_mud: float = Field(..., gt=0, description="Peso nominal del tubo en lodo (Wp) en lbs/ft.")
    block_weight: float = Field(..., gt=0, description="Peso del bloque (M) en lbs.")
    collar_weight_mud: float = Field(..., gt=0, description="Peso de los lastrabarrenas en lodo (Wc) en lbs/ft.")
    collar_length: float = Field(..., gt=0, description="Longitud de los lastrabarrenas (Lc) en pies (ft).")

class TonMileOutput(BaseModel):
    """
    Output model for Ton-Mile calculation result.
    """
    ton_miles: float = Field(..., description="Toneladas-Milla calculadas para el viaje redondo.")

