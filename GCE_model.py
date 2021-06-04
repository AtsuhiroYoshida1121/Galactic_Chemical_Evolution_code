#####################################################################################################################################
###
### galaxy chemical evolution(Suzuki & Maeda)
###
###
##################################################################################################################################
##################################################################################################################################
###
### First, solve the time evolution of H and He!
###
#################################################################################################################################

### using module

import numpy as np
import matplotlib.pyplot as plt
import warnings
from scipy import integrate
import csv
import copy

### warning ignore
warnings.simplefilter('ignore')

##################################################################################################################################
###
### evolution setup
###
##################################################################################################################################


### list

Mh = []    # gas mass
Mhe4 = []
Mc12 = []
Mn14 = []
Mo16 = []
Mna23 = []
Mmg24 = []
Mal27 = []
Msi28 = []
Mp31 = []
Ms32 = []
Mk39 = []
Mca40 = []
Msc45 = []
Mti48 = []
Mv51 = []
Mcr52 = []
Mmn55 = []
Mfe56 = []
Mni58 = []
Mco59 = []
Mcu63 = []
Mzn64 = []

Mccsn_mg24 = []
Magb_mg24 = []

Mccsn_fe56 = []
Magb_fe56 = []

Mall = []


SFR = []
z = []
redshift = []

### time set up

T = []   # time 

t0 = 0        # milkyway born time
T.append(t0)


i = 0         # time index 
qx = 0        # read time index


### initial gas value

gas_mass = 10**7

Rh = 0.75   # H ratio
Rhe =0.25   # He ratio
Rc12 = 0
Rn14 = 0
Ro16 = 0
Rna23 = 0
Rmg24 = 0
Ral27 = 0
Rsi28 = 0
Rp31 = 0
Rs32 = 0
Rk39 = 0
Rca40 = 0
Rsc45 = 0
Rti48 = 0
Rv51 = 0
Rcr52 = 0
Rmn55 = 0
Rfe56 = 0
Rni58 = 0
Rco59 = 0
Rcu63 = 0
Rzn64 = 0 

mh0 = Rh * gas_mass
mhe40 = Rhe * gas_mass
mc120= 0
mn140= 0
mo160= 0
mna230= 0
mmg240= 0
mal270= 0
msi280 = 0
mp310 = 0
ms320= 0
mk390= 0
mca400= 0
msc450= 0
mti480= 0
mv510= 0
mcr520= 0
mmn550= 0
mfe560= 0
mni580= 0
mco590= 0
mcu630= 0
mzn640= 0 

z0 = 0

Mh.append(mh0)
Mhe4.append(mhe40)
Mc12.append(mc120)
Mn14.append(mn140)
Mo16.append(mo160)
Mna23.append(mna230)
Mmg24.append(mmg240)
Mal27.append(mal270)
Msi28.append(msi280)
Mp31.append(mp310)
Ms32.append(ms320)
Mk39.append(mk390)
Mca40.append(mca400)
Msc45.append(msc450)
Mti48.append(mti480)
Mv51.append(mv510)
Mcr52.append(mcr520)
Mmn55.append(mmn550)
Mfe56.append(mfe560)
Mni58.append(mni580)
Mco59.append(mco590)
Mcu63.append(mcu630)
Mzn64.append(mzn640) 

Mccsn_mg24.append(0)
Magb_mg24.append(0)
Mccsn_fe56.append(0)
Magb_fe56.append(0)

SFR.append(0)
Mall.append(gas_mass)
z.append(z0)

##################################################################################################################################

##################################################################################################################################
###
### parameters
###
##################################################################################################################################


from parameters import *

### Yields Table

### SNe Ia

from SNIa_yields.SNeIa_yields import *

### SNe II 

from SNII_yields.yp import *
from SNII_yields.y4He import *
from SNII_yields.y12C import *
from SNII_yields.y14N import *
from SNII_yields.y16O import *
from SNII_yields.y23Na import *
from SNII_yields.y24Mg import *
from SNII_yields.y27Al import *
from SNII_yields.y28Si import *
from SNII_yields.y31P import *
from SNII_yields.y32S import *
from SNII_yields.y39K import *
from SNII_yields.y40Ca import *
from SNII_yields.y45Sc import *
from SNII_yields.y48Ti import *
from SNII_yields.y51V import *
from SNII_yields.y52Cr import *
from SNII_yields.y55Mn import *
from SNII_yields.y56Fe import *
from SNII_yields.y59Co import *
from SNII_yields.y58Ni import *
from SNII_yields.y63Cu import *
from SNII_yields.y64Zn import *


### AGB 

from AGB_yields.p import *
from AGB_yields.he4 import *
from AGB_yields.c12 import *
from AGB_yields.n14 import *
from AGB_yields.o16 import *
from AGB_yields.na23 import *
from AGB_yields.mg24 import *
from AGB_yields.al27 import *
from AGB_yields.si28 import *
from AGB_yields.p31 import *
from AGB_yields.s32 import *
from AGB_yields.k39 import *
from AGB_yields.ca40 import *
from AGB_yields.sc45 import *
from AGB_yields.ti48 import *
from AGB_yields.v51 import *
from AGB_yields.cr52 import *
from AGB_yields.mn55 import *
from AGB_yields.fe56 import *
from AGB_yields.ni58 import *
from AGB_yields.co59 import *
from AGB_yields.cu63 import *
from AGB_yields.zn64 import *


from hi_AGB_yields.p import *
from hi_AGB_yields.he4 import *
from hi_AGB_yields.c12 import *
from hi_AGB_yields.n14 import *
from hi_AGB_yields.o16 import *
from hi_AGB_yields.na23 import *
from hi_AGB_yields.mg24 import *
from hi_AGB_yields.al27 import *
from hi_AGB_yields.si28 import *
from hi_AGB_yields.p31 import *
from hi_AGB_yields.s32 import *
from hi_AGB_yields.k39 import *
#from hi_AGB_yields.ca40 import *
from hi_AGB_yields.sc45 import *
from hi_AGB_yields.ti48 import *
from hi_AGB_yields.v51 import *
from hi_AGB_yields.cr52 import *
from hi_AGB_yields.mn55 import *
from hi_AGB_yields.fe56 import *
from hi_AGB_yields.ni58 import *
from hi_AGB_yields.co59 import *
from hi_AGB_yields.cu63 import *
from hi_AGB_yields.zn64 import *

### PISNe

from PISNe_yields.y4He import *
from PISNe_yields.y12C import *
from PISNe_yields.y14N import *
from PISNe_yields.y16O import *
from PISNe_yields.y23Na import *
from PISNe_yields.y24Mg import *
from PISNe_yields.y27Al import *
from PISNe_yields.y28Si import *
from PISNe_yields.y31P import *
from PISNe_yields.y32S import *
from PISNe_yields.y39K import *
from PISNe_yields.y40Ca import *
from PISNe_yields.y45Sc import *
from PISNe_yields.y48Ti import *
from PISNe_yields.y51V import *
from PISNe_yields.y52Cr import *
from PISNe_yields.y55Mn import *
from PISNe_yields.y56Fe import *
from PISNe_yields.y59Co import *
from PISNe_yields.y58Ni import *
from PISNe_yields.y63Cu import *
from PISNe_yields.y64Zn import * 

### CVMS

from CVMS_yields.yp import *
from CVMS_yields.y4He import *
from CVMS_yields.y12C import *
from CVMS_yields.y14N import *
from CVMS_yields.y16O import *
from CVMS_yields.y23Na import *
from CVMS_yields.y24Mg import *
from CVMS_yields.y27Al import *
from CVMS_yields.y28Si import *
from CVMS_yields.y31P import *
from CVMS_yields.y32S import *
from CVMS_yields.y39K import *
from CVMS_yields.y40Ca import *
from CVMS_yields.y45Sc import *
from CVMS_yields.y48Ti import *
from CVMS_yields.y51V import *
from CVMS_yields.y52Cr import *
from CVMS_yields.y55Mn import *
from CVMS_yields.y56Fe import *
from CVMS_yields.y59Co import *
from CVMS_yields.y58Ni import *
from CVMS_yields.y63Cu import *
from CVMS_yields.y64Zn import * 

##################################################################################################################################

### infall

def M_in(ratio,t):
    if infall == 0:
        return 0
    elif infall == 1:
        return ratio * 3.3 * 10**(9) * np.exp(-t / 3)
    
#print(M_in(Rh,T[i]))


### fall back

def M_fb(elem):
    if fall_back == 0:
        return 0
    elif fall_back == 1:
        return 2.5 * elem / tsf

#print(M_fb(Mh[i]))    

### star formation

def Mall_sf(i): 
    return (Mh[i] + Mhe4[i]) / tsf

### element star formation

def M_sf(elem):
    return elem / tsf


###########################################################################################################################

### stellar life time

def tau(m):
    if m <= 0.6:
        return 160
    
    elif m > 0.6 and m <= 6.0:
        tau = 10**( ( 0.334 - (1.790 - 0.2232*(7.764 - np.log10(m)))**(1/2) ) / 0.1116 )
        return tau
    
    elif m > 6.0:
        return 1.2*m**(-1.85) + 0.003
    
### delayed star formation

def Mall_sf_delay(i,m):
    
    index = i - int(tau(m)/dt)
    
    if index < 0:
        return 1.0E-16
    elif index >= 0:
        msf =Mall_sf(index)
        return msf

    
###########################################################################################################################

### Metalisity

def Z(i):
    return 1 - (Mh[i] + Mhe4[i]) / Mall[i]

### delay metalicty
  
def metal(i,m):
    
    index = i - int(tau(m)/dt)
    
    if index < 0:
        return 1.0E-16
    elif index >= 0:
        return z[index]
    
    
### IMF normalize

C1 = integrate.quad(lambda x: x**(-alpha1+1), 0.08, bound)
C2 = integrate.quad(lambda x: x**(-alpha2+1), bound, 100)

C = C1[0] + C2[0]

### IMF

def IMF(m):
    if m <= bound:
        x = alpha1
    else:
        x = alpha2
        
    dndm = C**(-1) * m**(-x)
    
    return dndm

##################################################################################################################################

### CCSNe Yields

#meta = z[i]

def Y_cc(m,meta,a1,a2,a3,a4,a5,a6,a7,b1,b2,b3,b4,b5,b6,b7, \
        c1,c2,c3,c4,c5,c6,c7,d1,d2,d3,d4,d5,d6,d7):
    if meta < 0.001:
        if m < 13.0:
            return 0
        elif m >= 13.0 and m < 15.0:
            return a1
        elif m >= 15.0 and m < 18.0:
            return a2
        elif m >= 18.0 and m < 20.0:
            return a3
        elif m >= 20.0 and m < 25.0:
            return a4
        elif m >= 25.0 and m < 30.0:
            return a5
        elif m >= 30.0 and m < 40.0:
            return a6
        elif m >= 40.0 and m < 45.0:
            return a7
        else:
            return 0
        
    
    elif meta >= 0.001 and meta < 0.004:
        if m < 13.0:
            return 0
        elif m >= 13.0 and m < 15.0:
            return b1
        elif m >= 15.0 and m < 18.0:
            return b2
        elif m >= 18.0 and m < 20.0:
            return b3
        elif m >= 20.0 and m < 25.0:
            return b4
        elif m >= 25.0 and m < 30.0:
            return b5
        elif m >= 30.0 and m < 40.0:
            return b6
        elif m >= 40.0 and m < 45.0:
            return b7
        else:
            return 0
        
    elif meta >= 0.004 and meta < 0.02:
        if m < 13.0:
            return 0
        elif m >= 13.0 and m < 15.0:
            return c1
        elif m >= 15.0 and m < 18.0:
            return c2
        elif m >= 18.0 and m < 20.0:
            return c3
        elif m >= 20.0 and m < 25.0:
            return c4
        elif m >= 25.0 and m < 30.0:
            return c5
        elif m >= 30.0 and m < 40.0:
            return c6
        elif m >= 40.0 and m < 45.0:
            return c7
        else:
            return 0
    
    elif meta >= 0.02:
        if m < 13.0:
            return 0
        elif m >= 13.0 and m < 15.0:
            return d1
        elif m >= 15.0 and m < 18.0:
            return d2
        elif m >= 18.0 and m < 20.0:
            return d3
        elif m >= 20.0 and m < 25.0:
            return d4
        elif m >= 25.0 and m < 30.0:
            return d5
        elif m >= 30.0 and m < 40.0:
            return d6
        elif m >= 40.0 and m < 45.0:
            return d7
        else:
            return 0

#def M_cc(E,i):
    #return E * Mall_sf(i)

def M_cc(E):
    return E     

    
### integreted yields

def Eh_cc(i): 
    Eh_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_yp1,a_yp2,a_yp3,a_yp4,a_yp5,a_yp6,a_yp7,b_yp1,b_yp2,b_yp3,b_yp4,b_yp5,b_yp6,b_yp7,c_yp1,c_yp2,c_yp3,c_yp4,c_yp5,c_yp6,c_yp7,d_yp1,d_yp2,d_yp3,d_yp4,d_yp5,d_yp6,d_yp7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Eh_cc[0]

def Ehe4_cc(i):
    Ehe4_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y4He1,a_y4He2,a_y4He3,a_y4He4,a_y4He5,a_y4He6,a_y4He7,b_y4He1,b_y4He2,b_y4He3,b_y4He4,b_y4He5,b_y4He6,b_y4He7,c_y4He1,c_y4He2,c_y4He3,c_y4He4,c_y4He5,c_y4He6,c_y4He7,d_y4He1,d_y4He2,d_y4He3,d_y4He4,d_y4He5,d_y4He6,d_y4He7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Ehe4_cc[0]

def Ec12_cc(i): 
    Ec12_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y12C1,a_y12C2,a_y12C3,a_y12C4,a_y12C5,a_y12C6,a_y12C7,b_y12C1,b_y12C2,b_y12C3,b_y12C4,b_y12C5,b_y12C6,b_y12C7,c_y12C1,c_y12C2,c_y12C3,c_y12C4,c_y12C5,c_y12C6,c_y12C7,d_y12C1,d_y12C2,d_y12C3,d_y12C4,d_y12C5,d_y12C6,d_y12C7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Ec12_cc[0] 

