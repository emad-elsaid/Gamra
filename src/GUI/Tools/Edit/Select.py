'''
Created on Jun 10, 2010

@author: blaze
'''
from GUI.Tools.Tools import EditingTool
import cairo
import wx
import Document
import math


class Select(EditingTool):
    '''
    a tool to select one or many items from canvas.
    '''
    
    def __init__(self):
        EditingTool.__init__(self,name='Select', icon='select.png',Priority=1000)
        self.Scale = False
        self.Rotate = False
        self.Shear = False
        self.RotationOrigin = None
        self.CurrentAngle = None
        self.startPosition = None
        
    def Activate(self,canvas):
        EditingTool.Activate(self, canvas)
        self.Highlight()
        
    def Highlight(self):
        # create the highlight rectangle around selected objects
        doc = self.Canvas.Document
        
        # if something selected then make 
        # the boundary and control points
        if len(doc.SelectedObjects)>0 :
            # create the boundary box
            rect = doc.GetRect(doc.SelectedObjects)
            rect.Stroke.Width = 1
            rect.Antialias = cairo.ANTIALIAS_NONE
            rect.Fill.Color = (0,0,0,0)
            rect.Stroke.Dash = [3,2]
            
            #control points
            # l,r,t,b : left,right,top,bottom respectively
            self.lt = Document.ControlPoint(rect.Path.Points[0][1][0],rect.Path.Points[0][1][1])
            self.rt = Document.ControlPoint(rect.Path.Points[1][1][0],rect.Path.Points[0][1][1])
            self.rb = Document.ControlPoint(rect.Path.Points[1][1][0],rect.Path.Points[1][1][1])
            self.lb = Document.ControlPoint(rect.Path.Points[0][1][0],rect.Path.Points[1][1][1])
            self.t  = Document.ControlPoint((rect.Path.Points[0][1][0]+rect.Path.Points[1][1][0])/2.0
                                            ,rect.Path.Points[0][1][1])
            self.b  = Document.ControlPoint((rect.Path.Points[0][1][0]+rect.Path.Points[1][1][0])/2.0
                                            ,rect.Path.Points[1][1][1])
            self.l  = Document.ControlPoint(rect.Path.Points[0][1][0],
                                            (rect.Path.Points[0][1][1]+rect.Path.Points[1][1][1])/2.0)
            self.r  = Document.ControlPoint(rect.Path.Points[1][1][0],
                                            (rect.Path.Points[0][1][1]+rect.Path.Points[1][1][1])/2.0)
            
            # rotate controls
            self.rlt = Document.ControlPoint(rect.Path.Points[0][1][0]-5,rect.Path.Points[0][1][1]-5)
            self.rrt = Document.ControlPoint(rect.Path.Points[1][1][0]+5,rect.Path.Points[0][1][1]-5)
            self.rrb = Document.ControlPoint(rect.Path.Points[1][1][0]+5,rect.Path.Points[1][1][1]+5)
            self.rlb = Document.ControlPoint(rect.Path.Points[0][1][0]-5,rect.Path.Points[1][1][1]+5)
            
            # shear controls
            self.sl = Document.ControlPoint(rect.Path.Points[0][1][0]-6,
                                            (rect.Path.Points[0][1][1]+rect.Path.Points[1][1][1])/2.0)
            self.sr = Document.ControlPoint(rect.Path.Points[1][1][0]+6,
                                            (rect.Path.Points[0][1][1]+rect.Path.Points[1][1][1])/2.0)
            self.st = Document.ControlPoint((rect.Path.Points[0][1][0]+rect.Path.Points[1][1][0])/2.0
                                            ,rect.Path.Points[0][1][1]-6)
            self.sb = Document.ControlPoint((rect.Path.Points[0][1][0]+rect.Path.Points[1][1][0])/2.0
                                            ,rect.Path.Points[1][1][1]+6)
            
            self.Rect = rect
            
            # add control points to the toolObjects list 
            # to render it above the canvas
            doc.ToolObjects = [rect,self.lt,self.rt,
                               self.rb,self.lb, 
                               self.t, self.b,
                               self.l,self.r,
                               self.rlt,self.rrt,
                               self.rrb,self.rlb,
                               self.sl,self.sr,self.st,self.sb]
        else:
            self.Canvas.Document.ToolObjects = []
        self.Canvas.Refresh()
        
    def OnMouseLeftDown(self,event): 
        if (not self.InitiateScale()) and (not self.InitiateRotation()) and (not self.InitiateShear()) :
            self.InitiateSelecting(event)
            self.InitiateMove()
        self.Canvas.Document.ToolObjects = []
        EditingTool.OnMouseLeftDown(self, event)
    
    def InitiateScale(self):
        # get the selected Node from the toolObjects
        underMouse = self.Canvas.Document.GetUnderPixel(self.Canvas.Document.Mouse,
                                                        objects=self.Canvas.Document.ToolObjects[1:])
        # if something selected set the selected (to enable dragging)
        if underMouse!=None and underMouse in [self.lt,self.rt,self.rb,self.lb, self.t, self.b,self.l,self.r] :
            #set the node
            self.Scale = True
            self.SelectedNode = underMouse
            # and the current position of mouse
            self.ScaleStartPosition = self.Canvas.Document.Mouse
            # then set the origin point according to the selected corner
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
                
            self.Canvas.Document.ToolObjects = []
            self.Canvas.Refresh()
            return True
        return False
    
    def InitiateRotation(self):
        # get the selected Node from the toolObjects
        underMouse = self.Canvas.Document.GetUnderPixel(self.Canvas.Document.Mouse,
                                                        objects=self.Canvas.Document.ToolObjects[1:])
        # if something selected set the selected (to enable dragging)
        if underMouse!=None and underMouse in [self.rlt,self.rrt,self.rrb,self.rlb] :
            #set the node
            self.Rotate = True
            
            self.Canvas.Document.ToolObjects = []
            self.Canvas.Refresh()
            return True
        return False
    
    def InitiateShear(self):
        # get the selected Node from the toolObjects
        underMouse = self.Canvas.Document.GetUnderPixel(self.Canvas.Document.Mouse,
                                                        objects=self.Canvas.Document.ToolObjects[1:])
        # if something selected set the selected (to enable dragging)
        if underMouse!=None and underMouse in [self.sl,self.sr,self.st,self.sb] :
            self.ShearStart = self.Canvas.Document.Mouse
            if underMouse == self.st :
                self.Shear = self.sb
            if underMouse == self.sb :
                self.Shear = self.st
            if underMouse == self.sl :
                self.Shear = self.sr
            if underMouse == self.sr :
                self.Shear = self.sl
            
            self.Canvas.Document.ToolObjects = []
            self.Canvas.Refresh()
            return True
        return False
    
    def InitiateSelecting(self, event):
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
            elif selected not in self.Canvas.Document.SelectedObjects :
                self.Canvas.Document.SelectedObjects = [selected]
            
        # if nothing clicked then clear the tool objects and the selected objects
        else:
            self.Canvas.Document.SelectedObjects = []
            
        self.Highlight()
    
    def InitiateMove(self):
        # the moving starting part
        partSelected = self.Canvas.Document.GetUnderPixel(self.Canvas.Document.Mouse,
                                                          objects=self.Canvas.Document.SelectedObjects)
        # if something under the mouse then start drag operation
        # by putting start position in the tool.startposition
        if partSelected!=None :
            self.startPosition = self.Canvas.Document.Mouse
        else:
            self.startPosition = None
                    
    def OnMouseMove(self,event):
        if event.Dragging() and event.LeftIsDown() :
            if self.startPosition != None :
                self.MoveAction(event) 
            elif self.Scale :
                self.ScaleAction(event)
            elif self.Rotate :
                self.RotateAction(event)
            elif self.Shear :
                self.ShearAction(event)
            
            self.Canvas.Refresh() #refresh the canvas for each move
        EditingTool.OnMouseMove(self, event)
    
    def MoveAction(self, event):
        delta = [self.Canvas.Document.Mouse[0]-self.startPosition[0],
                     self.Canvas.Document.Mouse[1]-self.startPosition[1]]
            
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
        
    def ScaleAction(self,event):
        #creating the scale factor
        factor = [1,1]
        
        # check the delta if it's not zero then it's safe for division
        if self.Origin[0]-self.ScaleStartPosition[0] != 0 and self.Canvas.Document.Mouse[0]!=self.Origin[0]:
            factor[0] = float(self.Origin[0]-self.Canvas.Document.Mouse[0])/float(self.Origin[0]-self.ScaleStartPosition[0])
            
        if self.Origin[1]-self.ScaleStartPosition[1] != 0 and self.Canvas.Document.Mouse[1]!=self.Origin[1]:
            factor[1] = float(self.Origin[1]-self.Canvas.Document.Mouse[1])/float(self.Origin[1]-self.ScaleStartPosition[1])
        
        # if the scale from one side only then we
        # have to make the other axis does'nt resize
        # for example if the top middle node is moving then we'll not
        # resize the width we'll only resize height 
        if self.SelectedNode == self.t or self.SelectedNode == self.b : factor[0] = 1
        if self.SelectedNode == self.l or self.SelectedNode == self.r : factor[1] = 1
        
        # resize all selected objects by factor according to origin    
        for i in self.Canvas.Document.SelectedObjects :
            for point in i.Path.Points :
                if point[0] != None :
                    point[0][0] = (point[0][0]-self.Origin[0])*factor[0]+self.Origin[0]
                    point[0][1] = (point[0][1]-self.Origin[1])*factor[1]+self.Origin[1]
                point[1][0] = (point[1][0]-self.Origin[0])*factor[0]+self.Origin[0]
                point[1][1] = (point[1][1]-self.Origin[1])*factor[1]+self.Origin[1]
                if point[2] != None :
                    point[2][0] = (point[2][0]-self.Origin[0])*factor[0]+self.Origin[0]
                    point[2][1] = (point[2][1]-self.Origin[1])*factor[1]+self.Origin[1]
         
        '''
        update current mouse position
        that method of replacing the new position
        will fix the bug of 0 width/height freezing
        the problem was if i resize objects to 0 they'll 
        be frozen and doesn't resize any more
        '''
        newpos = list(self.ScaleStartPosition)
        if self.Canvas.Document.Mouse[0]!=self.Origin[0] :
            newpos[0] = self.Canvas.Document.Mouse[0]
            
        if self.Canvas.Document.Mouse[1]!=self.Origin[1] :
            newpos[1] = self.Canvas.Document.Mouse[1]
            
        self.ScaleStartPosition = tuple(newpos)
     
    
    def RotateAction(self,event):
        if  event.LeftIsDown() :
        
            #calculating the current angle
            if self.RotationOrigin == None :
                rect = self.Canvas.Document.GetRect(self.Canvas.Document.SelectedObjects)
                rectPoints = rect.Path.Points
                self.RotationOrigin = ((rectPoints[1][1][0]+rectPoints[0][1][0])/2.0,
                          (rectPoints[1][1][1]+rectPoints[0][1][1])/2.0)
                self.Canvas.Document.ToolObjects = [Document.Rectangle(self.RotationOrigin[0]-1,self.RotationOrigin[1]-1,2,2)]
                
            mouse = self.Canvas.Document.Mouse
            currentAngle = math.atan2( self.RotationOrigin[1]-mouse[1], mouse[0]-self.RotationOrigin[0])
            
            if self.CurrentAngle == None :
                self.CurrentAngle = currentAngle
                
            else:
                diff = self.CurrentAngle-currentAngle
                sin = math.sin(diff)
                cos = math.cos(diff)
                    
                for obj in self.Canvas.Document.SelectedObjects :
                    for point in obj.Path.Points :
                        for pair in point :
                            if pair != None :
                                pair[0] -= self.RotationOrigin[0]
                                pair[1] -= self.RotationOrigin[1]
                                x,y = pair
                                pair[0] = x*cos-y*sin+self.RotationOrigin[0]
                                pair[1] = x*sin+y*cos+self.RotationOrigin[1] 
                   
                self.CurrentAngle = currentAngle
    
    def ShearAction(self, event):
        delta = [self.Canvas.Document.Mouse[0]-self.ShearStart[0],
                     self.Canvas.Document.Mouse[1]-self.ShearStart[1]]
            
        if self.Shear==self.st or self.Shear==self.sb :
            oy = self.Shear.Path.Points[0][1][1]
            for obj in self.Canvas.Document.SelectedObjects:
                for points in obj.Path.Points:
                    if points[0]!=None :
                        points[0][0] = points[0][0]-delta[0]*(points[0][1]-oy)
                    points[1][0] = delta[0]*(points[1][1]-oy)
                    if points[2]!=None :
                        points[2][0] = delta[0]*(points[2][1]-oy)
                        
        self.ShearStart = self.Canvas.Document.Mouse
                       
    def OnMouseLeftUp(self, event):
        
        self.startPosition = None
        
        self.Scale = False
        self.ScaleStartPosition = None
        
        self.Rotate = False
        self.RotationOrigin = None
        self.CurrentAngle = None
        
        self.Shear = False
        
        self.Highlight()
        EditingTool.OnMouseLeftUp(self, event)
    
    def OnKeyDown(self,event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_PAGEUP or keycode == wx.WXK_NUMPAD_PAGEUP:
            self.OnPageUp()
        
        elif keycode == wx.WXK_PAGEDOWN or keycode == wx.WXK_NUMPAD_PAGEDOWN:
            self.OnPageDown()
        
        elif keycode == wx.WXK_HOME or keycode == wx.WXK_NUMPAD_HOME:
            self.OnHome()
            
        elif keycode == wx.WXK_END or keycode == wx.WXK_NUMPAD_END:
            self.OnEnd()
        
        elif keycode == wx.WXK_DELETE or keycode == wx.WXK_NUMPAD_DELETE:
            for SelectedObject in self.Canvas.Document.SelectedObjects:
                self.Canvas.Document.Objects.remove(SelectedObject)
            del self.Canvas.Document.SelectedObjects[:]
        
        self.Highlight()
        EditingTool.OnKeyDown(self, event)    
        
    def OnPageUp(self):
        for SelectedObject in self.Canvas.Document.SelectedObjects:
            if SelectedObject == self.Canvas.Document.Objects[-1]:
                return

        elements = [ (self.Canvas.Document.Objects.index(i),i) for i in self.Canvas.Document.SelectedObjects ]
        elements.sort(reverse=True)
        
        for index,SelectedObject in elements:
            self.Canvas.Document.Objects.remove(SelectedObject)
            self.Canvas.Document.Objects.insert(index+1, SelectedObject)
        self.Canvas.Refresh()
            
    def OnPageDown(self):
        for SelectedObject in self.Canvas.Document.SelectedObjects:
            if SelectedObject == self.Canvas.Document.Objects[0]:
                return
                
        elements = [ (self.Canvas.Document.Objects.index(i),i) for i in self.Canvas.Document.SelectedObjects ]
        elements.sort()
        
        for index,SelectedObject in elements:
            self.Canvas.Document.Objects.remove(SelectedObject)
            self.Canvas.Document.Objects.insert(index-1, SelectedObject)
        self.Canvas.Refresh()
        
    def OnHome(self):
        for SelectedObject in self.Canvas.Document.SelectedObjects:
            if SelectedObject == self.Canvas.Document.Objects[-1]:
                return
        
        elements = [ (self.Canvas.Document.Objects.index(i),i) for i in self.Canvas.Document.SelectedObjects ]
        elements.sort()
            
        for index,SelectedObject in elements:
            self.Canvas.Document.Objects.remove(SelectedObject)
            self.Canvas.Document.Objects.append(SelectedObject)
        self.Canvas.Refresh()
     
    def OnEnd(self):
        for SelectedObject in self.Canvas.Document.SelectedObjects:
            if SelectedObject == self.Canvas.Document.Objects[0]:
                return     
        
        elements = [ (self.Canvas.Document.Objects.index(i),i) for i in self.Canvas.Document.SelectedObjects ]
        elements.sort(reverse=True)
            
        for index,SelectedObject in elements:
            self.Canvas.Document.Objects.remove(SelectedObject)
            self.Canvas.Document.Objects.insert(0,SelectedObject)
        self.Canvas.Refresh()   
    
