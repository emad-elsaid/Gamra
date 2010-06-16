#!/usr/bin/python
'''
Created on Jun 3, 2010

@author: blaze
'''

import wx
from GUI.MainFrame import MainFrame
from GUI.Splash import Splash


class Gamra(wx.App):
    def OnInit(self):
        Splash("icons/splash.png",3000) #obj to show splash 3sec 
        self.AppName = "Gamra"
        self.VendorName = "Schoolar Projects"
        self.Version = "0.1"
        
        frame = MainFrame(size=wx.Size(1000,600))
        frame.Show(True)
        self.SetTopWindow = frame
        return True


if __name__ == '__main__':
    gamra_obj = Gamra()
    gamra_obj.MainLoop()
