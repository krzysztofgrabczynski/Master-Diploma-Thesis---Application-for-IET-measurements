import math
from typing import Tuple


def calculate_material_properties(
    L: float, b: float, m: float, t: float, f_f: float, f_t: float
) -> Tuple[float, float, float]:
    """
    Function to calculate Youngu's modulus, Dynamic Shear modulus and Poisson's ratio.
    """
    
    # Computing Youngu's modulus
    T_1 = (1000 + 6.585 * (t / L) ** 2) / 10**6
    youngs_modulus = 0.9465 * ((m * f_f**2) / b) * ((L**3) / (t**3)) * T_1

    # Computing Dynamic Shear modulus
    numerator = 1 + (b / t) ** 2
    denominator = 4 - (2.521 * t / b * (1 - (1.991 / (math.exp(math.pi * b / t) + 1))))
    element_1 = numerator / denominator
    element_2 = 1 + ((0.00851 * b**2) / L**2)
    element_3 = 0.060 * ((b / L) ** (3 / 2)) * ((b / t) - 1) ** 2
    R = (element_1 * element_2 - element_3) / 10**3

    dynamic_shear_modulus = (4 * L * m * f_t**2) / (b * t) * R

    # Computing Poisson's ratio
    poisson_ratio = (youngs_modulus / (2 * dynamic_shear_modulus)) - 1

    return youngs_modulus, dynamic_shear_modulus, poisson_ratio
