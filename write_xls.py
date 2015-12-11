#!/usr/bin/env python
# coding=utf-8

from xlrd import open_workbook;
from xlwt import easyxf;
from xlutils.copy import copy;
from xlutils.styles import Styles

def set_cell(ws, col, row, val, style):
    ws.write(row - 1, ord(col) - ord('A'), val, style);

rb = open_workbook("test.xls", formatting_info = True, on_demand = True);
wb = copy(rb);

# 极限负载
ws = wb.get_sheet(1);
rs = rb.sheet_by_name(u'极限负载');

styles = Styles(rb);
K20_style = styles[rs.cell(19, ord('K') - ord('A'))];
K20_xf = K20_style.xf;
K20_font = rb.font_list[0]#K20_style.xf.font_index];
print rb.colour_map[K20_font.colour_index];

style = easyxf(u'alignment: horizontal center, vertical center;'
        u'font: name 宋体, height 240');
rows = range(0, 20);
for val in rows:
    set_cell(ws, chr(ord('B') + val), 20, 123.45, styles[rs.cell(19, ord('B') - ord('A') + val)]);
wb.save("test2.xls");
