########################################################################
# Team Oak: Jessie Miller, Jack Garrison, Rusi Li, Jordan Lesniak
# AST304, Fall 2020
# Michigan State University
########################################################################

"""
COME BACK TO AND FINISH DENSITY EQUATION!
"""

"""
This script contains two functions. The first, pressure, calculates the 
pressure in terms of density and baryon-to-electron ratio, mue. The second
function, density, calculates teh density in terms of pressure and mue.
"""

### import constants ###
import astro_const as ac

### define pressure function ###
def pressure(rho, mue):
    """
    Arguments
        rho
            mass density (kg/m**3)
        mue
            baryon/electron ratio
    
    Returns
        electron degeneracy pressure (Pascal)
    """
    
    # replace following lines with formula (eqn 1 from instructions)
    p = (1/5)*(3/(8*ac.pi))**(2/3)*ac.h**2/(2*ac.m_e)*(rho/(mue*ac.m_u))**5/3
    return p

### define density function: COME BACK TO ###
def density(p, mue):
    """
    Arguments
        p
            electron degeneracy pressure (Pascal)
        mue
            baryon/electron ratio
        
    Returns
        mass density (kg/m**3)
    """
    
    # replace following lines with formula
    rho = 0.0
    return rho
