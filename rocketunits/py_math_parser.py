from math import *
import traceback
import sys
from io import BytesIO
from tokenize import tokenize, NUMBER, STRING, NAME, OP

# This code modified from BestCode expression parser:
# see: https://www.gobestcode.com/html/evaluate_math_expressions_pyth.html

class PyMathParser(object):
    '''
    Mathematical Expression Evaluator class.
    You can set the expression member, set the functions, variables and then call
    evaluate() function that will return you the result of the mathematical expression
    given as a string.
    '''
   
    '''
    Dictionary of functions that can be used in the expression.
    '''
    functions =  {'__builtins__':None};
   
    '''
    Dictionary of variables that can be used in the expression.
    '''
    variables = {'__builtins__':None};    

    def __init__(self):
        '''
        Constructor
        '''
        self.addDefaultFunctions()
        self.addDefaultVariables()
   
    def evaluate(self, expression):
        '''
        Evaluate the mathematical expression given as a string in the expression member variable.
       
        '''
        g = tokenize(BytesIO(expression.encode('utf-8')).readline)  # tokenize the string
        for t in g:
            if t.type == NAME:
                if t.string in self.variables or t.string in self.functions:
                    continue
                else:
                    return 'ERROR: "%s" NOT RECOGNIZED'%t.string
            if t.type == STRING:
                return 'ERROR: %s is a string.'%t.string
        
        
        
        try:
            ans = eval(expression, self.variables, self.functions)
        except:
            ex_type, ex_value, ex_traceback = sys.exc_info()
            ans = 'ERROR:' + str(ex_value)
            #print( 'tokenize g=',g )
            #for toknum, tokval, _, _, _ in g:
            #    print(  tokval )
            #for t in g:
            #    print(  t )
        return ans

    def addDefaultFunctions(self):
        '''
        Add the following Python functions to be used in a mathemtical expression:
        acos
        asin
        atan
        atan2
        ceil
        cos
        cosh
        degrees
        exp
        fabs
        floor
        fmod
        frexp
        hypot
        ldexp
        log
        log10
        modf
        pow
        radians
        sin
        sinh
        sqrt
        tan
        tanh
        '''
        self.functions['acos']=acos
        self.functions['asin']=asin
        self.functions['atan']=atan
        self.functions['atan2']=atan2
        self.functions['ceil']=ceil
        self.functions['cos']=cos
        self.functions['cosh']=cosh
        self.functions['degrees']=degrees
        self.functions['exp']=exp
        self.functions['fabs']=fabs
        self.functions['floor']=floor
        self.functions['fmod']=fmod
        self.functions['frexp']=frexp
        self.functions['hypot']=hypot
        self.functions['ldexp']=ldexp
        self.functions['log']=log
        self.functions['log10']=log10
        self.functions['modf']=modf
        self.functions['pow']=pow
        self.functions['radians']=radians
        self.functions['sin']=sin
        self.functions['sinh']=sinh
        self.functions['sqrt']=sqrt
        self.functions['tan']=tan
        self.functions['tanh']=tanh
       
    def addDefaultVariables(self):
        '''
        Add e and pi to the list of defined variables.
        '''
        self.variables['e']=e
        self.variables['pi']=pi

    def getVariableNames(self):
        '''
        Return a List of defined variables names in sorted order.
        '''
        mylist = list(self.variables.keys())
        try:
            mylist.remove('__builtins__')
        except ValueError:
            pass
        mylist.sort()
        return mylist


    def getFunctionNames(self):
        '''
        Return a List of defined function names in sorted order.
        '''
        mylist = list(self.functions.keys())
        try:
            mylist.remove('__builtins__')
        except ValueError:
            pass
        mylist.sort()
        return mylist

if __name__ == "__main__":
    
    
    pmp = PyMathParser()
    def result_print( s ):
        ans = pmp.evaluate(expr)
        print( 'ans=%20s'%ans, ' for expr=',expr )
        #try:
        #    ans = pmp.evaluate(expr)
        #    print( 'ans=%20s'%ans, ' for expr=',expr )
        #except:
        #    # Get current system exception
        #    ex_type, ex_value, ex_traceback = sys.exc_info()
        #    
        #    print( 'ERROR: "%s"'%expr, '=', ex_value)
        
    
    print('================== Should all PASS =====================')
    for expr in ['sqrt(4)', '45*pi/180', 'cos(45*pi/180)', 'cos(radians(45))', 
                 '1+ 2', '1+ 2+sin (.3 + .4)/e + pi', 'pi']:
        result_print( expr )
        
    
    print('================== Should all FAIL =====================')
    for expr in ['1+2+sin( .1 + y)', 'sys.exit()', '"25"', '"25',
                 'pwd()', 'print(3.333)', 'pi = 1', '5 + 7 *']:
        result_print( expr )
    
