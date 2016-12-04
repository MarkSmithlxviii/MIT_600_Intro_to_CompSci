allhope = 'global variable'
def toy (passtotoy):
    """Steal my variables"""
    myvar = 'local variable'
    print('passed to toy', passtotoy)
    print('global var', allhope)
    print('defined in function',myvar)
    allhope=('overwritten in function')
    print('global var', allhope)

toy('passed to toy')
