# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:05:11 2022

@author: Marco

Correlation done with:
    Copyright (c) 2019, P. Lutus -- http://arachnoid.com. All Rights Reserved.

"""
"""
InsideTempCorrelation
Polynomial degree 4, 241 x,y data pairs.
Correlation coefficient = 0.9997171165381333
Standard error = 0.35208126666591477
"""

InsideTempTerms = [
    -4.1075415767994585e+001,
     9.0300926316279206e-001,
    -5.9669197944509289e-003,
     2.3165028761097425e-005,
    -3.1737020760081827e-008
]

def InsideTemp(x):
  t = 1
  r = 0
  for c in InsideTempTerms:
    r += c * t
    t *= x
  return r



"""
OutsideTempCorrelation
Polynomial degree 5, 251 x,y data pairs.
Correlation coefficient = 0.9995725991459548
Standard error = 0.44787351623417965
"""

OutsideTempTerms = [
    -5.1227476301011251e+001,
     1.3181773134624792e+000,
    -1.5558812075030267e-002,
     1.1042275454463521e-004,
    -3.8062650831707564e-007,
     5.0900287913663655e-010
]

def OutsideTemp(x):
  t = 1
  r = 0
  for c in OutsideTempTerms:
    r += c * t
    t *= x
  return r