'''
Created on Jun 16, 2010

@author: ramdac
'''
import wx
from wx.lib.statbmp import GenStaticBitmap

class ColourPickerButton:
    '''
    A button that shows a panel contains an image which 
    resembles a palette of colors the user can choose from. 
    '''
    def __init__(self, parent, id, label = wx.EmptyString,pos = wx.DefaultPosition,  size = wx.DefaultSize, 
         style = 0, validator = wx.DefaultValidator, name = "button"):
        
        self.button = wx.Button(parent, id, label, pos, size, style, validator, name)
        self.button.Show(False)
        
        self.colour = wx.BLACK
        
        self.bmpImage = wx.Bitmap("../../data/palettes/colorcube.gif", wx.BITMAP_TYPE_GIF)
        buttonPosTuple = self.button.GetPositionTuple()
        self.panel = wx.Panel(parent, id, (buttonPosTuple[0] , buttonPosTuple[1] - self.bmpImage.GetHeight())
                , (self.bmpImage.GetWidth(), self.bmpImage.GetHeight()),  wx.TAB_TRAVERSAL)
        
        self.staticBitmap = GenStaticBitmap(self.panel, id, self.bmpImage, (0, 0), size)
        self.panel.Show(False)
        self.button.Bind(wx.EVT_BUTTON, self.OnClickButton)
        wx.EVT_LEFT_DOWN(self.staticBitmap, self.OnMouseDown)
    
    def Show(self, flag=True):
        self.button.Show(flag)
    
    def SetColour(self, colour):
        self.colour = colour
    
    def GetColour(self):
        return self.colour
    
    def OnMouseDown(self, event):
        image = self.bmpImage.ConvertToImage()
        x, y = event.GetPosition()
        r = image.GetRed(x, y) 
        g = image.GetGreen(x, y)
        b = image.GetBlue(x, y)
        self.colour.Set(r, g, b)
        self.panel.Show(False)
        
    def OnClickButton(self, event):
        '''
        Event Generated when the button clicked
        '''
        if self.panel.IsShown() == True:
            self.panel.Show(False)
            return
        self.panel.Show(True)
        
    
        
if __name__ == "__main__":
    A = wx.App()
    frame = wx.Frame(None, pos = (800, 600))
    frame.Show(True)
    a = ColourPickerButton(frame, -1, 'Hello', pos = (400, 300))
    a.Show(True)
    A.MainLoop()
    
