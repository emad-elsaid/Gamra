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
        EditingTool.__init__(self,name='Scale', icon='tool.png')
        
    def OnMouseLeftDown(self,event):
        print 'test'
        event.Skip()