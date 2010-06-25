'''
Created on Jun 23, 2010

@author: blaze
'''

class Generic:
    '''
    this is the generic editor , all editors will enherit it's
    functionality
    '''
    

    def __init__(self, icon='data/icons/photo.png', Periority=0 ):
        self.Periority = Periority
        
    def Activate(self, canvas ): pass
    def Deactivate(self, canvas): pass
        