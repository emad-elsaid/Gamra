'''
Created on Jun 9, 2010

@author: blaze
'''
import wx
import Document

class Canvas(wx.Panel):
    '''
    the canvas with a scrolled window, this will 
    abstract the operations of
    draw, scroll, resize,...etc
    '''
    def __init__(self, parent ):
        wx.Panel.__init__(self, parent, -1,style=wx.FULL_REPAINT_ON_RESIZE)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Document = Document.Document(500, 500)
