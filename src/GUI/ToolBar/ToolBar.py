'''
Created on Jun 10, 2010

@author: blaze
'''
import os
import wx
import Edit
from Edit import *

class ToolBar(wx.ToolBar):
    '''
    Window main toolbar, instansiate
    and add it, it'll load all tools
    and add them to himself then 
    handle all events to activate tools,deactivate
    and everything that is related to them.
    '''
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.TB_HORIZONTAL | wx.NO_BORDER, name=wx.PanelNameStr):
        wx.ToolBar.__init__(self, parent, id, pos, size, style, name)
        
        self.height = 10
        
        #================================================
        #=========== loading all tools ==================
        #================================================
        #========== Making objects of Editing tools ===== 
        editTools = []
        for tool in Edit.__all__:
            eval( 'editTools.append('+tool+'.'+tool+'())' )
            
        #========== Making buttons of Editing tools =====
        for v in editTools:
            tool = self.AddRadioTool(-1,
                     bitmap = wx.Bitmap( os.path.normpath("icons/"+v.icon)), 
                     shortHelp = v.name,
                     longHelp = v.__doc__
                     )
            tool.ClientData = v
            self.Bind(wx.EVT_MENU, self.OnToolChange, tool)
            
        self.AddSeparator()
        
        #================================================
        # Note: we have to merge all tools lists to (self.Tools)
        #================================================
        self.Tools = []
        self.Tools.extend(editTools)
        self.Tools[0].Activate()
        self.ActiveTool = self.Tools[0]
            
    def OnToolChange(self,event):
        
        #========= getting new tool
        toolbutton = self.FindById(event.Id)
        tool = toolbutton.ClientData
        
        #======== Activating and Deactivating
        self.ActiveTool.Deactivate()
        tool.Activate()
        
        #======== Setting new Tool
        self.ActiveTool = tool