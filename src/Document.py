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
        
    def add3(self,h1x,h1y,x,y,h2x,h2y):
        self.Points.append([[h1x,h1y],[x,y],[h2x,h2y]])
        
    def ToData(self): pass
    def FromData(self, data): pass

class Stroke:
    def __init__(self):
        self.Width = 1.0
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
        self.Color = (1,1,1,1)
        
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
        
    
    def Apply(self, context):
        if self.Visible :
            context.set_antialias(self.Antialias)
            self.Path.Apply(context)
            self.Fill.Apply(context)
            self.Stroke.Apply(context)
            
    def ToData(self): pass
    def FromData(self, data): pass
       
class Rectangle(Object):
    def __init__(self,x,y,w,h):
        Object.__init__(self)
        self.Path.add1(x, y)
        #self.Path.add1(x+w, y)
        self.Path.add1(x+w, y+h)
        #self.Path.add1(x, y+h)
        #self.Path.Closed = True
    def Apply(self,ctx):
        ctx.new_path()
        ctx.set_antialias(self.Antialias)
        ctx.rectangle(self.Path.Points[0][1][0],self.Path.Points[0][1][1],
                      self.Path.Points[1][1][0]-self.Path.Points[0][1][0],
                      self.Path.Points[1][1][1]-self.Path.Points[0][1][1])
        self.Fill.Apply(ctx)
        self.Stroke.Apply(ctx)
        
        
class ControlPoint(Object):
    def __init__(self,x,y):
        Object.__init__(self)
        self.Path.add1(x,y)
        self.Antialiase = cairo.ANTIALIAS_NONE
        
    def Apply(self,ctx):
        ctx.new_path()
        ctx.set_antialias(self.Antialias)
        ctx.rectangle(self.Path.Points[0][1][0]-2,self.Path.Points[0][1][1]-2,4,4)
        self.Fill.Apply(ctx)
        self.Stroke.Apply(ctx,False)
        ctx.rectangle(self.Path.Points[0][1][0]-3,self.Path.Points[0][1][1]-3,6,6)
        
    
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
        
        self.Objects = [Rectangle(5,5,100,100),
                        Rectangle(50,50,100,100),
                        Rectangle(110,110,100,100),
                        Rectangle(150,150,100,100)]
        self.ToolObjects = []
        
        self.SelectedObjects = []
        self.SelectedToolObjects = []
        
        self.Width = width
        self.Height = height
        
        self.Clip = [-100,-100,width,height]
        self.Antialias = cairo.ANTIALIAS_DEFAULT
        self.Zoom = 1
        
        self.Mouse = (0,0)
        
        self.Border = Rectangle(-2,-2,self.Width+2*2,self.Height+2*2)
        self.Border.Stroke.Width = 2
        self.Border.Antialias = cairo.ANTIALIAS_NONE
       
    def GetUnderPixel(self,pixel,returnList=False,objects=None):
        ctx = cairo.Context(cairo.ImageSurface(cairo.FORMAT_ARGB32,0,0))
        
        if objects==None :
            objects = self.Objects[:]
        else:
            objects = objects[:]
            
        objects.reverse()
        
        result = []
        for i in objects:
            i.Apply(ctx)
            if ctx.in_fill(pixel[0],pixel[1]) or ctx.in_stroke(pixel[0],pixel[1]) :
                if returnList :
                    result.append(i)
                else:
                    return i
        if returnList :
            return result
        else:
            return None
            
    
    def Render(self,dc):
        self.Clip[2:] = list(dc.GetSizeTuple())
        ctx = ContextFromDC(dc)
        ctx.translate(-self.Clip[0], -self.Clip[1])
        ctx.scale(self.Zoom,self.Zoom)
        
        self.Border.Apply(ctx)
        self.DrawAll(ctx, self.Objects)
        self.DrawAll(ctx, self.ToolObjects)
        
    def GetRect(self, Objects ):
        if len(Objects)==0 :
            return Rectangle(0,0,0,0)
        
        path = []
        for i in Objects:
            for point in i.Path.Points:
                path.append(point[1])
                
        l,t = path[0]
        r,b = path[0]
        for i in path:
            if i[0]<l :
                l = i[0]
            if i[1]<t :
                t = i[1]
            if i[0]>r :
                r = i[0]
            if i[1]>b :
                b = i[1]
        return Rectangle(l,t,r-l,b-t)
        
    def DrawAll(self, ctx, list):
        for i in list:
            i.Apply(ctx)
        
    def SetMouse(self,position):
        self.Mouse = self.Pixel2Coord(position)
        
    def Pixel2Coord(self,pixel):
            return (int((pixel[0] + self.Clip[0])/self.Zoom),
                    int((pixel[1] + self.Clip[1])/self.Zoom))
          
    def ToData(self): pass
    def FromData(self, data): pass
    
    