from GUI.Tools.Tools import VectorTool

import Document

class Pencil(VectorTool):
    '''
    this tool for drawing line the selected objects
    '''
    def __init__ (self):
        VectorTool.__init__(self,name='Line',icon='pencil.png')
    def OnMouseLeftDown(self,event):
        
        self.StartPoint = self.Canvas.Document.Mouse
        obj = Document.Object()
        obj.Fill.Color = (0,0,0,0)
        obj.Path.add1(self.StartPoint[0],self.StartPoint[1])
        
        self.Canvas.Document.Objects.append(obj)
        self.Canvas.Document.SelectedObjects = [self.Canvas.Document.Objects[-1]]
        self.Canvas.Refresh()
        self.Counter = 0
        
        
    def OnMouseMove(self,event):
        if event.Dragging() and event.LeftIsDown() :
            self.Counter += 1
            if self.Counter>3 :
                obj = self.Canvas.Document.Objects[-1]
                obj.Path.add1(self.Canvas.Document.Mouse[0],self.Canvas.Document.Mouse[1])
                self.Counter = 0
                self.Canvas.Refresh()
            
        VectorTool.OnMouseMove(self,event)