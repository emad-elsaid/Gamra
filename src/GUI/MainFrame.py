'''
Created on Jun 4, 2010

@author: blaze
'''
import wx
import os
import Canvas
import AboutBox
from EditorPanel import EditorPanel
import ToolBar
from MenuBar import MenuBar

class MainFrame(wx.Frame):
    
    def __init__(self,parent=None,id=-1, title="Gamra", pos = wx.DefaultPosition,
                 size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE):
        
        wx.Frame.__init__(self, parent, id, title,pos, size)
        
        #============= Creating About Box
        self.About = AboutBox.AboutBox()
        
        #============= Setting Frame Icon
        self.Icon = wx.Icon(os.path.normpath("data/icons/icon256.png"), wx.BITMAP_TYPE_PNG)
        
        #============= Making Main Menu        
        self.MenuBar = MenuBar()
        for event in self.MenuBar.Handlers :
            wx.EVT_MENU(self, event[0], event[1])
        
        #=================================================
        #======= Making Main layout of the window ========
        #=================================================
        box = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(box)
        
        #=============== Creating Canvas =================
        self.Canvas = Canvas.Canvas( self )  
        box.Add(self.Canvas, 10, wx.EXPAND | wx.ALL)
        
        #=============== Creating Toolbar =================
        tb = ToolBar.ToolBar(self)
        #The second parameter to make the vertical resizing factor to Zero and 
        #make Horizontal factor resizable 
        box.Add(tb, 0, wx.EXPAND | wx.ALL)
        
        self.Properties = EditorPanel(self, size = wx.Size(0, 100))
        box.Add(self.Properties, 0, wx.EXPAND | wx.ALL)
        
        #============= Creating statusbar
        self.CreateStatusBar()
        
        self.Maximize()
        
        
   