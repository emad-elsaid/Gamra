from Generic import Generic
import wx


class ObjectPanel(Generic):
    def __init__(self,parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize ):
        
        Generic.__init__(self, parent, id, pos, size,"data/icons/photo.png", Priority=0)
        
        self.rightSizer = wx.BoxSizer(wx.VERTICAL)
        
        self.ObjectName = wx.StaticText(self)
        self.rightSizer.Add(self.ObjectName,0, wx.ALIGN_TOP | wx.ALIGN_LEFT)
        
        g = wx.FlexGridSizer(2,4,3,3)
        s1 = wx.StaticText(self,-1,"X")
        self.x = wx.TextCtrl(self)
        s2 = wx.StaticText(self,-1,"Y")
        self.y = wx.TextCtrl(self)
        s3 = wx.StaticText(self,-1,"W")
        self.w = wx.TextCtrl(self)
        s4 = wx.StaticText(self,-1,"H")
        self.h = wx.TextCtrl(self)
        
        g.Add(s1)
        g.Add(self.x)
        g.Add(s2)
        g.Add(self.y)
        g.Add(s3)
        g.Add(self.w)
        g.Add(s4)
        g.Add(self.h)
        
        self.Show()
        self.mainSizer.Add(self.rightSizer, 0)
        self.rightSizer.Add(g)
        self.mainSizer.SetSizeHints(self)
        
    def Activate(self,canvas):
        if len(canvas.Document.SelectedObjects)==1 :
            self.Show()
        else:
            self.Hide()