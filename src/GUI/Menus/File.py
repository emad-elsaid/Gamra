'''
Created on Jul 8, 2010

@author: blaze
'''
import wx
import Exporters
from Exporters import *

class ExportersMenu(wx.Menu):
    def __init__(self):
        wx.Menu.__init__(self)
        self.Handlers = []
        for exporter in Exporters.__all__ :
            exporterObj = eval(exporter+'.'+exporter+'()')
            id = wx.NewId()
            self.Append(id, exporterObj.Label)
            self.Handlers.append((id,exporterObj.Launch))

class File(wx.Menu):

    def __init__(self):
        wx.Menu.__init__(self)
        self.Priority = 0
        self.Label = "File"
        self.Handlers = []
        
        self.ExporterObjs = ExportersMenu()
        self.AppendMenu(-1, 'Export', self.ExporterObjs)
        self.Handlers.extend(self.ExporterObjs.Handlers)
        
        self.Append(wx.ID_EXIT,"E&xit", "Terminate the program")
        self.Handlers.append([wx.ID_EXIT,self.OnExit])
        
    def OnExit(self, event):
        wx.GetApp().Frame.Close()
        