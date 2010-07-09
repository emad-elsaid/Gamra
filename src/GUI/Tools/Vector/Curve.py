'''
Created on Jul 7, 2010

@author: blaze
'''
from GUI.Tools.Tools import VectorTool
import Document

class Curve(VectorTool):
    '''
    Curve drawing tool
    '''

    def __init__(self):
        VectorTool.__init__(self, 'Curve', 'curve.png' )
    
    def Activate(self, canvas):
        VectorTool.Activate(self, canvas)
        self.Started = False 
        
    def OnMouseLeftDown(self,event):
        mouse = self.Canvas.Document.Mouse
        if not self.Started :
            self.Started = True
            self.Canvas.Document.ToolObjects = [Document.Rectangle(mouse[0]-3, mouse[1]-3, 6, 6)]
            obj = Document.Object()
            obj.Path.add1(mouse[0],mouse[1])
            self.Canvas.Document.Objects.append(obj)
        elif self.Canvas.Document.GetUnderPixel(mouse,objects=self.Canvas.Document.ToolObjects)!= None :
                self.Canvas.Document.Objects[-1].Path.Closed = True
                self.Canvas.Document.ToolObjects = []
                del self.Canvas.Document.Objects[-1].Path.Points[-1]
                self.Started = False
                
            
        self.Canvas.Refresh()
        VectorTool.OnMouseLeftDown(self, event)
    
    def OnMouseLeftUp(self, event):
        if self.Started :
            self.Canvas.Document.Objects[-1].Path.add1(self.Canvas.Document.Mouse[0],self.Canvas.Document.Mouse[1])
        VectorTool.OnMouseLeftUp(self, event)
        
    def OnMouseMove(self,event):
        if self.Started and not event.LeftIsDown() :
            self.Canvas.Document.Objects[-1].Path.Points[-1][1] = [self.Canvas.Document.Mouse[0],self.Canvas.Document.Mouse[1]]
            
        if event.Dragging() and event.LeftIsDown() :
            mouse = self.Canvas.Document.Mouse
            obj = self.Canvas.Document.Objects[-1]
            point = obj.Path.Points[-1]
            if not event.ShiftDown() :
                x = point[1][0]-(mouse[0]-point[1][0])
                y = point[1][1]-(mouse[1]-point[1][1])
                point[0] = [x,y]
            point[2] = list(mouse)
        
        self.Canvas.Refresh()    
        VectorTool.OnMouseMove(self, event)
        
    def Deactivate(self):
        if self.Started :
            del self.Canvas.Document.Objects[-1].Path.Points[-1]
            self.Canvas.Refresh()
            
        
        VectorTool.Deactivate(self)