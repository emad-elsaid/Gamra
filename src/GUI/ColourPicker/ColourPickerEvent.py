'''
Created on Jun 18, 2010

@author: ramdac
'''

import wx

""" A custom made Event Type"""
wxEVT_COLOURPICKER = wx.NewEventType()

class ColourPickerEvent(wx.Event):
    """
    A custom made Event generated when colour is chosen 
    from the ColourPickerButton
    """
    def __init__(self, id = wx.ID_ANY):
        wx.Event.__init__(id, wxEVT_COLOURPICKER)
        print "Colour Changed"
        
    
    