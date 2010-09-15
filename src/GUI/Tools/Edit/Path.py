'''
Created on Jul 21, 2010

@author: blaze
'''
from GUI.Tools.Tools import EditingTool
import Document
import cairo
import math


class Handler(Document.Object):
    def __init__(self, pointRef):
        Document.Object.__init__(self)
        self.Stroke.Color = (76.0/255.0, 158.0/255.0, 197.0/255.0, 1 )
        self.Ref = pointRef
        self.Antialias = cairo.ANTIALIAS_NONE
        
    def Apply(self,ctx):
        ctx.new_path()
        ctx.set_antialias(self.Antialias)
        ctx.arc(self.Ref[0],self.Ref[1],3,0,math.pi*2)
        self.Fill.Apply(ctx)
        self.Stroke.Apply(ctx,False)
        ctx.rectangle(self.Ref[0]-3,self.Ref[1]-3,6,6)
        
class Point(Document.Object):
    def __init__(self, pointRef):
        Document.Object.__init__(self)
        self.Stroke.Color = (76.0/255.0, 158.0/255.0, 197.0/255.0, 1 )
        self.Ref = [0,0]
        self.Point = pointRef
        self.Antialias = cairo.ANTIALIAS_NONE
        
    def Apply(self,ctx):
        for pair in self.Point :
            if pair!=None:
                pair[0]+=self.Ref[0]
                pair[1]+=self.Ref[1]
        self.Ref = [0,0]
                
        ctx.new_path()
        ctx.set_antialias(self.Antialias)
        ctx.rectangle(self.Point[1][0]-2,self.Point[1][1]-2,4,4)
        self.Fill.Apply(ctx)
        self.Stroke.Apply(ctx,False)
        ctx.rectangle(self.Point[1][0]-3,self.Point[1][1]-3,6,6)
                
class ControlLine(Document.Object):
    def __init__(self, p1,p2):
        Document.Object.__init__(self)
        self.Stroke.Color = (76.0/255.0, 158.0/255.0, 197.0/255.0, 1 )
        self.p1 = p1
        self.p2 = p2
        
    def Apply(self,ctx):
        ctx.new_path()
        ctx.set_antialias(self.Antialias)
        ctx.move_to(self.p1[0],self.p1[1])
        ctx.line_to(self.p2[0],self.p2[1])
        self.Fill.Apply(ctx)
        self.Stroke.Apply(ctx,False)

class Path(EditingTool):
    '''
    Path Editing tool
    '''


    def __init__(self):
        EditingTool.__init__(self, 'Path', 'path.png', 999)
        self.startPosition = None
    
    def Activate(self,canvas):
        EditingTool.Activate(self, canvas)
        if len(self.Canvas.Document.SelectedObjects)==0 :
            return
        points = self.Canvas.Document.SelectedObjects[0].Path.Points
        for p in points :
            if p[0]!=None :
                    self.Canvas.Document.ToolObjects.append(Handler(p[0]))
                    self.Canvas.Document.ToolObjects.append(ControlLine(p[0],p[1]))
            self.Canvas.Document.ToolObjects.append(Point(p))
            if p[2]!=None :
                    self.Canvas.Document.ToolObjects.append(Handler(p[2]))
                    self.Canvas.Document.ToolObjects.append(ControlLine(p[2],p[1]))
                    
        self.Canvas.Refresh()
        
    def OnMouseLeftDown(self,event):
        partSelected = self.Canvas.Document.GetUnderPixel(self.Canvas.Document.Mouse,
                                                          objects=self.Canvas.Document.ToolObjects)
        # if something under the mouse then start drag operation
        # by putting start position in the tool.startposition
        if partSelected!=None and partSelected.__class__!=ControlLine :
            self.startPosition = self.Canvas.Document.Mouse
            self.SelectedNode = partSelected 
        else:
            self.startPosition = None
            
        EditingTool.OnMouseLeftDown(self, event)
        
    def OnMouseMove(self,event):
        if self.startPosition!=None :
            delta = [self.Canvas.Document.Mouse[0]-self.startPosition[0],
                         self.Canvas.Document.Mouse[1]-self.startPosition[1]]
                
            self.SelectedNode.Ref[0] += delta[0]
            self.SelectedNode.Ref[1] += delta[1]
    
            self.startPosition = self.Canvas.Document.Mouse
            self.Canvas.Refresh()
        EditingTool.OnMouseMove(self, event)
        
    def OnMouseLeftUp(self,event):
        self.startPosition = None
        EditingTool.OnMouseLeftUp(self, event)