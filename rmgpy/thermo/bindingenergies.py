# cython: embedsignature=True, cdivision=True

###############################################################################
#                                                                             #
# RMG - Reaction Mechanism Generator                                          #
#                                                                             #
# Copyright (c) 2002-2020 Prof. William H. Green (whgreen@mit.edu),           #
# Prof. Richard H. West (r.west@neu.edu) and the RMG Team (rmg_dev@mit.edu)   #
#                                                                             #
# Permission is hereby granted, free of charge, to any person obtaining a     #
# copy of this software and associated documentation files (the 'Software'),  #
# to deal in the Software without restriction, including without limitation   #
# the rights to use, copy, modify, merge, publish, distribute, sublicense,    #
# and/or sell copies of the Software, and to permit persons to whom the       #
# Software is furnished to do so, subject to the following conditions:        #
#                                                                             #
# The above copyright notice and this permission notice shall be included in  #
# all copies or substantial portions of the Software.                         #
#                                                                             #
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER         #
# DEALINGS IN THE SOFTWARE.                                                   #
#                                                                             #
###############################################################################

import rmgpy.quantity
import rmgpy.constants as constants

################################################################################

class BindingEnergies:
    """
    A heat capacity model based on the NASA polynomial. Both the 
    seven-coefficient and nine-coefficient variations are supported.
    The attributes are:
    
    =============== ============================================================
    Attribute       Description
    =============== ============================================================
    `coeffs`        The seven or nine NASA polynomial coefficients
    `Tmin`          The minimum temperature in K at which the model is valid, or zero if unknown or undefined
    `Tmax`          The maximum temperature in K at which the model is valid, or zero if unknown or undefined
    `E0`            The energy at zero Kelvin (including zero point energy)
    `comment`       Information about the model (e.g. its source)
    =============== ============================================================

    """
    
    def __init__(self, binding_energies=None, surface_site_density=None, label=None, metal=None, facet=None, site=None, comment=''):
        
        if binding_energies:
            self.binding_energies = {atom: rmgpy.quantity.Energy(
                energy) for atom, energy in binding_energies.items()}
        else:
            self.binding_energies = binding_energies
        if surface_site_density:
            self.surface_site_density = rmgpy.quantity.SurfaceConcentration(surface_site_density)
        else:
            self.surface_site_density = surface_site_density
        self.label = label
        self.metal = metal
        self.facet = facet
        self.site = site
        self.comment = comment
        
    def __repr__(self):
        """
        Return a string representation that can be used to reconstruct the
        object.
        """
        return f'BindingEnergies_{self.label}'
