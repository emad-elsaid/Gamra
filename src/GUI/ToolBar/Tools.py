'''
Created on Jun 5, 2010

@author: blaze
'''
import wx
from wx.lib.graphics import GraphicsBitmap
import math

class Tool():
    '''
    the parent of all tools here
    '''
    def __init__(self, name='tool', icon='tool.png'):
        self.Name = name
        self.Icon = icon
            
    def Activate(self,canvas):
        self.Canvas = canvas
        self.Canvas.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
        self.Canvas.Bind(wx.EVT_MIDDLE_DOWN, self.OnMouseMiddleDown)
        self.Canvas.Bind(wx.EVT_RIGHT_DOWN, self.OnMouseRightDown)
        
        self.Canvas.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
        self.Canvas.Bind(wx.EVT_MIDDLE_UP, self.OnMouseMiddleUp)
        self.Canvas.Bind(wx.EVT_RIGHT_UP, self.OnMouseRightUp)
        
        self.Canvas.Bind(wx.EVT_MOTION, self.OnMouseMove)
        self.Canvas.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.Canvas.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        
        self.Canvas.Bind(wx.EVT_MOUSEWHEEL, self.OnWheel)
        self.Canvas.Bind(wx.EVT_PAINT, self.OnPaint)
        
    
    def Deactivate(self):
        self.Canvas.Unbind(wx.EVT_LEFT_DOWN)
        self.Canvas.Unbind(wx.EVT_MIDDLE_DOWN)
        self.Canvas.Unbind(wx.EVT_RIGHT_DOWN)
        
        self.Canvas.Unbind(wx.EVT_LEFT_UP)
        self.Canvas.Unbind(wx.EVT_MIDDLE_UP)
        self.Canvas.Unbind(wx.EVT_RIGHT_UP)
        
        self.Canvas.Unbind(wx.EVT_MOTION)
        self.Canvas.Unbind(wx.EVT_KEY_DOWN)
        self.Canvas.Unbind(wx.EVT_KEY_UP)
        
        self.Canvas.Unbind(wx.EVT_MOUSEWHEEL)
        self.Canvas.Unbind(wx.EVT_PAINT)
    
    def OnMouseLeftDown(self,event): event.Skip()
    
    def OnMouseMiddleDown(self,event): 
        self.StartPoint = self.Canvas.Document.Mouse
        event.Skip()
        
    def OnMouseRightDown(self,event): event.Skip()
    
    def OnMouseLeftUp(self,event): event.Skip()
    
    def OnMouseMiddleUp(self,event): 
        event.Skip()
        
    def OnMouseRightUp(self,event): event.Skip()
    
    def OnMouseMove(self,event): 
        
        self.Canvas.Document.SetMouse(event.Position)
        
        if(event.Dragging() and event.MiddleIsDown() ):
            newpoint = self.Canvas.Document.Mouse
            self.Canvas.Document.Clip[0] += newpoint[0]-self.StartPoint[0]
            self.Canvas.Document.Clip[1] += newpoint[1]-self.StartPoint[1]
            self.Canvas.Refresh()
                
        wx.GetApp().Frame.SetStatusText('Current Position:'+str(self.Canvas.Document.Mouse))
        event.Skip()
    
    def OnKeyDown(self,event): event.Skip()
    def OnKeyUp(self,event): event.Skip()
    
    def OnWheel(self,event):
        if(event.GetWheelRotation()>0):
            self.Canvas.Document.Zoom *= 1.1
        else:
            self.Canvas.Document.Zoom /= 1.1          
        
        self.Canvas.Refresh()
        
        event.Skip()
        
    def OnPaint(self, event):
        dc = wx.BufferedPaintDC(self.Canvas)
        dc.Clear()
        self.Canvas.Document.Render(dc)
    
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
    
        