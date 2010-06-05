'''
Created on Jun 5, 2010

@author: blaze
'''

class Tool():
    '''
    the parent of all tools here
    '''
    def __init__(self):
        pass
    
    def Activate(self):
        pass
    
    def Deactivate(self):
        pass
    
    def OnSelectionAdd(self):
        pass
    
    def OnSelectionSubtracted(self):
        pass
     
class EditingTool():
    '''
    Object editing tool parent like
    moving, rotating, scale, skew, shear...etc
    '''

    def __init__(self):
        pass
    
class VectorTool():
    '''
    vector adding, editing, drawing like
    pen tool, biezer curves, lines, 
    circle, rectangle, stars...etc
    '''
    def __init__(self):
        pass
        
class BitmapTool():
    '''
    bitmap editing tools like:
    rectangle, circle selections, burn, dodge
    '''
    def __init__(self):
        pass