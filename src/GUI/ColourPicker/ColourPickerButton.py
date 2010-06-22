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
    of a panel and make use of the paint event
    '''
    def __init__(self, parent, bmpImage, id = wx.ID_ANY, pos = wx.DefaultPosition, style = wx.TAB_TRAVERSAL ):
        
        self.bmpImage = bmpImage
        wx.Panel.__init__(self, parent, id, pos, wx.DefaultSize, style)
        
        self.colour = wx.BLACK
        self.colourTextCtrl = wx.TextCtrl(self, pos = (50, 0))
        self.colourTextCtrl.SetValue(self.colour.GetAsString(wx.C2S_HTML_SYNTAX))
        self.staticBitmap = GenStaticBitmap(self, id, self.bmpImage)
        self.colourPanel = wx.Panel(self, id, size = (50,20), style = wx.BORDER_DOUBLE)
        self.colourChooserButton = wx.BitmapButton(self, id, wx.Bitmap("../../data/icons/color_wheel.png", wx.BITMAP_TYPE_PNG))
        self.colourChooserDialog = wx.ColourDialog(self)
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.currentSelectionSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.colourPanel.SetBackgroundColour(wx.GREEN)
        
        self.currentSelectionSizer.Add(self.colourPanel)
        self.currentSelectionSizer.AddSpacer(10, 0)
        self.currentSelectionSizer.Add(self.colourTextCtrl)
        self.currentSelectionSizer.AddSpacer(20, 0)
        self.currentSelectionSizer.Add(self.colourChooserButton)
        self.mainSizer.Add(self.currentSelectionSizer)
        
        self.mainSizer.Add(self.staticBitmap, 0)
        
        
        self.mainSizer.SetSizeHints(self)
        self.staticBitmap.Show(True)
        self.SetSizer(self.mainSizer)
        
        #self.colourPanel = wx.Panel(self, wx.ID_ANY, (0, 0), (20, 15))
        self.image = self.bmpImage.ConvertToImage()
        
        wx.EVT_LEFT_DOWN(self.staticBitmap, self.OnMouseDown)
        self.colourChooserButton.Bind(wx.EVT_BUTTON, self.OnColourChooserButton)
        wx.EVT_MOTION(self.staticBitmap, self.OnMotion)
        #TODO: Add wxColourPickerControl
        
    def GetStaticBitmap(self):
        return self.staticBitmap
    
    def OnMotion(self, event):
        x, y = event.GetPosition()
        r = self.image.GetRed(x, y) 
        g = self.image.GetGreen(x, y)
        b = self.image.GetBlue(x, y)
        self.colourPanel.SetBackgroundColour(wx.Colour(r, g, b))
        self.SetColour(wx.Colour(r, g, b))
        self.colourTextCtrl.SetValue(self.colour.GetAsString(wx.C2S_HTML_SYNTAX))
    
    def OnColourChooserButton(self, event):
        clickedButton = self.colourChooserDialog.ShowModal()
        if clickedButton == wx.ID_OK:
            colour = self.colourChooserDialog.GetColourData().GetColour()
            self.colourPanel.SetBackgroundColour(colour)
            self.SetColour(colour)
            self.colourTextCtrl.SetValue(self.colour.GetAsString(wx.C2S_HTML_SYNTAX))
        elif clickedButton == wx.ID_CANCEL:
            return
        
    def OnMouseDown(self, event):
        x, y = event.GetPosition()
        r = self.image.GetRed(x, y) 
        g = self.image.GetGreen(x, y)
        b = self.image.GetBlue(x, y)
        self.colour.Set(r, g, b)
        self.Show(False)
        
    def GetColour(self):
        return self.colour
    
    def SetColour(self, colour):
        self.colour = colour

class ColourPickerButton(wx.Button):
    def __init__(self, parent, id, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.BU_EXACTFIT):
        wx.Button.__init__(self, parent, id, wx.EmptyString, pos, size, style)
        self.colour = wx.BLACK
        self.SetBackgroundColour(wx.Colour(self.colour.Red(), self.colour.Green(), self.colour.Blue()))
    def SetColour(self, colour):
        self.colour = colour
        self.UpdateColour()
    def GetColour(self):
        return self.colour
    def UpdateColour(self):   
        self.SetBackgroundColour(wx.Colour(self.colour.Red(), self.colour.Green(), self.colour.Blue()))
        
    
        
class ColourPickerWidget:
    '''
    A Widget that shows a panel contains an image which 
    resembles a palette of colors the user can choose from. 
    '''
    def __init__(self, parent, id, pos = wx.DefaultPosition,  size = wx.DefaultSize, 
         style = 0, validator = wx.DefaultValidator, name = "button"):
        
        self.button = ColourPickerButton(parent, id, pos, size)
        self.button.Show(True)
        
        
        
        self.bmpImage = wx.Bitmap("../../data/palettes/colorcube.gif", wx.BITMAP_TYPE_GIF)
        buttonPosTuple = self.button.GetPositionTuple()
        self.panel = ColourPickerPanel(parent, self.bmpImage, id, (buttonPosTuple[0] , buttonPosTuple[1] - self.bmpImage.GetHeight() - 50)
                ,wx.TAB_TRAVERSAL)
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
    a = ColourPickerWidget(frame, -1, (200, 400), (50, 50))#ColourPickerWidget(frame, -1, 'Hello', pos = (400, 300))
    
    a.Show(True)
    A.MainLoop()
    
