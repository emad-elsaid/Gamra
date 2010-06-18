'''
Created on Jun 10, 2010

@author: blaze
'''
from GUI.ToolBar.Tools import EditingTool

class Select(EditingTool):
    '''
    a tool to select one or many items from canvas.
    '''
    
    def __init__(self):
        EditingTool.__init__(self,name='Select', icon='select.png')