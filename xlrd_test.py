#!/usr/bin/env python
# coding=utf-8

import xlrd

data = xlrd.open_workbook('test.xls');
table = data.sheet_by_name(u'极限负载');
print table;
cell_C20 = table.cell(19, ord('C') - ord('A')).value;
print cell_C20;
