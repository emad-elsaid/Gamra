'''
Created on Jun 4, 2010

@author: blaze
'''
import wx

class AboutBox:
    '''
    the application specific about dialog 
    with information added
    '''
    def __init__(self):
        self.info = wx.AboutDialogInfo()
        
        self.info.Copyright = "All rights reserved for Schoolar Group"
        self.info.Description = "Gamra is a program aim to help webdesigners to \
create beautiful website using raster and vector images"
        self.info.AddDeveloper("Emad Elsaid <Blazeeboy@gmail.com>")
        self.info.Version = '0.1'
        self.info.Icon = wx.Icon('icon256.png',wx.BITMAP_TYPE_PNG)
        self.info.WebSite = "http://www.Gamra.com"
        
        self.info.SetLicence('''
        This program is free software; you can redistribute it and/or modify
       it under the terms of the GNU General Public License as published by
       the Free Software Foundation; either version 2 of the License, or
       (at your option) any later version.
       
       This program is distributed in the hope that it will be useful,
       but WITHOUT ANY WARRANTY; without even the implied warranty of
       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
       GNU General Public License for more details.
       
       You should have received a copy of the GNU General Public License
       along with this program; if not, write to the Free Software
       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
       MA 02110-1301, USA.
        ''')
        
    def Show(self):
        wx.AboutBox(self.info)