def En14_cc(i):
    En14_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y14N1,a_y14N2,a_y14N3,a_y14N4,a_y14N5,a_y14N6,a_y14N7,b_y14N1,b_y14N2,b_y14N3,b_y14N4,b_y14N5,b_y14N6,b_y14N7,c_y14N1,c_y14N2,c_y14N3,c_y14N4,c_y14N5,c_y14N6,c_y14N7,d_y14N1,d_y14N2,d_y14N3,d_y14N4,d_y14N5,d_y14N6,d_y14N7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return En14_cc[0] 
    
def Eo16_cc(i):
    Eo16_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y16O1,a_y16O2,a_y16O3,a_y16O4,a_y16O5,a_y16O6,a_y16O7,b_y16O1,b_y16O2,b_y16O3,b_y16O4,b_y16O5,b_y16O6,b_y16O7,c_y16O1,c_y16O2,c_y16O3,c_y16O4,c_y16O5,c_y16O6,c_y16O7,d_y16O1,d_y16O2,d_y16O3,d_y16O4,d_y16O5,d_y16O6,d_y16O7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Eo16_cc[0]

def Ena23_cc(i): 
    Ena23_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y23Na1,a_y23Na2,a_y23Na3,a_y23Na4,a_y23Na5,a_y23Na6,a_y23Na7,b_y23Na1,b_y23Na2,b_y23Na3,b_y23Na4,b_y23Na5,b_y23Na6,b_y23Na7,c_y23Na1,c_y23Na2,c_y23Na3,c_y23Na4,c_y23Na5,c_y23Na6,c_y23Na7,d_y23Na1,d_y23Na2,d_y23Na3,d_y23Na4,d_y23Na5,d_y23Na6,d_y23Na7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Ena23_cc[0] 


def Emg24_cc(i):
    Emg24_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y24Mg1,a_y24Mg2,a_y24Mg3,a_y24Mg4,a_y24Mg5,a_y24Mg6,a_y24Mg7,b_y24Mg1,b_y24Mg2,b_y24Mg3,b_y24Mg4,b_y24Mg5,b_y24Mg6,b_y24Mg7,c_y24Mg1,c_y24Mg2,c_y24Mg3,c_y24Mg4,c_y24Mg5,c_y24Mg6,c_y24Mg7,d_y24Mg1,d_y24Mg2,d_y24Mg3,d_y24Mg4,d_y24Mg5,d_y24Mg6,d_y24Mg7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Emg24_cc[0]

def Eal27_cc(i): 
    Eal27_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y27Al1,a_y27Al2,a_y27Al3,a_y27Al4,a_y27Al5,a_y27Al6,a_y27Al7,b_y27Al1,b_y27Al2,b_y27Al3,b_y27Al4,b_y27Al5,b_y27Al6,b_y27Al7,c_y27Al1,c_y27Al2,c_y27Al3,c_y27Al4,c_y27Al5,c_y27Al6,c_y27Al7,d_y27Al1,d_y27Al2,d_y27Al3,d_y27Al4,d_y27Al5,d_y27Al6,d_y27Al7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Eal27_cc[0] 

def Esi28_cc(i): 
    Esi28_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y28Si1,a_y28Si2,a_y28Si3,a_y28Si4,a_y28Si5,a_y28Si6,a_y28Si7,b_y28Si1,b_y28Si2,b_y28Si3,b_y28Si4,b_y28Si5,b_y28Si6,b_y28Si7,c_y28Si1,c_y28Si2,c_y28Si3,c_y28Si4,c_y28Si5,c_y28Si6,c_y28Si7,d_y28Si1,d_y28Si2,d_y28Si3,d_y28Si4,d_y28Si5,d_y28Si6,d_y28Si7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Esi28_cc[0] 

def Ep31_cc(i): 
    Ep31_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y31P1,a_y31P2,a_y31P3,a_y31P4,a_y31P5,a_y31P6,a_y31P7,b_y31P1,b_y31P2,b_y31P3,b_y31P4,b_y31P5,b_y31P6,b_y31P7,c_y31P1,c_y31P2,c_y31P3,c_y31P4,c_y31P5,c_y31P6,c_y31P7,d_y31P1,d_y31P2,d_y31P3,d_y31P4,d_y31P5,d_y31P6,d_y31P7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Ep31_cc[0]

def Es32_cc(i):
    Es32_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y32S1,a_y32S2,a_y32S3,a_y32S4,a_y32S5,a_y32S6,a_y32S7,b_y32S1,b_y32S2,b_y32S3,b_y32S4,b_y32S5,b_y32S6,b_y32S7,c_y32S1,c_y32S2,c_y32S3,c_y32S4,c_y32S5,c_y32S6,c_y32S7,d_y32S1,d_y32S2,d_y32S3,d_y32S4,d_y32S5,d_y32S6,d_y32S7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Es32_cc[0] 

def Ek39_cc(i): 
    Ek39_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y39K1,a_y39K2,a_y39K3,a_y39K4,a_y39K5,a_y39K6,a_y39K7,b_y39K1,b_y39K2,b_y39K3,b_y39K4,b_y39K5,b_y39K6,b_y39K7,c_y39K1,c_y39K2,c_y39K3,c_y39K4,c_y39K5,c_y39K6,c_y39K7,d_y39K1,d_y39K2,d_y39K3,d_y39K4,d_y39K5,d_y39K6,d_y39K7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Ek39_cc[0]


def Eca40_cc(i):
    Eca40_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y40Ca1,a_y40Ca2,a_y40Ca3,a_y40Ca4,a_y40Ca5,a_y40Ca6,a_y40Ca7,b_y40Ca1,b_y40Ca2,b_y40Ca3,b_y40Ca4,b_y40Ca5,b_y40Ca6,b_y40Ca7,c_y40Ca1,c_y40Ca2,c_y40Ca3,c_y40Ca4,c_y40Ca5,c_y40Ca6,c_y40Ca7,d_y40Ca1,d_y40Ca2,d_y40Ca3,d_y40Ca4,d_y40Ca5,d_y40Ca6,d_y40Ca7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Eca40_cc[0] 

def Esc45_cc(i):
    Esc45_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y45Sc1,a_y45Sc2,a_y45Sc3,a_y45Sc4,a_y45Sc5,a_y45Sc6,a_y45Sc7,b_y45Sc1,b_y45Sc2,b_y45Sc3,b_y45Sc4,b_y45Sc5,b_y45Sc6,b_y45Sc7,c_y45Sc1,c_y45Sc2,c_y45Sc3,c_y45Sc4,c_y45Sc5,c_y45Sc6,c_y45Sc7,d_y45Sc1,d_y45Sc2,d_y45Sc3,d_y45Sc4,d_y45Sc5,d_y45Sc6,d_y45Sc7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Esc45_cc[0]

def Eti48_cc(i): 
    Eti48_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y48Ti1,a_y48Ti2,a_y48Ti3,a_y48Ti4,a_y48Ti5,a_y48Ti6,a_y48Ti7,b_y48Ti1,b_y48Ti2,b_y48Ti3,b_y48Ti4,b_y48Ti5,b_y48Ti6,b_y48Ti7,c_y48Ti1,c_y48Ti2,c_y48Ti3,c_y48Ti4,c_y48Ti5,c_y48Ti6,c_y48Ti7,d_y48Ti1,d_y48Ti2,d_y48Ti3,d_y48Ti4,d_y48Ti5,d_y48Ti6,d_y48Ti7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Eti48_cc[0] 
    
def Ev51_cc(i): 
    Ev51_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y51V1,a_y51V2,a_y51V3,a_y51V4,a_y51V5,a_y51V6,a_y51V7,b_y51V1,b_y51V2,b_y51V3,b_y51V4,b_y51V5,b_y51V6,b_y51V7,c_y51V1,c_y51V2,c_y51V3,c_y51V4,c_y51V5,c_y51V6,c_y51V7,d_y51V1,d_y51V2,d_y51V3,d_y51V4,d_y51V5,d_y51V6,d_y51V7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Ev51_cc[0]

def Ecr52_cc(i):
    Ecr52_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y52Cr1,a_y52Cr2,a_y52Cr3,a_y52Cr4,a_y52Cr5,a_y52Cr6,a_y52Cr7,b_y52Cr1,b_y52Cr2,b_y52Cr3,b_y52Cr4,b_y52Cr5,b_y52Cr6,b_y52Cr7,c_y52Cr1,c_y52Cr2,c_y52Cr3,c_y52Cr4,c_y52Cr5,c_y52Cr6,c_y52Cr7,d_y52Cr1,d_y52Cr2,d_y52Cr3,d_y52Cr4,d_y52Cr5,d_y52Cr6,d_y52Cr7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Ecr52_cc[0] 

def Emn55_cc(i): 
    Emn55_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y55Mn1,a_y55Mn2,a_y55Mn3,a_y55Mn4,a_y55Mn5,a_y55Mn6,a_y55Mn7,b_y55Mn1,b_y55Mn2,b_y55Mn3,b_y55Mn4,b_y55Mn5,b_y55Mn6,b_y55Mn7,c_y55Mn1,c_y55Mn2,c_y55Mn3,c_y55Mn4,c_y55Mn5,c_y55Mn6,c_y55Mn7,d_y55Mn1,d_y55Mn2,d_y55Mn3,d_y55Mn4,d_y55Mn5,d_y55Mn6,d_y55Mn7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Emn55_cc[0]

def Efe56_cc(i):
    Efe56_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y56Fe1,a_y56Fe2,a_y56Fe3,a_y56Fe4,a_y56Fe5,a_y56Fe6,a_y56Fe7,b_y56Fe1,b_y56Fe2,b_y56Fe3,b_y56Fe4,b_y56Fe5,b_y56Fe6,b_y56Fe7,c_y56Fe1,c_y56Fe2,c_y56Fe3,c_y56Fe4,c_y56Fe5,c_y56Fe6,c_y56Fe7,d_y56Fe1,d_y56Fe2,d_y56Fe3,d_y56Fe4,d_y56Fe5,d_y56Fe6,d_y56Fe7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Efe56_cc[0]

def Eni58_cc(i):
    Eni58_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y58Ni1,a_y58Ni2,a_y58Ni3,a_y58Ni4,a_y58Ni5,a_y58Ni6,a_y58Ni7,b_y58Ni1,b_y58Ni2,b_y58Ni3,b_y58Ni4,b_y58Ni5,b_y58Ni6,b_y58Ni7,c_y58Ni1,c_y58Ni2,c_y58Ni3,c_y58Ni4,c_y58Ni5,c_y58Ni6,c_y58Ni7,d_y58Ni1,d_y58Ni2,d_y58Ni3,d_y58Ni4,d_y58Ni5,d_y58Ni6,d_y58Ni7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Eni58_cc[0]

def Eco59_cc(i): 
    Eco59_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y59Co1,a_y59Co2,a_y59Co3,a_y59Co4,a_y59Co5,a_y59Co6,a_y59Co7,b_y59Co1,b_y59Co2,b_y59Co3,b_y59Co4,b_y59Co5,b_y59Co6,b_y59Co7,c_y59Co1,c_y59Co2,c_y59Co3,c_y59Co4,c_y59Co5,c_y59Co6,c_y59Co7,d_y59Co1,d_y59Co2,d_y59Co3,d_y59Co4,d_y59Co5,d_y59Co6,d_y59Co7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Eco59_cc[0] 

def Ecu63_cc(i): 
    Ecu63_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y63Cu1,a_y63Cu2,a_y63Cu3,a_y63Cu4,a_y63Cu5,a_y63Cu6,a_y63Cu7,b_y63Cu1,b_y63Cu2,b_y63Cu3,b_y63Cu4,b_y63Cu5,b_y63Cu6,b_y63Cu7,c_y63Cu1,c_y63Cu2,c_y63Cu3,c_y63Cu4,c_y63Cu5,c_y63Cu6,c_y63Cu7,d_y63Cu1,d_y63Cu2,d_y63Cu3,d_y63Cu4,d_y63Cu5,d_y63Cu6,d_y63Cu7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Ecu63_cc[0]

def Ezn64_cc(i):
    Ezn64_cc = integrate.quad(lambda m: Y_cc(m,metal(i,m),a_y64Zn1,a_y64Zn2,a_y64Zn3,a_y64Zn4,a_y64Zn5,a_y64Zn6,a_y64Zn7,b_y64Zn1,b_y64Zn2,b_y64Zn3,b_y64Zn4,b_y64Zn5,b_y64Zn6,b_y64Zn7,c_y64Zn1,c_y64Zn2,c_y64Zn3,c_y64Zn4,c_y64Zn5,c_y64Zn6,c_y64Zn7,d_y64Zn1,d_y64Zn2,d_y64Zn3,d_y64Zn4,d_y64Zn5,d_y64Zn6,d_y64Zn7)*IMF(m)*Mall_sf_delay(i,m), 9, 100)
    return Ezn64_cc[0] 



##################################################################################################################################

### SNe Ia Yields

NIa = 1.5 * 10**(-3)
tdmax = 13.8
tdmin = 1.0
#tdmin = 50 * 10**(-3)

dt = 0.001

delay = int(tdmin / dt)  # delay step
#print(tdmin/dtx)

def D(x):
    const = NIa / np.log(tdmax / tdmin)
    
    if x > tdmin:
        return const / x
    else:
        return 0
    


def M_Ia(Y,qx):
    if qx > tdmin:
        if inverse == 0:
            d = Y * NIa * Mall_sf(i - delay)
            
            return d
        
        elif inverse == 1:
            integ = integrate.quad(lambda y: Mall_sf(int(y / dt)) * D(T[i] - y), 0, T[i] - tdmin)
            outeg = Y * integ[0]
            
            return outeg
    else:
        return 0

#print(M_Ia(Yh_Ia,qx))

#################################################################################################################################
### AGB yields

### low AGB yields

#meta = z[i]

