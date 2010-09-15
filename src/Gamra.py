#!/usr/bin/python
'''
Created on Jun 3, 2010

@author: blaze
'''

import wx
import os.path
from GUI.MainFrame import MainFrame
from GUI.Splash import Splash


class Gamra(wx.App):
    def OnInit(self):

        Splash(1)
        self.AppName = "Gamra"
        self.VendorName = "Schoolar Projects"
        self.Version = "0.1"
        
        self.Frame = MainFrame(size=(1000,600))
        self.SetTopWindow(self.Frame)
        self.Frame.Show()
        
        return True


if __name__ == '__main__':
    gamra_obj = Gamra()
    gamra_obj.MainLoop()
