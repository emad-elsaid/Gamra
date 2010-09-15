'''
Created on Jun 5, 2010

@author: blaze
'''
import wx
import Document
import cairo


class Tool():
    '''
    the parent of all tools here
    '''
    def __init__(self, name='tool', icon='tool.png', Priority = 0):
        self.Name = name
        self.Icon = icon
        self.Priority = Priority
    
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
        
        self.Canvas.Document.ToolObjects = []
        self.Canvas.Refresh()
    
    def OnMouseLeftDown(self,event): event.Skip()
    def OnMouseMiddleDown(self,event): 
        self.StartPoint = self.Canvas.Document.Mouse
        event.Skip()
        
    def OnMouseRightDown(self,event): event.Skip()
    
    def OnMouseLeftUp(self,event): 
        wx.GetApp().Frame.Properties.Refresh(wx.GetApp().Frame.Canvas)
        event.Skip()

    
    def OnMouseMiddleUp(self,event): event.Skip()
        
    def OnMouseRightUp(self,event): event.Skip()
    
    def OnMouseMove(self,event): 
        
        self.Canvas.Document.SetMouse(event.Position)
        
        if(event.Dragging() and event.MiddleIsDown() ):
            newpoint = self.Canvas.Document.Mouse
            zoom = self.Canvas.Document.Zoom
            self.Canvas.Document.Clip[0] -= int((newpoint[0]-self.StartPoint[0])*zoom)
            self.Canvas.Document.Clip[1] -= int((newpoint[1]-self.StartPoint[1])*zoom)
            self.Canvas.Refresh()
                
        wx.GetApp().Frame.SetStatusText(
                        'Current Position:'+str(self.Canvas.Document.Mouse)+
                        ', Zoom : '+str(self.Canvas.Document.Zoom*100)+'%'
                        )
        undermouse = self.Canvas.Document.GetUnderPixel(self.Canvas.Document.Mouse,
                                                        objects=self.Canvas.Document.ToolObjects)
        if( undermouse!=None and undermouse.__class__.__name__!='rect' ):
            self.Canvas.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        else:
            self.Canvas.SetCursor(wx.StockCursor(wx.CURSOR_DEFAULT))
        event.Skip()
    
    def OnKeyDown(self,event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_TAB:
                
            #check the visibility of the panel
            if  wx.GetApp().Frame.Properties.IsShown(): 
                wx.GetApp().Frame.Properties.Hide()
                wx.GetApp().Frame.Layout()
            else:
                wx.GetApp().Frame.Properties.Show()
                wx.GetApp().Frame.Layout()
        
        elif keycode == 49 or keycode == wx.WXK_NUMPAD1:
            self.Canvas.Document.Zoom = 1
            x = (self.Canvas.GetSizeTuple()[0] - self.Canvas.Document.Width) / 2
            y = (self.Canvas.Document.Height - self.Canvas.GetSizeTuple()[1]) / 2
            self.Canvas.Document.Clip[0] = -x
            self.Canvas.Document.Clip[1] = y
            self.Canvas.Refresh()
            
        elif keycode == 50 or keycode == wx.WXK_NUMPAD2:
            if len(self.Canvas.Document.SelectedObjects) > 0:
                rect =  self.Canvas.Document.GetRect(self.Canvas.Document.SelectedObjects)
                rectCenter = ( (rect.Path.Points[0][1][0] + rect.Path.Points[1][1][0]) / 2 , 
                            (rect.Path.Points[0][1][1] + rect.Path.Points[1][1][1]) / 2 )
                w1 = abs(rect.Path.Points[0][1][0] - rect.Path.Points[1][1][0])
                h1 = abs(rect.Path.Points[0][1][1] - rect.Path.Points[1][1][1])
                w2 = (self.Canvas.GetSizeTuple()[0] - w1) / 2
                h2 = (self.Canvas.GetSizeTuple()[1] - h1) / 2
                x = (rect.Path.Points[0][1][0] - w2) 
                y = (rect.Path.Points[0][1][1] - h2)  
                self.Canvas.Document.Clip[0] = x
                self.Canvas.Document.Clip[1] = y
                self.Canvas.Refresh() 
        
        event.Skip()    
            
    
    def OnKeyUp(self,event): event.Skip()
    
    def OnWheel(self,event):
        if(event.GetWheelRotation()>0):
            self.Canvas.Document.Zoom = round(self.Canvas.Document.Zoom*1.1,2)
        else:
            self.Canvas.Document.Zoom = round(self.Canvas.Document.Zoom/1.1,2)          
        
        self.Canvas.Refresh()
        
        event.Skip()
        
    def OnPaint(self, event):
        dc = wx.BufferedPaintDC(self.Canvas)
        dc.SetBackground(wx.Brush(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU)))
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
    
        