def Y_agb(m,meta,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16, \
         b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15, \
         c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15, \
         d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16):
    if meta < 0.0001:
        return 0
    
    elif meta >= 0.0001 and meta < 0.004:
        
        if m < 1.0:
            return 0
        elif m >= 1.0 and m < 1.25:
            return a1
        elif m >= 1.25 and m < 1.5:
            return a2
        elif m >= 1.5 and m < 1.75:
            return a3
        elif m >= 1.75 and m < 1.9:
            return a4
        elif m >= 1.9 and m < 2.1:
            return a5
        elif m >= 2.1 and m < 2.25:
            return a6
        elif m >= 2.25 and m < 2.5:
            return a7
        elif m >= 2.5 and m < 3.0:
            return a8
        elif m >= 3.0 and m < 3.5:
            return a9
        elif m >= 3.5 and m < 4.0:
            return a10
        elif m >= 4.0 and m < 4.5:
            return a11
        elif m >= 4.5 and m < 5.0:
            return a12
        elif m >= 5.0 and m < 5.5:
            return a13
        elif m >= 5.5 and m < 6.0:
            return a14
        elif m >= 6.0 and m < 6.5:
            return a15
        elif m >= 6.5 and m < 7.0:
            return a16
        else:
            return 0
        
    elif meta >= 0.004 and meta < 0.008:

        if m < 1.0:
            return 0
        elif m >= 1.0 and m < 1.25:
            return b1
        elif m >= 1.25 and m < 1.5:
            return b2
        elif m >= 1.5 and m < 1.75:
            return b3
        elif m >= 1.75 and m < 1.9:
            return b4
        elif m >= 1.9 and m < 2.1:
            return b5
        elif m >= 2.1 and m < 2.25:
            return b6
        elif m >= 2.25 and m < 2.5:
            return b7
        elif m >= 2.5 and m < 3.0:
            return b8
        elif m >= 3.0 and m < 3.5:
            return b9
        elif m >= 3.5 and m < 4.0:
            return b10
        elif m >= 4.0 and m < 4.5:
            return b11
        elif m >= 4.5 and m < 5.0:
            return b12
        elif m >= 5.0 and m < 5.5:
            return b13
        elif m >= 5.5 and m < 6.0:
            return b14
        elif m >= 6.0 and m < 6.5:
            return b15
        else:
            return 0 
        
    elif meta >= 0.008 and meta < 0.02:
        if m < 1.0:
            return 0
        elif m >= 1.0 and m < 1.25:
            return c1
        elif m >= 1.25 and m < 1.5:
            return c2
        elif m >= 1.5 and m < 1.75:
            return c3
        elif m >= 1.75 and m < 1.9:
            return c4
        elif m >= 1.9 and m < 2.1:
            return c5
        elif m >= 2.1 and m < 2.25:
            return c6
        elif m >= 2.25 and m < 2.5:
            return c7
        elif m >= 2.5 and m < 3.0:
            return c8
        elif m >= 3.0 and m < 3.5:
            return c9
        elif m >= 3.5 and m < 4.0:
            return c10
        elif m >= 4.0 and m < 4.5:
            return c11
        elif m >= 4.5 and m < 5.0:
            return c12
        elif m >= 5.0 and m < 5.5:
            return c13
        elif m >= 5.5 and m < 6.0:
            return c14
        elif m >= 6.0 and m < 6.5:
            return c15
        else:
            return 0 
    
    elif meta >= 0.02:
        if m < 1.0:
            return 0
        elif m >= 1.0 and m < 1.25:
            return d1
        elif m >= 1.25 and m < 1.5:
            return d2
        elif m >= 1.5 and m < 1.75:
            return d3
        elif m >= 1.75 and m < 1.9:
            return d4
        elif m >= 1.9 and m < 2.1:
            return d5
        elif m >= 2.1 and m < 2.25:
            return d6
        elif m >= 2.25 and m < 2.5:
            return d7
        elif m >= 2.5 and m < 3.0:
            return d8
        elif m >= 3.0 and m < 3.5:
            return d9
        elif m >= 3.5 and m < 4.0:
            return d10
        elif m >= 4.0 and m < 4.5:
            return d11
        elif m >= 4.5 and m < 5.0:
            return d12
        elif m >= 5.0 and m < 5.5:
            return d13
        elif m >= 5.5 and m < 6.0:
            return d14
        elif m >= 6.0 and m < 6.5:
            return d15
        elif m >= 6.5 and m < 7.0:
            return d16
        else:
            return 0 


            

#def M_agb(E,i):
    #if yagb == 1:
        #return E * Mall_sf(i)
    #elif yagb == 0:
        #return 0
        
def M_agb(E):
    if yagb == 1:
        return E 
    elif yagb == 0:
        return 0

### integrated yields
def Eh_agb(i):
    Eh_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1p,a_2p,a_3p,a_4p,a_5p,a_6p,a_7p,a_8p,a_9p,a_10p,a_11p,a_12p,a_13p,a_14p,a_15p,a_16p,b_1p,b_2p,b_3p,b_4p,b_5p,b_6p,b_7p,b_8p,b_9p,b_10p,b_11p,b_12p,b_13p,b_14p,b_15p,c_1p,c_2p,c_3p,c_4p,c_5p,c_6p,c_7p,c_8p,c_9p,c_10p,c_11p,c_12p,c_13p,c_14p,c_15p,d_1p,d_2p,d_3p,d_4p,d_5p,d_6p,d_7p,d_8p,d_9p,d_10p,d_11p,d_12p,d_13p,d_14p,d_15p,d_16p)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9) 
    return Eh_agb[0]

def Ehe4_agb(i):
    Ehe4_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1he4,a_2he4,a_3he4,a_4he4,a_5he4,a_6he4,a_7he4,a_8he4,a_9he4,a_10he4,a_11he4,a_12he4,a_13he4,a_14he4,a_15he4,a_16he4,b_1he4,b_2he4,b_3he4,b_4he4,b_5he4,b_6he4,b_7he4,b_8he4,b_9he4,b_10he4,b_11he4,b_12he4,b_13he4,b_14he4,b_15he4,c_1he4,c_2he4,c_3he4,c_4he4,c_5he4,c_6he4,c_7he4,c_8he4,c_9he4,c_10he4,c_11he4,c_12he4,c_13he4,c_14he4,c_15he4,d_1he4,d_2he4,d_3he4,d_4he4,d_5he4,d_6he4,d_7he4,d_8he4,d_9he4,d_10he4,d_11he4,d_12he4,d_13he4,d_14he4,d_15he4,d_16he4)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9) 
    return Ehe4_agb[0]

def Ec12_agb(i):
    Ec12_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1c12,a_2c12,a_3c12,a_4c12,a_5c12,a_6c12,a_7c12,a_8c12,a_9c12,a_10c12,a_11c12,a_12c12,a_13c12,a_14c12,a_15c12,a_16c12,b_1c12,b_2c12,b_3c12,b_4c12,b_5c12,b_6c12,b_7c12,b_8c12,b_9c12,b_10c12,b_11c12,b_12c12,b_13c12,b_14c12,b_15c12,c_1c12,c_2c12,c_3c12,c_4c12,c_5c12,c_6c12,c_7c12,c_8c12,c_9c12,c_10c12,c_11c12,c_12c12,c_13c12,c_14c12,c_15c12,d_1c12,d_2c12,d_3c12,d_4c12,d_5c12,d_6c12,d_7c12,d_8c12,d_9c12,d_10c12,d_11c12,d_12c12,d_13c12,d_14c12,d_15c12,d_16c12)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9)
    return Ec12_agb[0] 

def En14_agb(i):
    En14_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1n14,a_2n14,a_3n14,a_4n14,a_5n14,a_6n14,a_7n14,a_8n14,a_9n14,a_10n14,a_11n14,a_12n14,a_13n14,a_14n14,a_15n14,a_16n14,b_1n14,b_2n14,b_3n14,b_4n14,b_5n14,b_6n14,b_7n14,b_8n14,b_9n14,b_10n14,b_11n14,b_12n14,b_13n14,b_14n14,b_15n14,c_1n14,c_2n14,c_3n14,c_4n14,c_5n14,c_6n14,c_7n14,c_8n14,c_9n14,c_10n14,c_11n14,c_12n14,c_13n14,c_14n14,c_15n14,d_1n14,d_2n14,d_3n14,d_4n14,d_5n14,d_6n14,d_7n14,d_8n14,d_9n14,d_10n14,d_11n14,d_12n14,d_13n14,d_14n14,d_15n14,d_16n14)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9)
    return En14_agb[0] 

def Eo16_agb(i):
	Eo16_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1o16,a_2o16,a_3o16,a_4o16,a_5o16,a_6o16,a_7o16,a_8o16,a_9o16,a_10o16,a_11o16,a_12o16,a_13o16,a_14o16,a_15o16,a_16o16,b_1o16,b_2o16,b_3o16,b_4o16,b_5o16,b_6o16,b_7o16,b_8o16,b_9o16,b_10o16,b_11o16,b_12o16,b_13o16,b_14o16,b_15o16,c_1o16,c_2o16,c_3o16,c_4o16,c_5o16,c_6o16,c_7o16,c_8o16,c_9o16,c_10o16,c_11o16,c_12o16,c_13o16,c_14o16,c_15o16,d_1o16,d_2o16,d_3o16,d_4o16,d_5o16,d_6o16,d_7o16,d_8o16,d_9o16,d_10o16,d_11o16,d_12o16,d_13o16,d_14o16,d_15o16,d_16o16)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9)
	return Eo16_agb[0]

def Ena23_agb(i):
	Ena23_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1na23,a_2na23,a_3na23,a_4na23,a_5na23,a_6na23,a_7na23,a_8na23,a_9na23,a_10na23,a_11na23,a_12na23,a_13na23,a_14na23,a_15na23,a_16na23,b_1na23,b_2na23,b_3na23,b_4na23,b_5na23,b_6na23,b_7na23,b_8na23,b_9na23,b_10na23,b_11na23,b_12na23,b_13na23,b_14na23,b_15na23,c_1na23,c_2na23,c_3na23,c_4na23,c_5na23,c_6na23,c_7na23,c_8na23,c_9na23,c_10na23,c_11na23,c_12na23,c_13na23,c_14na23,c_15na23,d_1na23,d_2na23,d_3na23,d_4na23,d_5na23,d_6na23,d_7na23,d_8na23,d_9na23,d_10na23,d_11na23,d_12na23,d_13na23,d_14na23,d_15na23,d_16na23)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9)
	return Ena23_agb[0] 

def Emg24_agb(i):
    Emg24_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1mg24,a_2mg24,a_3mg24,a_4mg24,a_5mg24,a_6mg24,a_7mg24,a_8mg24,a_9mg24,a_10mg24,a_11mg24,a_12mg24,a_13mg24,a_14mg24,a_15mg24,a_16mg24,b_1mg24,b_2mg24,b_3mg24,b_4mg24,b_5mg24,b_6mg24,b_7mg24,b_8mg24,b_9mg24,b_10mg24,b_11mg24,b_12mg24,b_13mg24,b_14mg24,b_15mg24,c_1mg24,c_2mg24,c_3mg24,c_4mg24,c_5mg24,c_6mg24,c_7mg24,c_8mg24,c_9mg24,c_10mg24,c_11mg24,c_12mg24,c_13mg24,c_14mg24,c_15mg24,d_1mg24,d_2mg24,d_3mg24,d_4mg24,d_5mg24,d_6mg24,d_7mg24,d_8mg24,d_9mg24,d_10mg24,d_11mg24,d_12mg24,d_13mg24,d_14mg24,d_15mg24,d_16mg24)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9)
    return Emg24_agb[0]

def Eal27_agb(i):
    Eal27_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1al27,a_2al27,a_3al27,a_4al27,a_5al27,a_6al27,a_7al27,a_8al27,a_9al27,a_10al27,a_11al27,a_12al27,a_13al27,a_14al27,a_15al27,a_16al27,b_1al27,b_2al27,b_3al27,b_4al27,b_5al27,b_6al27,b_7al27,b_8al27,b_9al27,b_10al27,b_11al27,b_12al27,b_13al27,b_14al27,b_15al27,c_1al27,c_2al27,c_3al27,c_4al27,c_5al27,c_6al27,c_7al27,c_8al27,c_9al27,c_10al27,c_11al27,c_12al27,c_13al27,c_14al27,c_15al27,d_1al27,d_2al27,d_3al27,d_4al27,d_5al27,d_6al27,d_7al27,d_8al27,d_9al27,d_10al27,d_11al27,d_12al27,d_13al27,d_14al27,d_15al27,d_16al27)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9)
    return Eal27_agb[0] 

def Esi28_agb(i):
	Esi28_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1si28,a_2si28,a_3si28,a_4si28,a_5si28,a_6si28,a_7si28,a_8si28,a_9si28,a_10si28,a_11si28,a_12si28,a_13si28,a_14si28,a_15si28,a_16si28,b_1si28,b_2si28,b_3si28,b_4si28,b_5si28,b_6si28,b_7si28,b_8si28,b_9si28,b_10si28,b_11si28,b_12si28,b_13si28,b_14si28,b_15si28,c_1si28,c_2si28,c_3si28,c_4si28,c_5si28,c_6si28,c_7si28,c_8si28,c_9si28,c_10si28,c_11si28,c_12si28,c_13si28,c_14si28,c_15si28,d_1si28,d_2si28,d_3si28,d_4si28,d_5si28,d_6si28,d_7si28,d_8si28,d_9si28,d_10si28,d_11si28,d_12si28,d_13si28,d_14si28,d_15si28,d_16si28)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9)
	return Esi28_agb[0] 

def Ep31_agb(i):
	Ep31_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1p31,a_2p31,a_3p31,a_4p31,a_5p31,a_6p31,a_7p31,a_8p31,a_9p31,a_10p31,a_11p31,a_12p31,a_13p31,a_14p31,a_15p31,a_16p31,b_1p31,b_2p31,b_3p31,b_4p31,b_5p31,b_6p31,b_7p31,b_8p31,b_9p31,b_10p31,b_11p31,b_12p31,b_13p31,b_14p31,b_15p31,c_1p31,c_2p31,c_3p31,c_4p31,c_5p31,c_6p31,c_7p31,c_8p31,c_9p31,c_10p31,c_11p31,c_12p31,c_13p31,c_14p31,c_15p31,d_1p31,d_2p31,d_3p31,d_4p31,d_5p31,d_6p31,d_7p31,d_8p31,d_9p31,d_10p31,d_11p31,d_12p31,d_13p31,d_14p31,d_15p31,d_16p31)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9)
	return Ep31_agb[0] 

