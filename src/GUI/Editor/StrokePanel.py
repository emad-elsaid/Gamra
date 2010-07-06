'''
Created on Jul 5, 2010

@author: blaze
'''
import wx
from GUI.Editor.Generic import Generic
from GUI.ColourPicker import ColourPickerWidget

class StrokePanel(Generic):
    def __init__(self,parent):
        Generic.__init__(self, parent, iconPath="data/icons/pencil.png")
                
        vertical = wx.BoxSizer(wx.VERTICAL)
        
        firstLine = wx.BoxSizer(wx.HORIZONTAL)
        vertical.Add(firstLine)
        
        self.color = ColourPickerWidget.ColourPickerWidget(self)
        firstLine.Add(self.color)
        
        firstLine.Add(wx.StaticText(self,-1,"Thickness :"))
        
        self.widthCtrl = wx.TextCtrl(self,-1,'1')
        firstLine.Add(self.widthCtrl)
        
        self.mainSizer.Add(vertical)