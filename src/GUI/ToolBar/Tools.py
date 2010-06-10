'''
Created on Jun 5, 2010

@author: blaze
'''

class Tool():
    '''
    the parent of all tools here
    '''
    def __init__(self, name='tool', icon='tool.png',canvas=None):
        self.name = name
        self.icon = icon        
        self.canvas = canvas
    
    def Activate(self):
        pass
    
    def Deactivate(self):
        pass
    
    def OnSelectionAdd(self):
        pass
    
    def OnSelectionSubtract(self):
        pass
     
class EditingTool(Tool):
    '''
    Object editing tool parent like
    moving, rotating, scale, skew, shear...etc
    '''
    def __init__(self, name='tool', icon='tool.png',canvas=None):
        Tool.__init__(self, name='tool', icon='tool.png',canvas=None)
    
class VectorTool(Tool):
    '''
    vector adding, editing, drawing like
    pen tool, biezer curves, lines, 
    circle, rectangle, stars...etc
    '''
    def __init__(self, name='tool', icon='tool.png',canvas=None):
        Tool.__init__(self, name='tool', icon='tool.png',canvas=None)
        
class BitmapTool(Tool):
    '''
    bitmap editing tools like:
    rectangle, circle selections, burn, dodge
    '''
    def __init__(self, name='tool', icon='tool.png',canvas=None):
        Tool.__init__(self, name='tool', icon='tool.png',canvas=None)
    
        