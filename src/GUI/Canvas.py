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
    def __init__(self, parent, size):
        wx.Panel.__init__(self, parent, -1)
        self.Document = Document.Document(size[0], size[1])