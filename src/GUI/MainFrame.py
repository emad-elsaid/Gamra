'''
Created on Jun 4, 2010

@author: blaze
'''
import wx
import os
from AboutBox import AboutBox

class MainFrame(wx.Frame):
    
    def __init__(self,parent=None,id=-1, title="Gamra", pos = wx.DefaultPosition,
                 size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE):
        
        wx.Frame.__init__(self, parent, id, title,pos, size)
        
        self.CreateStatusBar()
        self.About = AboutBox()
        self.Icon = wx.Icon(os.path.normpath("GUI/icon256.png"), wx.BITMAP_TYPE_PNG)

        file_menu = wx.Menu()
        file_menu.Append(wx.ID_EXIT,"E&xit", "Terminate the program")

        help_menu = wx.Menu()
        help_menu.Append(wx.ID_ABOUT,"&About","More information about this program")
        
        menuBar = wx.MenuBar()
        menuBar.Append(file_menu, "&File")
        menuBar.Append(help_menu, "&Help")
        self.MenuBar = menuBar
                    
        #connecting functions with actions
        wx.EVT_MENU(self, wx.ID_EXIT, self.OnExit)
        wx.EVT_MENU(self, wx.ID_ABOUT, self.OnAbout)
        
    def OnExit(self, event):
        self.Close(True)
        
    def OnAbout(self, event):
        self.About.Show()
