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
K20_cell = rs.cell(19, ord('A') - ord('A'));
#K20_style = styles[rs.cell(0, ord('A') - ord('A'))];
K20_style = styles[K20_cell];
print K20_style;
#K20_xf = K20_style.xf;
K20_xf = rb.xf_list[K20_cell.xf_index];
print K20_cell.xf_index;
print K20_xf;
print K20_xf.is_style;
K20_font = rb.font_list[K20_xf.font_index];
print K20_font;
print K20_font.name;
print K20_font.height;
print rb.colour_map[K20_font.colour_index];
print K20_xf.background;
print K20_xf.background.background_colour_index;
print K20_xf.background.pattern_colour_index;
print rb.colour_map[K20_xf.background.background_colour_index];
color = K20_xf.background.pattern_colour_index;
print color;

style = easyxf(u'alignment: horizontal center, vertical center;'
        'font: name %s, height %s;' % (K20_font.name, K20_font.height),
        'pattern: pattern solid, fore_colour red;');
#style = parent_style;
rows = range(0, 20);
for val in rows:
    set_cell(ws, chr(ord('B') + val), 20, 123.45, style);
wb.save("test2.xls");
