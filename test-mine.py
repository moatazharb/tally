#!/usr/bin/python

from itaps import iMesh, iBase
from pyne import material
from pyne.material import Material, MaterialLibrary
import tally as gtag

'''
tag_values = ['mat:graveyard','mat:vacuum', 'mat:Nitrogen/rho:-0.001205', 'tally:photon/cell_flux',
             'tally:neutron/surface_current', 'mat:Steel, Stainless 321/rho:-2', 'mat:Lead/rho:-11.35', 'mat:Mercury/rho:-7.874']
'''             
#print gtag.check_matname(tag_values)

gtag.get_tag_values('../../test/tally/test-1.h5m')

#tally_list=gtag.check_tallyname(tag_values)
#print tally_list
