"""
DrillCalc - Module 1: Hoisting System & Structure
Author: Antony Picon, Mechanical Engineer
Description: Pure Python engine for Hoisting System calculations based on API 4F/9B.
"""
import math

class HoistingEngine:
    """
    Pure Logic Service for Hoisting System Calculations.
    Adheres to API 4F/9B standards.
    """

    @staticmethod
    def calculate_efficiency(N: int, S: int, K: float = 1.04) -> float:
        """
        Calculates the efficiency (eta) of the hoisting system.
        Formula: (K^N - 1) / (K^S * N * (K - 1))
        Ref: API 4F / 9B
        """
        if K <= 1.0:
            raise ValueError("Friction factor K must be greater than 1.0")
        if N <= 0:
            raise ValueError("Number of lines N must be greater than 0")
        
        numerator = (K ** N) - 1
        denominator = (K ** S) * N * (K - 1)
        return numerator / denominator

    @staticmethod
    def calculate_fast_line_tension(W_hook: float, N: int, efficiency: float) -> float:
        """
        Calculates Fast Line Tension (F_fast).
        Formula: W_hook / (N * efficiency)
        """
        if efficiency <= 0:
            raise ValueError("Efficiency must be greater than 0")
        return W_hook / (N * efficiency)

    @staticmethod
    def calculate_dead_line_load(W_hook: float, N: int) -> float:
        """
        Calculates Dead Line Load (F_dead).
        Formula: W_hook / N
        """
        return W_hook / N

    @staticmethod
    def calculate_derrick_load(W_hook: float, F_fast: float, F_dead: float) -> float:
        """
        Calculates Total Derrick Load (F_derrick).
        Formula: W_hook + F_fast + F_dead
        """
        return W_hook + F_fast + F_dead

    @staticmethod
    def calculate_safety_factor(LB_nom: float, F_fast: float) -> float:
        """
        Calculates Safety Factor (FD).
        Formula: LB_nom / F_fast
        """
        if F_fast <= 0:
            return float('inf') # Theoretically infinite safety if no load
        return LB_nom / F_fast

    @staticmethod
    def determine_alert_level(fd: float) -> str:
        """
        Determines the alert level based on Safety Factor.
        Criteria:
        - FD < 2.0: DANGER
        - 2.0 <= FD < 3.0: CAUTION
        - FD >= 3.0: SAFE
        """
        if fd < 2.0:
            return "DANGER"
        elif fd < 3.0:
            return "CAUTION"
        else:
            return "SAFE"
