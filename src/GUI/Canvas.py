'''
Created on Jun 9, 2010

@author: blaze
'''
import wx
from wx.lib.floatcanvas.FloatCanvas import FloatCanvas

class Canvas(wx.ScrolledWindow):
    '''
    the canvas with a scrolled window, this will 
    abstract the operations of
    draw, scroll, resize,...etc
    '''


    def __init__(self, parent ,id=-1, pos = wx.DefaultPosition, 
                 size = wx.Size(1000,1000), style = [wx.HSCROLL, wx.VSCROLL],
                 name = "scrolledWindow"):
        
        wx.ScrolledWindow.__init__(self, parent, id, pos)
        self.canvas = FloatCanvas( self, -1, size )
        self.SetScrollbars( 20, 20, size[0]/20, size[1]/20 )