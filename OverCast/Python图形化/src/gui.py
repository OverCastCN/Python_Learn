#coding:utf-8
import wx

# 显示窗口
# app = wx.App()
# frame = wx.Frame(None)
# frame.Show()
#
# app.MainLoop()

# 增加按钮
# app = wx.App()
# frame = wx.Frame(None)
# btn = wx.Button(frame)
# frame.Show()
# app.MainLoop()

# app = wx.App()
# frame = wx.Frame(None,title = "Simeple Editor")
# loadButton = wx.Button(frame,label ='open')
# saveButton = wx.Button(frame,label = "save")
# # 这个部分的save按妞会被覆盖
# frame.Show()
#
# app.MainLoop()

app = wx.App()
frame = wx.Frame(None,title = "Simeple Editor",size = (410,355))
loadButton = wx.Button(frame,label ='open',pos = (255,5),size = (80,25))
saveButton = wx.Button(frame,label = "save",pos = (355,5),size = (80,25))
framename = wx.TextCtrl(frame,pos= (5,5),size = (210,25))
contents = wx.TextCtrl(frame,pos = (5,5),size = (390,260),style =wx.TE_MULTILINE|wx.HSCROLL)

frame.Show()

app.MainLoop()
