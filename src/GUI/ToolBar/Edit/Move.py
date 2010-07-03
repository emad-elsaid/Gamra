'''
Created on July 2, 2010

@author: Ahmed Ghanem
'''
from GUI.ToolBar.Tools import EditingTool
import cairo
class Move(EditingTool):
	
   def __init__(self):
        EditingTool.__init__(self,name='Move', icon='move.png')
        #on activate the we get the selected objects onelt on the canavas
   def Activate(self,canvas):
        doc = canvas.Document
        doc.ToolObjects = doc.SelectedObjects          
        EditingTool.Activate(self, canvas)
        
   def OnMouseLeftDown(self,event):
        partSelected = self.Canvas.Document.GetUnderPixel(self.Canvas.Document.Mouse, objects=self.Canvas.Document.ToolObjects)
        if partSelected!=None :
            self.SelectedNode = partSelected
            self.startPosition = self.Canvas.Document.Mouse
        else:
            self.SelectedNode = None
            self.startPosition = None
        EditingTool.OnMouseLeftDown(self, event)
        
   def OnMouseMove(self,event):
        if event.Dragging() and event.LeftIsDown() and self.SelectedNode != None  :
            delta = [self.Canvas.Document.Mouse[0]-self.startPosition[0],
                     self.Canvas.Document.Mouse[1]-self.startPosition[1]]
                  #for each object move it's points
            for obj in self.Canvas.Document.SelectedObjects:
				for points in obj.Path.Points:
					points[1][0] += delta[0]
					points[1][1] += delta[1]
                
            self.startPosition = self.Canvas.Document.Mouse
            self.Canvas.Refresh() #refresh the canvas for each move
        EditingTool.OnMouseMove(self, event)
        
	