def Es32_agb(i):
    Es32_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1s32,a_2s32,a_3s32,a_4s32,a_5s32,a_6s32,a_7s32,a_8s32,a_9s32,a_10s32,a_11s32,a_12s32,a_13s32,a_14s32,a_15s32,a_16s32,b_1s32,b_2s32,b_3s32,b_4s32,b_5s32,b_6s32,b_7s32,b_8s32,b_9s32,b_10s32,b_11s32,b_12s32,b_13s32,b_14s32,b_15s32,c_1s32,c_2s32,c_3s32,c_4s32,c_5s32,c_6s32,c_7s32,c_8s32,c_9s32,c_10s32,c_11s32,c_12s32,c_13s32,c_14s32,c_15s32,d_1s32,d_2s32,d_3s32,d_4s32,d_5s32,d_6s32,d_7s32,d_8s32,d_9s32,d_10s32,d_11s32,d_12s32,d_13s32,d_14s32,d_15s32,d_16s32)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9)
    return Es32_agb[0] 

#def Ek39_agb(i):
#Ek39_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1k39,a_2k39,a_3k39,a_4k39,a_5k39,a_6k39,a_7k39,a_8k39,a_9k39,a_10k39,a_11k39,a_12k39,a_13k39,a_14k39,a_15k39,a_16k39,b_1k39,b_2k39,b_3k39,b_4k39,b_5k39,b_6k39,b_7k39,b_8k39,b_9k39,b_10k39,b_11k39,b_12k39,b_13k39,b_14k39,b_15k39,c_1k39,c_2k39,c_3k39,c_4k39,c_5k39,c_6k39,c_7k39,c_8k39,c_9k39,c_10k39,c_11k39,c_12k39,c_13k39,c_14k39,c_15k39,d_1k39,d_2k39,d_3k39,d_4k39,d_5k39,d_6k39,d_7k39,d_8k39,d_9k39,d_10k39,d_11k39,d_12k39,d_13k39,d_14k39,d_15k39,d_16k39)*IMF(m)*Mall_sf_delay(i), 0.08, 9)
#return Ek39_agb[0] 

#def Eca40_agb(i):
#Eca40_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1ca40,a_2ca40,a_3ca40,a_4ca40,a_5ca40,a_6ca40,a_7ca40,a_8ca40,a_9ca40,a_10ca40,a_11ca40,a_12ca40,a_13ca40,a_14ca40,a_15ca40,a_16ca40,b_1ca40,b_2ca40,b_3ca40,b_4ca40,b_5ca40,b_6ca40,b_7ca40,b_8ca40,b_9ca40,b_10ca40,b_11ca40,b_12ca40,b_13ca40,b_14ca40,b_15ca40,c_1ca40,c_2ca40,c_3ca40,c_4ca40,c_5ca40,c_6ca40,c_7ca40,c_8ca40,c_9ca40,c_10ca40,c_11ca40,c_12ca40,c_13ca40,c_14ca40,c_15ca40,d_1ca40,d_2ca40,d_3ca40,d_4ca40,d_5ca40,d_6ca40,d_7ca40,d_8ca40,d_9ca40,d_10ca40,d_11ca40,d_12ca40,d_13ca40,d_14ca40,d_15ca40,d_16ca40)*IMF(m)*Mall_sf_delay(i), 0.08, 9)
#return Eca40_agb[0] 

#def Esc45_agb(i):
#Esc45_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1sc45,a_2sc45,a_3sc45,a_4sc45,a_5sc45,a_6sc45,a_7sc45,a_8sc45,a_9sc45,a_10sc45,a_11sc45,a_12sc45,a_13sc45,a_14sc45,a_15sc45,a_16sc45,b_1sc45,b_2sc45,b_3sc45,b_4sc45,b_5sc45,b_6sc45,b_7sc45,b_8sc45,b_9sc45,b_10sc45,b_11sc45,b_12sc45,b_13sc45,b_14sc45,b_15sc45,c_1sc45,c_2sc45,c_3sc45,c_4sc45,c_5sc45,c_6sc45,c_7sc45,c_8sc45,c_9sc45,c_10sc45,c_11sc45,c_12sc45,c_13sc45,c_14sc45,c_15sc45,d_1sc45,d_2sc45,d_3sc45,d_4sc45,d_5sc45,d_6sc45,d_7sc45,d_8sc45,d_9sc45,d_10sc45,d_11sc45,d_12sc45,d_13sc45,d_14sc45,d_15sc45,d_16sc45)*IMF(m)*Mall_sf_delay(i), 0.08, 9)
#return Esc45_agb[0]

#def Eti48_agb(i):
#Eti48_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1ti48,a_2ti48,a_3ti48,a_4ti48,a_5ti48,a_6ti48,a_7ti48,a_8ti48,a_9ti48,a_10ti48,a_11ti48,a_12ti48,a_13ti48,a_14ti48,a_15ti48,a_16ti48,b_1ti48,b_2ti48,b_3ti48,b_4ti48,b_5ti48,b_6ti48,b_7ti48,b_8ti48,b_9ti48,b_10ti48,b_11ti48,b_12ti48,b_13ti48,b_14ti48,b_15ti48,c_1ti48,c_2ti48,c_3ti48,c_4ti48,c_5ti48,c_6ti48,c_7ti48,c_8ti48,c_9ti48,c_10ti48,c_11ti48,c_12ti48,c_13ti48,c_14ti48,c_15ti48,d_1ti48,d_2ti48,d_3ti48,d_4ti48,d_5ti48,d_6ti48,d_7ti48,d_8ti48,d_9ti48,d_10ti48,d_11ti48,d_12ti48,d_13ti48,d_14ti48,d_15ti48,d_16ti48)*IMF(m)*Mall_sf_delay(i), 0.08, 9)
#return Eti48_agb[0] 

#def Ev51_agb(i):
#Ev51_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1v51,a_2v51,a_3v51,a_4v51,a_5v51,a_6v51,a_7v51,a_8v51,a_9v51,a_10v51,a_11v51,a_12v51,a_13v51,a_14v51,a_15v51,a_16v51,b_1v51,b_2v51,b_3v51,b_4v51,b_5v51,b_6v51,b_7v51,b_8v51,b_9v51,b_10v51,b_11v51,b_12v51,b_13v51,b_14v51,b_15v51,c_1v51,c_2v51,c_3v51,c_4v51,c_5v51,c_6v51,c_7v51,c_8v51,c_9v51,c_10v51,c_11v51,c_12v51,c_13v51,c_14v51,c_15v51,d_1v51,d_2v51,d_3v51,d_4v51,d_5v51,d_6v51,d_7v51,d_8v51,d_9v51,d_10v51,d_11v51,d_12v51,d_13v51,d_14v51,d_15v51,d_16v51)*IMF(m)*Mall_sf_delay(i), 0.08, 9)
#return Ev51_agb[0] 

#def Ecr52_agb(i):
#Ecr52_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1cr52,a_2cr52,a_3cr52,a_4cr52,a_5cr52,a_6cr52,a_7cr52,a_8cr52,a_9cr52,a_10cr52,a_11cr52,a_12cr52,a_13cr52,a_14cr52,a_15cr52,a_16cr52,b_1cr52,b_2cr52,b_3cr52,b_4cr52,b_5cr52,b_6cr52,b_7cr52,b_8cr52,b_9cr52,b_10cr52,b_11cr52,b_12cr52,b_13cr52,b_14cr52,b_15cr52,c_1cr52,c_2cr52,c_3cr52,c_4cr52,c_5cr52,c_6cr52,c_7cr52,c_8cr52,c_9cr52,c_10cr52,c_11cr52,c_12cr52,c_13cr52,c_14cr52,c_15cr52,d_1cr52,d_2cr52,d_3cr52,d_4cr52,d_5cr52,d_6cr52,d_7cr52,d_8cr52,d_9cr52,d_10cr52,d_11cr52,d_12cr52,d_13cr52,d_14cr52,d_15cr52,d_16cr52)*IMF(m)*Mall_sf_delay(i), 0.08, 9)
#return Ecr52_agb[0] 

#def Emn55_agb(i):
#mn55_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1mn55,a_2mn55,a_3mn55,a_4mn55,a_5mn55,a_6mn55,a_7mn55,a_8mn55,a_9mn55,a_10mn55,a_11mn55,a_12mn55,a_13mn55,a_14mn55,a_15mn55,a_16mn55,b_1mn55,b_2mn55,b_3mn55,b_4mn55,b_5mn55,b_6mn55,b_7mn55,b_8mn55,b_9mn55,b_10mn55,b_11mn55,b_12mn55,b_13mn55,b_14mn55,b_15mn55,c_1mn55,c_2mn55,c_3mn55,c_4mn55,c_5mn55,c_6mn55,c_7mn55,c_8mn55,c_9mn55,c_10mn55,c_11mn55,c_12mn55,c_13mn55,c_14mn55,c_15mn55,d_1mn55,d_2mn55,d_3mn55,d_4mn55,d_5mn55,d_6mn55,d_7mn55,d_8mn55,d_9mn55,d_10mn55,d_11mn55,d_12mn55,d_13mn55,d_14mn55,d_15mn55,d_16mn55)*IMF(m)*Mall_sf_delay(i), 0.08, 9)
#return Emn55_agb[0] 

def Efe56_agb(i):
	Efe56_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1fe56,a_2fe56,a_3fe56,a_4fe56,a_5fe56,a_6fe56,a_7fe56,a_8fe56,a_9fe56,a_10fe56,a_11fe56,a_12fe56,a_13fe56,a_14fe56,a_15fe56,a_16fe56,b_1fe56,b_2fe56,b_3fe56,b_4fe56,b_5fe56,b_6fe56,b_7fe56,b_8fe56,b_9fe56,b_10fe56,b_11fe56,b_12fe56,b_13fe56,b_14fe56,b_15fe56,c_1fe56,c_2fe56,c_3fe56,c_4fe56,c_5fe56,c_6fe56,c_7fe56,c_8fe56,c_9fe56,c_10fe56,c_11fe56,c_12fe56,c_13fe56,c_14fe56,c_15fe56,d_1fe56,d_2fe56,d_3fe56,d_4fe56,d_5fe56,d_6fe56,d_7fe56,d_8fe56,d_9fe56,d_10fe56,d_11fe56,d_12fe56,d_13fe56,d_14fe56,d_15fe56,d_16fe56)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9) 
	return Efe56_agb[0]

def Eni58_agb(i):
    Eni58_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1ni58,a_2ni58,a_3ni58,a_4ni58,a_5ni58,a_6ni58,a_7ni58,a_8ni58,a_9ni58,a_10ni58,a_11ni58,a_12ni58,a_13ni58,a_14ni58,a_15ni58,a_16ni58,b_1ni58,b_2ni58,b_3ni58,b_4ni58,b_5ni58,b_6ni58,b_7ni58,b_8ni58,b_9ni58,b_10ni58,b_11ni58,b_12ni58,b_13ni58,b_14ni58,b_15ni58,c_1ni58,c_2ni58,c_3ni58,c_4ni58,c_5ni58,c_6ni58,c_7ni58,c_8ni58,c_9ni58,c_10ni58,c_11ni58,c_12ni58,c_13ni58,c_14ni58,c_15ni58,d_1ni58,d_2ni58,d_3ni58,d_4ni58,d_5ni58,d_6ni58,d_7ni58,d_8ni58,d_9ni58,d_10ni58,d_11ni58,d_12ni58,d_13ni58,d_14ni58,d_15ni58,d_16ni58)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9)
    return Eni58_agb[0]

def Eco59_agb(i):
    Eco59_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1co59,a_2co59,a_3co59,a_4co59,a_5co59,a_6co59,a_7co59,a_8co59,a_9co59,a_10co59,a_11co59,a_12co59,a_13co59,a_14co59,a_15co59,a_16co59,b_1co59,b_2co59,b_3co59,b_4co59,b_5co59,b_6co59,b_7co59,b_8co59,b_9co59,b_10co59,b_11co59,b_12co59,b_13co59,b_14co59,b_15co59,c_1co59,c_2co59,c_3co59,c_4co59,c_5co59,c_6co59,c_7co59,c_8co59,c_9co59,c_10co59,c_11co59,c_12co59,c_13co59,c_14co59,c_15co59,d_1co59,d_2co59,d_3co59,d_4co59,d_5co59,d_6co59,d_7co59,d_8co59,d_9co59,d_10co59,d_11co59,d_12co59,d_13co59,d_14co59,d_15co59,d_16co59)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9)
    return Eco59_agb[0] 

#def Ecu63_agb(i):
#Ecu63_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1cu63,a_2cu63,a_3cu63,a_4cu63,a_5cu63,a_6cu63,a_7cu63,a_8cu63,a_9cu63,a_10cu63,a_11cu63,a_12cu63,a_13cu63,a_14cu63,a_15cu63,a_16cu63,b_1cu63,b_2cu63,b_3cu63,b_4cu63,b_5cu63,b_6cu63,b_7cu63,b_8cu63,b_9cu63,b_10cu63,b_11cu63,b_12cu63,b_13cu63,b_14cu63,b_15cu63,c_1cu63,c_2cu63,c_3cu63,c_4cu63,c_5cu63,c_6cu63,c_7cu63,c_8cu63,c_9cu63,c_10cu63,c_11cu63,c_12cu63,c_13cu63,c_14cu63,c_15cu63,d_1cu63,d_2cu63,d_3cu63,d_4cu63,d_5cu63,d_6cu63,d_7cu63,d_8cu63,d_9cu63,d_10cu63,d_11cu63,d_12cu63,d_13cu63,d_14cu63,d_15cu63,d_16cu63)*IMF(m)*Mall_sf_delay(i), 0.08, 9)
#return Ecu63_agb[0] 

