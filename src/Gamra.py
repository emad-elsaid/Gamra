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
        #commented because it hides hte menubar if enabled
        #Splash("data/icons/splash.png",3000) #obj to show splash 3sec 
        self.AppName = "Gamra"
        self.VendorName = "Schoolar Projects"
        self.Version = "0.1"
        
        self.Frame = MainFrame(size=wx.Size(1000,600))
        self.Frame.Show(True)
        self.SetTopWindow = self.Frame
        return True


if __name__ == '__main__':
    gamra_obj = Gamra()
    gamra_obj.MainLoop()
