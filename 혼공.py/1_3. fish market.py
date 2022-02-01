# 모듈 임포트
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 맥 에서 엑셀 파일 열때
import openpyxl
import xlrd

# fish data 가져오기
df = pd.read_csv('/Users/noyeonjeong/Desktop/python workspace/혼공.py/Fish.csv')
# print(df)

# bream 데이터 처리 (length2, weight)
bream_dataframe = df[df.Species  == 'Bream']
# print(bream_dataframe)
bream_length = []
bream_length.append(bream_dataframe['Length2'])
bream_weight =[]
bream_weight.append(bream_dataframe['Weight'])
# print(bream_length)
# print(bream_weight)

# bream 데이터 시각화
# plt.scatter(bream_length, bream_weight)
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

# smelt 데이터 처리 (length2, weight)
smelt_dataframe = df[df.Species == 'Smelt']
# print(smelt_dataframe)
smelt_length =[]
smelt_length.append(smelt_dataframe['Length2'])
smelt_weight =[]
smelt_weight.append(smelt_dataframe['Weight'])

# smelt 데이터 시각화
# plt.scatter(smelt_length, smelt_weight)
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

# bream 그래프 + smelt 그래프
# plt.scatter(bream_length, bream_weight)
# plt.scatter(smelt_length, smelt_weight)
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

# 머신러닝 등장
# fish data 변수에다 하나로 합치기
length = bream_length + smelt_length
weight = bream_weight + smelt_weight
# print(type(length))
# print(type(weight))

for len, wei in zip(length, weight):
    print(len, wei)
