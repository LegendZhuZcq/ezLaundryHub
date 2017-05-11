#!/usr/bin/python

import wx
import os
import ouimeaux
from ouimeaux.environment import Environment

machine1Code = "1001"
machine2Code = "1002"

env = Environment()
env.start()
env.discover(5)

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size = (600,300))
        panel = wx.Panel(self, wx.ID_ANY)
        self.instruction = wx.StaticText(panel, label="Type your access code:", pos = (20,5))
        self.textbox = wx.TextCtrl(panel, value = "", pos =(20,35), size = (350,30))
        self.confirmButton = wx.Button(panel, label = "Enter", pos =(180,65), size = (60,35))
        self.Bind(wx.EVT_BUTTON, self.ConfirmClick,self.confirmButton)
        #Create Number Panel
        buttonVertical = 55
        for row in (("1","2","3","4","5"),("6","7","8","9", "0"),("c")):
            buttonVertical = buttonVertical + 45
            buttonHorizon = 50
            for label in row:
                b=wx.Button(panel, -1, label, pos=(buttonHorizon, buttonVertical), size = (55,35))
                buttonHorizon = buttonHorizon + 60
                self.Bind(wx.EVT_BUTTON, self.OnButton, b)

        
        self.Show(True)

    def ConfirmClick(self, event):
        accessCode = self.textbox.GetValue()
        if accessCode == machine1Code or accessCode == machine2Code:
            selectedSwitch = env.get_switch	('1').on()
            self.instruction.SetLabel("Machine 1 is ready")

    def OnButton(self, event):
                 label = event.GetEventObject().GetLabel()
                 if label == "c": self.textbox.SetValue("")
                 else:self.textbox.SetValue(self.textbox.GetValue()+label)
            
 
app = wx.App(False)
frame = MyFrame(None, 'ezLaundry')
app.MainLoop()
                
