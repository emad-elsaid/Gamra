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
        
        # get current document to process
        doc = canvas.Document
        
        # if something selected then make 
        # the boundary and control points
        if len(doc.SelectedObjects)>0 :
            # create the boundary box
            rect = doc.GetRect(doc.SelectedObjects)
            rect.Stroke.Width = 1
            rect.Antialiase = cairo.ANTIALIAS_NONE
            rect.Fill.Color = (0,0,0,0)
            rect.Stroke.Dash = [1,1]
            
            #control points
            # l,r,t,b : left,right,top,bottom respectvly
            self.lt = Document.ControlPoint(rect.Path.Points[0][1][0],rect.Path.Points[0][1][1])
            self.rt = Document.ControlPoint(rect.Path.Points[2][1][0],rect.Path.Points[0][1][1])
            self.rb = Document.ControlPoint(rect.Path.Points[2][1][0],rect.Path.Points[2][1][1])
            self.lb = Document.ControlPoint(rect.Path.Points[0][1][0],rect.Path.Points[2][1][1])
            self.t  = Document.ControlPoint((rect.Path.Points[0][1][0]+rect.Path.Points[2][1][0])/2.0
                                            ,rect.Path.Points[0][1][1])
            self.b  = Document.ControlPoint((rect.Path.Points[0][1][0]+rect.Path.Points[2][1][0])/2.0
                                            ,rect.Path.Points[2][1][1])
            self.l  = Document.ControlPoint(rect.Path.Points[0][1][0],
                                            (rect.Path.Points[0][1][1]+rect.Path.Points[2][1][1])/2.0)
            self.r  = Document.ControlPoint(rect.Path.Points[2][1][0],
                                            (rect.Path.Points[0][1][1]+rect.Path.Points[2][1][1])/2.0)
            self.Rect = rect
            
            # add control points to the toolObjects list 
            # to render it above the canvas
            doc.ToolObjects = [rect,self.lt,self.rt,
                               self.rb,self.lb, 
                               self.t, self.b,
                               self.l,self.r]
            
        EditingTool.Activate(self, canvas)
        
    def OnMouseLeftDown(self,event):
        
        # get the selected Node from the toolObjects
        underMouse = self.Canvas.Document.GetUnderPixel(self.Canvas.Document.Mouse,
                                                        objects=self.Canvas.Document.ToolObjects[1:])
        
        # if something selected set the selected (to enable dragging
        if underMouse!=None :
            #set teh node
            self.SelectedNode = underMouse
            # and the current position of mouse
            self.startPosition = self.Canvas.Document.Mouse
            # then set the origin point accoirding to the selected corner
            # i set the origin the opposite point of the selected
            if underMouse==self.rb :
                self.Origin = self.lt.Path.Points[0][1]
            if underMouse==self.lt :
                self.Origin = self.rb.Path.Points[0][1]
            if underMouse==self.rt :
                self.Origin = self.lb.Path.Points[0][1]
            if underMouse==self.lb :
                self.Origin = self.rt.Path.Points[0][1]
            if underMouse==self.t :
                self.Origin = self.b.Path.Points[0][1]
            if underMouse==self.b :
                self.Origin = self.t.Path.Points[0][1]
            if underMouse==self.l :
                self.Origin = self.r.Path.Points[0][1]
            if underMouse==self.r :
                self.Origin = self.l.Path.Points[0][1]
        # if nothing selected then clear the selected node and the position
        # just in case
        else:
            self.SelectedNode = None
            self.startPosition = None
        # we have to process the parent event to complete the application
        # default behaviour
        EditingTool.OnMouseLeftDown(self, event)
        
    def OnMouseMove(self,event):
        if event.Dragging() and event.LeftIsDown() and self.SelectedNode != None  :
            #creating the scale factor
            factor = [1,1]
            
            # check the delta if it's not zero then it's safe for division
            if self.Origin[0]-self.startPosition[0] != 0 :
                factor[0] = float(self.Origin[0]-self.Canvas.Document.Mouse[0])/float(self.Origin[0]-self.startPosition[0])
                
            if self.Origin[1]-self.startPosition[1] != 0:
                factor[1] = float(self.Origin[1]-self.Canvas.Document.Mouse[1])/float(self.Origin[1]-self.startPosition[1])
            
            # if the scale from one side only then we
            # have to make the other axis does'nt resize
            # for example if the top middle node is moving then we'll not
            # resize the width we'll only resize height 
            if self.SelectedNode == self.t or self.SelectedNode == self.b : factor[0] = 1
            if self.SelectedNode == self.l or self.SelectedNode == self.r : factor[1] = 1
            
            # resize the tool objects (boundary and nodes)
            # some Math here to transform according to some origin point
            for i in self.Canvas.Document.ToolObjects :
                for point in i.Path.Points :
                    point[1][0] = float(point[1][0]-self.Origin[0])*factor[0]+self.Origin[0]
                    point[1][1] = float(point[1][1]-self.Origin[1])*factor[1]+self.Origin[1]
            
            # resize all selected objects by factor according to origin    
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
             
            # update current mouse position 
            self.startPosition = self.Canvas.Document.Mouse
            # update canvas view
            self.Canvas.Refresh()
        EditingTool.OnMouseMove(self, event)
        
        