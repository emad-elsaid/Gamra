'''
Created on Jun 16, 2010

@author: ramdac
'''
import wx
import os.path
 
class ColourPickerButton:
    def __init__(self, parent, id, label = wx.EmptyString,pos = wx.DefaultPosition,  size = wx.DefaultSize, 
         style = 0, validator = wx.DefaultValidator, name = "button"        ):
        
        self.button = wx.Button(parent, id, label, pos, size, style, validator, name)
        self.button.Show(False)
        
        self.paletteImage = wx.Image("data/asd/colorcube.gif")
        self.bmpImage = self.paletteImage.ConvertToBitmap()
        
        self.panel = wx.Panel(parent, wx.ID_ANY, self.button.GetPosition(), (self.bmpImage.GetWidth(), self.bmpImage.GetHeight()), wx.TAB_TRAVERSAL)
        self.panel.Show(False)
        
        self.button.Bind(wx.EVT_BUTTON, self.OnClick)
    
    
    def Show(self, flag=True):
        
        self.button.Show(flag)
    
    def OnClick(self, event):
        if self.panel.IsShown() == True:
            self.panel.Show(False)
            return
        self.panel.Show(True)
        
    
        
if __name__ == "__main__":
    A = wx.App()
    frame = wx.Frame(None)
    frame.Show(True)
    a = ColourPickerButton(frame, -1, 'Hello')
    
    a.Show(True)
    A.MainLoop()
    
