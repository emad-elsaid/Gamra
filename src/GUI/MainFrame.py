'''
Created on Jun 4, 2010

@author: blaze
'''
import wx
import os
import Canvas
import AboutBox
from ToolBar import ToolBar
from GUI.ColourPicker.ColourPickerWidget import ColourPickerWidget

class MainFrame(wx.Frame):
    
    def __init__(self,parent=None,id=-1, title="Gamra", pos = wx.DefaultPosition,
                 size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE):
        
        wx.Frame.__init__(self, parent, id, title,pos, size)
        
        #============= Creating statusbar
        self.CreateStatusBar()
        
        #============= Creating About Box
        self.About = AboutBox.AboutBox()
        
        #============= Setting Frame Icon
        self.Icon = wx.Icon(os.path.normpath("data/icons/icon256.png"), wx.BITMAP_TYPE_PNG)
        
        #============= Making Main Menu
        file_menu = wx.Menu()
        file_menu.Append(wx.ID_EXIT,"E&xit", "Terminate the program")

        help_menu = wx.Menu()
        help_menu.Append(wx.ID_ABOUT,"&About","More information about this program")
        
        menuBar = wx.MenuBar()
        menuBar.Append(file_menu, "&File")
        menuBar.Append(help_menu, "&Help")
        self.MenuBar = menuBar
        
        #=================================================
        #======= Making Main layout of the window ========
        #=================================================
        box = wx.BoxSizer(wx.VERTICAL)
        self.SetAutoLayout(True)
        self.SetSizer(box)
        self.Layout()
        
        #=============== Creating Canvas =================
        self.Canvas = Canvas.Canvas( self, size=(1000,1000) )  
        box.Add(self.Canvas, 10, wx.EXPAND | wx.ALL)
        
        #=============== Creating Toolbar =================
        tb = ToolBar.ToolBar(self)
        #The second parameter to make the vertical resizing factor to Zero and 
        #make Horizontal factor resizable 
        box.Add(tb, 0, wx.EXPAND | wx.ALL)
        
        #====== TODO: the properties table
        self.Properties = wx.Panel( self, size=(0,100) )
        self.Properties.SetBackgroundColour("blue")
        box.Add(self.Properties, 0, wx.EXPAND | wx.ALL)
        
        c = ColourPickerWidget(self.Properties,-1,wx.Color(20,20,50))
        
        #connecting functions with actions
        wx.EVT_MENU(self, wx.ID_EXIT, self.OnExit)
        wx.EVT_MENU(self, wx.ID_ABOUT, self.OnAbout)
                
    def OnExit(self, event):
        self.Close(True)
        
    def OnAbout(self, event):
        self.About.Show()
