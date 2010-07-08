'''
Created on Jul 8, 2010

@author: blaze
'''
import wx

class File(wx.Menu):

    def __init__(self):
        wx.Menu.__init__(self)
        self.Priority = 0
        self.Label = "File"
        self.Append(wx.ID_EXIT,"E&xit", "Terminate the program")
        self.Handlers = [[wx.ID_EXIT,self.OnExit]]
        
    def OnExit(self, event):
        wx.GetApp().Frame.Close()
        