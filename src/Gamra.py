#!/usr/bin/python
'''
Created on Jun 3, 2010

@author: blaze
'''

from wx import App
from MainFrame import MainFrame

class Gamra(App):
    def OnInit(self):
        self.AppName = "Gamra"
        self.VendorName = "Schoolar Projects"
        self.Version = "0.1"
        
        frame = MainFrame()
        frame.Show(True)
        self.SetTopWindow(frame)
        return True


if __name__ == '__main__':
    gamra_obj = Gamra()
    gamra_obj.MainLoop()