#!/usr/bin/env python
# -*- coding: ascii -*-

r"""
RocketUnits provides a graphic user interface (GUI) for engineering units conversion.

RocketUnits provides units conversion for a number of engineering categories.
Included units categories include: Acceleration, Angle, AngVelocity, 
Area, CoeffThermExp(CTE), DeltaT, Density, ElementDensity, Energy, EnergySpec, 
Force, Frequency, HeatCapacity, HeatFlux, HxCoeff, Isp, Length, Mass, MassFlow, 
MolecularWt, Power, Pressure, SurfaceTension, Tank_PV/W, Temperature, 
ThermalCond, Time, Velocity, Viscosity_Dynamic, Viscosity_Kinematic, Volume, 
and VolumeFlow.
Unit conversion can be performed either with the included GUI, or directly
from python by importing the units conversion data file.


RocketUnits
Copyright (C) 2020  Applied Python

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

-----------------------

"""
import os
here = os.path.abspath(os.path.dirname(__file__))


# for multi-file projects see LICENSE file for authorship info
# for single file projects, insert following information
__author__ = 'Charlie Taylor'
__copyright__ = 'Copyright (c) 2020 Charlie Taylor'
__license__ = 'GPL-3'

# run metadata_reset.py to update version number
__version__ = '0.1.10'  # METADATA_RESET:__version__ = '<<version>>'
__email__ = "cet@appliedpython.com"
__status__ = "4 - Beta" # "3 - Alpha", "4 - Beta", "5 - Production/Stable"

#
# import statements here. (built-in first, then 3rd party, then yours)
#

categoryD = {}    # index=category name, value=list of members (e.g. 'Area':['inch**2', 'ft**2', 'cm**2', 'm**2'])
cat_defaultD = {} # index=category name, value=default units (e.g. 'Area':'inch**2')
unit_catD = {}    # index=units name, value=category (e.g. 'inch':'Length')
conv_factD = {}   # index=units name, value=float conversion value to default units (e.g. 'cm':1.0/2.54)
offsetD = {}      # index=units name, value=float offset value (e.g. 'cm':0.0)

# N = 1 kg-m/sec**2,  g = 9.80665 m/sec**2
# (NOTE: time=='s',  Isp=='sec')

def get_version():
    return __version__

def parse_float_string( sinp="1 atm" ):
    """
    Given a string input, parse into float and units string.
    String must be of format "<number> <units>" (at least one space)
    
    Return tuple of (float, units string)
    NOTE: if input is NOT a string, return None, None
    """
    if type(sinp) != type("string"):
        return None, None
        
    sL = sinp.split()
    if len(sL) != 2:
        raise('sinp="%s" String must be of format "<number> <units>"'%sinp)
        
    fstr, ustr = sL
    return float(fstr), ustr # (float, units string)
    

def convert_string( sinp="1 atm", rtn_units="psia" ):
    """
    Given a string input, parse into float of desired units.
    String must be of format "<number> <units>" (at least one space)
    NOTE: if input is NOT a string, simply return it.
    """
    if type(sinp) != type("string"):
        return sinp

    sL = sinp.split()
    if len(sL) != 2:
        raise('sinp="%s" String must be of format "<number> <units>"'%sinp)

    if sL[0] == "None":
        return None
    else:
        val = float(sL[0])
    units = sL[1]
    return convert_value(val, units, rtn_units)

def create_category( c_name='', def_units='' ):
    """Create a Units Category and define the default units"""
    cat_defaultD[c_name]  = def_units
    unit_catD[def_units]  = c_name
    conv_factD[def_units] = float(1.0)
    offsetD[def_units]    = float(0.0)
    
# Read As: 1 default unit = conv_factor u_name units
def add_units_to_category( c_name="", u_name="", conv_factor=1.0, offset=0.0 ):
    """
    Add conversion factor and offset for Units(u_name) to Category(c_name)
    Read As: 1 default unit = conv_factor u_name units
    """
    unit_catD[u_name]  = c_name
    conv_factD[u_name] = float(conv_factor)
    offsetD[u_name]    = float(offset)
    
    if c_name in categoryD:
        categoryD[ c_name ].append( u_name )
    else:
        categoryD[ c_name ] = [u_name]

def units_in_category( u_name="", c_name=""):
    """Return True if units are in category."""
    return unit_catD[u_name] == c_name
    
def chk_units_in_category( units, category ):
    """Raise an error if units are not in category"""
    if category not in categoryD:
        s = '\nCategories = ' + ', '.join( sorted( list( categoryD.keys() ) ) )
        raise Exception('ERROR: category "%s" is not recognized.'%(category, ) + s)
    
    if not unit_catD.get(units, ''):
        s = '\nCategory "%s" = '%category + ', '.join( categoryD[category] )
        raise Exception('ERROR: units "%s" are not recognized.'%(units, ) + s)

    if not units_in_category(u_name=units, c_name=category):
        s = '\nCategory "%s" = '%category + ', '.join( categoryD[category] )

        raise Exception('ERROR: units "%s" are not in category "%s"'%(units, category) + s)
    return True

def convert_value( inp_val=20.0, inp_units='degC', out_units='degK'):
    """Convert inp_val from inp_units to out_units and return.
        :param inp_val   : input value to be converted
        :param inp_units : units of inp_val
        :param out_units : desired output units
        :type inp_val   : float
        :type inp_units : str
        :type out_units : str
        :return: value converted from inp_units to out_units
        :retype: float
    """
    # convert inp_val to default units
    def_unit_val = (inp_val - offsetD[inp_units]) / conv_factD[inp_units]
    # convert from default units to requested output units
    return def_unit_val * conv_factD[out_units] + offsetD[out_units]
    
# Read As: 1 default unit = conv_factD target units
def get_value_str( inp_val=20.0, inp_units='degC', out_units='degK', fmt='%g'):
    val = convert_value(inp_val=inp_val, inp_units=inp_units, out_units=out_units)
    return fmt%val + ' %s'%out_units

def get_category( units ):
    """return the category that units belongs to."""
    if units in unit_catD:
        return unit_catD[ units ]
    return ''

