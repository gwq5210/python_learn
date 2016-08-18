#!/usr/bin/env python
# coding=utf-8

from xlrd import open_workbook;
from xlwt import easyxf;
from xlutils.copy import copy;
from xlutils.styles import Styles

class XlsMod:
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
    xlsMod.Save("target.xls");
