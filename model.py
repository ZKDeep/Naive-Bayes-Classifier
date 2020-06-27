# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 15:40:48 2020

@author: zubair
"""
import numpy as np

def nc(value, attribute, x , y, label):
    count = 0
    records_x = x[attribute]
    col_y = y.columns[0]
    records_y = y[col_y]
    if isinstance(value,int) == True: 
        re = []
        #print("new function")
        for objs in range(len(records_x)):
            if records_y[objs] == label:
                re.append(records_x[objs])
                red = np.array(re)
        mean = np.average(red)
        stand_d = np.std(red)
        prob = (1/(np.sqrt((2*np.pi)) * stand_d)) * np.exp2(-((value - mean)*(value - mean))/(2*(stand_d)*(stand_d)))
        return(prob)
    else:
        for objs in range(len(records_x)):
            #print(records_x[objs])
            if value == records_x[objs] and label == records_y[objs]:
                count = count + 1
    if isinstance(value,int) == False and count == 0:
        mss = m_est(x,y, attribute, label)
        return(mss)
#        isinstance(25,int)
    else:        
        prob = count/ y[y.values == label].shape[0]
        return(prob)


    

def unique_a_c(x, y):
    att = []
    uni = []
    classes = []
    for i in range(len(x.columns)):
        col = x.columns[i]
        att.append(col)
        coll = x[col]
        a = np.array(coll)
        unique = np.unique(a)
        uni.append(unique)
    #print(y)
    un = np.array(y)
    un = np.unique(un)
    classes = un  
    return(uni, att, classes)


def test(test_record, x, y):
    uni, att, classes = (unique_a_c(x,y))
    results = []
    for label in classes:
        #print(label)
        pp = []
        for i in range(len(att)):
            value = test_record[i]
            attribute = att[i]
            #print(attribute + "= " + str(value))
            prob = nc(value, attribute, x, y, label)
            #print(prob)
            #print(prob)
            pp.append(prob)
        product = 1
        
        for item in pp:
            product = product * item
        results.append(product)
    return(classes, results)
    


def m(y, label):
    count = 0
    yz = np.array(y)
    for lab in yz:
        #print(lab)
        if label == lab:
            count = count + 1
    return(count)

def m_est(x,y, attribute, label):
    n = len(x)
    #n_c = nc(x, y, attribute, label)
    n_c = 0
    m_m = m(y, label)
    p = 1/m_m
    
    p_x_y = (n_c + (m_m*p))/(n + m_m)
    return(p_x_y)