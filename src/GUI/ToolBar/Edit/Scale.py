'''
Created on Jun 10, 2010

@author: blaze
'''
from GUI.ToolBar.Tools import EditingTool

class Scale(EditingTool):
    '''
    a tool to Scale element or even a punch of them
    '''
    
    def __init__(self):
        EditingTool.__init__(self,name='Scale', icon='tool.png',canvas=None)
        
    def Activate(self):
        print 'test the Scale activation'
    def Deactivate(self):
        print 'scale deactivated'