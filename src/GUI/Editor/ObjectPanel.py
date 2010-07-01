from Generic import Generic
import wx


class ObjectPanel(Generic):
    def __init__(self,parent,id=wx.ID_ANY,pos=wx.DefaultPosition,size=wx.DefaultSize):
        Generic.__init__(self, parent, id, pos, (200,200),"data/icons/photo.png", Priority=0)
        self.rightSizer = wx.BoxSizer(wx.VERTICAL)
        self.rightSizer.Add(wx.StaticText(self,-1),0, wx.ALIGN_TOP | wx.ALIGN_CENTER)
        self.mainSizer.AddSpacer(wx.Size(30, 30))
        self.mainSizer.Add(self.rightSizer, 0)
        self.rightSizer.AddSpacer(wx.Size(30, 30))
        g = wx.FlexGridSizer(2,4,20,20)
        s1 = wx.StaticText(self,-1,"X")
        x = wx.TextCtrl(self,-1,"")
        s2 = wx.StaticText(self,-1,"Y")
        y = wx.TextCtrl(self,-1,"")
        s3 = wx.StaticText(self,-1,"W")
        w = wx.TextCtrl(self,-1,"")
        s4 = wx.StaticText(self,-1,"H")
        h = wx.TextCtrl(self,-1,"")
        
        g.Add(s1)
        g.Add(x)
        g.Add(s2)
        g.Add(y)
        g.Add(s3)
        g.Add(w)
        g.Add(s4)
        g.Add(h)
        
        
        self.rightSizer.Add(g)
        self.rightSizer.Fit(self)
        self.Show()
           
         
         
    
if __name__ == '__main__':
    
    app = wx.PySimpleApp()
    
    frame = wx.Frame(None)
    panel = ObjectPanel(frame)
    panel.Show()
    #frame.AutoLayout = True
    frame.Show(True)
    app.MainLoop()