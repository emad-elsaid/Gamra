'''
Created on Jul 5, 2010

@author: blaze
'''
import wx
from GUI.Editor.Generic import Generic
from GUI.ColourPicker import ColourPickerWidget
from GUI.ColourPicker import ColourPickerEvent

class StrokePanel(Generic):
    def __init__(self,parent):
        Generic.__init__(self, parent, iconPath="data/icons/pencil.png")
                
        vertical = wx.BoxSizer(wx.VERTICAL)
        
        firstLine = wx.BoxSizer(wx.HORIZONTAL)
        vertical.Add(firstLine)
        
        self.color = ColourPickerWidget.ColourPickerWidget(self)
        firstLine.Add(self.color)
       
        firstLine.Add(wx.StaticText(self,-1,"Thickness :"))
        
        self.widthCtrl = wx.SpinCtrl(self,-1,'1', style= wx.SP_ARROW_KEYS | wx.SP_WRAP)
        firstLine.Add(self.widthCtrl)
        self.mainSizer.AddSpacer(wx.Size(5, 5))
        
        
        self.mainSizer.Add(vertical)
        self.mainSizer.AddSpacer(wx.Size(10, 10))
    
    def Activate(self,canvas):
        if len(canvas.Document.SelectedObjects)==1 :
            self.Show()
            self.widthCtrl.SetValue(canvas.Document.SelectedObjects[0].Stroke.Width)
            self.widthCtrl.SetRange(1, 1000)
            self.color.SetColour(canvas.Document.SelectedObjects[0].Stroke.Color)
            self.widthCtrl.Bind(wx.EVT_SPINCTRL, self.OnWidthSpinCtrl)
            self.Bind(ColourPickerEvent.EVT_COLOURPICKER, self.OnColourChoice)
        
        else:
            self.Hide()

    def OnColourChoice(self, event):
        wx.GetApp().Frame.Canvas.Document.SelectedObjects[0].Stroke.Color = event.GetColour()
        wx.GetApp().Frame.Canvas.Refresh()
        event.Skip()
    
    def OnWidthSpinCtrl(self, event):
        wx.GetApp().Frame.Canvas.Document.SelectedObjects[0].Stroke.Width = self.widthCtrl.GetValue()
        wx.GetApp().Frame.Canvas.Refresh()
        event.Skip()
