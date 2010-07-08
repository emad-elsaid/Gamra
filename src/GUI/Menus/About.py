'''
Created on Jul 8, 2010

@author: blaze
'''
import wx

class About(wx.Menu):

    def __init__(self):
        wx.Menu.__init__(self)
        self.Priority = 0
        self.Label = "Help"
        self.Append(wx.ID_ABOUT, "E&xit", "Terminate the program")
        self.Handlers = [[wx.ID_ABOUT,self.OnAbout]]
        
    def OnAbout(self, event):
        wx.GetApp().Frame.About.Show()