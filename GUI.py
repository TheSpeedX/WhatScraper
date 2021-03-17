# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Oct 26 2018)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class MainFrame
###########################################################################


class MainFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"WhatScraper GUI", pos=wx.DefaultPosition, size=wx.Size(
            500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        HeaderSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.TitleText = wx.StaticText(
            self, wx.ID_ANY, u"WhatScraper", wx.DefaultPosition, wx.DefaultSize, 0)
        self.TitleText.Wrap(-1)

        self.TitleText.SetFont(wx.Font(
            14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))

        HeaderSizer.Add(self.TitleText, 0, wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(
            self, wx.ID_ANY, u"Scrape indefinitely", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        HeaderSizer.Add(self.m_staticText2, 0, wx.TOP |
                        wx.BOTTOM | wx.RIGHT, 15)

        bSizer1.Add(HeaderSizer, 0, wx.ALL | wx.EXPAND, 10)

        ScraperMenuSizer = wx.BoxSizer(wx.VERTICAL)

        CategorySizer = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Scrape Origin"), wx.VERTICAL)

        self.radio_Google = wx.RadioButton(CategorySizer.GetStaticBox(
        ), wx.ID_ANY, u"From Google Search", wx.DefaultPosition, wx.DefaultSize, 0)
        CategorySizer.Add(self.radio_Google, 0, wx.ALL, 5)

        self.radio_ListSite = wx.RadioButton(CategorySizer.GetStaticBox(
        ), wx.ID_ANY, u"Group Sharing Sites", wx.DefaultPosition, wx.DefaultSize, 0)
        CategorySizer.Add(self.radio_ListSite, 0, wx.ALL, 5)

        self.radio_CheckFile = wx.RadioButton(CategorySizer.GetStaticBox(
        ), wx.ID_ANY, u"From File", wx.DefaultPosition, wx.DefaultSize, 0)
        self.radio_CheckFile.Enable(False)

        CategorySizer.Add(self.radio_CheckFile, 0, wx.ALL, 5)

        ScraperMenuSizer.Add(CategorySizer, 1, wx.ALIGN_TOP |
                             wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        self.ScraperScrollWindow = wx.ScrolledWindow(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL | wx.VSCROLL)
        self.ScraperScrollWindow.SetScrollRate(5, 5)
        MainScraperSizer = wx.BoxSizer(wx.VERTICAL)

        self.button_StartScraper = wx.Button(
            self.ScraperScrollWindow, wx.ID_ANY, u"Start Scraper", wx.DefaultPosition, wx.DefaultSize, 0)
        MainScraperSizer.Add(self.button_StartScraper, 0, wx.ALL, 5)

        self.ScrapedList = wx.ListCtrl(
            self.ScraperScrollWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        MainScraperSizer.Add(self.ScrapedList, 0, wx.ALIGN_TOP | wx.EXPAND, 5)

        self.ScraperScrollWindow.SetSizer(MainScraperSizer)
        self.ScraperScrollWindow.Layout()
        MainScraperSizer.Fit(self.ScraperScrollWindow)
        ScraperMenuSizer.Add(self.ScraperScrollWindow,
                             3, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(ScraperMenuSizer, 3, wx.ALIGN_TOP | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.radio_Google.Bind(wx.EVT_RADIOBUTTON, self.RadioGoogle)
        self.radio_ListSite.Bind(wx.EVT_RADIOBUTTON, self.RadioListSite)
        self.radio_CheckFile.Bind(wx.EVT_RADIOBUTTON, self.RadioCheckFile)
        self.button_StartScraper.Bind(wx.EVT_BUTTON, self.startScraper)

        # Initialize Columns
        self.ScrapedList.InsertColumn(0, "Group Name", width=100)
        self.ScrapedList.InsertColumn(1, "Group URL", width=100)

        self.ScrapedData = list()
        self.SelectedInformationOrigin = 0

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def RadioGoogle(self, event):
        event.Skip()

    def RadioListSite(self, event):
        event.Skip()

    def RadioCheckFile(self, event):
        event.Skip()

    def startScraper(self, event):
        event.Skip()

    # Append to list function
    def appendObjectToList(self, input_object: tuple):
        self.ScrapedData.append(input_object)
        self.ScrapedList.DeleteAllItems()
        for object in self.ScrapedData:
            index = self.ScrapedList.InsertItem(
                len(self.ScrapedData),
                0
            )
            self.ScrapedList.SetItem(index, 0, object[0])
            self.ScrapedList.SetItem(index, 1, object[1])
            self.ScrapedList.SetItemData(index, 0)
