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
        self.editTools = []
        for tool in Edit.__all__:
            eval( 'self.editTools.append( '+tool+'.'+tool+'())' )
            
        #========== Making buttons of Editing tools =====
        for v in self.editTools:
            self.AddTool(-1,
                     wx.Bitmap( os.path.normpath("icons/"+v.icon)), 
                     wx.Bitmap( os.path.normpath("icons/"+v.icon)),
                     isToggle=True,
                     shortHelpString = v.name,
                     longHelpString = v.__doc__
                     )
        
        
