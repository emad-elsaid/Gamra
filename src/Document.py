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
        
    def Apply(self, context ):
        
        context.new_path()
        
        if len(self.Points)>0 :
            context.move_to(self.Points[0][1][0],self.Points[0][1][1])
            
        for i in range( 1, len(self.Points) ):
            self.Draw(context, i-1, i)
        
        if self.Closed :
            self.Draw(context, -1, 0)
            context.close_path()
    
    def Draw(self, context, i, j):
        if self.Points[i][2]==None and self.Points[j][0]==None :
            context.line_to(self.Points[j][1][0],self.Points[j][1][1])
        elif self.Points[i][2]==None :
            context.curve_to(self.Points[i][1][0],self.Points[i][1][1],
                             self.Points[j][0][0],self.Points[j][0][1],
                             self.Points[j][1][0],self.Points[j][1][1])
        elif self.Points[j][0]==None :
            context.curve_to(self.Points[i][2][0],self.Points[i][2][1],
                             self.Points[j][1][0],self.Points[j][1][1],
                             self.Points[j][1][0],self.Points[j][1][1])
        else:
            context.curve_to(self.Points[i][2][0],self.Points[i][2][1],
                             self.Points[j][0][0],self.Points[j][0][1],
                             self.Points[j][1][0],self.Points[j][1][1])
            
    def add1(self, x, y): 
        self.Points.append([None,[x,y],None])
           
    def add2(self,hx,hy,x,y):
        self.Points.append([[hx,hy],[x,y],[hx,hy]])
        
    def add3(self,h1x,h1y,x,y,h2x,h2y):
        self.Points.append([[h1x,h1y],[x,y],[h2x,h2y]])
        
    def Scale(self,xScale,yScale): pass
    def Translate(self,xDelta,yDelta): pass
    def ToData(self): pass
    def FromData(self, data): pass

class Stroke:
    def __init__(self):
        self.Width = 2.0
        self.Dash = []
        self.DashOffset = 0
        self.Cap = cairo.LINE_CAP_BUTT
        self.Join = cairo.LINE_JOIN_MITER
        self.Color = (0,0,0,1)
        
    def Apply(self, context, preserve=True ):
        context.set_line_width( self.Width )
        context.set_dash( self.Dash, 1 )
        context.set_line_cap( self.Cap )
        context.set_line_join( self.Join )
        context.set_source_rgba(self.Color[0],self.Color[1],self.Color[2],self.Color[3])
        
        if preserve :
            context.stroke_preserve()
        else:
            context.stroke()
        
        
    def ToData(self): pass
    def FromData(self, data): pass

class Fill:
    def __init__(self):
        self.Rule = cairo.FILL_RULE_WINDING
        self.Color = (0.5,0.5,0.5,1)
        
    def Apply(self, context, preserve=True ):
        context.set_fill_rule(self.Rule)
        context.set_source_rgba(self.Color[0],self.Color[1],self.Color[2],self.Color[3])
        if preserve :
            context.fill_preserve()
        else:
            context.fill()
        
        
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
        self.Antialias = cairo.ANTIALIAS_DEFAULT
        self.Fill = Fill()
        self.Visible = True
        self.Locked = False
        
    def Scale(self,xScale,yScale): pass
    def Translate(self,xDelta,yDelta): pass
    
    def Apply(self, context):
        if self.Visible :
            context.set_antialias(self.Antialias)
            self.Path.Apply(context)
            self.Fill.Apply(context)
            self.Stroke.Apply(context)
        
        
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
        border = Object()
        border.Stroke.Width = bor
        border.Fill.Color = (1,1,1,1)        
        border.Path.add1(-bor*2, -bor*2)
        border.Path.add1(self.Width+bor*2, -bor*2)
        border.Path.add1(self.Width+bor*2, self.Height+bor*2)
        border.Path.add1(-bor*2, self.Height+bor*2)
        border.Path.Closed = True
        border.Antialias = cairo.ANTIALIAS_NONE
        border.Apply(ctx)
        
    def SetMouse(self,position):
        self.Mouse = self.Pixel2Coord(position)
        
    def Pixel2Coord(self,pixel):
            return (int((pixel[0] + self.Clip[0])/self.Zoom),
                    int((pixel[1] + self.Clip[1])/self.Zoom))
          
    def ToData(self): pass
    def FromData(self, data): pass
    
    