'''
Created on Jun 10, 2010

@author: blaze
'''
from GUI.Tools.Tools import EditingTool
import cairo
import wx
import Document


class Select(EditingTool):
    '''
    a tool to select one or many items from canvas.
    '''
    
    def __init__(self):
        EditingTool.__init__(self,name='Select', icon='select.png',Priority=1000)
        
    def Activate(self,canvas):
        EditingTool.Activate(self, canvas)
        self.Highlight()
        
    def Highlight(self):
        # create the highlight rectangle around selected objects 
        highlight = self.Canvas.Document.GetRect(self.Canvas.Document.SelectedObjects)
        highlight.Stroke.Dash = [5,5]
        highlight.Fill.Color = (0,0,0,0)
        highlight.Antialiase = cairo.ANTIALIAS_NONE
        self.Canvas.Document.ToolObjects = [highlight]
        self.Canvas.Refresh()
        
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
            elif selected not in self.Canvas.Document.SelectedObjects :
                self.Canvas.Document.SelectedObjects = [selected]
            
        # if nothing clicked then clear the toolobjects and the selected objects
        else:
            self.Canvas.Document.ToolObjects = []
            self.Canvas.Document.SelectedObjects = []
        
        
        # the moving starting part
        partSelected = self.Canvas.Document.GetUnderPixel(self.Canvas.Document.Mouse, objects=self.Canvas.Document.SelectedObjects)
        # if something under the mouse then start drag operation
        # by putting start position in the tool.startposition
        if partSelected!=None :
            self.startPosition = self.Canvas.Document.Mouse
            
        else:
            self.startPosition = None    
        # after all reftesh the canvas
        self.Highlight()
        event.Skip()
    
    
    def OnMouseMove(self,event):
        if event.Dragging() and event.LeftIsDown() and self.startPosition!=None :
            self.Canvas.Document.ToolObjects = []
            
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
            self.Canvas.Refresh() #refresh the canvas for each move
        EditingTool.OnMouseMove(self, event)
        
    def OnMouseLeftUp(self, event):
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
        self.Canvas.Refresh()
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
    
