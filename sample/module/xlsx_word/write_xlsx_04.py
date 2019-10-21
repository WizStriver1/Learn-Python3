# -*- coding: utf-8 -*-
from datetime import datetime
import xlsxwriter

def main():

    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('Expenses04.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.set_default_row(20)
    worksheet.set_column('A:A', 10.88)
    worksheet.set_column('B:O', 16.5)
    worksheet.set_column('P:P', 24.75)

    title_format = workbook.add_format({
        'bold': True,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 13.5,
        'font_name': 'Microsoft YaHei UI'
    })

    diagonal_format = workbook.add_format({
        'diag_type': 2,
        'border': 1,
        'align': 'left',
        'valign': 'vcenter',
        'font_size': 11,
        'font_name': 'Microsoft YaHei UI'
    })

    normal_format = workbook.add_format({
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 11,
        'font_name': 'Microsoft YaHei UI'
    })

    th_expenses = [
        ['name', '登录名'],
        ['model_no', '构建次数'],
        ['SDE', '核心算法模块'],
        ['EVS', '解释方差分'],
        ['MAE', '平均绝对误差'],
        ['MSE', '均方误差'],
        ['MSLE', '均方对数误差'],
        ['Startdate', '样本选取起始日期'],
        ['Enddate', '样本选取的截止日期'],
        ['inputtime1', '样本预测跨度'],
        ['inputtime2', '样本预测长度'],
        ['r', '无风险利率'],
        ['kappa', '均值回归因子'],
        ['theta', '价格长期过程均值'],
        ['theta_SVS', '价格波动率的长期过程均值']
    ]

    worksheet.merge_range(0, 0, 0, len(th_expenses), u'江西财经大学——推断统计学在金融大数据分析中应用的虚拟仿真实验参数记录表', title_format)

    worksheet.merge_range('A2:A3', u'''              参数
      记录''', diagonal_format)

    # Start from the first cell. Rows and columns are zero indexed.
    row = 1
    col = 1

    for name, langname in th_expenses:
        worksheet.write_string  (row,       col, name,                       normal_format)
        worksheet.write_string  (row + 1,   col, langname.decode('utf-8'),   normal_format)
        col += 1

    row = 3
    col = 0

    val_expenses = [
        ['1', 'xxx', '1', 'GBMSDE1', '-0.7595764', '0.2972204', '0.1398859', '0.0000045', '2017-06-01', '2017-06-30', '10', '60', '0.05', '-', '-', '-'],
        ['1', 'xxx', '1', 'GBMSDE1', '-0.7595764', '0.2972204', '0.1398859', '0.0000045', '2017-06-01', '2017-06-30', '10', '60', '0.05', '-', '-', '-'],
        ['1', 'xxx', '1', 'GBMSDE1', '-0.7595764', '0.2972204', '0.1398859', '0.0000045', '2017-06-01', '2017-06-30', '10', '60', '0.05', '-', '-', '-'],
        ['1', 'xxx', '1', 'GBMSDE1', '-0.7595764', '0.2972204', '0.1398859', '0.0000045', '2017-06-01', '2017-06-30', '10', '60', '0.05', '-', '-', '-'],
        ['1', 'xxx', '1', 'GBMSDE1', '-0.7595764', '0.2972204', '0.1398859', '0.0000045', '2017-06-01', '2017-06-30', '10', '60', '0.05', '-', '-', '-']
    ]

    for val in val_expenses:
        for col_num in range(len(val)):
            worksheet.write_string  (row,   col + col_num, val[col_num].decode('utf-8'),   normal_format)
        row += 1

    workbook.close()

main()