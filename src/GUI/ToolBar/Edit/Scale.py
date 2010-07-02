'''
Created on Jul 2, 2010

@author: blaze
'''
from GUI.ToolBar.Tools import EditingTool
import cairo
import Document

class Scale(EditingTool):
    '''
    a Tool that scales the selected objects
    '''


    def __init__(self):
        EditingTool.__init__(self,name='Scale', icon='scale.png')
        self.SelectedNode = None
        
    def Activate(self,canvas):
        doc = canvas.Document
        if len(doc.SelectedObjects)>0 :
            rect = doc.GetRect(doc.SelectedObjects)
            rect.Stroke.Width = 1
            rect.Antialiase = cairo.ANTIALIAS_NONE
            rect.Fill.Color = (0,0,0,0)
            rect.Stroke.Dash = [1,1]
            
            #control points
            self.lt = Document.ControlPoint(rect.Path.Points[0][1][0],rect.Path.Points[0][1][1])
            self.rt = Document.ControlPoint(rect.Path.Points[1][1][0],rect.Path.Points[1][1][1])
            self.rb = Document.ControlPoint(rect.Path.Points[2][1][0],rect.Path.Points[2][1][1])
            self.lb = Document.ControlPoint(rect.Path.Points[3][1][0],rect.Path.Points[3][1][1])
            self.Rect = rect
            
            doc.ToolObjects = [rect,self.lt,self.rt,self.rb,self.lb]
            
        EditingTool.Activate(self, canvas)
        
    def OnMouseLeftDown(self,event):
        underMouse = self.Canvas.Document.GetUnderPixel(self.Canvas.Document.Mouse,
                                                        objects=self.Canvas.Document.ToolObjects[1:])
        if underMouse!=None :
            self.SelectedNode = underMouse
            self.startPosition = self.Canvas.Document.Mouse
            if underMouse==self.rb :
                self.Origin = self.Rect.Path.Points[0][1]
            if underMouse==self.lt :
                self.Origin = self.Rect.Path.Points[2][1]
            if underMouse==self.rt :
                self.Origin = self.Rect.Path.Points[3][1]
            if underMouse==self.lb :
                self.Origin = self.Rect.Path.Points[1][1]
        else:
            self.SelectedNode = None
            self.startPosition = None
        EditingTool.OnMouseLeftDown(self, event)
        
    def OnMouseMove(self,event):
        if event.Dragging() and event.LeftIsDown() and self.SelectedNode != None  :
            if self.Origin[0]-self.startPosition[0] != 0 and self.Origin[1]-self.startPosition[1] != 0:
                factor = [float(self.Origin[0]-self.Canvas.Document.Mouse[0])/
                               float(self.Origin[0]-self.startPosition[0]),
                               float(self.Origin[1]-self.Canvas.Document.Mouse[1])/
                               float(self.Origin[1]-self.startPosition[1])]
            
                for i in self.Canvas.Document.ToolObjects :
                    for point in i.Path.Points :
                        point[1][0] = float(point[1][0]-self.Origin[0])*factor[0]+self.Origin[0]
                        point[1][1] = float(point[1][1]-self.Origin[1])*factor[1]+self.Origin[1]
                    
                for i in self.Canvas.Document.SelectedObjects :
                    for point in i.Path.Points :
                        if point[0] != None :
                            point[0][0] = (point[1][0]-self.Origin[0])*factor[0]+self.Origin[0]
                            point[0][1] = (point[1][1]-self.Origin[1])*factor[1]+self.Origin[1]
                        point[1][0] = (point[1][0]-self.Origin[0])*factor[0]+self.Origin[0]
                        point[1][1] = (point[1][1]-self.Origin[1])*factor[1]+self.Origin[1]
                        if point[2] != None :
                            point[2][0] = (point[1][0]-self.Origin[0])*factor[0]+self.Origin[0]
                            point[2][1] = (point[1][1]-self.Origin[1])*factor[1]+self.Origin[1]
                        
                self.startPosition = self.Canvas.Document.Mouse
                self.Canvas.Refresh()
        EditingTool.OnMouseMove(self, event)
        
        