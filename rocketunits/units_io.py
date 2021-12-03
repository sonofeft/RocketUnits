#!/usr/bin/env python
# -*- coding: ascii -*-

r"""
For code using fixed internal physical units, units_io facilitates the use of 
different units for program input and output.

units_io requires all unit input parameters to be strings of the form "value units".
For example "14.7 psia" or "98.6 degF".
units_io assumes that the parameter default strings hold the internal units of the parameters.
Output parameters can be specified either by name, or generically as "SI", "English" or "Both".

"""

#
# import statements here. (built-in first, then 3rd party, then yours)
import inspect
from rocketunits.rocket_units import convert_string, convert_value
from rocketunits.rocket_units import chk_units_in_category, SI_unitsD
from rocketunits.rocket_units import get_category, display_def_unitsD


class Units(object):
    """
    For code using fixed internal physical units, units_io facilitates 
    the use of different units for program input and output.
    """

    def __init__(self, meth, init_varsD):
        """Analyse the method or class given and save info describing the I/O"""

        sig = inspect.signature( meth )
        #print( "inspect.signature( meth ) =", sig, type(sig) )
        #print("Initial init_varsD =", init_varsD)

        self.default_unitsD = {} # key=parameter name, value=default units
        self.user_input_valueD = {} # key=parameter name, value=input value (may be "val units" string)
        self.user_input_unitsD = {} # key=parameter name, value=user input units.

        # Assume Both English and SI unless "English" or "SI" is input
        self.set_output_units( init_varsD.get("output_units","Both") )


        # current_varsD will hold values of parameters after calling set_vars_dict
        self.current_varsD = None # will be set to locals()/vars() of calling function/class

        # iterate over input values
        for name,inp_val in init_varsD.items():
            if name != "self":
                self.user_input_valueD[name] = inp_val

        # iterate over parameters to get default units
        for name,p in sig.parameters.items():
            if type(p.default) == type("string"):
                try:
                    sL = p.default.split()
                    _, units = sL # value can be number or None
                    if len(sL) == 2 and get_category(units) != '':
                        self.default_unitsD[name] = units
                except:
                    pass
            else:
                self.default_unitsD[name] = '' # empty string for no units

        # now that default units have been established, see if user input something different
        for name, def_units in self.default_unitsD.items():
            # only allow user to input units string for params with default units

            self.user_input_unitsD[name] = '' # for now, assume no user input units
            if def_units: 
                # see if user input units in a string like: "2.3 ft"
                input_str = self.user_input_valueD[name]
                if type(input_str) == type("string"):
                    sL = input_str.split()
                else:
                    sL = [input_str]

                if len(sL) == 2:
                    try:
                        _val, user_units = sL
                        
                        d_category = get_category( def_units )
                        chk_units_in_category( user_units, d_category )
                        self.user_input_unitsD[name] = user_units
                    except:
                        raise Exception('Input of "%s" for parameter "%s" has wrong format. '%(input_str, name) +\
                                        'should be "value units" like: "2.3 ft"' )


        #  set the string format used by u_print.
        self.set_print_template()

    #                                      name = val units - desc
    def set_print_template(self, template="%12s = %-45s | %s"):
        """Set the output string formatting template used by u_print"""
        self.template = template

    def set_output_units(self, output_units="Both"):
        if output_units.lower() in ["english", "si", "both"]:
            self.output_units = output_units
        else:
            raise Exception('WARNING: output_units"%s" NOT recognized. MUST be "English", "SI" or "Both"'%output_units)

    def get_input_value(self, name, def_units=""):
        """For inputs defined by default strings, return value in internal units"""
        if name not in self.default_unitsD: # default units may equal blank ""
            # default_unitsD will include positional arguments and keyword arguments
            raise Exception('ERROR: get_input_value called for unknown variable="%s"'%name)

        if def_units: # user is trying to set default units
            if self.default_unitsD.get(name, ''):
                # disallow names that already have a default units value
                raise Exception('ERROR: get_input_value may NOT redefine ' + \
                    '"%s" default units from "%s" to "%s"'%(name, self.default_unitsD[name],def_units) )
            else:
                # allow defining default units for variable w/o existing default units.
                self.default_unitsD[name] = def_units



        input_str = self.user_input_valueD[name]
        internal_units=self.default_unitsD[name]
        val = convert_string( sinp=input_str, rtn_units=internal_units )
        return val

    def force_inch(self, unit):
        '''Regulates the different forms of inch units that are output.'''
        if unit == 'in':
            return 'inch'
        elif unit == 'inch**2':
            return 'in**2'
        elif unit == 'inch**3':
            return 'in**3'
        else:
            return unit

    def __get_output_str(self, inp_val=0.0, inp_units="", 
                       out_units="", default_units="", user_inp_units="",
                       fmt="%g"):
        """
        Given an input value and its units, return a string with
        English, SI or Both units.
        If different primary units are desired, specify them with "out_units".
        At the end, if default_units are not included, include them.
        """

        inp_units = self.force_inch(inp_units)
        out_units = self.force_inch(out_units)
        default_units = self.force_inch(default_units)
        user_inp_units = self.force_inch(user_inp_units)

        category = get_category( inp_units )
        if not category:
            s = fmt%inp_val
            return s


        used_set = set() # set of units included in outout already
        sL = []

        if user_inp_units:
            chk_units_in_category( user_inp_units, category )

            val = convert_value(inp_val, inp_units, user_inp_units)
            s = fmt%val + " %s"%user_inp_units
            sL.append(s)
            used_set.add( user_inp_units )

        if out_units:
            chk_units_in_category( out_units, category )

            val = convert_value(inp_val, inp_units, out_units)
            s = fmt%val + " %s"%out_units
            sL.append(s)
            used_set.add( out_units )

        # always show inp_units
        if inp_units not in used_set:
            s = fmt%inp_val + " %s"%inp_units
            sL.append(s)
            used_set.add( inp_units )

        # always show default units.
        if default_units not in used_set:
            val = convert_value(inp_val, inp_units, default_units)
            s = fmt%val + " %s"%default_units
            sL.append(s)
            used_set.add( default_units )

        # finally, add SI and/or English
        if self.output_units == "SI":
            si_units = SI_unitsD[category]
            if si_units not in used_set:
                val = convert_value(inp_val, inp_units, si_units)
                s = fmt%val + " %s"%si_units
                sL.append(s)
                used_set.add( si_units )
        elif self.output_units == "English":
            eng_units = self.force_inch( display_def_unitsD[category] )
            if eng_units not in used_set:
                val = convert_value(inp_val, inp_units, eng_units)
                s = fmt%val + " %s"%eng_units
                sL.append(s)
                used_set.add( eng_units )
        else:
            # add both SI and English
            eng_units = self.force_inch( display_def_unitsD[category] )
            if eng_units  not in used_set:
                val = convert_value(inp_val, inp_units, eng_units)
                s1 = fmt%val + " %s"%eng_units
                sL.append(s1)
                used_set.add( eng_units )
            si_units = SI_unitsD[category]
            if si_units not in used_set:
                val = convert_value(inp_val, inp_units, si_units)
                s2 = fmt%val + " %s"%si_units
                sL.append(s2)
                used_set.add( si_units )

        s = sL[0]
        if len(sL) > 1:
            #s = s1 + " (%s)"% s2
            s += " (" + ", ".join( [_s for _s in sL[1:]] ) + ")"

        return s

    def set_vars_dict(self, varsD=None):
        """Calling function or class instance will set its current locals()/vars()"""
        self.current_varsD = varsD

    def u_print(self, name, desc="", primary_units="", added_units="", fmt="%g"):
        """
        Print the string returned by u_string.
        Use output template to print variable "name" in desired units.
        if primary_units is input, it will be listed first in the output line.
        if added_units is input, it will be listed 2nd in the output line.
        If SI or English is different from primary_units or added_units they will be added.
        """
        s = self.u_string(name, primary_units=primary_units, 
                          added_units=added_units, desc=desc, fmt=fmt)
        print(s)

    def u_string(self, name, desc="", primary_units="", added_units="", fmt="%g"):
        """
        Return a string created by using the output template.
        The template shows variable "name" in desired units.
        if primary_units is input, it will be listed first in the output line.
        if added_units is input, it will be listed 2nd in the output line.
        If SI or English is different from primary_units or added_units they will be added.
        """

        # make sure that units agree with default units of variable name
        if self.default_unitsD.get(name, ''):
            category = get_category( self.default_unitsD[name] )
            if category:
                if primary_units:
                    chk_units_in_category( primary_units, category )
                if added_units:
                    chk_units_in_category( added_units, category )

        else: # not in default_unitsD, so if primary_units are given, assign them
            if primary_units:
                category = get_category( primary_units )
                if category:
                    self.default_unitsD[name] = primary_units
                else:
                    raise Exception('Did not recognize units="%s"'%primary_units )

                if added_units:
                    chk_units_in_category( added_units, category )

        # get numeric value from locals()/vars() of calling function/class instance
        val = self.current_varsD[name]
        # if default units are known for "name", then check to see if added_units are input
        if self.default_unitsD.get(name, ''):
            if added_units:
                # put value into added_units
                val = convert_value( inp_val=val, inp_units=self.default_unitsD[name], 
                                    out_units=added_units)
            else:
                # w/o added_units from user, simply use known units
                added_units = self.default_unitsD[name]
                #print('Found internal units = "%s"'%added_units)

        # inp_val=0.0, added_units="", primary_units="", fmt="%g")
        s = self.__get_output_str( inp_val=val, inp_units=added_units, 
                                 out_units=primary_units,  
                                 default_units=self.default_unitsD.get(name, ''),
                                 user_inp_units=self.user_input_unitsD.get(name, ''),
                                 fmt=fmt)

        return self.template%(name, s, desc  )

    def set_units_same_as(self, new_name, old_name):
        """Set the units of an internal parameter to the same as an existing parameter."""

        # It's an error if new_name already has default units
        if self.default_unitsD.get(new_name, ''):
            raise Exception('In set_units_same_as, new_name="%s"'%new_name +\
                            ' already has default units="%s".'%self.default_unitsD[new_name])

        # It's an error if old_name is not already known
        if not self.default_unitsD.get(old_name, ''):
            raise Exception('In set_units_same_as, old_name="%s" does NOT have default units.'%old_name)

        self.default_unitsD[new_name] = self.default_unitsD[old_name]


    def set_units(self, name='', units=''):
        """Set the units of an internal parameter."""

        if not name:
            raise Exception('In set_units, "name" can NOT be blank.')

        # allow name to be specified as having no units
        if units=='':
            self.default_unitsD[name] = units
            return

        category = get_category( units )
        # It's an error if units are not in RocketUnits
        if not category:
            raise Exception('In set_units, units="%s" is NOT recognized.'%units)

        self.default_unitsD[name] = units
        
    def set_user_units(self, name='', user_units=''):
        """Set units input by the user"""

        if not name:
            raise Exception('In set_units, "name" can NOT be blank.')

        category = get_category( user_units )
        # It's an error if units are not in RocketUnits
        if not category:
            raise Exception('In set_units, user_units="%s" is NOT recognized.'%user_units)
        
        self.user_input_unitsD[name] = user_units        

