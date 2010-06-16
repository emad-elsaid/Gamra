'''
Created on Jun 16, 2010

@author: ramdac
'''
import wx

 
class ColourPickerButton:
    def __init__(self, parent, id, label = wx.EmptyString,pos = wx.DefaultPosition,  size = wx.DefaultSize, 
         style = 0, validator = wx.DefaultValidator, name = "button"):
        
        self.button = wx.Button(parent, id, label, pos, size, style, validator, name)
        self.button.Show(False)
        
        
        self.bmpImage = wx.Bitmap("../../data/palettes/colorcube.gif", wx.BITMAP_TYPE_GIF)
        
        self.panel = wx.Panel(parent, wx.ID_ANY, self.button.GetPosition(), (self.bmpImage.GetWidth(), self.bmpImage.GetHeight()),  wx.TAB_TRAVERSAL)
        wx.WindowDC(parent).DrawBitmap(self.bmpImage, 0, 0)
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
    frame = wx.Frame(None, pos = (500, 400))
    frame.Show(True)
    a = ColourPickerButton(frame, -1, 'Hello', pos = (100, 100))
    a.Show(True)
    A.MainLoop()
    
