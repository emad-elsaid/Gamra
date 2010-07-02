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
        
    def Activate(self,canvas):
        doc = canvas.Document
        if len(doc.SelectedObjects)>0 :
            rect = doc.GetRect(doc.SelectedObjects)
            rect.Stroke.Width = 0.5
            rect.Antialiase = cairo.ANTIALIAS_NONE
            rect.Fill.Color = (0,0,0,0)
            
            #control points
            self.lt = Document.ControlPoint(rect.Path.Points[0][1][0],rect.Path.Points[0][1][1])
            self.rt = Document.ControlPoint(rect.Path.Points[1][1][0],rect.Path.Points[1][1][1])
            self.rb = Document.ControlPoint(rect.Path.Points[2][1][0],rect.Path.Points[2][1][1])
            self.lb = Document.ControlPoint(rect.Path.Points[3][1][0],rect.Path.Points[3][1][1])
            
            doc.ToolObjects = [rect,self.lt,self.rt,self.rb,self.lb]
            
        EditingTool.Activate(self, canvas)