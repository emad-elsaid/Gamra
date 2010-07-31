'''
Created on Jun 23, 2010

@author: blaze
'''
import wx
class Generic(wx.Panel):
    '''
    this is the generic editor , all editors will inherit it's
    functionality
    '''
    

    def __init__(self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.DefaultSize, iconPath='data/icons/photo.png', Priority=0 ):
        wx.Panel.__init__(self, parent, id, pos, size)
        self.Priority = Priority
        self.icon = wx.Bitmap(iconPath, wx.BITMAP_TYPE_PNG)
        staticBitmap = wx.StaticBitmap(self, wx.ID_ANY, self.icon)
        self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.leftSizer = wx.BoxSizer(wx.VERTICAL)
        self.leftSizer.Add(staticBitmap, 0, wx.ALIGN_TOP | wx.ALIGN_CENTER)
        self.mainSizer.AddSpacer(5)
        self.mainSizer.Add( wx.StaticLine( self, -1, (0,0), (1,80), style=wx.LI_VERTICAL ) )
        self.mainSizer.AddSpacer(5)
        self.mainSizer.Add(self.leftSizer, 0)
        self.mainSizer.AddSpacer(10)
        self.SetSizer(self.mainSizer)
        self.Show(False)
        
    def Activate(self, canvas ): pass
    def Deactivate(self, canvas): pass
        