#def Ezn64_agb(i):
# Ezn64_agb = integrate.quad(lambda m: Y_agb(m,metal(i,m),a_1zn64,a_2zn64,a_3zn64,a_4zn64,a_5zn64,a_6zn64,a_7zn64,a_8zn64,a_9zn64,a_10zn64,a_11zn64,a_12zn64,a_13zn64,a_14zn64,a_15zn64,a_16zn64,b_1zn64,b_2zn64,b_3zn64,b_4zn64,b_5zn64,b_6zn64,b_7zn64,b_8zn64,b_9zn64,b_10zn64,b_11zn64,b_12zn64,b_13zn64,b_14zn64,b_15zn64,c_1zn64,c_2zn64,c_3zn64,c_4zn64,c_5zn64,c_6zn64,c_7zn64,c_8zn64,c_9zn64,c_10zn64,c_11zn64,c_12zn64,c_13zn64,c_14zn64,c_15zn64,d_1zn64,d_2zn64,d_3zn64,d_4zn64,d_5zn64,d_6zn64,d_7zn64,d_8zn64,d_9zn64,d_10zn64,d_11zn64,d_12zn64,d_13zn64,d_14zn64,d_15zn64,d_16zn64)*IMF(m)*Mall_sf_delay(i), 0.08, 9)
#return Ezn64_agb[0] 


#################################################################################################################################

### high AGB yields

#meta = z[i]

def Y_hiagb(m,meta,a1,a2,a3,a4,b1,b2,b3,b4,b5,c1,c2,c3,c4,c5):
    if meta < 0.004:
        return 0
    
    elif meta >= 0.004 and meta < 0.008:
        
        if m < 6.5:
            return 0
        elif m >= 6.5 and m < 7.0:
            return a1
        elif m >= 7.0 and m < 7.5:
            return a2
        elif m >= 7.5 and m < 8.0:
            return a3
        elif m >= 8.0 and m < 8.5:
            return a4
        else:
            return 0
        
    elif meta >= 0.008 and meta < 0.02:
        if m < 6.5:
            return 0
        elif m >= 6.5 and m < 7.0:
            return b1
        elif m >= 7.0 and m < 7.5:
            return b2
        elif m >= 7.5 and m < 8.0:
            return b3
        elif m >= 8.0 and m < 8.5:
            return b4
        elif m >= 8.5 and m < 9.0:
            return b5
        else:
            return 0
    
    elif meta >= 0.02:
        if m < 6.5:
            return 0
        elif m >= 6.5 and m < 7.0:
            return c1
        elif m >= 7.0 and m < 7.5:
            return c2
        elif m >= 7.5 and m < 8.0:
            return c3
        elif m >= 8.0 and m < 8.5:
            return c4
        elif m >= 8.5 and m < 9.0:
            return c5
        else:
            return 0

#def M_hiagb(E,i):
    #if yagb == 1:
        #return E * Mall_sf(i)
    #elif yagb == 0:
        #return 0

def M_hiagb(E):
    if yagb == 1:
        return E 
    elif yagb == 0:
        return 0
    

### integrated yields    

def Eh_hiagb(i):
    Eh_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1p,hi_a_2p,hi_a_3p,hi_a_4p,hi_b_1p,hi_b_2p,hi_b_3p,hi_b_4p,hi_b_5p,hi_c_1p,hi_c_2p,hi_c_3p,hi_c_4p,hi_c_5p)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9) 
    return Eh_hiagb[0] 

def Ehe4_hiagb(i):
    Ehe4_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1he4,hi_a_2he4,hi_a_3he4,hi_a_4he4,hi_b_1he4,hi_b_2he4,hi_b_3he4,hi_b_4he4,hi_b_5he4,hi_c_1he4,hi_c_2he4,hi_c_3he4,hi_c_4he4,hi_c_5he4)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9) 
    return Ehe4_hiagb[0] 

def Ec12_hiagb(i):
    Ec12_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1c12,hi_a_2c12,hi_a_3c12,hi_a_4c12,hi_b_1c12,hi_b_2c12,hi_b_3c12,hi_b_4c12,hi_b_5c12,hi_c_1c12,hi_c_2c12,hi_c_3c12,hi_c_4c12,hi_c_5c12)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9) 
    return Ec12_hiagb[0]

def En14_hiagb(i):
    En14_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1n14,hi_a_2n14,hi_a_3n14,hi_a_4n14,hi_b_1n14,hi_b_2n14,hi_b_3n14,hi_b_4n14,hi_b_5n14,hi_c_1n14,hi_c_2n14,hi_c_3n14,hi_c_4n14,hi_c_5n14)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9) 
    return En14_hiagb[0] 

def Eo16_hiagb(i):
    Eo16_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1o16,hi_a_2o16,hi_a_3o16,hi_a_4o16,hi_b_1o16,hi_b_2o16,hi_b_3o16,hi_b_4o16,hi_b_5o16,hi_c_1o16,hi_c_2o16,hi_c_3o16,hi_c_4o16,hi_c_5o16)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9) 
    return Eo16_hiagb[0] 

def Ena23_hiagb(i):
    Ena23_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1na23,hi_a_2na23,hi_a_3na23,hi_a_4na23,hi_b_1na23,hi_b_2na23,hi_b_3na23,hi_b_4na23,hi_b_5na23,hi_c_1na23,hi_c_2na23,hi_c_3na23,hi_c_4na23,hi_c_5na23)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9) 
    return Ena23_hiagb[0] 

def Emg24_hiagb(i):
    Emg24_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1mg24,hi_a_2mg24,hi_a_3mg24,hi_a_4mg24,hi_b_1mg24,hi_b_2mg24,hi_b_3mg24,hi_b_4mg24,hi_b_5mg24,hi_c_1mg24,hi_c_2mg24,hi_c_3mg24,hi_c_4mg24,hi_c_5mg24)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9) 
    return Emg24_hiagb[0] 

def Eal27_hiagb(i):
	Eal27_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1al27,hi_a_2al27,hi_a_3al27,hi_a_4al27,hi_b_1al27,hi_b_2al27,hi_b_3al27,hi_b_4al27,hi_b_5al27,hi_c_1al27,hi_c_2al27,hi_c_3al27,hi_c_4al27,hi_c_5al27)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9) 
	return Eal27_hiagb[0]

def Esi28_hiagb(i):
    Esi28_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1si28,hi_a_2si28,hi_a_3si28,hi_a_4si28,hi_b_1si28,hi_b_2si28,hi_b_3si28,hi_b_4si28,hi_b_5si28,hi_c_1si28,hi_c_2si28,hi_c_3si28,hi_c_4si28,hi_c_5si28)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9) 
    return Esi28_hiagb[0]

def Ep31_hiagb(i):
    Ep31_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1p31,hi_a_2p31,hi_a_3p31,hi_a_4p31,hi_b_1p31,hi_b_2p31,hi_b_3p31,hi_b_4p31,hi_b_5p31,hi_c_1p31,hi_c_2p31,hi_c_3p31,hi_c_4p31,hi_c_5p31)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9) 
    return Ep31_hiagb[0] 


def Es32_hiagb(i):
    Es32_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1s32,hi_a_2s32,hi_a_3s32,hi_a_4s32,hi_b_1s32,hi_b_2s32,hi_b_3s32,hi_b_4s32,hi_b_5s32,hi_c_1s32,hi_c_2s32,hi_c_3s32,hi_c_4s32,hi_c_5s32)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9) 
    return Es32_hiagb[0] 

#def Ek39_hiagb(i):
#Ek39_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1k39,hi_a_2k39,hi_a_3k39,hi_a_4k39,hi_b_1k39,hi_b_2k39,hi_b_3k39,hi_b_4k39,hi_b_5k39,hi_c_1k39,hi_c_2k39,hi_c_3k39,hi_c_4k39,hi_c_5k39)*IMF(m)*Mall_sf_delay(i), 0.08, 9) 
#return Ek39_hiagb[0]


#def Eca40_hiagb(i):
#Eca40_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1ca40,hi_a_2ca40,hi_a_3ca40,hi_a_4ca40,hi_b_1ca40,hi_b_2ca40,hi_b_3ca40,hi_b_4ca40,hi_b_5ca40,hi_c_1ca40,hi_c_2ca40,hi_c_3ca40,hi_c_4ca40,hi_c_5ca40)*IMF(m)*Mall_sf_delay(i), 0.08, 9) 
#return Eca40_hiagb[0] 

#def Esc45_hiagb(i):
#Esc45_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1sc45,hi_a_2sc45,hi_a_3sc45,hi_a_4sc45,hi_b_1sc45,hi_b_2sc45,hi_b_3sc45,hi_b_4sc45,hi_b_5sc45,hi_c_1sc45,hi_c_2sc45,hi_c_3sc45,hi_c_4sc45,hi_c_5sc45)*IMF(m)*Mall_sf_delay(i), 0.08, 9) 
#return Esc45_hiagb[0] 

#def Eti48_hiagb(i):
#Eti48_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1ti48,hi_a_2ti48,hi_a_3ti48,hi_a_4ti48,hi_b_1ti48,hi_b_2ti48,hi_b_3ti48,hi_b_4ti48,hi_b_5ti48,hi_c_1ti48,hi_c_2ti48,hi_c_3ti48,hi_c_4ti48,hi_c_5ti48)*IMF(m)*Mall_sf_delay(i), 0.08, 9) 
#return Eti48_hiagb[0]

#def Emn55_hiagb(i):
#Emn55_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1mn55,hi_a_2mn55,hi_a_3mn55,hi_a_4mn55,hi_b_1mn55,hi_b_2mn55,hi_b_3mn55,hi_b_4mn55,hi_b_5mn55,hi_c_1mn55,hi_c_2mn55,hi_c_3mn55,hi_c_4mn55,hi_c_5mn55)*IMF(m)*Mall_sf_delay(i), 0.08, 9) 
#return Emn55_hiagb[0]

#def Ev51_hiagb(i):
#Ev51_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1v51,hi_a_2v51,hi_a_3v51,hi_a_4v51,hi_b_1v51,hi_b_2v51,hi_b_3v51,hi_b_4v51,hi_b_5v51,hi_c_1v51,hi_c_2v51,hi_c_3v51,hi_c_4v51,hi_c_5v51)*IMF(m)*Mall_sf_delay(i), 0.08, 9) 
#return Ev51_hiagb[0] 


#def Ecr52_hiagb(i):
#Ecr52_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1cr52,hi_a_2cr52,hi_a_3cr52,hi_a_4cr52,hi_b_1cr52,hi_b_2cr52,hi_b_3cr52,hi_b_4cr52,hi_b_5cr52,hi_c_1cr52,hi_c_2cr52,hi_c_3cr52,hi_c_4cr52,hi_c_5cr52)*IMF(m)*Mall_sf_delay(i), 0.08, 9) 
#return Ecr52_hiagb[0] 

def Efe56_hiagb(i):
    Efe56_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1fe56,hi_a_2fe56,hi_a_3fe56,hi_a_4fe56,hi_b_1fe56,hi_b_2fe56,hi_b_3fe56,hi_b_4fe56,hi_b_5fe56,hi_c_1fe56,hi_c_2fe56,hi_c_3fe56,hi_c_4fe56,hi_c_5fe56)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9) 
    return Efe56_hiagb[0] 

def Eni58_hiagb(i):
    Eni58_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1ni58,hi_a_2ni58,hi_a_3ni58,hi_a_4ni58,hi_b_1ni58,hi_b_2ni58,hi_b_3ni58,hi_b_4ni58,hi_b_5ni58,hi_c_1ni58,hi_c_2ni58,hi_c_3ni58,hi_c_4ni58,hi_c_5ni58)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9) 
    return Eni58_hiagb[0] 

def Eco59_hiagb(i):
    Eco59_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1co59,hi_a_2co59,hi_a_3co59,hi_a_4co59,hi_b_1co59,hi_b_2co59,hi_b_3co59,hi_b_4co59,hi_b_5co59,hi_c_1co59,hi_c_2co59,hi_c_3co59,hi_c_4co59,hi_c_5co59)*IMF(m)*Mall_sf_delay(i,m), 0.08, 9) 
    return Eco59_hiagb[0]

#def Ecu63_hiagb(i):
#Ecu63_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1cu63,hi_a_2cu63,hi_a_3cu63,hi_a_4cu63,hi_b_1cu63,hi_b_2cu63,hi_b_3cu63,hi_b_4cu63,hi_b_5cu63,hi_c_1cu63,hi_c_2cu63,hi_c_3cu63,hi_c_4cu63,hi_c_5cu63)*IMF(m)*Mall_sf_delay(i), 0.08, 9) 
#return Ecu63_hiagb[0] 


#def Ezn64_hiagb(i):
#Ezn64_hiagb = integrate.quad(lambda m: Y_hiagb(m,metal(i,m),hi_a_1zn64,hi_a_2zn64,hi_a_3zn64,hi_a_4zn64,hi_b_1zn64,hi_b_2zn64,hi_b_3zn64,hi_b_4zn64,hi_b_5zn64,hi_c_1zn64,hi_c_2zn64,hi_c_3zn64,hi_c_4zn64,hi_c_5zn64)*IMF(m)*Mall_sf_delay(i), 0.08, 9) 
#return Ezn64_hiagb[0] 

################################################################################################################################

### PISNe yields

def trans(Mhe_core):
    return 20 + (24/13) * Mhe_core

def Y_pisne(m,meta,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14):
    if meta < 0.001:
        if m < trans(65.0):
            return 0
        elif m >= trans(65.0) and m < trans(70.0):
            return a1
        elif m >= trans(70.0) and m < trans(75.0):
            return a2
        elif m >= trans(75.0) and m < trans(80.0):
            return a3
        elif m >= trans(80.0) and m < trans(85.0):
            return a4
        elif m >= trans(85.0) and m < trans(90.0):
            return a5
        elif m >= trans(90.0) and m < trans(95.0):
            return a6
        elif m >= trans(95.0) and m < trans(100.0):
            return a7
        elif m >= trans(100.0) and m < trans(105.0):
            return a8
        elif m >= trans(105.0) and m < trans(110.0):
            return a9
        elif m >= trans(110.0) and m < trans(115.0):
            return a10
        elif m >= trans(115.0) and m < trans(120.0):
            return a11
        elif m >= trans(120.0) and m < trans(125.0):
            return a12
        elif m >= trans(125.0) and m < trans(130.0):
            return a13
        elif m >= trans(130) and m < trans(133.3):
            return a14
        else:
            return 0
       
    elif meta >= 0.001:
        return 0
    
