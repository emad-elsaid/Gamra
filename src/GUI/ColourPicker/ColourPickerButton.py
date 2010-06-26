'''
Created on Jun 16, 2010

@author: ramdac
'''
import wx
import re
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
        #The button that this panel is connected with 
        #TODO:Change this habit
        self.button = None
        self.colour = wx.BLACK
        self.colourTextCtrl = wx.TextCtrl(self, pos = (50, 0), style = wx.TE_PROCESS_ENTER)
        self.colourTextCtrl.SetValue(self.colour.GetAsString(wx.C2S_HTML_SYNTAX))
        self.staticBitmap = GenStaticBitmap(self, id, self.bmpImage)
        self.colourPanel = wx.Panel(self, id, size = (50,20), style = wx.BORDER_DOUBLE)
        self.colourChooserButton = wx.BitmapButton(self, id, wx.Bitmap("data/icons/color_wheel.png", wx.BITMAP_TYPE_PNG))
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
        self.colourTextCtrl.Bind(wx.EVT_TEXT_ENTER, self.OnTextCtrl)
        wx.EVT_LEFT_DOWN(self.staticBitmap, self.OnMouseDown)
        self.colourChooserButton.Bind(wx.EVT_BUTTON, self.OnColourChooserButton)
        wx.EVT_MOTION(self.staticBitmap, self.OnMotion)
        
        
    def GetStaticBitmap(self):
        return self.staticBitmap
    
    def OnTextCtrl(self, event):
        textCtrlValue = self.colourTextCtrl.GetValue()
        if re.match(r'#[0-9a-fA-F]{6}', textCtrlValue) == None:
			self.colour.SetFromString("#FFFFFF")
			
        else:
			self.colour.SetFromString(textCtrlValue)
        self.UpdatePanel()
        self.button.SetBackgroundColour(self.colour)
        self.Show(False)
                
    def UpdatePanel(self):
        self.colourPanel.SetBackgroundColour(self.colour)
        self.colourTextCtrl.SetValue(self.colour.GetAsString(wx.C2S_HTML_SYNTAX))
        
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
            self.button.SetBackgroundColour(self.colour)
            self.Show(False)
        elif clickedButton == wx.ID_CANCEL:
            return
        
    def OnMouseDown(self, event):
        x, y = event.GetPosition()
        r = self.image.GetRed(x, y) 
        g = self.image.GetGreen(x, y)
        b = self.image.GetBlue(x, y)
        self.colour.Set(r, g, b)
        self.button.SetColour(self.colour)
        self.Show(False)
        
    def GetColour(self):
        return self.colour
    
    def SetColour(self, colour):
        self.colour = colour
        self.UpdatePanel()
    def SetButton(self, button = None):
        '''
        To make this class to change the colour of the ColourPickerButton
        I know it is a bad habit but until i make an event class that indicates
        a colour has been choosen
        '''
        self.button = button


class ColourPickerButton(wx.Button):
    def __init__(self, parent, id, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.BU_EXACTFIT):
        wx.Button.__init__(self, parent, id, wx.EmptyString, pos, size, style)
    def SetColour(self, colour):
        self.SetBackgroundColour(colour)
    
        
    
        
class ColourPickerWidget:
    '''
    A Widget that shows a panel contains an image which 
    resembles a palette of colors the user can choose from. 
    '''
    def __init__(self, parent, id, colour, pos = wx.DefaultPosition,  size = wx.DefaultSize, 
         style = 0, validator = wx.DefaultValidator, name = "button"):
        
        self.button = ColourPickerButton(parent, id, pos, size)
        self.button.Show(True)
        
        self.bmpImage = wx.Bitmap("data/palettes/colorcube.gif", wx.BITMAP_TYPE_GIF)
        buttonPosTuple = self.button.GetPositionTuple()
        self.panel = ColourPickerPanel(parent, self.bmpImage, id, (buttonPosTuple[0] , buttonPosTuple[1] - self.bmpImage.GetHeight() - 27)
                ,wx.TAB_TRAVERSAL)
        self.panel.Show(False)
        self.panel.SetButton(self.button)
        self.SetColour(colour)
        self.button.Bind(wx.EVT_BUTTON, self.OnClickButton) 
       
    
    def Show(self, flag=True):
        self.button.Show(flag)
    
    def SetColour(self, colour):
        self.panel.SetColour(colour)
        self.button.SetBackgroundColour(colour)
    def GetColour(self):
        colour =  self.panel.GetColour()
        return colour.Get(True)
    
    def OnClickButton(self, event):
        '''
        Event Generated when the button clicked
        '''
        if self.panel.IsShown() == True:
            self.button.SetColour(self.panel.GetColour())
            self.panel.Show(False)
            return
        self.panel.Show(True)

