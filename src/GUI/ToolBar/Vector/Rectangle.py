'''
Created on Jul 7, 2010

@author: blaze
'''
from GUI.ToolBar.Tools import VectorTool
import Document

class Rectangle(VectorTool):
    '''
    Rectangle drawing tool
    '''

    def __init__(self):
        VectorTool.__init__(self, 'Rectangle', 'rectangle.png' )
        
    def OnMouseLeftDown(self,event):
        obj = Document.Rectangle( self.Canvas.Document.Mouse[0],self.Canvas.Document.Mouse[1],0,0 )
        self.Canvas.Document.Objects.append(obj)
        self.Canvas.Refresh()
        VectorTool.OnMouseLeftDown(self, event)
    
    def OnMouseMove(self,event):
        if event.Dragging() and event.LeftIsDown() :
            mouse = self.Canvas.Document.Mouse
            self.Canvas.Document.Objects[-1].Path.Points[1][1][0] = mouse[0]
            self.Canvas.Document.Objects[-1].Path.Points[1][1][1] = mouse[1]
            self.Canvas.Refresh()
        VectorTool.OnMouseMove(self, event)