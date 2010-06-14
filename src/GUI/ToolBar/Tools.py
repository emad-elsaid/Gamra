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
    
    def OnMouseLeftDown(self,event): event.Skip()
    def OnMouseMiddleDown(self,event): event.Skip()
    def OnMouseRightDown(self,event): event.Skip()
    
    def OnMouseLeftUp(self,event): event.Skip()
    def OnMouseMiddleUp(self,event): event.Skip()
    def OnMouseRightUp(self,event): event.Skip()
    
    def OnMouseMove(self,event): event.Skip()
    
    def OnKeyDown(self,event): event.Skip()
    def OnKeyUp(self,event): event.Skip()
    
    def OnWheel(self,event): event.Skip()
    def OnPaint(self, event): event.Skip()
    
     
class EditingTool(Tool):
    '''
    Object editing tool parent like
    moving, rotating, scale, skew, shear...etc
    '''
    pass
    
class VectorTool(Tool):
    '''
    vector adding, editing, drawing like
    pen tool, biezer curves, lines, 
    circle, rectangle, stars...etc
    '''
    pass
        
class BitmapTool(Tool):
    '''
    bitmap editing tools like:
    rectangle, circle selections, burn, dodge
    '''
    pass
    
        