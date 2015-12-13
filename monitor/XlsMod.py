#!/usr/bin/env python
# coding=utf-8

from xlrd import open_workbook;
from xlwt import easyxf;
from xlutils.copy import copy;
from xlutils.styles import Styles

class XlsMod:
    testApiSet = set(["SEND_HB", "OPEN_HB", "GET_SEND", "GET_RECV"])
    apiRowMap = {"SEND_HB": 19, "RUSH_CHECK": 20, "OPEN_CHECK": 21, "OPEN_HB_100": 22, "OPEN_HB": 23,
            "CHANGE_STATUS": 24, "GET_DHEADER": 25, "GET_DLIST": 26, "GET_SEND": 27, "GET_RECV": 28,
            "DEL_SEND": 29, "DEL_RECV": 30};
    dataColMap = {"THREAD_NUM": 1, "TPS": 2, "AVG_TIME": 3, "MAX_TIME": 4, "LEVEL3": 5, "LEVEL2": 6,
            "LEVEL1": 7, "LSVR_CPU": 8, "LRSYNC_CPU": 9, "LSVR_IN": 10, "LSVR_OUT": 11, "SR_ACCESS_CPU": 12,
            "SR_ACCESS_IN": 13, "SR_ACCESS_OUT": 14, "D_ACCESS_CPU": 15, "D_ACCESS_IN": 16, "D_ACCESS_OUT": 17,
            "SR_CACHE_CPU": 18, "SR_CACHE_IN": 19, "SR_CACHE_OUT": 20, "D_CACHE_CPU": 21, "D_CACHE_IN": 22,
            "D_CACHE_OUT": 23};
    def __init__(self, name):
        self.filename = name;
        self.rb = open_workbook(self.filename, formatting_info = True, on_demand = True);
        self.wb = copy(self.rb);

    def GetCellStyle(self, row, col, sheet_idx = 0):
        rsheet = self.rb.sheet_by_index(sheet_idx);
        c = rsheet.cell(row, col);
        xf = self.rb.xf_list[c.xf_index];
        font = self.rb.font_list[xf.font_index];
        fontName = font.name;
        fontHeight = font.height;
        style = easyxf(u'alignment: horizontal center, vertical center;'
                'font: name %s, height %s;' % (fontName, fontHeight));
        return style;

    def SetCell(self, row, col, val, sheet_idx = 0):
        style = self.GetCellStyle(row, col, sheet_idx);
        wsheet = self.wb.get_sheet(sheet_idx);
        wsheet.write(row, col, val, style);

    def Save(self, filename):
        self.wb.save(filename);

if __name__ == "__main__":
    xlsMod = XlsMod("test.xls");
    for key in XlsMod.dataColMap:
        xlsMod.SetCell(XlsMod.apiRowMap["SEND_HB"], XlsMod.dataColMap[key], XlsMod.dataColMap[key], 1);
    xlsMod.Save("target.xls");
