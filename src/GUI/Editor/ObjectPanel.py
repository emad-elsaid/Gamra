from Generic import Generic
import wx


class ObjectPanel(Generic):
    def __init__(self,parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize ):
        
        Generic.__init__(self, parent, id, pos, size,"data/icons/photo.png", Priority=1000)
        
        self.rightSizer = wx.BoxSizer(wx.VERTICAL)
        
        self.ObjectName = wx.StaticText(self)
        self.rightSizer.Add(self.ObjectName,0, wx.ALIGN_TOP | wx.ALIGN_LEFT)
        
        g = wx.FlexGridSizer(2,4,3,3)
        s1 = wx.StaticText(self,-1,"X")
        self.x = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER)
        
        s2 = wx.StaticText(self,-1,"Y")
        self.y = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER)
        
        
        s3 = wx.StaticText(self,-1,"W")
        self.w = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER)
        
        
        s4 = wx.StaticText(self,-1,"H")
        self.h = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER)
        
        
        g.Add(s1)
        g.Add(self.x)
        g.Add(s2)
        g.Add(self.y)
        g.Add(s3)
        g.Add(self.w)
        g.Add(s4)
        g.Add(self.h)
        
        self.mainSizer.Add(self.rightSizer, 0)
        self.rightSizer.Add(g)
        self.mainSizer.SetSizeHints(self)
        
    def Activate(self,canvas):
        if len(canvas.Document.SelectedObjects)==1 :
            rect = canvas.Document.GetRect(canvas.Document.SelectedObjects)
            self.w.ChangeValue("%s" %(rect.Path.Points[1][1][0]-rect.Path.Points[0][1][0]))
            self.h.ChangeValue("%s" %(rect.Path.Points[1][1][1]-rect.Path.Points[0][1][1]))
            self.x.ChangeValue("%s" %(rect.Path.Points[0][1][0]))
            self.y.ChangeValue("%s" %(rect.Path.Points[0][1][1]))
            
            self.x.Bind(wx.EVT_TEXT, self.OnTextCtrlX)
            self.y.Bind(wx.EVT_TEXT, self.OnTextCtrlY)
            self.w.Bind(wx.EVT_TEXT, self.OnTextCtrlW)
            self.h.Bind(wx.EVT_TEXT, self.OnTextCtrlH)    
            
            self.selected = canvas.Document.SelectedObjects[0]
            cls = str(self.selected.__class__).split(".")
            cls = cls[1]
            self.ObjectName.SetLabel("     %s" % (cls))
            self.Show()
        
        else:
            self.Hide()
    
    def Deactivate(self, canvas):
        self.x.Unbind(wx.EVT_TEXT)
        self.y.Unbind(wx.EVT_TEXT)
        self.w.Unbind(wx.EVT_TEXT)
        self.h.Unbind(wx.EVT_TEXT)    
            
    def OnTextCtrlX(self, event):
        if event.GetString()=='' : return
        
        rect = wx.GetApp().Frame.Canvas.Document.GetRect(wx.GetApp().Frame.Canvas.Document.SelectedObjects)
        first_point = rect.Path.Points[0][1][0]        
        diff = int(event.GetString()) - first_point
        for point in self.selected.Path.Points:
            point[1][0] +=  diff
            if point[0] != None :
                point[0][0] +=  diff
            if point[2] != None :
                point[2][0] +=  diff
        wx.GetApp().Frame.Canvas.Refresh()
    
    def OnTextCtrlY(self, event):
        if event.GetString()=='' : return
        
        rect = wx.GetApp().Frame.Canvas.Document.GetRect(wx.GetApp().Frame.Canvas.Document.SelectedObjects)
        first_point = rect.Path.Points[0][1][1]
        diff = int(event.GetString()) - first_point
        for point in self.selected.Path.Points:
            point[1][1] += diff
            if point[0] != None :
                point[0][1] +=  diff
            if point[2] != None :
                point[2][1] +=  diff
        self.GetParent().Parent.Canvas.Refresh()
        
    def OnTextCtrlW(self, event):
        if event.GetString()=='' : return
        if float( event.GetString() ) <= 0:
            return 
        
        rect = wx.GetApp().Frame.Canvas.Document.GetRect(wx.GetApp().Frame.Canvas.Document.SelectedObjects)
        w = abs(rect.Path.Points[0][1][0] - rect.Path.Points[1][1][0])
        new_w = float( event.GetString() )
        factor = float(new_w / w)
        
        x_topleft = rect.Path.Points[0][1][0]
        
        sliced_list = self.selected.Path.Points[1:]
        '''To skip doing scaling operation on top left point of the object (a.k.a first element)'''
        for points in sliced_list:
            points[1][0] = (points[1][0] - x_topleft) * factor + x_topleft
            if points[0] != None :
                '''If there are handlers exist'''
                points[0][0] = (points[0][0] - x_topleft) * factor + x_topleft
            if points[2] != None :
                points[2][0] = (points[2][0] - x_topleft) * factor + x_topleft
        
        wx.GetApp().Frame.Canvas.Refresh()
        
    def OnTextCtrlH(self, event):
        if event.GetString()=='' : return
        if float( event.GetString() ) <= 0:
            return 
        
        rect = wx.GetApp().Frame.Canvas.Document.GetRect(wx.GetApp().Frame.Canvas.Document.SelectedObjects)
        h = abs(rect.Path.Points[0][1][1] - rect.Path.Points[1][1][1])
        new_h = float( event.GetString() )
        factor = float(new_h / h)
        
        y_topleft = rect.Path.Points[0][1][1]
        
        sliced_list = self.selected.Path.Points[1:]
        '''To skip doing scaling operation on top left point of the object (a.k.a first element)'''
        for points in sliced_list:
            points[1][1] = (points[1][1] - y_topleft) * factor + y_topleft
            if points[0] != None :
                '''If there are handlers exist'''
                points[0][1] = (points[0][1] - y_topleft) * factor + y_topleft
            if points[2] != None :
                points[2][1] = (points[2][1] - y_topleft) * factor + y_topleft
        
        wx.GetApp().Frame.Canvas.Refresh()
