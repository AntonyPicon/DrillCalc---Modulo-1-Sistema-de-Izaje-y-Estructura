"""
DrillCalc - Module 1: Hoisting System & Structure
Author: Antony Picon, Mechanical Engineer
Description: Service for Ton-Mile calculations based on API RP 9B.
"""

class TonMileEngine:
    """
    Pure Logic Service for Ton-Mile Calculations.
    Adheres to API RP 9B standards.
    """

    @staticmethod
    def calculate_round_trip(
        depth: float,
        stand_length: float,
        pipe_weight_mud: float,
        block_weight: float,
        collar_weight_mud: float,
        collar_length: float
    ) -> float:
        """
        Calculates Ton-Miles for a Round Trip.
        Formula: T_R = [D * (L + D) * W_m + 4 * D * (M + 0.5 * C)] / (5280 * 2000)
        Where C = L_c * (W_cm - W_m)
        """
        # C = Excess weight of drill collar assembly in mud (lbs)
        excess_collar_weight = collar_length * (collar_weight_mud - pipe_weight_mud)
        
        # Numerator components
        pipe_component = depth * (stand_length + depth) * pipe_weight_mud
        block_collar_component = 4 * depth * (block_weight + 0.5 * excess_collar_weight)
        
        # Calculation in ft-lbs
        total_work_ft_lbs = pipe_component + block_collar_component
        
        # Convert to Ton-Miles (1 Ton = 2000 lbs, 1 Mile = 5280 ft)
        ton_miles = total_work_ft_lbs / (5280 * 2000)
        
        return round(ton_miles, 2)
