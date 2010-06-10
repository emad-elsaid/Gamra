'''
Created on Jun 10, 2010

@author: blaze
'''
import os
import wx
from Edit import Select
#======== importing all tools

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
        #============ Editing tools 
        self.editTools = []
        for tool in self.listTools('Edit'):
            #eval('from Edit import '+tool)
            expr ='self.editTools.append( '+tool+'.'+tool+'())'
            eval( expr )
        
        print self.editTools
        
        self.AddTool(-1,
                     wx.Bitmap( os.path.normpath("icons/select.png")), 
                     wx.Bitmap( os.path.normpath("icons/select.png"))
                     )
        
    def listTools(self,category):
        editingTools = os.listdir(os.path.normpath('GUI/ToolBar/'+category))
        return [ i.split('.')[0] for i in editingTools if i.endswith('.py') and i!='__init__.py']
        
        