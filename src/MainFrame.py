'''
Created on Jun 4, 2010

@author: blaze
'''
from wx import *
from AboutBox import AboutBox

class MainFrame(Frame):
    
    def __init__(self,parent=None,id=-1, title="Firepy", pos = wx.DefaultPosition,
                 size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE):
        
        wx.Frame.__init__(self, parent, id, title,pos, size)
        
        self.CreateStatusBar()

        file_menu = wx.Menu()
        file_menu.Append(ID_EXIT,"E&xit", "Terminate the program")

        help_menu = wx.Menu()
        help_menu.Append(ID_ABOUT,"&About","More information about this program")
        
        menuBar = wx.MenuBar()
        menuBar.Append(file_menu, "&File")
        menuBar.Append(help_menu, "&Help")
        self.MenuBar = menuBar
        
            
        #connecting functions with actions
        EVT_MENU(self, ID_EXIT, self.OnExit)
        EVT_MENU(self, ID_ABOUT, self.OnAbout)
        
        self.About = AboutBox()
        
    def OnExit(self, event):
        self.Close(True)
        
    def OnAbout(self, event):
        self.About.Show()
