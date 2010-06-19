'''
Created on Jun 16, 2010

@author: ramdac
'''
import wx
from wx.lib.statbmp import GenStaticBitmap

class ColourPickerPanel(wx.Panel):
    '''
    A Panel that contains a palette image which the user can choose from
    I separated it from the ColourPickerButton to have the functionality 
    of a panel and make use of the paint image
    '''
    def __init__(self, parent, bmpImage, id = wx.ID_ANY, pos = wx.DefaultPosition, style = wx.TAB_TRAVERSAL ):
        self.bmpImage = bmpImage
        wx.Panel.__init__(self, parent, id, pos, (self.bmpImage.GetWidth(), self.bmpImage.GetHeight() + 50), style)
        self.colour = wx.BLACK
        self.boxSizer = wx.BoxSizer(wx.VERTICAL)
        self.staticBitmap = GenStaticBitmap(self, id, self.bmpImage, (0, 0), wx.DefaultSize)
        self.boxSizer.Add(self.staticBitmap, wx.EXPAND)
        self.buttonBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.ColourPickerButton = wx.ColourPickerCtrl(self, wx.ID_ANY, style = wx.CLRP_SHOW_LABEL)
        self.buttonBoxSizer.Add( self.ColourPickerButton, wx.ALIGN_LEFT)
        self.boxSizer.Add(self.buttonBoxSizer, wx.ALIGN_BOTTOM)
        self.SetSizer(self.boxSizer)
        
        wx.EVT_LEFT_DOWN(self.staticBitmap, self.OnMouseDown)
        #TODO: Add wxColourPickerControl
        
    def GetStaticBitmap(self):
        return self.staticBitmap
    
    def OnMouseDown(self, event):
        image = self.bmpImage.ConvertToImage()
        x, y = event.GetPosition()
        r = image.GetRed(x, y) 
        g = image.GetGreen(x, y)
        b = image.GetBlue(x, y)
        self.colour.Set(r, g, b)
        self.ColourPickerButton.SetColour(self.colour)
        self.Show(False)
        
    def GetColour(self):
        return self.colour
    def SetColour(self, colour):
        pass
        
class ColourPickerWidget:
    '''
    A Widget that shows a panel contains an image which 
    resembles a palette of colors the user can choose from. 
    '''
    def __init__(self, parent, id, label = wx.EmptyString,pos = wx.DefaultPosition,  size = wx.DefaultSize, 
         style = 0, validator = wx.DefaultValidator, name = "button"):
        
        self.button = wx.Button(parent, id, label, pos, size, style, validator, name)
        self.button.Show(False)
        
        
        
        self.bmpImage = wx.Bitmap("../../data/palettes/colorcube.gif", wx.BITMAP_TYPE_GIF)
        buttonPosTuple = self.button.GetPositionTuple()
        self.panel = ColourPickerPanel(parent, self.bmpImage, id, (buttonPosTuple[0] , buttonPosTuple[1] - self.bmpImage.GetHeight() - 50)
                ,  wx.TAB_TRAVERSAL)
        
        
        self.panel.Show(False)
        self.button.Bind(wx.EVT_BUTTON, self.OnClickButton)
        
    
    def Show(self, flag=True):
        self.button.Show(flag)
    
    def SetColour(self, colour):
        self.colour = colour
    
    def GetColour(self):
        return self.colour
    
    
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
    a = ColourPickerWidget(frame, -1, 'Hello', pos = (400, 300))
    a.Show(True)
    A.MainLoop()
    
