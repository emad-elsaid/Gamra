'''
Created on Jun 10, 2010

@author: blaze
'''
from GUI.ToolBar.Tools import EditingTool
import cairo
class Select(EditingTool):
    '''
    a tool to select one or many items from canvas.
    '''
    
    def __init__(self):
        EditingTool.__init__(self,name='Select', icon='select.png',Priority=1000)
        
    def Activate(self,canvas):
        # after all reftesh the canvas
        self.Canvas = canvas
        self.CreateBoundary()
        EditingTool.Activate(self, canvas)
        
    def OnMouseLeftDown(self,event):
        selected = self.Canvas.Document.GetUnderPixel(self.Canvas.Document.Mouse)
        # check if there is something selected
        if( selected!=None ):
            
            # check if shift is down, that will add,remove element from selection
            if event.ShiftDown() :
                if( selected in self.Canvas.Document.SelectedObjects ):
                    self.Canvas.Document.SelectedObjects.remove(selected)
                else:
                    self.Canvas.Document.SelectedObjects.append(selected)
                    
            #if shift is not down, the selection will be only the object
            else:
                self.Canvas.Document.SelectedObjects = [selected]
                # if nothing clicked then clear the toolobjects and the selected objects
        else:
            self.Canvas.Document.ToolObjects = []
            self.Canvas.Document.SelectedObjects = []
        # after all reftesh the canvas
        self.CreateBoundary()
        EditingTool.OnMouseLeftDown(self, event)
        
    
    def OnKeyUp(self,event):
        self.CreateBoundary()
        EditingTool.OnMouseLeftDown(self, event)
    
    def CreateBoundary(self):
        # create the highlight rectangle around selected objects 
        highlight = self.Canvas.Document.GetRect(self.Canvas.Document.SelectedObjects)
        highlight.Stroke.Dash = [5,5]
        highlight.Fill.Color = (0,0,0,0)
        highlight.Antialiase = cairo.ANTIALIAS_NONE
        self.Canvas.Document.ToolObjects = [highlight]
        self.Canvas.Refresh()