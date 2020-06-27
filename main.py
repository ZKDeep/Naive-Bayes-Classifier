# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 12:54:06 2020

@author: zubair
"""

import numpy as np
import pandas as pd
import model


### call your classification dataset here
data = pd.read_csv("vertebrate.csv")


## call the attribute indexes here
cols_x = [1,2,3,4,5,6,7]
x = data[data.columns[cols_x]]

## call the label index from dataset here
cols_y = [8]
y = data[data.columns[cols_y]]


### pass your test record directly here only with attribute values only.
test_record_1 = ['cold-blooded', 'scales', 'yes', 'yes', 'no', 'no', 'no']



clas, prob = model.test(test_record_1, x, y)

#np.argmax(prob)
print("Your test record is from Class =========> " + clas[np.argmax(prob)])





