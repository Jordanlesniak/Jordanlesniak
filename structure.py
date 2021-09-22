########################################################################
# Team Oak: Jessie Miller, Jack Garrison, Rusi Li, Jordan Lesniak
# AST304, Fall 2020
# Michigan State University
########################################################################

"""
<Description of this module goes here: what it does, how it's used.>
"""

import numpy as np
from eos import pressure, density
from ode import rk4
from astro_const import ac

def stellar_derivatives(m,z,mue):
    """
    RHS of Lagrangian differential equations for radius and pressure
    
    Arguments
        m
            current value of the mass
        z (array)
            current values of (radius, pressure)
        mue
            ratio, nucleons to electrons.  For a carbon-oxygen white dwarf, 
            mue = 2.
        
    Returns
        dzdm (array)
            Lagrangian derivatives dr/dm, dP/dm
    """
    
    dzdm = np.zeros_like(z)
    r = z[0]
    rho = density(r, mue)
    
    ### equations from section 2.3 ###
    dzdm[0] = (4*ac.pi*r**2*rho)**(-1)
    dzdm[1] = (-ac.G*m) / (4*ac.pi*r**4)
    
    return dzdm

def central_values(Pc,delta_m,mue):
    """
    Constructs the boundary conditions at the edge of a small, constant density 
    core of mass delta_m with central pressure P_c
    
    Arguments
        Pc
            central pressure (units = Pascals)
        delta_m
            core mass (units = kg)
        mue
            nucleon/electron ratio
    
    Returns
        z = array([ r, p ])
            central values of radius and pressure (units = meters, Pascals)
    """
    z = np.zeros(2)
    
    ### compute initial values of z = [ r, p ] ###
    rho_c = density(Pc, mue)
    
    ### equation 9 from instructions ###
    z[0] = ((3*delta_m) / (4*ac.pi*rho_c))**(1/3)
    
    ### equation 7 from instructions ###
    z[1] = Pc
    
    
    return z
    
def lengthscales(m,z,mue):
    """
    Computes the radial length scale H_r and the pressure length H_P
    
    Arguments
        m
            current mass coordinate (units = kg)
        z (array)
           [ r, p ] (units = meters, pascals)
        mue
            mean electron weight
    
    Returns
        z/|dzdm| (units = meters, pascals)
    """

    # fill this in
    
    ### compute density ###
    rho = density(z[1, mue]) ##may need another input
    
    ### compute H_r using eqn 10 ###
    H_r = 4*ac.pi*z[0]**3*rho
    
    ### compute H_p using eqn 11 ###
    H_p = 4*ac.pi*z[0]**4*z[1] / ac.G*m
    
    pass

    return H_r, H_p
    
def integrate(Pc,delta_m,eta = 10**(-10),xi,mue =_ac.m_e.value,max_steps=10000):
    """
    Integrates the scaled stellar structure equations

    Arguments
        Pc
            central pressure (units = Pascals)
        delta_m
            initial offset from center (units = kg)
        eta
            The integration stops when P < eta * Pc
        xi
            The stepsize is set to be xi*min(p/|dp/dm|, r/|dr/dm|)
        mue
            mean electron mass
        max_steps
            solver will quit and throw error if this more than max_steps are 
            required (default is 10000)
                        
    Returns
        m_step, r_step, p_step
            arrays containing mass coordinates, radii and pressures during 
            integration (m_steps = kg, r_step = meters, p_steps = Pascals)
    """
        
    m_step = np.zeros(max_steps)
    r_step = np.zeros(max_steps)
    p_step = np.zeros(max_steps)
    
    # set starting conditions using central values
    
    Nsteps = 0
    initial_mass = _ac.M_sun.value
    ##initial_radius = _ac.R_sun.value #???????
    ##initial_pressure = pressure(rho, mue) #????????
    for step in range(max_steps):
        radius = z[0]
        pressure = z[1]
        # are we at the surface?
        if (pressure < eta*Pc):
            break
        # store the step
        m_step[step] = ### in kg
        r_step[step] = 
        p_step[step] = 
        
        # set the stepsize
        stepsize_m = (0.01) * initial_mass #??
        stepsize_r = (0.01) * radius #??
        stepsize_p = (0.01) * pressure #??
        
        # take a step
        
        # increment the counter
        Nsteps += 1
    # if the loop runs to max_steps, then signal an error
    else:
        raise Exception('too many iterations')
        
    return m_step[0:Nsteps],r_step[0:Nsteps],p_step[0:Nsteps]

def pressure_guess(m,mue):
    """
    Computes a guess for the central pressure based on virial theorem and mass-
    radius relation. 
    
    Arguments
        m
            mass of white dwarf (units are kg)
        mue
            mean electron mass
    
    Returns
        P
            guess for pressure
    """
    #### eqn 16 from instructions ###
    Pguess = ac.G**5 / ac.K_e**4 (m*mue**2)**(10/3)
    
    return Pguess