# Creating Unit Category for "Acceleration"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="Acceleration", def_units="ft/s**2" )
add_units_to_category( c_name="Acceleration", u_name="cm/s**2"  , conv_factor=30.48, offset=0.0 )
add_units_to_category( c_name="Acceleration", u_name="ft/s**2"  , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Acceleration", u_name="gee"      , conv_factor=0.031080948777, offset=0.0 )
add_units_to_category( c_name="Acceleration", u_name="m/s**2"   , conv_factor=0.3048, offset=0.0 )
add_units_to_category( c_name="Acceleration", u_name="mile/hr/s", conv_factor=0.681818181818, offset=0.0 )

# Creating Unit Category for "Angle"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="Angle", def_units="deg" )
add_units_to_category( c_name="Angle", u_name="arcmin"    , conv_factor=60.0, offset=0.0 )
add_units_to_category( c_name="Angle", u_name="arcsec"    , conv_factor=3600.0, offset=0.0 )
add_units_to_category( c_name="Angle", u_name="circle"    , conv_factor=0.00277777777778, offset=0.0 )
add_units_to_category( c_name="Angle", u_name="deg"       , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Angle", u_name="grad"      , conv_factor=1.11111111111, offset=0.0 )
add_units_to_category( c_name="Angle", u_name="rad"       , conv_factor=0.0174532925199, offset=0.0 )
add_units_to_category( c_name="Angle", u_name="revolution", conv_factor=0.00277777777778, offset=0.0 )

# Creating Unit Category for "AngVelocity"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="AngVelocity", def_units="rpm" )
add_units_to_category( c_name="AngVelocity", u_name="deg/min", conv_factor=360.0, offset=0.0 )
add_units_to_category( c_name="AngVelocity", u_name="deg/s"  , conv_factor=6.0, offset=0.0 )
add_units_to_category( c_name="AngVelocity", u_name="rad/min", conv_factor=6.28318530718, offset=0.0 )
add_units_to_category( c_name="AngVelocity", u_name="rad/s"  , conv_factor=0.10471975512, offset=0.0 )
add_units_to_category( c_name="AngVelocity", u_name="rpm"    , conv_factor=1.0, offset=0.0 )

# Creating Unit Category for "Area"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="Area", def_units="inch**2" )
add_units_to_category( c_name="Area", u_name="acre"   , conv_factor=1.59422507907e-07, offset=0.0 )
add_units_to_category( c_name="Area", u_name="cm**2"  , conv_factor=6.4516, offset=0.0 )
add_units_to_category( c_name="Area", u_name="ft**2"  , conv_factor=0.00694444444444, offset=0.0 )
add_units_to_category( c_name="Area", u_name="in**2"  , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Area", u_name="inch**2", conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Area", u_name="m**2"   , conv_factor=0.00064516, offset=0.0 )
add_units_to_category( c_name="Area", u_name="mile**2", conv_factor=2.49097668605e-10, offset=0.0 )

# Creating Unit Category for "CoeffThermExp(CTE)"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="CoeffThermExp(CTE)", def_units="1/degF" )
add_units_to_category( c_name="CoeffThermExp(CTE)", u_name="1/degC", conv_factor=1.8, offset=0.0 )
add_units_to_category( c_name="CoeffThermExp(CTE)", u_name="1/degF", conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="CoeffThermExp(CTE)", u_name="1/degK", conv_factor=1.8, offset=0.0 )
add_units_to_category( c_name="CoeffThermExp(CTE)", u_name="1/degR", conv_factor=1.0, offset=0.0 )

# Creating Unit Category for "DeltaT"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="DeltaT", def_units="delF" )
add_units_to_category( c_name="DeltaT", u_name="delC", conv_factor=0.5555555555555556, offset=0.0 )
add_units_to_category( c_name="DeltaT", u_name="delF", conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="DeltaT", u_name="delK", conv_factor=0.5555555555555556, offset=0.0 )
add_units_to_category( c_name="DeltaT", u_name="delR", conv_factor=1.0, offset=0.0 )

# Creating Unit Category for "Density"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="Density", def_units="lbm/inch**3" )
add_units_to_category( c_name="Density", u_name="g/ml"            , conv_factor=27.6799047102, offset=0.0 )
add_units_to_category( c_name="Density", u_name="kg/m**3"         , conv_factor=27679.9047102, offset=0.0 )
add_units_to_category( c_name="Density", u_name="lbm/ft**3"       , conv_factor=1728.0, offset=0.0 )
add_units_to_category( c_name="Density", u_name="lbm/galUS"       , conv_factor=231.0, offset=0.0 )
add_units_to_category( c_name="Density", u_name="lbm/in**3"       , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Density", u_name="lbm/inch**3"     , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Density", u_name="ounce/galUS"     , conv_factor=3696.0, offset=0.0 )
add_units_to_category( c_name="Density", u_name="SG"              , conv_factor=27.6799047102, offset=0.0 )
add_units_to_category( c_name="Density", u_name="slug/ft**3"      , conv_factor=53.7078794867, offset=0.0 )
add_units_to_category( c_name="Density", u_name="specific_gravity", conv_factor=27.6799047102, offset=0.0 )

# Creating Unit Category for "ElementDensity"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="ElementDensity", def_units="elem/cm**2" )
add_units_to_category( c_name="ElementDensity", u_name="elem/cm**2", conv_factor=0.15500031000062, offset=0.0 )
add_units_to_category( c_name="ElementDensity", u_name="elem/in**2", conv_factor=1.0, offset=0.0 )

# Creating Unit Category for "Energy"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="Energy", def_units="BTU" )
add_units_to_category( c_name="Energy", u_name="BTU"   , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Energy", u_name="cal"   , conv_factor=252.164400722, offset=0.0 )
add_units_to_category( c_name="Energy", u_name="erg"   , conv_factor=10550558526.2, offset=0.0 )
add_units_to_category( c_name="Energy", u_name="ft*lbf", conv_factor=778.169262266, offset=0.0 )
add_units_to_category( c_name="Energy", u_name="J"     , conv_factor=1055.05585262, offset=0.0 )
add_units_to_category( c_name="Energy", u_name="kcal"  , conv_factor=0.252164400722, offset=0.0 )
add_units_to_category( c_name="Energy", u_name="kJ"    , conv_factor=1.05505585262, offset=0.0 )
add_units_to_category( c_name="Energy", u_name="kW*hr" , conv_factor=0.000293071070172, offset=0.0 )
add_units_to_category( c_name="Energy", u_name="W*hr"  , conv_factor=0.293071070172, offset=0.0 )

# Creating Unit Category for "EnergySpec"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="EnergySpec", def_units="BTU/lbm" )
add_units_to_category( c_name="EnergySpec", u_name="BTU/lbm" , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="EnergySpec", u_name="cal/g"   , conv_factor=0.555927342256, offset=0.0 )
add_units_to_category( c_name="EnergySpec", u_name="J/g"     , conv_factor=2.326, offset=0.0 )
add_units_to_category( c_name="EnergySpec", u_name="J/kg"    , conv_factor=2326.0, offset=0.0 )
add_units_to_category( c_name="EnergySpec", u_name="kcal/g"  , conv_factor=0.000555927342256, offset=0.0 )
add_units_to_category( c_name="EnergySpec", u_name="kcal/kg" , conv_factor=0.555927342256, offset=0.0 )
add_units_to_category( c_name="EnergySpec", u_name="kJ/kg"   , conv_factor=2.326, offset=0.0 )
add_units_to_category( c_name="EnergySpec", u_name="kW*hr/kg", conv_factor=0.000646111111111, offset=0.0 )

# Creating Unit Category for "Force"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="Force", def_units="lbf" )
add_units_to_category( c_name="Force", u_name="dyn", conv_factor=444822.161526, offset=0.0 )
add_units_to_category( c_name="Force", u_name="kN" , conv_factor=0.00444822161526, offset=0.0 )
add_units_to_category( c_name="Force", u_name="lbf", conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Force", u_name="N"  , conv_factor=4.44822161526, offset=0.0 )

# Creating Unit Category for "Frequency"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="Frequency", def_units="Hz" )
add_units_to_category( c_name="Frequency", u_name="GHz", conv_factor=1e-09, offset=0.0 )
add_units_to_category( c_name="Frequency", u_name="Hz" , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Frequency", u_name="kHz", conv_factor=0.001, offset=0.0 )
add_units_to_category( c_name="Frequency", u_name="MHz", conv_factor=1e-06, offset=0.0 )

# Creating Unit Category for "HeatCapacity"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="HeatCapacity", def_units="BTU/lbm/delF" )
add_units_to_category( c_name="HeatCapacity", u_name="BTU/lbm/degF", conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="HeatCapacity", u_name="BTU/lbm/delF", conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="HeatCapacity", u_name="BTU/lbm/F"   , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="HeatCapacity", u_name="cal/g/C"     , conv_factor=1.00066921606, offset=0.0 )
add_units_to_category( c_name="HeatCapacity", u_name="cal/g/degC"  , conv_factor=1.00066921606, offset=0.0 )
add_units_to_category( c_name="HeatCapacity", u_name="cal/g/delC"  , conv_factor=1.00066921606, offset=0.0 )
add_units_to_category( c_name="HeatCapacity", u_name="J/kg/degK"   , conv_factor=4186.8, offset=0.0 )
add_units_to_category( c_name="HeatCapacity", u_name="J/kg/delK"   , conv_factor=4186.8, offset=0.0 )
add_units_to_category( c_name="HeatCapacity", u_name="J/kg/K"      , conv_factor=4186.8, offset=0.0 )
add_units_to_category( c_name="HeatCapacity", u_name="kcal/g/C"    , conv_factor=0.00100066921606, offset=0.0 )
add_units_to_category( c_name="HeatCapacity", u_name="kcal/g/degC" , conv_factor=0.00100066921606, offset=0.0 )
add_units_to_category( c_name="HeatCapacity", u_name="kcal/g/delC" , conv_factor=0.00100066921606, offset=0.0 )
add_units_to_category( c_name="HeatCapacity", u_name="kJ/kg/degK"  , conv_factor=4.1868, offset=0.0 )
add_units_to_category( c_name="HeatCapacity", u_name="kJ/kg/delK"  , conv_factor=4.1868, offset=0.0 )
add_units_to_category( c_name="HeatCapacity", u_name="kJ/kg/K"     , conv_factor=4.1868, offset=0.0 )

# Creating Unit Category for "HeatFlux"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="HeatFlux", def_units="BTU/in**2/s" ) 
add_units_to_category( c_name="HeatFlux", u_name="BTU/in**2/s" , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="HeatFlux", u_name="cal/cm**2/s" , conv_factor=39.08556574283321, offset=0.0 )
add_units_to_category( c_name="HeatFlux", u_name="BTU/ft**2/s" , conv_factor=144.0, offset=0.0 )
add_units_to_category( c_name="HeatFlux", u_name="W/cm**2"     , conv_factor=163.53400706801415, offset=0.0 )
add_units_to_category( c_name="HeatFlux", u_name="kcal/m**2/s" , conv_factor=390.8556574283321, offset=0.0 )
add_units_to_category( c_name="HeatFlux", u_name="W/in**2"     , conv_factor=1055.056, offset=0.0 )
add_units_to_category( c_name="HeatFlux", u_name="cal/cm**2/hr", conv_factor=140708.03667419957, offset=0.0 )
add_units_to_category( c_name="HeatFlux", u_name="BTU/ft**2/hr", conv_factor=518400.0, offset=0.0 )
add_units_to_category( c_name="HeatFlux", u_name="kcal/m**2/hr", conv_factor=1407080.3667419956, offset=0.0 )
add_units_to_category( c_name="HeatFlux", u_name="J/s/m**2"    , conv_factor=1635340.0706801414, offset=0.0 )
add_units_to_category( c_name="HeatFlux", u_name="W/m**2"      , conv_factor=1635340.0706801414, offset=0.0 )

# Creating Unit Category for "HxCoeff"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="HxCoeff", def_units="BTU/inch**2/s/delF" )
add_units_to_category( c_name="HxCoeff", u_name="BTU/ft**2/hr/degF" , conv_factor=518400.0, offset=0.0 )
add_units_to_category( c_name="HxCoeff", u_name="BTU/ft**2/hr/delF" , conv_factor=518400.0, offset=0.0 )
add_units_to_category( c_name="HxCoeff", u_name="BTU/ft**2/hr/F"    , conv_factor=518400.0, offset=0.0 )
add_units_to_category( c_name="HxCoeff", u_name="BTU/inch**2/s/degF", conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="HxCoeff", u_name="BTU/inch**2/s/delF", conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="HxCoeff", u_name="BTU/inch**2/s/F"   , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="HxCoeff", u_name="cal/cm**2/s/C"     , conv_factor=70.3540085094, offset=0.0 )
add_units_to_category( c_name="HxCoeff", u_name="cal/cm**2/s/degC"  , conv_factor=70.3540085094, offset=0.0 )
add_units_to_category( c_name="HxCoeff", u_name="cal/cm**2/s/delC"  , conv_factor=70.3540085094, offset=0.0 )
add_units_to_category( c_name="HxCoeff", u_name="kcal/m**2/hr/C"    , conv_factor=2532744.30634, offset=0.0 )
add_units_to_category( c_name="HxCoeff", u_name="kcal/m**2/hr/degC" , conv_factor=2532744.30634, offset=0.0 )
add_units_to_category( c_name="HxCoeff", u_name="kcal/m**2/hr/delC" , conv_factor=2532744.30634, offset=0.0 )
add_units_to_category( c_name="HxCoeff", u_name="W/m**2/C"          , conv_factor=2943611.71603, offset=0.0 )
add_units_to_category( c_name="HxCoeff", u_name="W/m**2/degC"       , conv_factor=2943611.71603, offset=0.0 )
add_units_to_category( c_name="HxCoeff", u_name="W/m**2/delC"       , conv_factor=2943611.71603, offset=0.0 )

# Creating Unit Category for "Isp"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="Isp", def_units="sec" )
add_units_to_category( c_name="Isp", u_name="km/sec"     , conv_factor=0.00980665, offset=0.0 )
add_units_to_category( c_name="Isp", u_name="lbf-sec/lbm", conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Isp", u_name="m/sec"      , conv_factor=9.80665, offset=0.0 )
add_units_to_category( c_name="Isp", u_name="N-sec/kg"   , conv_factor=9.80665, offset=0.0 )
add_units_to_category( c_name="Isp", u_name="sec"        , conv_factor=1.0, offset=0.0 )

# Creating Unit Category for "Length"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="Length", def_units="inch" )
add_units_to_category( c_name="Length", u_name="angstrom"         , conv_factor=254000000.0, offset=0.0 )
add_units_to_category( c_name="Length", u_name="astronomical_unit", conv_factor=1.69788512916e-13, offset=0.0 )
add_units_to_category( c_name="Length", u_name="cm"               , conv_factor=2.54, offset=0.0 )
add_units_to_category( c_name="Length", u_name="ft"               , conv_factor=0.0833333333333, offset=0.0 )
add_units_to_category( c_name="Length", u_name="in"               , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Length", u_name="inch"             , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Length", u_name="km"               , conv_factor=2.54e-05, offset=0.0 )
add_units_to_category( c_name="Length", u_name="light_year"       , conv_factor=2.6847819948e-18, offset=0.0 )
add_units_to_category( c_name="Length", u_name="m"                , conv_factor=0.0254, offset=0.0 )
add_units_to_category( c_name="Length", u_name="micron"           , conv_factor=25400.0, offset=0.0 )
add_units_to_category( c_name="Length", u_name="mil"              , conv_factor=1000.0, offset=0.0 )
add_units_to_category( c_name="Length", u_name="mile"             , conv_factor=1.57828282828e-05, offset=0.0 )
add_units_to_category( c_name="Length", u_name="mm"               , conv_factor=25.4, offset=0.0 )
add_units_to_category( c_name="Length", u_name="nautical_mile"    , conv_factor=1.37149377616e-05, offset=0.0 )
add_units_to_category( c_name="Length", u_name="yd"               , conv_factor=0.0277777777778, offset=0.0 )

# Creating Unit Category for "Mass"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="Mass", def_units="lbm" )
add_units_to_category( c_name="Mass", u_name="g"         , conv_factor=453.59237, offset=0.0 )
add_units_to_category( c_name="Mass", u_name="gal_H2O"   , conv_factor=0.120048019208, offset=0.0 )
add_units_to_category( c_name="Mass", u_name="kg"        , conv_factor=0.45359237, offset=0.0 )
add_units_to_category( c_name="Mass", u_name="lbm"       , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Mass", u_name="long_ton"  , conv_factor=0.000446428571429, offset=0.0 )
add_units_to_category( c_name="Mass", u_name="metric_ton", conv_factor=0.00045359237, offset=0.0 )
add_units_to_category( c_name="Mass", u_name="short_ton" , conv_factor=0.0005, offset=0.0 )
add_units_to_category( c_name="Mass", u_name="slug"      , conv_factor=0.031080948777, offset=0.0 )

# Creating Unit Category for "MassFlow"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="MassFlow", def_units="lbm/s" )
add_units_to_category( c_name="MassFlow", u_name="g/hr"   , conv_factor=1632932.532, offset=0.0 )
add_units_to_category( c_name="MassFlow", u_name="g/min"  , conv_factor=27215.5422, offset=0.0 )
add_units_to_category( c_name="MassFlow", u_name="g/s"    , conv_factor=453.59237, offset=0.0 )
add_units_to_category( c_name="MassFlow", u_name="kg/hr"  , conv_factor=1632.932532, offset=0.0 )
add_units_to_category( c_name="MassFlow", u_name="kg/min" , conv_factor=27.2155422, offset=0.0 )
add_units_to_category( c_name="MassFlow", u_name="kg/s"   , conv_factor=0.45359237, offset=0.0 )
add_units_to_category( c_name="MassFlow", u_name="lbm/hr" , conv_factor=3600.0, offset=0.0 )
add_units_to_category( c_name="MassFlow", u_name="lbm/min", conv_factor=60.0, offset=0.0 )
add_units_to_category( c_name="MassFlow", u_name="lbm/s"  , conv_factor=1.0, offset=0.0 )

# Creating Unit Category for "MolecularWt"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="MolecularWt", def_units="g/gmole" )
add_units_to_category( c_name="MolecularWt", u_name="g/gmole"   , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="MolecularWt", u_name="lbm/lbmole", conv_factor=1.0, offset=0.0 )

# Creating Unit Category for "Power"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="Power", def_units="hp" ) 
add_units_to_category( c_name="Power", u_name="MW"       , conv_factor=0.0007456998715822702, offset=0.0 )
add_units_to_category( c_name="Power", u_name="kcal/s"   , conv_factor=0.17822654674528446, offset=0.0 )
add_units_to_category( c_name="Power", u_name="BTU/s"    , conv_factor=0.7067870061705446, offset=0.0 )
add_units_to_category( c_name="Power", u_name="kJ/s"     , conv_factor=0.7456998715822701, offset=0.0 )
add_units_to_category( c_name="Power", u_name="kW"       , conv_factor=0.7456998715822701, offset=0.0 )
add_units_to_category( c_name="Power", u_name="hp"       , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Power", u_name="cal/s"    , conv_factor=178.22654674528442, offset=0.0 )
add_units_to_category( c_name="Power", u_name="ft*lbf/s" , conv_factor=549.9999999999999, offset=0.0 )
add_units_to_category( c_name="Power", u_name="kcal/hr"  , conv_factor=641.615568283024, offset=0.0 )
add_units_to_category( c_name="Power", u_name="J/s"      , conv_factor=745.6998715822701, offset=0.0 )
add_units_to_category( c_name="Power", u_name="W"        , conv_factor=745.6998715822701, offset=0.0 )
add_units_to_category( c_name="Power", u_name="BTU/hr"   , conv_factor=2544.43322221396, offset=0.0 )
add_units_to_category( c_name="Power", u_name="kJ/hr"    , conv_factor=2684.519537696173, offset=0.0 )
add_units_to_category( c_name="Power", u_name="cal/hr"   , conv_factor=641615.5682830239, offset=0.0 )
add_units_to_category( c_name="Power", u_name="ft*lbf/hr", conv_factor=1979999.9999999995, offset=0.0 )
add_units_to_category( c_name="Power", u_name="J/hr"     , conv_factor=2684519.5376961725, offset=0.0 )

# Creating Unit Category for "Pressure"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="Pressure", def_units="psia" )
add_units_to_category( c_name="Pressure", u_name="atm"        , conv_factor=0.0680459639099, offset=0.0 )
add_units_to_category( c_name="Pressure", u_name="bar"        , conv_factor=0.0689475729317, offset=0.0 )
add_units_to_category( c_name="Pressure", u_name="inHg"       , conv_factor=2.036021, offset=0.0 )
add_units_to_category( c_name="Pressure", u_name="kPa"        , conv_factor=6.89475729317, offset=0.0 )
add_units_to_category( c_name="Pressure", u_name="hPa"        , conv_factor=68.9475729317, offset=0.0 )
add_units_to_category( c_name="Pressure", u_name="lbf/ft**2"  , conv_factor=144.0, offset=0.0 )
add_units_to_category( c_name="Pressure", u_name="lbf/inch**2", conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Pressure", u_name="mmHg"       , conv_factor=51.71493, offset=0.0 )
add_units_to_category( c_name="Pressure", u_name="MPa"        , conv_factor=0.00689475729317, offset=0.0 )
add_units_to_category( c_name="Pressure", u_name="N/cm**2"    , conv_factor=0.689475729317, offset=0.0 )
add_units_to_category( c_name="Pressure", u_name="N/m**2"     , conv_factor=6894.75729317, offset=0.0 )
add_units_to_category( c_name="Pressure", u_name="Pa"         , conv_factor=6894.75729317, offset=0.0 )
add_units_to_category( c_name="Pressure", u_name="psf"        , conv_factor=144.0, offset=0.0 )
add_units_to_category( c_name="Pressure", u_name="psia"       , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Pressure", u_name="psid"       , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Pressure", u_name="torr"       , conv_factor=51.7149325715, offset=0.0 )

# Creating Unit Category for "SurfaceTension"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="SurfaceTension", def_units="lbf/in" )
add_units_to_category( c_name="SurfaceTension", u_name="dyne/cm", conv_factor=175126.83698643, offset=0.0 )
add_units_to_category( c_name="SurfaceTension", u_name="lbf/ft" , conv_factor=12.0, offset=0.0 )
add_units_to_category( c_name="SurfaceTension", u_name="lbf/in" , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="SurfaceTension", u_name="mN/m"   , conv_factor=175126.836986, offset=0.0 )
add_units_to_category( c_name="SurfaceTension", u_name="N/m"    , conv_factor=175.126836986, offset=0.0 )


# Creating Unit Category for "Tank_PV/W"
# Read As: 1 default unit = conv_factor u_name units
create_category( c_name="Tank_PV/W", def_units="psia-in**3/lbm" )
add_units_to_category( c_name="Tank_PV/W", u_name="psia-in**3/lbm", conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Tank_PV/W", u_name="psia-ft**3/lbm", conv_factor=1.0/1728.0, offset=0.0 )
add_units_to_category( c_name="Tank_PV/W", u_name="MPa-liter/kg"  , conv_factor=0.00024908891, offset=0.0 )
add_units_to_category( c_name="Tank_PV/W", u_name="bar-liter/kg"  , conv_factor=0.0024908891, offset=0.0 )


# Creating Unit Category for "Temperature"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="Temperature", def_units="degR" )
add_units_to_category( c_name="Temperature", u_name="degC", conv_factor=0.5555555555555556, offset=-273.15 )
add_units_to_category( c_name="Temperature", u_name="degF", conv_factor=1.0, offset=-459.67 )
add_units_to_category( c_name="Temperature", u_name="degK", conv_factor=0.5555555555555556, offset=0.0 )
add_units_to_category( c_name="Temperature", u_name="degR", conv_factor=1.0, offset=0.0 )

# Creating Unit Category for "ThermalCond"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="ThermalCond", def_units="BTU/hr/ft/delF" )
add_units_to_category( c_name="ThermalCond", u_name="BTU/hr/ft/degF" , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="ThermalCond", u_name="BTU/hr/ft/delF" , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="ThermalCond", u_name="BTU/hr/ft/F"    , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="ThermalCond", u_name="BTU/s/ft/degF"  , conv_factor=0.0002777777777777778, offset=0.0 )
add_units_to_category( c_name="ThermalCond", u_name="BTU/s/ft/delF"  , conv_factor=0.0002777777777777778, offset=0.0 )
add_units_to_category( c_name="ThermalCond", u_name="BTU/s/ft/F"     , conv_factor=0.0002777777777777778, offset=0.0 )
add_units_to_category( c_name="ThermalCond", u_name="BTU/s/inch/degF", conv_factor=2.31481481481e-05, offset=0.0 )
add_units_to_category( c_name="ThermalCond", u_name="BTU/s/inch/delF", conv_factor=2.31481481481e-05, offset=0.0 )
add_units_to_category( c_name="ThermalCond", u_name="BTU/s/inch/F"   , conv_factor=2.31481481481e-05, offset=0.0 )
add_units_to_category( c_name="ThermalCond", u_name="cal/s/cm/C"     , conv_factor=0.00413655512995, offset=0.0 )
add_units_to_category( c_name="ThermalCond", u_name="cal/s/cm/degC"  , conv_factor=0.00413655512995, offset=0.0 )
add_units_to_category( c_name="ThermalCond", u_name="cal/s/cm/delC"  , conv_factor=0.00413655512995, offset=0.0 )
add_units_to_category( c_name="ThermalCond", u_name="cal/s/m/C"      , conv_factor=0.413655512995, offset=0.0 )
add_units_to_category( c_name="ThermalCond", u_name="cal/s/m/degC"   , conv_factor=0.413655512995, offset=0.0 )
add_units_to_category( c_name="ThermalCond", u_name="cal/s/m/delC"   , conv_factor=0.413655512995, offset=0.0 )
add_units_to_category( c_name="ThermalCond", u_name="W/cm/C"         , conv_factor=0.0173073466637, offset=0.0 )
add_units_to_category( c_name="ThermalCond", u_name="W/cm/degC"      , conv_factor=0.0173073466637, offset=0.0 )
add_units_to_category( c_name="ThermalCond", u_name="W/cm/delC"      , conv_factor=0.0173073466637, offset=0.0 )
add_units_to_category( c_name="ThermalCond", u_name="W/m/K"          , conv_factor=1.73073466637, offset=0.0 )

# Creating Unit Category for "Time"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="Time", def_units="s" )
add_units_to_category( c_name="Time", u_name="day"     , conv_factor=1.15740740741e-05, offset=0.0 )
add_units_to_category( c_name="Time", u_name="hr"      , conv_factor=0.000277777777778, offset=0.0 )
add_units_to_category( c_name="Time", u_name="microsec", conv_factor=1000000.0, offset=0.0 )
add_units_to_category( c_name="Time", u_name="millisec", conv_factor=1000.0, offset=0.0 )
add_units_to_category( c_name="Time", u_name="min"     , conv_factor=0.0166666666667, offset=0.0 )
add_units_to_category( c_name="Time", u_name="ms"      , conv_factor=1000.0, offset=0.0 )
add_units_to_category( c_name="Time", u_name="nanosec" , conv_factor=1000000000.0, offset=0.0 )
add_units_to_category( c_name="Time", u_name="s"       , conv_factor=1.0, offset=0.0 )
#                                             this is an average year, not a 365 day year.
add_units_to_category( c_name="Time", u_name="year"    , conv_factor=3.16887646408e-08, offset=0.0 )

# Creating Unit Category for "Velocity"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="Velocity", def_units="ft/s" )
add_units_to_category( c_name="Velocity", u_name="cm/s"   , conv_factor=30.48, offset=0.0 )
add_units_to_category( c_name="Velocity", u_name="ft/s"   , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Velocity", u_name="inch/s" , conv_factor=12.0, offset=0.0 )
add_units_to_category( c_name="Velocity", u_name="km/hr"  , conv_factor=1.09728, offset=0.0 )
add_units_to_category( c_name="Velocity", u_name="m/s"    , conv_factor=0.3048, offset=0.0 )
add_units_to_category( c_name="Velocity", u_name="mile/hr", conv_factor=0.681818181818, offset=0.0 )

# Creating Unit Category for "Viscosity_Dynamic"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="Viscosity_Dynamic", def_units="poise" )
add_units_to_category( c_name="Viscosity_Dynamic", u_name="cp"         , conv_factor=100.0, offset=0.0 )
add_units_to_category( c_name="Viscosity_Dynamic", u_name="cpoise"     , conv_factor=100.0, offset=0.0 )
add_units_to_category( c_name="Viscosity_Dynamic", u_name="kg/hr/cm"   , conv_factor=3.6, offset=0.0 )
add_units_to_category( c_name="Viscosity_Dynamic", u_name="kg/hr/m"    , conv_factor=360.0, offset=0.0 )
add_units_to_category( c_name="Viscosity_Dynamic", u_name="kg/s/cm"    , conv_factor=0.001, offset=0.0 )
add_units_to_category( c_name="Viscosity_Dynamic", u_name="kg/s/m"     , conv_factor=0.1, offset=0.0 )
add_units_to_category( c_name="Viscosity_Dynamic", u_name="lbm/hr/ft"  , conv_factor=241.90883105, offset=0.0 )
add_units_to_category( c_name="Viscosity_Dynamic", u_name="lbm/hr/inch", conv_factor=20.1590692542, offset=0.0 )
add_units_to_category( c_name="Viscosity_Dynamic", u_name="lbm/s/ft"   , conv_factor=0.067196897514, offset=0.0 )
add_units_to_category( c_name="Viscosity_Dynamic", u_name="lbm/s/inch" , conv_factor=0.0055997414595, offset=0.0 )
add_units_to_category( c_name="Viscosity_Dynamic", u_name="Pa*s"       , conv_factor=0.1, offset=0.0 )
add_units_to_category( c_name="Viscosity_Dynamic", u_name="poise"      , conv_factor=1.0, offset=0.0 )

# Creating Unit Category for "Viscosity_Kinematic"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="Viscosity_Kinematic", def_units="ft**2/s" )
add_units_to_category( c_name="Viscosity_Kinematic", u_name="centistokes", conv_factor=92903.04, offset=0.0 )
add_units_to_category( c_name="Viscosity_Kinematic", u_name="ft**2/hr"   , conv_factor=3600.0, offset=0.0 )
add_units_to_category( c_name="Viscosity_Kinematic", u_name="ft**2/s"    , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Viscosity_Kinematic", u_name="m**2/s"     , conv_factor=0.09290304, offset=0.0 )
add_units_to_category( c_name="Viscosity_Kinematic", u_name="stokes"     , conv_factor=929.0304, offset=0.0 )

# Creating Unit Category for "Volume"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="Volume", def_units="inch**3" )
add_units_to_category( c_name="Volume", u_name="barOil" , conv_factor=0.000103071531643, offset=0.0 )
add_units_to_category( c_name="Volume", u_name="cm**3"  , conv_factor=16.387064, offset=0.0 )
add_units_to_category( c_name="Volume", u_name="cup"    , conv_factor=0.0692640692641, offset=0.0 )
add_units_to_category( c_name="Volume", u_name="ft**3"  , conv_factor=0.000578703703704, offset=0.0 )
add_units_to_category( c_name="Volume", u_name="galUK"  , conv_factor=0.00360465014991, offset=0.0 )
add_units_to_category( c_name="Volume", u_name="galUS"  , conv_factor=0.004329004329, offset=0.0 )
add_units_to_category( c_name="Volume", u_name="in**3"  , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Volume", u_name="inch**3", conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="Volume", u_name="liter"  , conv_factor=0.016387064, offset=0.0 )
add_units_to_category( c_name="Volume", u_name="m**3"   , conv_factor=1.6387064e-05, offset=0.0 )
add_units_to_category( c_name="Volume", u_name="pint"   , conv_factor=0.034632034632, offset=0.0 )
add_units_to_category( c_name="Volume", u_name="quart"  , conv_factor=0.017316017316, offset=0.0 )
add_units_to_category( c_name="Volume", u_name="yd**3"  , conv_factor=2.14334705075e-05, offset=0.0 )

# Creating Unit Category for "VolumeFlow"
# Read As: 1 default unit = conv_factor u_name units
create_category(       c_name="VolumeFlow", def_units="inch**3/s" )
add_units_to_category( c_name="VolumeFlow", u_name="ft**3/hr"   , conv_factor=2.08333333333, offset=0.0 )
add_units_to_category( c_name="VolumeFlow", u_name="ft**3/min"  , conv_factor=0.0347222222222, offset=0.0 )
add_units_to_category( c_name="VolumeFlow", u_name="ft**3/s"    , conv_factor=0.000578703703704, offset=0.0 )
add_units_to_category( c_name="VolumeFlow", u_name="galUS/day"  , conv_factor=374.025974026, offset=0.0 )
add_units_to_category( c_name="VolumeFlow", u_name="galUS/hr"   , conv_factor=15.5844155844, offset=0.0 )
add_units_to_category( c_name="VolumeFlow", u_name="galUS/min"  , conv_factor=0.25974025974, offset=0.0 )
add_units_to_category( c_name="VolumeFlow", u_name="galUS/s"    , conv_factor=0.004329004329, offset=0.0 )
add_units_to_category( c_name="VolumeFlow", u_name="gpm"        , conv_factor=0.25974025974, offset=0.0 )
add_units_to_category( c_name="VolumeFlow", u_name="inch**3/hr" , conv_factor=3600.0, offset=0.0 )
add_units_to_category( c_name="VolumeFlow", u_name="inch**3/min", conv_factor=60.0, offset=0.0 )
add_units_to_category( c_name="VolumeFlow", u_name="inch**3/s"  , conv_factor=1.0, offset=0.0 )
add_units_to_category( c_name="VolumeFlow", u_name="l/s"        , conv_factor=0.016387064, offset=0.0 )
add_units_to_category( c_name="VolumeFlow", u_name="m**3/hr"    , conv_factor=0.0589934304, offset=0.0 )
add_units_to_category( c_name="VolumeFlow", u_name="m**3/s"     , conv_factor=1.6387064e-05, offset=0.0 )
add_units_to_category( c_name="VolumeFlow", u_name="ml/hr"      , conv_factor=58993.4304, offset=0.0 )
add_units_to_category( c_name="VolumeFlow", u_name="ml/min"     , conv_factor=983.22384, offset=0.0 )
add_units_to_category( c_name="VolumeFlow", u_name="ml/s"       , conv_factor=16.387064, offset=0.0 )
        

# ============== some common conversions ===================
def get_degK( val, inp_units ):
    """ val uses input units... e.g. 25, 'degC' """
    return convert_value( inp_val=float( val ), inp_units=inp_units, out_units='degK')
    
def get_degR( val, inp_units ):
    """ val uses input units... e.g. 25, 'degC' """
    return convert_value(  inp_val=float( val ), inp_units=inp_units, out_units='degR')

categoryL = list( categoryD.keys() )
categoryL.sort(key=str.lower)

MAX_UNIT_CHARS = 0
for unit in conv_factD.keys():
    MAX_UNIT_CHARS = max( MAX_UNIT_CHARS, len(unit) )
UNIT_FMT_STR = '%%%is'%MAX_UNIT_CHARS

# === to simplify output in GUI, use display_unitsD to pick units to display
# === Note that redundant units are hand-deleted

display_def_unitsD = {} # index=category, value=default units
display_def_unitsD["Acceleration"] = "ft/s**2"
display_def_unitsD["Angle"] = "deg"
display_def_unitsD["AngVelocity"] = "rpm"
display_def_unitsD["Area"] = "inch**2"
display_def_unitsD["CoeffThermExp(CTE)"] = "1/degF"
display_def_unitsD["DeltaT"] = "delF"
display_def_unitsD["Density"] = "lbm/in**3"
display_def_unitsD["ElementDensity"] = "elem/cm**2"
display_def_unitsD["Energy"] = "BTU"
display_def_unitsD["EnergySpec"] = "BTU/lbm"
display_def_unitsD["Force"] = "lbf"
display_def_unitsD["Frequency"] = "Hz"
display_def_unitsD["HeatCapacity"] = "BTU/lbm/F"
display_def_unitsD["HeatFlux"] = "BTU/in**2/s"
display_def_unitsD["HxCoeff"] = "BTU/inch**2/s/F"
display_def_unitsD["Isp"] = "sec"
display_def_unitsD["Length"] = "inch"
display_def_unitsD["Mass"] = "lbm"
display_def_unitsD["MassFlow"] = "lbm/s"
display_def_unitsD["MolecularWt"] = "g/gmole"
display_def_unitsD["Power"] = "hp"
display_def_unitsD["Pressure"] = "psia"
display_def_unitsD["SurfaceTension"] = "lbf/in"
display_def_unitsD["Tank_PV/W"] = "psia-in**3/lbm"
display_def_unitsD["Temperature"] = "degF"
display_def_unitsD["ThermalCond"] = "BTU/hr/ft/F"
display_def_unitsD["Time"] = "s"
display_def_unitsD["Velocity"] = "ft/s"
display_def_unitsD["Viscosity_Dynamic"] = "poise"
display_def_unitsD["Viscosity_Kinematic"] = "ft**2/s"
display_def_unitsD["Volume"] = "inch**3"
display_def_unitsD["VolumeFlow"] = "inch**3/s"


display_unitsD = {} # index=category, value = unit list in show order (small to large)
display_unitsD['Acceleration'] =  ['gee', 'm/s**2', 'mile/hr/s', 'ft/s**2', 'cm/s**2']
display_unitsD['Angle'] =  ['circle', 'revolution', 'rad', 'deg', 'grad', 'arcmin', 'arcsec']
display_unitsD['AngVelocity'] =  ['rad/s', 'rpm', 'deg/s', 'rad/min', 'deg/min']
display_unitsD['Area'] =  ['mile**2', 'acre', 'm**2', 'ft**2', 'in**2', 'inch**2', 'cm**2']
display_unitsD['CoeffThermExp(CTE)'] = ['1/degF', '1/degR', '1/degC', '1/degK']
display_unitsD['DeltaT'] =  ['delC', 'delK', 'delF', 'delR']
display_unitsD['Density'] =  ['lbm/in**3', 'g/ml', 'SG', 'specific_gravity', 'slug/ft**3', 'lbm/galUS', 'lbm/ft**3', 'ounce/galUS', 'kg/m**3']
display_unitsD['ElementDensity'] =  ['elem/cm**2', 'elem/in**2']
display_unitsD['Energy'] =  ['kW*hr', 'kcal', 'W*hr', 'BTU', 'kJ', 'cal', 'ft*lbf', 'J', 'erg']
display_unitsD['EnergySpec'] =  ['kcal/g', 'kW*hr/kg', 'cal/g', 'kcal/kg', 'BTU/lbm', 'J/g', 'kJ/kg', 'J/kg']
display_unitsD['Force'] =  ['kN', 'lbf', 'N', 'dyn']
display_unitsD['Frequency'] =  ['GHz', 'MHz', 'kHz', 'Hz']
display_unitsD['HeatCapacity'] =  ['kcal/g/C', 'BTU/lbm/F', 'cal/g/C',  'kJ/kg/K', 'J/kg/K']
display_unitsD["HeatFlux"] = ['BTU/in**2/s', 'cal/cm**2/s', 'BTU/ft**2/s', 'W/cm**2', 'kcal/m**2/s', 'W/in**2', 'cal/cm**2/hr', 'BTU/ft**2/hr', 'kcal/m**2/hr', 'J/s/m**2', 'W/m**2']
display_unitsD['HxCoeff'] =  [ 'BTU/inch**2/s/F', 'cal/cm**2/s/C', 'BTU/ft**2/hr/F', 'kcal/m**2/hr/C',  'W/m**2/C']
display_unitsD['Isp'] =  ['km/sec', 'lbf-sec/lbm', 'sec', 'm/sec', 'N-sec/kg']
display_unitsD['Length'] =  ['light_year', 'astronomical_unit', 'nautical_mile', 'mile', 'km', 'm', 'yd', 'ft', 'inch', 'cm', 'mm', 'mil', 'micron', 'angstrom']
display_unitsD['Mass'] =  ['long_ton', 'metric_ton', 'short_ton', 'slug', 'gal_H2O', 'kg', 'lbm', 'g']
display_unitsD['MassFlow'] =  ['kg/s', 'lbm/s', 'kg/min', 'lbm/min', 'g/s', 'kg/hr', 'lbm/hr', 'g/min', 'g/hr']
display_unitsD['MolecularWt'] =  ['g/gmole', 'lbm/lbmole']
display_unitsD["Power"] = ['MW', 'kcal/s', 'BTU/s', 'kJ/s', 'kW', 'hp', 'cal/s', 'ft*lbf/s', 'kcal/hr', 'J/s', 'W', 'BTU/hr', 'kJ/hr', 'cal/hr', 'ft*lbf/hr', 'J/hr']
display_unitsD['Pressure'] =  ['MPa', 'atm', 'bar', 'N/cm**2', 'lbf/inch**2', 'psia', 'psid', 'inHg', 'kPa', 'mmHg', 'torr', 'hPa', 'lbf/ft**2', 'psf', 'N/m**2', 'Pa']
display_unitsD['SurfaceTension'] =  ['lbf/in', 'lbf/ft', 'N/m', 'mN/m', 'dyne/cm']
display_unitsD["Tank_PV/W"] = ["MPa-liter/kg", "psia-ft**3/lbm" ,"bar-liter/kg", "psia-in**3/lbm"]
display_unitsD['Temperature'] =  ['degC', 'degK', 'degF', 'degR']
display_unitsD['ThermalCond'] =  [ 'BTU/s/inch/F', 'BTU/s/ft/F', 'cal/s/cm/C', 'W/cm/C', 'cal/s/m/C',  'BTU/hr/ft/F', 'W/m/K']
display_unitsD['Time'] =  ['year', 'day', 'hr', 'min', 's', 'millisec', 'ms', 'microsec', 'nanosec']
display_unitsD['Velocity'] =  ['m/s', 'mile/hr', 'ft/s', 'km/hr', 'inch/s', 'cm/s']
display_unitsD['Viscosity_Dynamic'] =  ['kg/s/cm', 'lbm/s/inch', 'lbm/s/ft', 'kg/s/m', 'Pa*s', 'poise', 'kg/hr/cm', 'lbm/hr/inch', 'cp', 'cpoise', 'lbm/hr/ft', 'kg/hr/m']
display_unitsD['Viscosity_Kinematic'] =  ['m**2/s', 'ft**2/s', 'stokes', 'ft**2/hr', 'centistokes']
display_unitsD['Volume'] =  ['m**3', 'yd**3', 'barOil', 'ft**3', 'galUK', 'galUS', 'liter', 'quart', 'pint', 'cup', 'in**3', 'inch**3', 'cm**3']
display_unitsD['VolumeFlow'] =  ['m**3/s', 'ft**3/s', 'galUS/s', 'l/s', 'ft**3/min', 'm**3/hr', 'galUS/min', 'gpm', 'inch**3/s', 'ft**3/hr', 'galUS/hr', 'ml/s', 'inch**3/min', 'galUS/day', 'ml/min', 'inch**3/hr', 'ml/hr']

# English units are held in display_def_unitsD
SI_unitsD = {} # index=category, value = SI units for UnitsIO
SI_unitsD['Acceleration'] =  'm/s**2'
SI_unitsD['Angle'] =  'deg'
SI_unitsD['AngVelocity'] =  'deg/s'
SI_unitsD['Area'] =   'm**2'
SI_unitsD['CoeffThermExp(CTE)'] = '1/degC'
SI_unitsD['DeltaT'] =  'delK'
SI_unitsD['Density'] =  'kg/m**3'
SI_unitsD['ElementDensity'] =  'elem/cm**2'
SI_unitsD['Energy'] =  'J'
SI_unitsD['EnergySpec'] =  'J/kg'
SI_unitsD['Force'] =  'N'
SI_unitsD['Frequency'] =  'Hz'
SI_unitsD['HeatCapacity'] =  'J/kg/K'
SI_unitsD["HeatFlux"] = "kcal/m**2/s"
SI_unitsD['HxCoeff'] =  'cal/cm**2/s/C'
SI_unitsD['Isp'] =  'm/sec'
SI_unitsD['Length'] =  'm'
SI_unitsD['Mass'] =  'kg'
SI_unitsD['MassFlow'] =  'kg/s'
SI_unitsD['MolecularWt'] =  'g/gmole'
SI_unitsD['Power'] =  'cal/s'
SI_unitsD['Pressure'] =  'Pa'
SI_unitsD['SurfaceTension'] =  'N/m'
SI_unitsD['Tank_PV/W'] = "bar-liter/kg"
SI_unitsD['Temperature'] =  'degK'
SI_unitsD['ThermalCond'] =  'W/m/K'
SI_unitsD['Time'] =  's'
SI_unitsD['Velocity'] =  'm/s'
SI_unitsD['Viscosity_Dynamic'] =  'kg/s/m'
SI_unitsD['Viscosity_Kinematic'] =  'm**2/s'
SI_unitsD['Volume'] =  'm**3'
SI_unitsD['VolumeFlow'] =  'm**3/s'

def main():
    print("version:", get_version())
    print( categoryL )
    print()
    
    for outunits in ['lbf-sec/lbm', 'm/sec', 'km/sec', 'N-sec/kg']:
        print( '452.3 sec Isp =',  get_value_str(452.3, 'sec', outunits, fmt='%g') )
    
    
    
    for i,cat in enumerate(categoryL):
        print( '%s(%i %s)'%(cat, len(categoryD[cat]), cat_defaultD[cat]), end=' ' )
        if i>0 and i%5==0:
            print()
    print()
    


    print( 'MAX_UNIT_CHARS =',MAX_UNIT_CHARS )
    
    for units in ['degC','degF','degK','degR']:
        print( '20C =', '%g'%convert_value( 20.0, 'degC', units), units )
        
    for units in ['degC','degF','degK','degR']:
        print( '20 %s ='%units, '%g'%get_degK( 20.0, units ), 
               'degK  = ', '%g'%get_degR( 20.0, units ), 'degR' )
    
    
    print( 'Check SurfaceTension:', convert_value(1.0, 'lbf/in', 'N/m'), convert_value(1.0, 'lbf/in', 'dyne/cm') )
    
    print( 'Check Frequency:', convert_value(5555.0, 'Hz', 'kHz'), convert_value(6.666, 'kHz', 'MHz') )
    

    print( "String input Check: 1 atm =", convert_string( sinp="1 atm", rtn_units="psia" ), 'psia' )
    print( "String input Check: 1 atm =", convert_string( sinp=14.7, rtn_units="psia" ), 'psia' )
    print( "String input Check: 1 atm =", convert_string( sinp=" 1   atm ", rtn_units="psia" ), 'psia' )

    print("Check degF in Temperature =", units_in_category( u_name="degF", c_name="Temperature"))


    def show_convert( sinp, out_units):
        val = convert_string(sinp, out_units)
        print( sinp, " -->", val, out_units )
    show_convert("500000 psia-in**3/lbm", "MPa-liter/kg")
    show_convert("500000 psia-in**3/lbm", "psia-ft**3/lbm")
    show_convert("500000 psia-in**3/lbm", "bar-liter/kg")
    show_convert("240 bar-liter/kg", "MPa-liter/kg")

if __name__ == "__main__":
    main()
