'''
Created on Jun 18, 2010

@author: ramdac
'''

import wx
import wx.lib.newevent
""" A custom made Event Type"""
myEVT_COLOURPICKER = wx.NewEventType()
EVT_COLOURPICKER = wx.PyEventBinder(myEVT_COLOURPICKER, 1)


class ColourPickerEvent(wx.PyCommandEvent):
    """
    A custom made Event generated when colour is chosen 
    from the ColourPickerButton
    """
    def __init__(self, evtType, winid, colour = None ):
        wx.PyCommandEvent.__init__(self, evtType, winid)
        self.colour = colour
    
    def GetColour(self):
        return (self.colour[0]/255.0, self.colour[1]/255.0, self.colour[2]/255.0, self.colour[3]/255.0)
        
