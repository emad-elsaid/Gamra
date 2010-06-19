'''
Created on Jun 14, 2010

@author: blaze

@summary: This is like a Database tables of our Application Data
            it contain all data structure of the Image Document, and may
            contain library structure and so.
'''
import cairo
from wx.lib.wxcairo import ContextFromDC
import math

class Path:
    def __init__(self):
        self.Points = []
        self.Closed = False
        
    def Apply(self, context ): pass
    def ToData(self): pass
    def FromData(self, data): pass

class Stroke:
    def __init__(self):
        self.Width = 2.0
        self.Antialias = cairo.ANTIALIAS_DEFAULT
        self.Dash = []
        self.DashOffset = 0
        self.Cap = cairo.LINE_CAP_BUTT
        self.Join = cairo.LINE_JOIN_MITER
        
    def Apply(self, context, preserve=True ): pass
    def ToData(self): pass
    def FromData(self, data): pass

class Fill:
    def __init__(self):
        self.Rule = cairo.FILL_RULE_WINDING
        
    def Apply(self, context, preserve=True ): pass
    def ToData(self): pass
    def FromData(self, data): pass
    
class Object:
    '''
    the main object, out Image document will contain 
    many object of this we'll render them over each 
    others using the document Render
    '''
    def __init__(self):
        self.Path = Path()
        self.Stroke = Stroke()
        self.Fill = Fill()
        self.Visible = True
        self.Locked = False
        
    def Render(self): pass
    def ToData(self): pass
    def FromData(self, data): pass
       
class MetaData:
    '''
    this is the meta data class for document
    it'll hold all data of the author, creation date
    last modification...etc.
    '''
    
    def __init__(self):
        self.Author = ''
        self.Created = ''
        self.Modified = ''
        self.Comment = ''
        
    def ToData(self): pass
    def FromData(self, data): pass
    
class Document:
    '''
    Image main document
    '''
    def __init__(self,width,height):
        self.MetaData = MetaData
        
        self.Objects = []
        self.ToolObjects = []
        
        self.SelectedObjects = []
        self.SelectedToolsObjects = []
        
        self.Width = width
        self.Height = height
        
        self.Clip = [-100,-100,width,height]
        self.Antialias = cairo.ANTIALIAS_DEFAULT
        self.Zoom = 1
        
        self.Mouse = (0,0)
       
    def GetUnderPixel(self,pixel): pass
    
    def Render(self,dc):
        self.Clip[2:] = list(dc.GetSizeTuple())
        ctx = ContextFromDC(dc)
        ctx.translate(-self.Clip[0], -self.Clip[1])
        ctx.scale(self.Zoom,self.Zoom)
        
        bor = 2/self.Zoom
        ctx.set_line_width(bor)
        ctx.rectangle(-1,-1,self.Width+bor*2,self.Height+bor*2)
        ctx.set_antialias(cairo.ANTIALIAS_NONE)
        ctx.set_source_rgb(1, 1, 1)
        ctx.fill_preserve()
        ctx.set_source_rgb(0, 0, 0)
        ctx.stroke()
        ctx.set_antialias(cairo.ANTIALIAS_DEFAULT)
        
    def SetMouse(self,position):
        self.Mouse = self.Pixel2Coord(position)
        
    def Pixel2Coord(self,pixel):
            return (int((pixel[0] + self.Clip[0])/self.Zoom),
                    int((pixel[1] + self.Clip[1])/self.Zoom))
          
    def ToData(self): pass
    def FromData(self, data): pass
    
    