#!/usr/bin/env python
# -*- coding: ascii -*-

"""
Look for a line of code ending with a comment that starts with "# METADATA_RESET:"

Use the template after "# METADATA_RESET:" to change the code portion of the line.

For example:

__version__ = '0.0.1'  # METADATA_RESET:__version__ = '<<version>>'
"""

def render_line( line, metadataD ):
    """Change the line of code using values from dictionary, metadataD.
    
       Items in metadataD look like: {"<<version>>":"1.2.3", "<<author>>":"Buster Boop"}
    """
    
    sL = line.split("# METADATA_RESET:")
    code_str = sL[-1].rstrip()
    print('  Change:', sL[0].rstrip() )
    
    for key,val in metadataD.items():
        if code_str.find(key) >= 0:
            code_str = code_str.replace( key, val )
            
    print('      To:', code_str)
    return code_str + '  # METADATA_RESET:' + sL[-1]

def render_file( full_file_name, metadataD ):
    """Look through file for "# METADATA_RESET:"
       Render lines where it is found.
    """
    with open(full_file_name, 'r') as f:
        lineL = list(f)    # will include \n at end of line
        
    for i,line in enumerate(lineL):
        if line.find("# METADATA_RESET:") >= 0:
            print('In File:', full_file_name)
            if line.endswith('\n'):
                lineL[i] = render_line( line[:-1], metadataD ) + '\n'
            else:
                lineL[i] = render_line( line, metadataD )
            
    with open(full_file_name, 'w') as f:
        f.write( ''.join(lineL) )
    
if __name__ == "__main__":
    import os
    
    # see: https://packaging.python.org/guides/distributing-packages-using-setuptools/
    #      for version number advice
    """
    semantic versioning is a 3-part MAJOR.MINOR.MAINTENANCE numbering scheme, 
    where the project author increments:

    MAJOR version when they make incompatible API changes,
    MINOR version when they add functionality in a backwards-compatible manner, and
    MAINTENANCE version when they make backwards-compatible bug fixes.    
    """
    metadataD =  {"<<version>>":"0.1.9"} # <== change value then run

    render_file( os.path.abspath('./docs/conf.py'), metadataD )
    render_file( os.path.abspath('./setup.py'), metadataD )
    #render_file( os.path.abspath('./rocketunits/_version.py'), metadataD )
    render_file( os.path.abspath('./rocketunits/rocket_units.py'), metadataD )
    render_file( os.path.abspath('./rocketunits/__init__.py'), metadataD )
    
    