'''
Created on Jul 8, 2010

@author: blaze
'''
import wx
import GUI.Menus
from GUI.Menus import *

class MenuBar(wx.MenuBar):

    def __init__(self):
        wx.MenuBar.__init__(self)
        
        menuList = []
        for menu in GUI.Menus.__all__ :
            menuTemp = eval(menu+'.'+menu+'()')
            menuList.append((menuTemp.Priority,menuTemp))
        menuList.sort(reverse=True)
        
        self.Handlers = []
        for priority,menu in menuList :
            self.Append(menu,menu.Label)  
            self.Handlers.extend(menu.Handlers)