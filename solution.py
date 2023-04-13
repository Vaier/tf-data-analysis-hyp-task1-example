import pandas as pd
import numpy as np
import scipy.stats as stats

chat_id = 1251251937

def solution(x_success: int,
             x_cnt: int,
             y_success: int,
             leads_test: int) -> bool:
    control_failures = x_cnt - x_success
    test_failures =  leads_test - y_success
    table = [[x_success, control_failures], [y_success, test_failures]]
    row_totals = [sum(row) for row in table]
    col_totals = [sum(col) for col in zip(*table)]
    total = sum(table[0]) + sum(table[1])
    expected = [[row_totals[i] * col_totals[j] / total for j in range(2)] for i in range(2)]
    chisq, pval = stats.chisquare([table[0][0], table[1][0]], f_exp=[expected[0][0], expected[1][0]])
    alpha = 0.07
    return pval < alpha