def main():        

    def bar(my_pi, a="14.7 psia",b="1.0 gee",c="55.0 mile/hr", 
            i=42, output_units="English"): 

        # set the internal values of all the input variables with units.
        my_units = Units( bar, vars() )
        
        a = my_units.get_input_value("a")
        b = my_units.get_input_value("b")
        c = my_units.get_input_value("c")

        my_pi = my_units.get_input_value("my_pi")
        my_units.set_units( "my_pi", "rad" )

        # do any calculations and create output variables.
        x_out = 10 * c # units same as "c"
        my_units.set_units_same_as("x_out", "c")

        # print(my_pi,a,b,c,i,x_out)
        # print("vars() =", vars())

        # give Units object the current locals()/vars()
        my_units.set_vars_dict( vars() )
        u_print = my_units.u_print
        my_units.set_print_template( template="%8s = %-35s --> %s")

        u_print("my_pi", "Angle of interest")
        u_print("my_pi", "Angle of interest", "deg")
        u_print("my_pi", primary_units="circle")

        u_print("a", desc="Ambient Pressure", added_units="atm")
        u_print("b", "Initial Acceleration")
        u_print("c", "Highway speed")
        u_print("x_out", "10 times c")

        u_print("i", primary_units="J", desc="Some random energy")
        
        # print()
        # print("varsD =", vars())
        # print()
        # print("default_unitsD = ", my_units.default_unitsD)
        # print()
        # print("user_input_valueD = ", my_units.user_input_valueD)

        

    print("=============  English  ================")
    bar( 3.14159, a="2 atm", b="64 ft/s**2" )
    print("=============  SI  ================")
    bar( 3.14159, a="2 atm", b="64 ft/s**2", output_units="SI" )
    print("=============  Both  ================")
    bar( 3.14159, a="2 atm", b="64 ft/s**2", output_units="Both" )


if __name__ == '__main__':
    main()