import wx
import wx.grid as grid
class MyApp(wx.App):
    '''Application Class'''
    def OnInit(self):
        '''Initialize'''
        self.frame = MyFrame()
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

class DisplayPanel(wx.Panel):
    '''class myPanel'''
    
    def __init__(self, parent):
        '''Constructor'''
        wx.Panel.__init__(self, parent)
       
        self.SetBackgroundColour(wx.Colour(228, 228, 128))
        self.SetSize(wx.Size(1101, 601))
        
        self.InitUI()

    def InitUI(self):
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        

    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        for i in range(0, 1210, 110):
            pass
            dc.DrawLine(i, 0, i, 600)
            #dc.DrawLine(0, j, 1100, j)
            #print(f'drawing line: ({i}, 0) to ({i}, 600)' )
        #Draw horizontal lines
        for j in range(0, 675, 75):
            #dc.DrawLine(i, 0, i, 600)
            dc.DrawLine(0, j, 1100, j)
        # for i in range(0, 1200, 100):
        #     for j in range(0, 600, 60):
        #         dc.DrawLine(0, j, 1100, j)
        for k in range(0, 600, 15):
            dc.DrawLine(545, k, 555, k)
        for k in range(0, 1100, 22):
            dc.DrawLine(k, 295, k, 305)

class TimeBasePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, pos=(0, 600))
        self.SetBackgroundColour(wx.Colour(128, 128, 228))
        self.SetSize(wx.Size(600, 99))

        btn1us = wx.Button(self, label='1us', pos=(30, 620),
        size=(wx.Size(50, 30)))
        self.Bind(wx.EVT_BUTTON, self.meas1ms, btn1us)
        #self.Layout()
    def meas1ms(self, ev ):
        pass
class TimeBasePanel2(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, pos=(0, 600))
        self.SetBackgroundColour(wx.Colour(255, 128, 228))
        #self.SetSize(wx.Size(1101, 99))        
        self.SetSize(wx.Size(600, 99)) 
    #def IsShown(self):

class VoltScalePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, pos=(1100, 0))
        self.SetBackgroundColour(wx.Colour(128, 228, 128))
        self.SetSize(wx.Size(199, 600))
        

class VoltScalePanel2(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, pos=(1100, 0))
        self.SetBackgroundColour(wx.Colour(128, 228, 228))
        self.SetSize(wx.Size(199, 600))
        
class MyFrame(wx.Frame):
    '''Class to build the Frame'''
    def __init__(self):
        ''' Constructor '''
        wx.Frame.__init__(self, None, title='Box sizers', size=(1300, 718))
        self.panel = DisplayPanel(self)
        self.panel1= TimeBasePanel(self)
        self.panel2= TimeBasePanel2(self)
        #self.panel2.Hide()

        self.panel3 = VoltScalePanel2(self)
        
        sizer = wx.BoxSizer()
        self.SetBackgroundColour(wx.Colour(100, 100, 255))
        self.SetSizer(sizer)
        x_Meas_Button = wx.Button(self, label='X-Measure', pos=(1010, 620),
        size=(wx.Size(90, 30)))
        self.Bind(wx.EVT_BUTTON, self.switchTimeMenu, x_Meas_Button)
        #self.Show()
        self.Layout()       

    def switchTimeMenu(self, event):
        if self.panel1.IsShown():
            self.panel1.Hide()
            self.panel2.Show()
        else:
            self.panel1.Show()
            self.panel2.Hide()
        self.Layout()

def main1():
    app = MyApp(False)
    #frame = MyFrame()
    app.MainLoop()

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='test2', size=(800, 600))
        self.splitter = wx.SplitterWindow(self)
        self.panelOne = MainPanel(self.splitter)

    def AddPanel(self):
        self.newPanel = SecondPanel(self, 1, 1)
        self.sizer.Add(self.newPanel, 1, wx.EXPAND)
        self.sizer.Layout()
class SecondPanel(wx.Panel):
    def __init__(self, parent, a, b):
        wx.Panel.__init__(self, parent=parent)

        MyGrid=grid.Grid(self)
        MyGrid.CreateGrid(a,b)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(MyGrid, 0, wx.EXPAND)
        self.SetSier(sizer)
class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.txtOne = wx.StaticText(self, -1, label='paradoba', pos=(20, 10))
        self.txtPlace = wx.TextCtrl(self, pos=(20,30))
        self.txtTwo = wx.StaticText(self, -1, label='', pos=(20, 40))
        self.SetBackgroundColour(wx.Colour(128, 128, 255))
        button = wx.Button(self, label = 'search', pos=(20, 70))
        button.Bind(wx.EVT_BUTTON, self.onButton)

    def onButton(self, event):
        var=self.txtPlace.GetValue()
        if len(var) == 9 or len(var) == 11:
            print('???')
        
        self.GetParent().GetParent().AddPanel()

def main2():
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main2()
    