def M_pisne(E):
    if ypisne == 1:
        return E
    elif ypisne == 0:
        return 0
    
### integreted yields


def Ehe4_pisne(i):
    E4He_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y4He1,y4He2,y4He3,y4He4,y4He5,y4He6,y4He7,y4He8,y4He9,y4He10,y4He11,y4He12,y4He13,y4He14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E4He_pisne[0]

def Ec12_pisne(i):
    E12C_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y12C1,y12C2,y12C3,y12C4,y12C5,y12C6,y12C7,y12C8,y12C9,y12C10,y12C11,y12C12,y12C13,y12C14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E12C_pisne[0]

def En14_pisne(i):
    E14N_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y14N1,y14N2,y14N3,y14N4,y14N5,y14N6,y14N7,y14N8,y14N9,y14N10,y14N11,y14N12,y14N13,y14N14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E14N_pisne[0]

def Eo16_pisne(i):
    E16O_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y16O1,y16O2,y16O3,y16O4,y16O5,y16O6,y16O7,y16O8,y16O9,y16O10,y16O11,y16O12,y16O13,y16O14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E16O_pisne[0]

def Ena23_pisne(i):
    E23Na_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y23Na1,y23Na2,y23Na3,y23Na4,y23Na5,y23Na6,y23Na7,y23Na8,y23Na9,y23Na10,y23Na11,y23Na12,y23Na13,y23Na14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E23Na_pisne[0]

def Emg24_pisne(i):
    E24Mg_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y24Mg1,y24Mg2,y24Mg3,y24Mg4,y24Mg5,y24Mg6,y24Mg7,y24Mg8,y24Mg9,y24Mg10,y24Mg11,y24Mg12,y24Mg13,y24Mg14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E24Mg_pisne[0]

def Eal27_pisne(i):
    E27Al_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y27Al1,y27Al2,y27Al3,y27Al4,y27Al5,y27Al6,y27Al7,y27Al8,y27Al9,y27Al10,y27Al11,y27Al12,y27Al13,y27Al14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E27Al_pisne[0]

def Esi28_pisne(i):
    E28Si_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y28Si1,y28Si2,y28Si3,y28Si4,y28Si5,y28Si6,y28Si7,y28Si8,y28Si9,y28Si10,y28Si11,y28Si12,y28Si13,y28Si14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E28Si_pisne[0]

def Ep31_pisne(i):
    E31P_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y31P1,y31P2,y31P3,y31P4,y31P5,y31P6,y31P7,y31P8,y31P9,y31P10,y31P11,y31P12,y31P13,y31P14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E31P_pisne[0]

def Es32_pisne(i):
    E32S_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y32S1,y32S2,y32S3,y32S4,y32S5,y32S6,y32S7,y32S8,y32S9,y32S10,y32S11,y32S12,y32S13,y32S14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E32S_pisne[0]

def Ek39_pisne(i):
    E39K_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y39K1,y39K2,y39K3,y39K4,y39K5,y39K6,y39K7,y39K8,y39K9,y39K10,y39K11,y39K12,y39K13,y39K14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E39K_pisne[0]

def Eca40_pisne(i):
    E40Ca_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y40Ca1,y40Ca2,y40Ca3,y40Ca4,y40Ca5,y40Ca6,y40Ca7,y40Ca8,y40Ca9,y40Ca10,y40Ca11,y40Ca12,y40Ca13,y40Ca14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E40Ca_pisne[0]

def Esc45_pisne(i):
    E45Sc_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y45Sc1,y45Sc2,y45Sc3,y45Sc4,y45Sc5,y45Sc6,y45Sc7,y45Sc8,y45Sc9,y45Sc10,y45Sc11,y45Sc12,y45Sc13,y45Sc14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E45Sc_pisne[0]

def Eti48_pisne(i):
    E48Ti_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y48Ti1,y48Ti2,y48Ti3,y48Ti4,y48Ti5,y48Ti6,y48Ti7,y48Ti8,y48Ti9,y48Ti10,y48Ti11,y48Ti12,y48Ti13,y48Ti14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E48Ti_pisne[0]

def Ev51_pisne(i):
    E51V_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y51V1,y51V2,y51V3,y51V4,y51V5,y51V6,y51V7,y51V8,y51V9,y51V10,y51V11,y51V12,y51V13,y51V14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E51V_pisne[0]

def Ecr52_pisne(i):
    E52Cr_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y52Cr1,y52Cr2,y52Cr3,y52Cr4,y52Cr5,y52Cr6,y52Cr7,y52Cr8,y52Cr9,y52Cr10,y52Cr11,y52Cr12,y52Cr13,y52Cr14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E52Cr_pisne[0]

def Emn55_pisne(i):
    E55Mn_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y55Mn1,y55Mn2,y55Mn3,y55Mn4,y55Mn5,y55Mn6,y55Mn7,y55Mn8,y55Mn9,y55Mn10,y55Mn11,y55Mn12,y55Mn13,y55Mn14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E55Mn_pisne[0]

def Efe56_pisne(i):
    E56Fe_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y56Fe1,y56Fe2,y56Fe3,y56Fe4,y56Fe5,y56Fe6,y56Fe7,y56Fe8,y56Fe9,y56Fe10,y56Fe11,y56Fe12,y56Fe13,y56Fe14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E56Fe_pisne[0]

def Eco59_pisne(i):
    E59Co_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y59Co1,y59Co2,y59Co3,y59Co4,y59Co5,y59Co6,y59Co7,y59Co8,y59Co9,y59Co10,y59Co11,y59Co12,y59Co13,y59Co14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E59Co_pisne[0]

def Eni58_pisne(i):
    E58Ni_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y58Ni1,y58Ni2,y58Ni3,y58Ni4,y58Ni5,y58Ni6,y58Ni7,y58Ni8,y58Ni9,y58Ni10,y58Ni11,y58Ni12,y58Ni13,y58Ni14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E58Ni_pisne[0]

def Ecu63_pisne(i):
    E63Cu_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y63Cu1,y63Cu2,y63Cu3,y63Cu4,y63Cu5,y63Cu6,y63Cu7,y63Cu8,y63Cu9,y63Cu10,y63Cu11,y63Cu12,y63Cu13,y63Cu14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E63Cu_pisne[0]

def Ezn64_pisne(i):
    E64Zn_pisne = integrate.quad(lambda m: Y_pisne(m,metal(i,m),y64Zn1,y64Zn2,y64Zn3,y64Zn4,y64Zn5,y64Zn6,y64Zn7,y64Zn8,y64Zn9,y64Zn10,y64Zn11,y64Zn12,y64Zn13,y64Zn14)*IMF(m)*Mall_sf_delay(i,m), 140, 270)
    return E64Zn_pisne[0]
    
################################################################################################################################

### CVMS Yields

def Y_cvms(m,meta,a1,a2):
    if meta < 0.001:
        if m < 266.0:
            return 0
        elif m >= 266.0 and m < 750.0:
            return a1
        elif m >= 750.0 and m < 1250.0:
            return a2
        else:
            return 0
    
    elif meta >= 0.001:
        return 0
    
def M_cvms(E):
    if ycvms == 1:
        return E
    elif ycvms == 0:
        return 0
    
### integrated yields

def Eh_cvms(i):
    Eh_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),yp1,yp2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return Eh_cvms[0]
def Ehe4_cvms(i):
    E4He_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y4He1,y4He2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E4He_cvms[0]
def Ec12_cvms(i):
    E12C_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y12C1,y12C2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E12C_cvms[0]
def En14_cvms(i):
    E14N_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y14N1,y14N2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E14N_cvms[0]
def Eo16_cvms(i):
    E16O_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y16O1,y16O2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E16O_cvms[0]
def Ena23_cvms(i):
    E23Na_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y23Na1,y23Na2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E23Na_cvms[0]
def Emg24_cvms(i):
    E24Mg_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y24Mg1,y24Mg2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E24Mg_cvms[0]
def Eal27_cvms(i):
    E27Al_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y27Al1,y27Al2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E27Al_cvms[0]
def Esi28_cvms(i):
    E28Si_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y28Si1,y28Si2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E28Si_cvms[0]
def Ep31_cvms(i):
    E31P_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y31P1,y31P2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E31P_cvms[0]
def Es32_cvms(i):
    E32S_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y32S1,y32S2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E32S_cvms[0]
def Ek39_cvms(i):
    E39K_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y39K1,y39K2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E39K_cvms[0]
def Eca40_cvms(i):
    E40Ca_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y40Ca1,y40Ca2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E40Ca_cvms[0]
def Esc45_cvms(i):
    E45Sc_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y45Sc1,y45Sc2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E45Sc_cvms[0]
def Eti48_cvms(i):
    E48Ti_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y48Ti1,y48Ti2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E48Ti_cvms[0]
def Ev51_cvms(i):
    E51V_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y51V1,y51V2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E51V_cvms[0]
def Ecr52_cvms(i):
    E52Cr_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y52Cr1,y52Cr2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E52Cr_cvms[0]
def Emn55_cvms(i):
    E55Mn_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y55Mn1,y55Mn2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E55Mn_cvms[0]
def Efe56_cvms(i):
    E56Fe_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y56Fe1,y56Fe2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E56Fe_cvms[0]
def Eco59_cvms(i):
    E59Co_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y59Co1,y59Co2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E59Co_cvms[0]
def Eni58_cvms(i):
    E58Ni_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y58Ni1,y58Ni2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E58Ni_cvms[0]
def Ecu63_cvms(i):
    E63Cu_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y63Cu1,y63Cu2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E63Cu_cvms[0]
def Ezn64_cvms(i):
    E64Zn_cvms = integrate.quad(lambda m: Y_cvms(m,metal(i,m),y64Zn1,y64Zn2)*IMF(m)*Mall_sf_delay(i,m), 266, 1250)
    return E64Zn_cvms[0]



################################################################################################################################
########################################################################################
###
### galaxy lifetime to redshift 
###
########################################################################################

### parameter

AU = 1.495978707 * 10**(11.0)              #[m]
pc = AU/(np.tan((1.0/3600.0)*np.pi/180.0)) #[m]
s = (365.25*24.0*60.0*60.0)**(-1)          #[yr]

### Plank collaboration ; Plank 2015 results

h_0_67 = 0.6727                    #67.27+-0.66 [km/s/Mpc]  ; PLANK satellite
h_0 = 100.0*h_0_67                 #[km/s/Mpc] ; current Hubble parameter
H_0 = 10**(3.0)/(s*10**6*pc)*h_0   #[1/yr]

omega_matter_0 = 0.1427 * h_0_67**(-2.0) 
omega_lambda_0 = 0.6844                  
omega_radiation_0 = 4.13 * 10**(-5) * h_0_67**(-2.0) 
omega_k_0 = 1.0 - (omega_matter_0+omega_lambda_0+omega_radiation_0)

def integrand(z):
    integrand = 1.0/(H_0*(1.0+z)*np.sqrt(omega_matter_0*(1.0+z)**(3.0) + omega_radiation_0*(1.0+z)**(4.0) + omega_lambda_0 + omega_k_0*(1.0+z)**(2.0)))
    return integrand

def integration(z1):
    result = np.zeros(len(z1))
    for i in range(len(z1)):
        integration = integrate.quad(lambda z : integrand(z),0.0,z1[i])[0]
        result[i] = integration/10**9 
    return result

### limit (max universe lifetime)

limit = integrate.quad(lambda z : integrand(z),0.0,np.inf)[0]/10**9

z1 = np.arange(0.01,3500,0.05)
time = integration(z1)

age = limit - time
age_of_universe = age[::-1]
z2 = z1[::-1]

def gNV(lis, num):
    idx = np.abs(np.asarray(lis) - num).argmin()
    return z2[idx]


################################################################################################################################

########################################################################################
###
### element mass evolution
###
########################################################################################


