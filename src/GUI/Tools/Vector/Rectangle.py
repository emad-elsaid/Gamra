'''
Created on Jul 7, 2010

@author: blaze
'''
from GUI.Tools.Tools import VectorTool
import Document

class Rectangle(VectorTool):
    '''
    Rectangle drawing tool
    '''

    def __init__(self):
        VectorTool.__init__(self, 'Rectangle', 'rectangle.png' )
        
    def OnMouseLeftDown(self,event):
        obj = Document.Object()
        opath = obj.Path
        x,y = self.Canvas.Document.Mouse 
        opath.add1(x, y)
        opath.add1(x, y)
        opath.add1(x, y)
        opath.add1(x, y)
        opath.Closed = True
        
        self.Canvas.Document.Objects.append(obj)
        self.Canvas.Refresh()
        VectorTool.OnMouseLeftDown(self, event)
    
    def OnMouseMove(self,event):
        if event.Dragging() and event.LeftIsDown() :
            x,y = self.Canvas.Document.Mouse
            points = self.Canvas.Document.Objects[-1].Path.Points 
            points[1][1][0] = x
            points[2][1][0] = x
            points[2][1][1] = y
            points[3][1][1] = y 
            self.Canvas.Refresh()
        VectorTool.OnMouseMove(self, event)