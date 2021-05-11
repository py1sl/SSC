""" 
Neutron production module
Part of SSC
Author: S Lilley
"""

import numpy as np


def calc_n_yield(p_energy, target_A_num, fission=False):
    """ Carpenter formula for neutron yield in a solid target 10cm diam, 60cm long
        energy should be in GeV.
        ref: Carpenter, NIM 145:91-113, 1977
    """
    if fission:
       neutron_yield = 50 * (p_energy - 0.120)  # for U238
    else:
        neutron_yield = 0.1 * (p_energy - 0.120) * (target_A_num + 20)
    return neutron_yield
