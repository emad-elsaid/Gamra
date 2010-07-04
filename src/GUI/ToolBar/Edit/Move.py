'''
Created on July 2, 2010

@author: Ahmed Ghanem
'''
from GUI.ToolBar.Tools import EditingTool
import cairo

class Move(EditingTool):
    '''
    this tool for moving the selected objects
    '''
    
    def __init__(self):
        EditingTool.__init__(self,name='Move', icon='move.png')

    #on activate the we get the selected objects onelt on the canavas
    def Activate(self,canvas):
       
           # Create the boundary box
           if len(canvas.Document.SelectedObjects)>0 :
               rect = canvas.Document.GetRect(canvas.Document.SelectedObjects)
               rect.Antialiase = cairo.ANTIALIAS_NONE
               rect.Fill.Color = (0,0,0,0)
               rect.Stroke.Dash = [1,1]
               # make it the only tools objects in canvas
               # tool objects are rendered over the canvas
               canvas.Document.ToolObjects = [rect]
           EditingTool.Activate(self, canvas)
        

    def OnMouseLeftDown(self,event):
    	# check if something from the selected objects is under the mouse
    	partSelected = self.Canvas.Document.GetUnderPixel(self.Canvas.Document.Mouse, objects=self.Canvas.Document.SelectedObjects)
        
        # if something under the mouse then start drag operation
        # by putting start position in the tool.startposition
        if partSelected!=None :
            self.startPosition = self.Canvas.Document.Mouse
            
        else:
            self.startPosition = None
            
        EditingTool.OnMouseLeftDown(self, event)
        
        

    def OnMouseMove(self,event):
        if event.Dragging() and event.LeftIsDown() and self.startPosition!=None :
            delta = [self.Canvas.Document.Mouse[0]-self.startPosition[0],
                     self.Canvas.Document.Mouse[1]-self.startPosition[1]]
            
            # move  the boundary box
            for points in self.Canvas.Document.ToolObjects[0].Path.Points:
                    points[1][0] += delta[0]
                    points[1][1] += delta[1]
                    
            #for each object move it's points
            for obj in self.Canvas.Document.SelectedObjects:
                for points in obj.Path.Points:
                    if points[0]!=None :
                        points[0][0] += delta[0]
                        points[0][1] += delta[1]
                    points[1][0] += delta[0]
                    points[1][1] += delta[1]
                    if points[2]!=None :
                        points[2][0] += delta[0]
                        points[2][1] += delta[1]
                
            self.startPosition = self.Canvas.Document.Mouse
            self.Canvas.Refresh() #refresh the canvas for each move
        EditingTool.OnMouseMove(self, event)
        
    
