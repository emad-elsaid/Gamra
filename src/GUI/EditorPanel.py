'''
@author Ramdac
'''

import wx
import Editor
from Editor import *

class EditorPanel(wx.Panel):
    def __init__(self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TAB_TRAVERSAL):
        
        wx.Panel.__init__(self, parent, id, pos, size, style)
        
        #=======A box Sizer that will manage all Editors side by side
        self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        #======Temporary List to construct the objects in====#
        editorsList = [] 
        
        for editor in Editor.__all__:
            eval( 'editorsList.append('+editor+'.'+editor+'(self))' )
        
        #=======Making the list of objects that will going to be used from outside the class======#
        self.Editors = []
        self.Editors.extend(editorsList)
        
        #Adding the editor objects to sizer side by side 
        for editor in self.Editors:
            self.mainSizer.Add(editor, 0, wx.EXPAND)
        
        self.mainSizer.Fit(self)
        self.SetSizer(self.mainSizer)
        
    
    def Refresh(self, canvas):
        #Deactivate all editors then activate it
        for editor in self.Editors:
            editor.Deactivate(canvas)
        
        for editor in self.Editors:
            editor.Activate(canvas)
