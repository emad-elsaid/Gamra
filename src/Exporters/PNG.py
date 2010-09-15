'''
Created on Jul 9, 2010

@author: blaze
'''
import wx
import cairo
from Exporters.Generic import Generic


class PNG(Generic):

    def __init__(self):
        Generic.__init__(self, "Export PNG Image", "PNG file (*.png)|*.png", 'png')
        
    def Export(self):
        document = wx.GetApp().Frame.Canvas.Document
        objects = document.Objects
        
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, document.Width, document.Height )
        ctx = cairo.Context(surface)
        for i in objects :
            i.Apply(ctx)
            
        surface.write_to_png(self.File)