'''
Created on Jun 14, 2010

@author: blaze

@summary: This is like a Database tables of our Application Data
            it contain all data structure of the Image Document, and may
            contain library structure and so.
'''
import cairo
from wx.lib.wxcairo import ContextFromDC

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
        
        self.Clip = [0,0,width,height]
        self.Antialias = cairo.ANTIALIAS_DEFAULT
        self.Zoom = 1
        
        self.Mouse = [0,0]
       
    def GetUnderPixel(self,pixel): pass
    def Render(self,dc):
        self.Clip[2:] = list(dc.GetSizeTuple())
        ctx = ContextFromDC(dc)
        ctx.set_line_width(15)
        ctx.move_to(125, 25)
        ctx.line_to(225, 225)
        ctx.rel_line_to(-200, 0)
        ctx.close_path()
        ctx.set_source_rgba(0, 0, 0.5, 1)
        ctx.stroke()
        
    
    def ToData(self): pass
    def FromData(self, data): pass
    
    