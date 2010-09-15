'''
Created on Jul 5, 2010

@author: blaze
'''
import wx
import cairo
from GUI.Editor.Generic import Generic
from GUI.ColourPicker import ColourPickerWidget
from GUI.ColourPicker import ColourPickerEvent

class FillPanel(Generic):
    def __init__(self,parent):
        Generic.__init__(self, parent, iconPath="data/icons/fill.png")
                
        vertical = wx.BoxSizer(wx.VERTICAL)
        
        firstLine = wx.BoxSizer(wx.HORIZONTAL)
        vertical.Add(firstLine)
        
        self.color = ColourPickerWidget.ColourPickerWidget(self)
        firstLine.Add(self.color)
        
        firstLine.AddSpacer(wx.Size(5, 5))
        self.windingFill = wx.RadioButton(self, -1, "Winding", style = wx.RB_GROUP)
        self.oddFill = wx.RadioButton(self, -1, "Odd")
        firstLine.Add(self.windingFill)
        firstLine.Add(self.oddFill)
        
        self.mainSizer.AddSpacer(wx.Size(5, 5))
        
        
        self.mainSizer.Add(vertical)
        self.mainSizer.AddSpacer(wx.Size(10, 10))
    
    def Activate(self,canvas):
        if len(canvas.Document.SelectedObjects)==1 :
            self.Show()
            self.color.SetColour(canvas.Document.SelectedObjects[0].Fill.Color)
            self.Bind(ColourPickerEvent.EVT_COLOURPICKER, self.OnColourChoice)
            
            self.windingFill.Bind(wx.EVT_RADIOBUTTON, self.OnWindRadioButton)
            self.oddFill.Bind(wx.EVT_RADIOBUTTON, self.OnOddRadioButton)
        
        else:
            self.Hide()

    def OnColourChoice(self, event):
        wx.GetApp().Frame.Canvas.Document.SelectedObjects[0].Fill.Color = event.GetColour()
        wx.GetApp().Frame.Canvas.Refresh()
        event.Skip()
    
    def OnWindRadioButton(self, event):
        wx.GetApp().Frame.Canvas.Document.SelectedObjects[0].Fill.Rule = cairo.FILL_RULE_WINDING
        wx.GetApp().Frame.Canvas.Refresh()
        event.Skip()
    
    def OnOddRadioButton(self, event):
        wx.GetApp().Frame.Canvas.Document.SelectedObjects[0].Fill.Rule = cairo.FILL_RULE_EVEN_ODD
        wx.GetApp().Frame.Canvas.Refresh()
        event.Skip()
