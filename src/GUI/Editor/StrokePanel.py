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
       
        self.Bind(ColourPickerEvent.EVT_COLOURPICKER, self.OnColourChoice)
        
        firstLine.Add(wx.StaticText(self,-1,"Thickness :"))
        
        self.widthCtrl = wx.TextCtrl(self,-1,'1', style=wx.TE_PROCESS_ENTER)
        firstLine.Add(self.widthCtrl)
        self.mainSizer.AddSpacer(wx.Size(5, 5))
        self.widthCtrl.Bind(wx.EVT_TEXT, self.OnWidthTextCtrl)
        
        self.mainSizer.Add(vertical)
        self.mainSizer.AddSpacer(wx.Size(10, 10))
    def Activate(self,canvas):
        if len(canvas.Document.SelectedObjects)==1 :
            self.Show()
            self.widthCtrl.SetValue("%s" %(canvas.Document.SelectedObjects[0].Stroke.Width))
            self.color.SetColour(canvas.Document.SelectedObjects[0].Stroke.Color)
            
        else:
            self.Hide()

    def OnColourChoice(self, event):
        wx.GetApp().Frame.Canvas.Document.SelectedObjects[0].Stroke.Color = event.GetColour()
        wx.GetApp().Frame.Canvas.Refresh()
        
    
    def OnWidthTextCtrl(self, event):
        if( event.GetString() != ''):
            value = float(event.GetString())
            wx.GetApp().Frame.Canvas.Document.SelectedObjects[0].Stroke.Width = value
            wx.GetApp().Frame.Canvas.Refresh()
            event.Skip()