while T[i] < tmax:
        
    
    ## light element
    dMh = (M_in(Rh,T[i]) - M_fb(Mh[i]) - M_sf(Mh[i]) + M_cc(Eh_cc(i)) + M_Ia(Yh_Ia,qx) + M_agb(Eh_agb(i)) + M_hiagb(Eh_hiagb(i)) + M_cvms(Eh_cvms(i)) ) * dt
    dMhe4 = (M_in(Rhe,T[i]) - M_fb(Mhe4[i]) - M_sf(Mhe4[i]) + M_cc(Ehe4_cc(i)) + M_Ia(Yhe4_Ia,qx) + M_agb(Ehe4_agb(i)) + M_hiagb(Ehe4_hiagb(i)) + M_pisne(Ehe4_pisne(i)) + M_cvms(Ehe4_cvms(i)) ) * dt
    
    
    ## heavy element
    dMc12 = (M_in(Rhe,T[i]) - M_fb(Mc12[i]) - M_sf(Mc12[i]) + M_cc(Ec12_cc(i)) + M_Ia(Yc12_Ia,qx) + M_agb(Ec12_agb(i)) + M_hiagb(Ec12_hiagb(i)) + M_pisne(Ec12_pisne(i)) + M_cvms(Ec12_cvms(i)) ) * dt
    dMfe56 = (M_in(Rhe,T[i]) - M_fb(Mfe56[i]) - M_sf(Mfe56[i]) + M_cc(Efe56_cc(i)) + M_Ia(Yfe56_Ia,qx) + M_agb(Efe56_agb(i)) + M_hiagb(Efe56_hiagb(i)) + M_pisne(Efe56_pisne(i)) + M_cvms(Efe56_cvms(i)) ) * dt
    dMmg24 = (M_in(Rhe,T[i]) - M_fb(Mmg24[i]) - M_sf(Mmg24[i]) + M_cc(Emg24_cc(i)) + M_Ia(Ymg24_Ia,qx) + M_agb(Emg24_agb(i)) + M_hiagb(Emg24_hiagb(i)) + M_pisne(Emg24_pisne(i)) + M_cvms(Emg24_cvms(i)) ) * dt
    dMo16 = (M_in(Rhe,T[i]) - M_fb(Mo16[i]) - M_sf(Mo16[i]) + M_cc(Eo16_cc(i)) + M_Ia(Yo16_Ia,qx) + M_agb(Eo16_agb(i)) + M_hiagb(Eo16_hiagb(i)) + M_pisne(Eo16_pisne(i)) + M_cvms(Eo16_cvms(i)) ) * dt

    mh = Mh[i]
    mhe4 = Mhe4[i]
    mh += dMh
    mhe4 += dMhe4
   
    mc12 = Mc12[i]
    mc12 += dMc12	
    mfe56 = Mfe56[i]
    mfe56 += dMfe56
    mmg24 = Mmg24[i]
    mmg24 += dMmg24
    mo16 = Mo16[i]
    mo16 += dMo16

    ### aditional element
    dMn14 = (M_in(Rhe,T[i]) - M_fb(Mn14[i]) - M_sf(Mn14[i]) + M_cc(En14_cc(i)) + M_Ia(Yn14_Ia,qx) + M_agb(En14_agb(i)) + M_hiagb(En14_hiagb(i)) + M_pisne(En14_pisne(i)) + M_cvms(En14_cvms(i)) ) * dt
    mn14 = Mn14[i]
    mn14 += dMn14
    dMna23 = (M_in(Rhe,T[i]) - M_fb(Mna23[i]) - M_sf(Mna23[i]) + M_cc(Ena23_cc(i)) + M_Ia(Yna23_Ia,qx) + M_agb(Ena23_agb(i)) + M_hiagb(Ena23_hiagb(i)) + M_pisne(Ena23_pisne(i)) + M_cvms(Ena23_cvms(i)) ) * dt
    mna23 = Mna23[i]
    mna23 += dMna23
    dMal27 = (M_in(Rhe,T[i]) - M_fb(Mal27[i]) - M_sf(Mal27[i]) + M_cc(Eal27_cc(i)) + M_Ia(Yal27_Ia,qx) + M_agb(Eal27_agb(i)) + M_hiagb(Eal27_hiagb(i)) + M_pisne(Eal27_pisne(i)) + M_cvms(Eal27_cvms(i)) ) * dt
    mal27 = Mal27[i]
    mal27 += dMal27
    dMsi28 = (M_in(Rhe,T[i]) - M_fb(Msi28[i]) - M_sf(Msi28[i]) + M_cc(Esi28_cc(i)) + M_Ia(Ysi28_Ia,qx) + M_agb(Esi28_agb(i)) + M_hiagb(Esi28_hiagb(i)) + M_pisne(Esi28_pisne(i)) + M_cvms(Esi28_cvms(i)) ) * dt
    msi28 = Msi28[i]
    msi28 += dMsi28
    dMp31 = (M_in(Rhe,T[i]) - M_fb(Mp31[i]) - M_sf(Mp31[i]) + M_cc(Ep31_cc(i)) + M_Ia(Yp31_Ia,qx) + M_agb(Ep31_agb(i)) + M_hiagb(Ep31_hiagb(i)) + M_pisne(Ep31_pisne(i)) + M_cvms(Ep31_cvms(i)) ) * dt
    mp31 = Mp31[i]
    mp31 += dMp31
    dMs32 = (M_in(Rhe,T[i]) - M_fb(Ms32[i]) - M_sf(Ms32[i]) + M_cc(Es32_cc(i)) + M_Ia(Ys32_Ia,qx) + M_agb(Es32_agb(i)) + M_hiagb(Es32_hiagb(i)) + M_pisne(Es32_pisne(i)) + M_cvms(Es32_cvms(i)) ) * dt
    ms32 = Ms32[i]
    ms32 += dMs32
    dMni58 = (M_in(Rhe,T[i]) - M_fb(Mni58[i]) - M_sf(Mni58[i]) + M_cc(Eni58_cc(i)) + M_Ia(Yni58_Ia,qx) + M_agb(Eni58_agb(i)) + M_hiagb(Eni58_hiagb(i)) + M_pisne(Eni58_pisne(i)) + M_cvms(Eni58_cvms(i)) ) * dt
    mni58 = Mni58[i]
    mni58 += dMni58
    dMco59 = (M_in(Rhe,T[i]) - M_fb(Mco59[i]) - M_sf(Mco59[i]) + M_cc(Eco59_cc(i)) + M_Ia(Yco59_Ia,qx) + M_agb(Eco59_agb(i)) + M_hiagb(Eco59_hiagb(i)) + M_pisne(Eco59_pisne(i)) + M_cvms(Eco59_cvms(i)) ) * dt
    mco59 = Mco59[i]
    mco59 += dMco59


    dMcu63 = (M_in(Rcu63,T[i]) - M_fb(Mcu63[i]) - M_sf(Mcu63[i]) + M_cc(Ecu63_cc(i)) + M_Ia(Ycu63_Ia,qx) + M_pisne(Ecu63_pisne(i)) + M_cvms(Ecu63_cvms(i)))* dt
    mcu63 = Mcu63[i]
    mcu63 += dMcu63
    dMzn64 = (M_in(Rzn64,T[i]) - M_fb(Mzn64[i]) - M_sf(Mzn64[i]) + M_cc(Ezn64_cc(i)) + M_Ia(Yzn64_Ia,qx) + M_pisne(Ezn64_pisne(i)) + M_cvms(Ezn64_cvms(i)))* dt
    mzn64 = Mzn64[i]
    mzn64 += dMzn64
    dMca40 = (M_in(Rca40,T[i]) - M_fb(Mca40[i]) - M_sf(Mca40[i]) + M_cc(Eca40_cc(i)) + M_Ia(Yca40_Ia,qx) + M_pisne(Eca40_pisne(i)) + M_cvms(Eca40_cvms(i)))* dt
    mca40 = Mca40[i]
    mca40 += dMca40
    dMk39 = (M_in(Rk39,T[i]) - M_fb(Mk39[i]) - M_sf(Mk39[i]) + M_cc(Ek39_cc(i)) + M_Ia(Yk39_Ia,qx) + M_pisne(Ek39_pisne(i)) + M_cvms(Ek39_cvms(i)))* dt
    mk39 = Mk39[i]
    mk39 += dMk39
    dMsc45 = (M_in(Rsc45,T[i]) - M_fb(Msc45[i]) - M_sf(Msc45[i]) + M_cc(Esc45_cc(i)) + M_Ia(Ysc45_Ia,qx) + M_pisne(Esc45_pisne(i)) + M_cvms(Esc45_cvms(i)))* dt
    msc45 = Msc45[i]
    msc45 += dMsc45
    dMti48 = (M_in(Rti48,T[i]) - M_fb(Mti48[i]) - M_sf(Mti48[i]) + M_cc(Eti48_cc(i)) + M_Ia(Yti48_Ia,qx) + M_pisne(Eti48_pisne(i)) + M_cvms(Eti48_cvms(i)))* dt
    mti48 = Mti48[i]
    mti48 += dMti48
    dMv51 = (M_in(Rv51,T[i]) - M_fb(Mv51[i]) - M_sf(Mv51[i]) + M_cc(Ev51_cc(i)) + M_Ia(Yv51_Ia,qx) + M_pisne(Ev51_pisne(i)) + M_cvms(Ev51_cvms(i)))* dt
    mv51 = Mv51[i]
    mv51 += dMv51
    dMcr52 = (M_in(Rcr52,T[i]) - M_fb(Mcr52[i]) - M_sf(Mcr52[i]) + M_cc(Ecr52_cc(i)) + M_Ia(Ycr52_Ia,qx) + M_pisne(Ecr52_pisne(i)) + M_cvms(Ecr52_cvms(i)))* dt
    mcr52 = Mcr52[i]
    mcr52 += dMcr52
    dMmn55 = (M_in(Rmn55,T[i]) - M_fb(Mmn55[i]) - M_sf(Mmn55[i]) + M_cc(Emn55_cc(i)) + M_Ia(Ymn55_Ia,qx) + M_pisne(Emn55_pisne(i)) + M_cvms(Emn55_cvms(i)))* dt
    mmn55 = Mmn55[i]
    mmn55 += dMmn55
    mall=mh+mhe4+mc12+mn14+mo16+mna23+mmg24+mal27+msi28+mp31+ms32+mk39+mca40+msc45+mti48+mv51+mcr52+mmn55+mfe56+mni58+mco59+mcu63+mzn64 

    
    sfr = Mall_sf(i)
    
    zup = Z(i)
    
    
    t = T[i]
    t_uni = T[i] + limit - tmax
    rs = gNV(age_of_universe, t_uni)
    
    t += dt

    Mh.append(mh)
    Mhe4.append(mhe4)
    Mc12.append(mc12)
    Mn14.append(mn14)
    Mo16.append(mo16)
    Mna23.append(mna23)
    Mmg24.append(mmg24)
    Mal27.append(mal27)
    Msi28.append(msi28)
    Mp31.append(mp31)
    Ms32.append(ms32)
    Mk39.append(mk39)
    Mca40.append(mca40)
    Msc45.append(msc45)
    Mti48.append(mti48)
    Mv51.append(mv51)
    Mcr52.append(mcr52)
    Mmn55.append(mmn55)
    Mfe56.append(mfe56)
    Mni58.append(mni58)
    Mco59.append(mco59)
    Mcu63.append(mcu63)
    Mzn64.append(mzn64) 
    
    Mccsn_mg24.append(M_cc(Emg24_cc(i)))
    Magb_mg24.append(M_agb(Emg24_agb(i)))

    Mccsn_fe56.append(M_cc(Efe56_cc(i)))
    Magb_fe56.append(M_agb(Efe56_agb(i)))
    
    Mall.append(mall)
    
    z.append(zup)
    
    T.append(t)
    SFR.append(sfr)
    redshift.append(rs)
    
    i = len(T) -1
    qx = T[i]
    
    meta = z[i]

####################################################################################################################################################################################################################################################################

##################################################################################################################################
###
### [Fe/H] vs [X/Fe] plot
### 
###
################################################################################################################################

##### data
u = 1.660 * 10**(-27)
M_sun = 1.989 * 10**(30)

Fe56_mass = 55.85 * u
Mg24_mass = 24.31 * u
H_mass = 1.008 * u
O16_mass = 16.00 * u
C12_mass = 12.01 * u	

### atomic number

from solar_composition import *

### solar abundance

#R_fe56 = efe56 / eall
#R_mg24 = emg24 / eall
#R_h = eh1 / eall
#R_o16 = eo16 / eall
#R_c12 = ec12 / eall


### solar number density

n_c12_so = M_sun * R_c12 / C12_mass
n_fe56_so = M_sun * R_fe56 / Fe56_mass
n_mg24_so = M_sun * R_mg24 / Mg24_mass
n_h_so = M_sun * R_h / H_mass
n_o16_so = M_sun * R_o16 / O16_mass


### abundance ratio

Mfe561 = copy.copy(Mfe56)
Mfe561.remove(0)
#print(Mfe1)
Mh1 = copy.copy(Mh)
#Mh1.remove(0)
Mmg241 = copy.copy(Mmg24)
Mmg241.remove(0)
Mo161 = copy.copy(Mo16)
Mo161.remove(0)
Mc121 = copy.copy(Mc12)
Mc121.remove(0)
T1 = copy.copy(T)
T1.remove(0)

### aditional data

N14_mass = 14.01 * u
#R_n14 = en14 / eall
n_n14_so = M_sun * R_n14 / N14_mass
Mn141 = copy.copy(Mn14)
Mn141.remove(0)

S32_mass = 32.07 * u
#R_s32 = es32 / eall
n_s32_so = M_sun * R_s32 / S32_mass
Ms321 = copy.copy(Ms32)
Ms321.remove(0) 

Ca40_mass = 40.08 * u
#R_ca40 = eca40 / eall
n_ca40_so = M_sun * R_ca40 / Ca40_mass
Mca401 = copy.copy(Mca40)
Mca401.remove(0)  

Na23_mass = 22.99 * u
#R_na23 = ena23 / eall
n_na23_so = M_sun * R_na23 / Na23_mass
Mna231 = copy.copy(Mna23)
Mna231.remove(0)

Al27_mass = 26.98 * u
#R_al27 = eal27 / eall
n_al27_so = M_sun * R_al27 / Al27_mass
Mal271 = copy.copy(Mal27)
Mal271.remove(0) 

Si28_mass = 26.98 * u
#R_si28 = esi28 / eall
n_si28_so = M_sun * R_si28 / Si28_mass
Msi281 = copy.copy(Msi28)
Msi281.remove(0) 

P31_mass = 30.97 * u
#R_p31 = ep31 / eall
n_p31_so = M_sun * R_p31 / P31_mass
Mp311 = copy.copy(Mp31)
Mp311.remove(0) 

K39_mass = 39.10 * u
#R_k39 = ek39 / eall
n_k39_so = M_sun * R_k39 / K39_mass
Mk391 = copy.copy(Mk39)
Mk391.remove(0)

Sc45_mass = 44.96 * u
#R_sc45 = esc45 / eall
n_sc45_so = M_sun * R_sc45 / Sc45_mass
Msc451 = copy.copy(Msc45)
Msc451.remove(0) 

Ti48_mass = 47.88 * u
#R_ti48 = eti48 / eall
n_ti48_so = M_sun * R_ti48 / Ti48_mass
Mti481 = copy.copy(Mti48)
Mti481.remove(0) 

V51_mass = 50.94 * u
#R_v51 = ev51 / eall
n_v51_so = M_sun * R_v51 / V51_mass
Mv511 = copy.copy(Mv51)
Mv511.remove(0)

Cr52_mass = 52.00 * u
#R_cr52 = ecr52 / eall
n_cr52_so = M_sun * R_cr52 / Cr52_mass
Mcr521 = copy.copy(Mcr52)
Mcr521.remove(0) 

Mn55_mass = 54.94 * u
#R_mn55 = emn55 / eall
n_mn55_so = M_sun * R_mn55 / Mn55_mass
Mmn551 = copy.copy(Mmn55)
Mmn551.remove(0) 
 
