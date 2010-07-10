'''
Created on Jul 8, 2010

@author: blaze
'''
import wx
from Document import Document
import Exporters
from Exporters import *
from GUI.Canvas import Canvas

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
        
        self.Append(wx.ID_NEW, 'New')
        self.Handlers.append([wx.ID_NEW, self.OnNew])
        
        self.Append(wx.ID_OPEN, 'Open...')
        self.Handlers.append([wx.ID_OPEN, self.OnOpen])
        
        self.Append(wx.ID_SAVEAS, 'Save As...')
        self.Handlers.append([wx.ID_SAVEAS,self.OnSaveAs])
        
        self.ExporterObjs = ExportersMenu()
        self.AppendMenu(-1, 'Export', self.ExporterObjs)
        self.Handlers.extend(self.ExporterObjs.Handlers)
        
        self.Append(wx.ID_EXIT,"E&xit", "Terminate the program")
        self.Handlers.append([wx.ID_EXIT,self.OnExit])
        
        
    def OnNew(self, event):
        canvas = wx.GetApp().Frame.Canvas
        canvas.Document = Document(1000,500)
        canvas.Refresh()
        
    def OnSaveAs(self, event):
        frame = wx.GetApp().Frame
        saveDLG = wx.FileDialog( frame, 'Save As...', wildcard='Gamra Graphics (*.gmg)|*.gmg', style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT )
        
        if saveDLG.ShowModal()==wx.ID_OK :
            File = saveDLG.GetPath()
            if not File.endswith('.gmg') :
                File += '.gmg'
                
            File = str(File)
            data = frame.Canvas.Document.ToData()
            filePtr = file(File, 'w')
            filePtr.write(data)
            filePtr.close()
           
    def OnOpen(self, event):
        frame = wx.GetApp().Frame
        saveDLG = wx.FileDialog( frame, 'Open...', wildcard='Gamra Graphics (*.gmg)|*.gmg', style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST )
        
        if saveDLG.ShowModal()==wx.ID_OK :
            File = str(saveDLG.GetPath())
            filePtr = file( File, 'r')
            data = filePtr.read()
            frame.Canvas.Document.FromData(data)
            frame.Canvas.Refresh()
    
    def OnExit(self, event):
        wx.GetApp().Frame.Close()