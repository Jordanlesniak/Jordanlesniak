########################################################################
# Team Oak: Jessie Miller, Jack Garrison, Rusi Li, Jordan Lesniak
# AST304, Fall 2020
# Michigan State University
########################################################################

"""
Reads in table 4 of Joyce et al. (2018) containing masses and radii
of white dwarf stars. You should not need to alter this file. 
"""

from numpy import genfromtxt

class WhiteDwarf:
    def __init__(self,source,instrument,R,R_err,M,M_err):
        self.source = source
        self.instrument = instrument
        self.radius = R
        self.radius_error = R_err
        self.mass = M
        self.mass_error = M_err      

class MassRadiusObservations:
    """
    Lightweight class storing data complied by Joyce et al. (2018), MNRAS 
    479, 1612 (Table 4).  To use:
    
    In [1]: from observations import MassRadiusObservations

    In [2]: obs = MassRadiusObservations()

    In [3]: obs.masses
    Out[3]: 
    array([0.927, 0.607, 0.643, 0.541, 0.59 , 0.398, 0.277, 0.729, 0.543,
           0.723, 0.559, 0.524, 0.633, 0.376])

    In [4]: obs.radii
    Out[4]: 
    array([0.802, 1.461, 1.457, 1.34 , 1.378, 1.418, 1.464, 1.235, 1.42 ,
           1.717, 2.183, 1.452, 1.993, 1.504])

    In [5]: obs.radius_errors
    Out[5]: 
    array([0.011, 0.009, 0.036, 0.013, 0.011, 0.009, 0.018, 0.018, 0.014,
           0.009, 0.043, 0.024, 0.009, 0.042])
    
    In [6]: for source,info in obs.sources.items():
        ...:     print('{0:20} M = {1:5.3f} +/- {2:5.3f} Msun'.format(source,info.mass,info.mass_error))

    Sirius B             M = 0.927 +/- 0.107 Msun
    HZ43                 M = 0.643 +/- 0.065 Msun
    ...
    and so on.  See the test at bottom for an example.
    """

    def __init__(self):
        self._data = genfromtxt(\
            'Joyce.txt',
            delimiter=[16,12,7,7,12,8],
            names=['source','instrument','R','R_err','M','M_err'],
            dtype=['S16','S12','f8','f8','f8','f8'],
            autostrip=True)
        self._observations = {}
        sources = [str(s,'utf-8') for s in self._data['source']]
        instruments = [str(s,'utf-8') for s in self._data['instrument']]
        for s, i, m, r, m_e, r_e in zip(sources, instruments, self._data['M'],
            self._data['R'], self._data['M_err'], self._data['R_err']):
            self._observations[s] = WhiteDwarf(s,i,r,r_e,m,m_e)

    @property
    def sources(self):
        return self._observations

    @property
    def masses(self):
        return self._data['M']

    @property
    def radii(self):
        return self._data['R']

    @property
    def mass_errors(self):
        return self._data['M_err']
        
    @property
    def radius_errors(self):
        return self._data['R_err']

    def gen_latex_table(self):
        lines=[ r'\begin{tabular}{llrrrr}' ]
        lines.append(\
        "source     & instrument & $M$   & $\Delta M$ & $R$ & $\Delta R$ \\")
        lines.append(\
        "           &     & \multicolumn{2}{c}{$(\Msun)$} & \multicolumn{2}{c}{$(0.01\,\Rsun)$}\\")
        lines.append("\hline")
        
        for wd in self._observations:
            lines.append(r'{0:16s} & {1:4s} & {2:5.3f} & {3:5.3f} & {4:5.3f} & {5:5.3f}\\'.format(\
                wd,self._observations[wd].instrument,
                self._observations[wd].mass,
                self._observations[wd].mass_error,
                self._observations[wd].radius,
                self._observations[wd].radius_error))
        lines.append(r'\end{tabular}')
        return lines


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    obs = MassRadiusObservations()
    plotfile = 'MR_Joyce.png'
    tabfile = 'Joyce-table4.tex'
    print('making plot {}'.format(plotfile))
    plt.xlabel(r'$M/M_\odot$')
    plt.ylabel(r'$R/(0.01\,R_\odot)$')
    
    plt.errorbar(obs.masses,obs.radii,\
        yerr=obs.radius_errors,xerr=obs.mass_errors,fmt='ko',markersize=4)
    plt.savefig(plotfile)

    print('writing {}'.format(tabfile))
    with open(tabfile,'w') as fancytab:
        for line in obs.gen_latex_table():
            fancytab.write(line+'\n')

        
    