Ni58_mass = 58.69 * u
#R_ni58 = eni58 / eall
n_ni58_so = M_sun * R_ni58 / Ni58_mass
Mni581 = copy.copy(Mni58)
Mni581.remove(0)

Co59_mass = 58.93 * u
#R_co59 = eco59 / eall
n_co59_so = M_sun * R_co59 / Co59_mass
Mco591 = copy.copy(Mco59)
Mco591.remove(0) 

Cu63_mass = 63.55 * u
#R_cu63 = ecu63 / eall
n_cu63_so = M_sun * R_cu63 / Cu63_mass
Mcu631 = copy.copy(Mcu63)
Mcu631.remove(0)    

Zn64_mass = 63.93 * u
#R_zn64 = ezn64 / eall
n_zn64_so = M_sun * R_zn64 / Zn64_mass
Mzn641 = copy.copy(Mzn64)
Mzn641.remove(0)

################################################################################################################################

### abundance formalizm
 
fe56_h = [(np.log10((x*M_sun/Fe56_mass) / (y*M_sun/H_mass)) - np.log10(n_fe56_so / n_h_so) ) \
        for (x, y) in zip(Mfe561, Mh1)] 

o16_h = [(np.log10((x*M_sun/O16_mass) / (y*M_sun/H_mass)) + 12 ) \
        for (x, y) in zip(Mo161, Mh1)] 

#fe56_mg24 = [(np.log10((x*M_sun/Fe56_mass) / (y*M_sun/Mg24_mass)) - np.log10(n_fe56_so / n_mg24_so) ) \
        #for (x, y) in zip(Mfe561, Mmg241)] 
    
mg24_fe56 = [(np.log10((x*M_sun/Mg24_mass) / (y*M_sun/Fe56_mass)) - np.log10(n_mg24_so / n_fe56_so) ) \
        for (x, y) in zip(Mmg241, Mfe561)] 


def X_fe56(mass,X,n_x_so):
    x_fe56 = [(np.log10((x*M_sun/mass) / (y*M_sun/Fe56_mass)) - np.log10(n_x_so / n_fe56_so) ) \
            for (x, y) in zip(X, Mfe561)]
    
    return x_fe56 

def X_o16(mass,X):
    x_o16 = [(np.log10((x*M_sun/mass) / (y*M_sun/O16_mass))) \
            for (x, y) in zip(X, Mo161)]
    
    return x_o16


##################################################################################################################################

### mass evolution

### hydrogen evolution data
Mh_T = zip(T,Mh)
with open('H.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(Mh_T)

### helium evolution data
Mhe4_T = zip(T,Mhe4)
with open('He4.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(Mhe4_T)

### SFR evolution data
SFR_T = zip(T1,SFR)
with open('SFR.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(SFR_T)

### carbon evolution data
Mc12_T = zip(T,Mc12)
with open('C12.csv', 'w') as f:
	writer = csv.writer(f, delimiter='\t')
	writer.writerows(Mc12_T) 

### iron evolution data
Mfe56_T = zip(T,Mfe56)
with open('Fe56.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(Mfe56_T)

### magnesium evolution data
Mmg24_T = zip(T,Mmg24)
with open('Mg24.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(Mmg24_T)

### oxygen evolution data
Mo16_T = zip(T,Mo16)
with open('O16.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(Mo16_T)

Mn14_T = zip(T,Mn14)
with open('N14.csv', 'w') as f:
	writer = csv.writer(f, delimiter='\t')
	writer.writerows(Mn14_T)

	
Ms32_T = zip(T,Ms32)
with open('S32.csv', 'w') as f:
	writer = csv.writer(f, delimiter='\t')
	writer.writerows(Ms32_T) 

Mca40_T = zip(T,Mca40)
with open('Ca40.csv', 'w') as f:
	writer = csv.writer(f, delimiter='\t')
	writer.writerows(Mca40_T) 

    ### iron evolution data
Mna23_T = zip(T,Mna23)
with open('Na23.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Mna23_T)

### magnesium evolution data
Mal27_T = zip(T,Mal27)
with open('Al27.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Mal27_T)
    
Msi28_T = zip(T,Msi28)
with open('Al27.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Msi28_T) 

### oxygen evolution data
Mp31_T = zip(T,Mp31)
with open('P31.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Mp31_T)

Mk39_T = zip(T,Mk39)
with open('K39.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Mk39_T)


Msc45_T = zip(T,Msc45)
with open('Sc45.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Msc45_T) 

Mti48_T = zip(T,Mti48)
with open('Ti48.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Mti48_T) 

### iron evolution data
Mv51_T = zip(T,Mv51)
with open('V51.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Mv51_T)

### magnesium evolution data
Mcr52_T = zip(T,Mcr52)
with open('Cr52.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Mcr52_T)

### oxygen evolution data
Mmn55_T = zip(T,Mmn55)
with open('Mn55.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Mmn55_T)

Mni58_T = zip(T,Mni58)
with open('Ni58.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Mni58_T)


Mco59_T = zip(T,Mco59)
with open('Co59.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Mco59_T) 

Mcu63_T = zip(T,Mcu63)
with open('Cu63.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Mcu63_T) 

### iron evolution data
Mzn64_T = zip(T,Mzn64)
with open('Zn64.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Mzn64_T)


##################################################################################################################################
### abundance evolution

###  [Fe/H] evolution plot
vs = zip(T1,fe56_h)
with open('FeHvsT.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(vs)

###  [Mg/Fe] evolution plot
vs = zip(T1,X_fe56(Mg24_mass,Mmg241,n_mg24_so))
with open('MgFevsT.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(vs)

###  [O/Fe] evolution plot
vs = zip(T1,X_fe56(O16_mass,Mo161,n_o16_so))
with open('OFevsT.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(vs)
        
###  [Si/Fe] evolution plot
vs = zip(T1,X_fe56(Si28_mass,Msi281,n_si28_so))
with open('SiFevsT.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(vs)
        
###  [C/Fe] evolution plot
vs = zip(T1,X_fe56(C12_mass,Mc121,n_c12_so))
with open('CFevsT.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(vs)

###  [N/Fe] evolution plot
vs = zip(T1,X_fe56(N14_mass,Mn141,n_n14_so))
with open('NFevsT.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(vs)

###  [Al/Fe] evolution plot
vs = zip(T1,X_fe56(Al27_mass,Mal271,n_al27_so))
with open('AlFevsT.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(vs)

###  [Mn/Fe] evolution plot
vs = zip(T1,X_fe56(Mn55_mass,Mmn551,n_mn55_so))
with open('MnFevsT.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(vs)
        
###  [Cr/Fe] evolution plot
vs = zip(T1,X_fe56(Cr52_mass,Mcr521,n_cr52_so))
with open('CrFevsT.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(vs)

###  [Co/Fe] evolution plot
vs = zip(T1,X_fe56(Co59_mass,Mco591,n_co59_so))
with open('CoFevsT.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(vs)        

###  [Ni/Fe] evolution plot
vs = zip(T1,X_fe56(Ni58_mass,Mni581,n_ni58_so))
with open('NiFevsT.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(vs)
        
###  [Ti/Fe] evolution plot
vs = zip(T1,X_fe56(Ti48_mass,Mti481,n_ti48_so))
with open('TiFevsT.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(vs)
        
###  [Sc/Fe] evolution plot
vs = zip(T1,X_fe56(Sc45_mass,Msc451,n_sc45_so))
with open('ScFevsT.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(vs)
        
###  SFR evolution plot
vs = zip(T1,SFR)
with open('SFR.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(vs)

###  metalicity evolution plot
vs = zip(T,z)
with open('metal.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(vs)

##################################################################################################################################

### [x/Fe] vs [Fe/H]

### [Fe/H] vs [C/Fe] plot
vs = zip(fe56_h,X_fe56(C12_mass,Mc121,n_c12_so))
with open('FeHvsCFe.csv', 'w') as f:
	writer = csv.writer(f, delimiter='\t')
	writer.writerows(vs) 

###  [Fe/H] vs [Mg/Fe] plot
vs = zip(fe56_h,X_fe56(Mg24_mass,Mmg241,n_mg24_so))
with open('FeHvsMgFe.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(vs)

###  [Fe/H] vs [O/Fe] plot
vs = zip(fe56_h,X_fe56(O16_mass,Mo161,n_o16_so))
with open('FeHvsOFe.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(vs)

### [Fe/H] vs [N/Fe] plot
vs = zip(fe56_h,X_fe56(N14_mass,Mn141,n_n14_so))
with open('FeHvsNFe.csv', 'w') as f:
	writer = csv.writer(f, delimiter='\t')
	writer.writerows(vs) 


### [Fe/H] vs [S/Fe] plot
vs = zip(fe56_h,X_fe56(S32_mass,Ms321,n_s32_so))
with open('FeHvsSFe.csv', 'w') as f:
	writer = csv.writer(f, delimiter='\t')
	writer.writerows(vs) 


### [Fe/H] vs [Ca/Fe] plot
vs = zip(fe56_h,X_fe56(Ca40_mass,Mca401,n_ca40_so))
with open('FeHvsCaFe.csv', 'w') as f:
	writer = csv.writer(f, delimiter='\t')
	writer.writerows(vs) 
    
### [Fe/H] vs [Na/Fe] plot
vs = zip(fe56_h,X_fe56(Na23_mass,Mna231,n_na23_so))
with open('FeHvsNaFe.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(vs) 

### [Fe/H] vs [Al/Fe] plot
vs = zip(fe56_h,X_fe56(Al27_mass,Mal271,n_al27_so))
with open('FeHvsAlFe.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(vs) 
    
### [Fe/H] vs [Si/Fe] plot
vs = zip(fe56_h,X_fe56(Si28_mass,Msi281,n_si28_so))
with open('FeHvsSiFe.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(vs) 
    

### [Fe/H] vs [P/Fe] plot
vs = zip(fe56_h,X_fe56(P31_mass,Mp311,n_p31_so))
with open('FeHvsPFe.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(vs) 

### [Fe/H] vs [K/Fe] plot
vs = zip(fe56_h,X_fe56(K39_mass,Mna231,n_na23_so))
with open('FeHvsKFe.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(vs) 

### [Fe/H] vs [Sc/Fe] plot
vs = zip(fe56_h,X_fe56(Sc45_mass,Msc451,n_sc45_so))
with open('FeHvsScFe.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(vs)     
    
### [Fe/H] vs [Ti/Fe] plot
vs = zip(fe56_h,X_fe56(Ti48_mass,Mti481,n_ti48_so))
with open('FeHvsTiFe.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(vs) 

### [Fe/H] vs [V/Fe] plot
vs = zip(fe56_h,X_fe56(V51_mass,Mna231,n_na23_so))
with open('FeHvsVFe.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(vs) 

### [Fe/H] vs [Cr/Fe] plot
vs = zip(fe56_h,X_fe56(Cr52_mass,Mcr521,n_cr52_so))
with open('FeHvsCrFe.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(vs) 
    
### [Fe/H] vs [Mn/Fe] plot
vs = zip(fe56_h,X_fe56(Mn55_mass,Mmn551,n_mn55_so))
with open('FeHvsMnFe.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(vs) 

### [Fe/H] vs [Ni/Fe] plot
vs = zip(fe56_h,X_fe56(Ni58_mass,Mna231,n_na23_so))
with open('FeHvsNiFe.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(vs) 

### [Fe/H] vs [Co/Fe] plot
vs = zip(fe56_h,X_fe56(Co59_mass,Mco591,n_co59_so))
with open('FeHvsCoFe.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(vs) 
    
### [Fe/H] vs [Cu/Fe] plot
vs = zip(fe56_h,X_fe56(Cu63_mass,Mcu631,n_cu63_so))
with open('FeHvsCuFe.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(vs) 

### [Fe/H] vs [Zn/Fe] plot
vs = zip(fe56_h,X_fe56(Zn64_mass,Mna231,n_na23_so))
with open('FeHvsZnFe.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(vs) 
################################################################################################################################

### [O/H] vs [Fe/O] plot

vs = zip(o16_h,X_o16(Fe56_mass,Mfe561))
with open('OHvsFeO.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(vs) 
    
### [Fe/Mg] vs redshift

vs = zip(redshift,mg24_fe56)
with open('MgFevsredshift.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(vs) 
    


################################################################################################################################

### test 7-1

## vs time

Mccsn_mg24_T = zip(T,Mccsn_mg24)
with open('Mg24_ccsn.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Mccsn_mg24_T)
    
Magb_mg24_T = zip(T,Magb_mg24)
with open('Mg24_agb.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Magb_mg24_T)  
    
Mccsn_fe56_T = zip(T,Mccsn_fe56)
with open('Fe56_ccsn.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Mccsn_fe56_T)

Magb_fe56_T = zip(T,Magb_fe56)
with open('Fe56_agb.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Magb_fe56_T) 
    
SFR_T = zip(T,SFR)
with open('SFR_T.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(SFR_T) 
    
## vs [Fe/H]

Mccsn_mg241 = copy.copy(Mccsn_mg24)
Mccsn_mg241.remove(0)

Magb_mg241 = copy.copy(Magb_mg24)
Magb_mg241.remove(0) 

Mccsn_mg24_feh = zip(fe56_h,Mccsn_mg241)
with open('Mg24_ccsn_feh.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Mccsn_mg24_feh)

Magb_mg24_feh = zip(fe56_h,Magb_mg241)
with open('Mg24_agb_feh.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Magb_mg24_feh)
    
Mccsn_fe561 = copy.copy(Mccsn_fe56)
Mccsn_fe561.remove(0) 
Magb_fe561 = copy.copy(Magb_fe56)
Magb_fe561.remove(0) 
    
Mccsn_fe56_feh = zip(fe56_h,Mccsn_fe561)
with open('Fe56_ccsn_feh.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Mccsn_fe56_feh)

Magb_fe56_feh = zip(fe56_h,Magb_fe561)
with open('Fe56_agb_feh.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(Magb_fe56_feh)
    
SFR1 = copy.copy(SFR)
SFR1.remove(0) 

SFR_feh = zip(fe56_h,SFR1)
with open('SFR_feh.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(SFR_feh)

################################################################################################################################


