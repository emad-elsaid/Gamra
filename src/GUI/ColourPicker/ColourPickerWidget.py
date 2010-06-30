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
        self.colourTextCtrl = wx.TextCtrl(self, pos = (50, 0), style = wx.TE_READONLY)
        self.colourTextCtrl.SetValue(self.colour.GetAsString(wx.C2S_HTML_SYNTAX))
        self.staticBitmap = GenStaticBitmap(self, id, self.bmpImage)
        self.colourPanel = wx.Panel(self, id, size = (50,20), style = wx.BORDER_DOUBLE)
        self.colourChooserButton = wx.BitmapButton(self, id, wx.Bitmap("data/icons/color_wheel.png", wx.BITMAP_TYPE_PNG))
        self.colourChooserDialog = wx.ColourDialog(self)
        self.colourChooserDialog.CentreOnScreen()
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
        self.SetAutoLayout(True)
        self.staticBitmap.Show(True)
        self.mainSizer.Fit(self)
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
        print 'Hello'
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
        self.GetParent().Dismiss()
        clickedButton = self.colourChooserDialog.ShowModal()
        if clickedButton == wx.ID_OK:
            colour = self.colourChooserDialog.GetColourData().GetColour()
            self.colourPanel.SetBackgroundColour(colour)
            self.SetColour(colour)
            self.colourTextCtrl.SetValue(self.colour.GetAsString(wx.C2S_HTML_SYNTAX))
            self.button.SetBackgroundColour(self.colour)
            self.Show(False)
            #The parent of the panel is the wxPopupTransientWindow
            self.GetParent().Dismiss()
        elif clickedButton == wx.ID_CANCEL:
            self.GetParent().Popup()
            return
        
    def OnMouseDown(self, event):
        x, y = event.GetPosition()
        r = self.image.GetRed(x, y) 
        g = self.image.GetGreen(x, y)
        b = self.image.GetBlue(x, y)
        self.colour.Set(r, g, b)
        self.button.SetColour(self.colour)
        self.Show(False)
        self.GetParent().Dismiss()
        
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

   
        
class ColourPickerWidget(wx.Button):
    '''
    A Widget that shows a panel contains an image which 
    resembles a palette of colors the user can choose from. 
  '''
    def __init__(self, parent, id, colour, pos = wx.DefaultPosition,  size = (25,25), 
       style=0, validator = wx.DefaultValidator, name = "button"):
        wx.Button.__init__(self, parent, id, wx.EmptyString, pos, size, style, validator, name)
        self.Show(True)
        
        self.bmpImage = wx.Bitmap("data/palettes/colorcube.gif", wx.BITMAP_TYPE_GIF)
        self.popupWindow = wx.PopupTransientWindow(parent)
        self.popupWindow.SetAutoLayout(True)
        self.panel = ColourPickerPanel(self.popupWindow, self.bmpImage, id, wx.DefaultPosition
                ,wx.TAB_TRAVERSAL)
        self.popupWindow.Dismiss()
        self.panel.GetSizer().Fit(self.popupWindow)
        self.panel.Show(True)
        self.panel.SetButton(self)
        self.SetColour(colour)
        self.Bind(wx.EVT_BUTTON, self.OnClickButton) 
       
    def SetColour(self, colour):
        if colour.__class__!=wx.Colour:
            colour = wx.Color(colour[0]*255,colour[1]*255,colour[2]*255,colour[3]*255)
        self.panel.SetColour(colour)
        self.SetBackgroundColour(colour)
        
    def GetColour(self):
        colour =  self.panel.GetColour().Get(True)
        colour = (colour[0]/255.0,colour[1]/255.0,colour[2]/255.0,colour[3]/255.0)
        return colour
    
    def OnClickButton(self, event):
        '''
        Event Generated when the button clicked
        '''
        buttonPosTuple = self.GetScreenPositionTuple()
        self.popupWindow.Position((buttonPosTuple[0] , buttonPosTuple[1] ), wx.DefaultSize)
        if self.popupWindow.IsShown() == True:
            self.SetColour(self.panel.GetColour())
            self.popupWindow.Dismiss()
            return
        self.popupWindow.Popup()
        self.panel.Show(True)


if __name__ == "__main__":
    a = wx.App()
    frame = wx.Frame(None, -1, "Hello", size = (500, 500))
    x = ColourPickerWidget(frame, -1, wx.CYAN, pos = (200, 300), size = (30, 30))
    print x.GetColour()
    frame.Show(True)
    a.MainLoop()
