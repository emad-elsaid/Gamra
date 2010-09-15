from GUI.Tools.Tools import VectorTool

import Document

class Line(VectorTool):
    '''
    this tool for drawing line the selected objects
    '''
    def __init__ (self):
        VectorTool.__init__(self,name='Line',icon='line.png')
    def OnMouseLeftDown(self,event):
        
        self.StartPoint = self.Canvas.Document.Mouse
        obj = Document.Object()
        obj.Path.add1(self.StartPoint[0],self.StartPoint[1])
        obj.Path.add1(self.StartPoint[0],self.StartPoint[1])
        
        self.Canvas.Document.Objects.append(obj)
        self.Canvas.Document.SelectedObjects = [self.Canvas.Document.Objects[-1]]
        self.Canvas.Refresh()
        
        
    def OnMouseMove(self,event):
        if event.Dragging() and event.LeftIsDown() :
            obj = self.Canvas.Document.Objects[-1]
            obj.Path.Points[1][1][0] = self.Canvas.Document.Mouse[0]
            obj.Path.Points[1][1][1] = self.Canvas.Document.Mouse[1]
            self.Canvas.Refresh()
            
        VectorTool.OnMouseMove(self,event)