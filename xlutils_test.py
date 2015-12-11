#!/usr/bin/env python
# coding=utf-8

from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook("test.xls", formatting_info = True, on_demand = True);
rs = rb.sheet_by_name(u"极限负载");
wb = copy(rb);
ws = wb.get_sheet(1);
cell = ws.cell(20, ord('K') - ord('A'));
print cell;
ws.write(20, ord('K') - ord('A'), u"123.4");
wb.save("test2.xls");
