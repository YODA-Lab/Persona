from basic_function import confidence_choose
from basic_function import inverse_function
from basic_function import sort_dict_by_values
from basic_function import spearman_rank_correlation

import pandas as pd
import random

k = 1
s = 1
def C1_1_trust_based_update(row, s, r):
	# h: True, i: True, f: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['h'] == True) & (df['i'] == True) & (df['f'] == True)].iterrows():
		add_sum = df[((df['h'] == False) | (df['i'] == False) | (df['f'] == False)) & ((df['a'] == row['a']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Third_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Third_response_based_updated'] +  k * add_sum

	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']* (1 - k))
	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def C1_1_trust_update():
	# h: True, i: True, f: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['h'] == True) & (df['i'] == True) & (df['f'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['h'] == True) & (df['i'] == True) & (df['f'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)



def C1_2_trust_based_update(row, s, r):
	# h: True, g: True, d: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['h'] == True) & (df['g'] == True) & (df['d'] == True)].iterrows():
		add_sum = df[((df['h'] == False) | (df['g'] == False) | (df['d'] == False)) & ((df['a'] == row['a']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['i'] == row['i']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Third_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Third_response_based_updated'] +  k * add_sum

	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']* (1 - k))
	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def C1_2_trust_update():
	# h: True, g: True, d: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['g'] == True) & (df['h'] == True) & (df['d'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['g'] == True) & (df['h'] == True) & (df['d'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def C1_3_trust_based_update(row, s, r):
	# h: True, g: True, a: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['h'] == True) & (df['g'] == True) & (df['a'] == True)].iterrows():
		add_sum = df[((df['h'] == False) | (df['g'] == False) | (df['a'] == False))&  ((df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['i'] == row['i']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Third_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Third_response_based_updated'] +  k * add_sum

	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']* (1 - k))
	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def C1_3_trust_update():
	# h: True, g: True, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['g'] == True) & (df['h'] == True) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['g'] == True) & (df['h'] == True) & (df['a'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)



def C2_1_trust_based_update(row, s, r):
	# h: True, i: True, g: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['h'] == True) & (df['g'] == True) & (df['i'] == True)].iterrows():
		add_sum = df[((df['h'] == False) | (df['g'] == False) | (df['i'] == False)) & ((df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['a'] == row['a']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Third_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Third_response_based_updated'] +  k * add_sum

	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']* (1 - k))
	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def C2_1_trust_update():
	# h: True, i: True, g: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['h'] == True) & (df['i'] == True) & (df['g'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['h'] == True) & (df['i'] == True) & (df['g'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def C2_2_trust_based_update(row, s, r):
	# g: False, h: True, a: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['h'] == True) & (df['g'] == False) & (df['a'] == True)].iterrows():
		add_sum = df[((df['h'] == False) | (df['g'] == True) | (df['a'] == False)) & ((df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['i'] == row['i']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Third_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Third_response_based_updated'] +  k * add_sum

	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']* (1 - k))
	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def C2_2_trust_update():
	# g: False, h: True, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['g'] == False) & (df['h'] == True) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['g'] == False) & (df['h'] == True) & (df['a'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def C2_3_trust_based_update(row, s, r):
	# h: True, g: True, a: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['h'] == True) & (df['g'] == True) & (df['a'] == True)].iterrows():
		add_sum = df[((df['h'] == False) | (df['g'] == False) | (df['a'] == False))&  ((df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['i'] == row['i']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Third_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Third_response_based_updated'] +  k * add_sum

	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']* (1 - k))
	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def C2_3_trust_update():
	# h: True, g: True, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['g'] == True) & (df['h'] == True) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['g'] == True) & (df['h'] == True) & (df['a'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def C3_1_trust_based_update(row, s, r):
	# h: True, i: True, f: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['h'] == True) & (df['f'] == True) & (df['i'] == True)].iterrows():
		add_sum = df[((df['h'] == False) | (df['f'] == False) | (df['i'] == False)) & ((df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['a'] == row['a']) & (df['g'] == row['g']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Third_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Third_response_based_updated'] +  k * add_sum

	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']* (1 - k))
	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def C3_1_trust_update():
	# h: True, i: True, g: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['h'] == True) & (df['i'] == True) & (df['f'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['h'] == True) & (df['i'] == True) & (df['f'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def C3_2_trust_based_update(row, s, r):
	# g: False, h: True, a: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['h'] == True) & (df['g'] == False) & (df['a'] == True)].iterrows():
		add_sum = df[((df['h'] == False) | (df['g'] == True) | (df['a'] == False)) & ((df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['i'] == row['i']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Third_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Third_response_based_updated'] +  k * add_sum

	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']* (1 - k))
	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def C3_2_trust_update():
	# g: False, h: True, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['g'] == False) & (df['h'] == True) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['g'] == False) & (df['h'] == True) & (df['a'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def C3_3_trust_based_update(row, s, r):
	# h: True, g: True, a: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['h'] == True) & (df['g'] == True) & (df['a'] == True)].iterrows():
		add_sum = df[((df['h'] == False) | (df['g'] == False) | (df['a'] == False))&  ((df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['i'] == row['i']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Third_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Third_response_based_updated'] +  k * add_sum

	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']* (1 - k))
	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)



def C3_3_trust_update():
	# h: True, g: True, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['g'] == True) & (df['h'] == True) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['g'] == True) & (df['h'] == True) & (df['a'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def fourth_trust_update(num1, num2):
	if num1 == 1:
		if num2 == 1:
			C1_1_trust_update()
		elif num2 == 2:
			C1_2_trust_update()
		elif num2 == 3:
			C1_3_trust_update()
	elif num1 == 2:
		if num2 == 1:
			C2_1_trust_update()
		elif num2 == 2:
			C2_2_trust_update()
		elif num2 == 3:
			C2_3_trust_update()
	elif num1 == 3:
		if num2 == 1:
			C3_1_trust_update()
		elif num2 == 2:
			C3_2_trust_update()
		elif num2 == 3:
			C3_3_trust_update()



def C1_1_1_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['f'] == True) | (df['j'] == True) | (df['h'] == True)].iterrows():
		add_sum = df[((df['f'] == False) & (df['e'] == False) & (df['d'] == row['d']) & (df['a'] == row['a'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['h'] == False) & (df['i'] == row['i']) & (df['j'] == False) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['f'] == False) & (df['j'] == False) & (df['h'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())

	df.to_csv('truth_table.csv', index=False)


def C1_1_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# j: False, h: False
	for index, row in df[(df['j'] == False) & (df['h'] == False)].iterrows():
		add_sum = df[((df['j'] == True) | (df['h'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['g'] == row['g']) & (df['i'] == row['i']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['i'] == False) | (df['f'] == False) | (df['k'] == False) | (df['j'] == False)].iterrows():
		add_sum = df[((df['f'] == True) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == row['a'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['h'] == True) & (df['i'] == True) & (df['j'] == True) & (df['k'] == True))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['i'] == True) &  (df['f'] == True) & (df['k'] == True) & (df['j'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())

	
	df.to_csv('truth_table.csv', index=False)

def C1_1_2_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['f'] == True) | (df['j'] == False) | (df['i'] == True)].iterrows():
		add_sum = df[((df['f'] == False) & (df['e'] == False) & (df['d'] == row['d']) & (df['a'] == row['a'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == row['h']) & (df['j'] == True) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['f'] == False) & (df['j'] == True) & (df['i'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def C1_1_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# j: True, i: False
	for index, row in df[(df['j'] == True) & (df['i'] == False)].iterrows():
		add_sum = df[((df['j'] == False) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['i'] == False) | (df['f'] == False) | (df['k'] == False) ].iterrows():
		add_sum = df[((df['f'] == True) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == row['a'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['h'] == True) & (df['i'] == True) & (df['j'] == row['j']) & (df['k'] == True))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['i'] == True) &  (df['f'] == True) & (df['k'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())

	
	df.to_csv('truth_table.csv', index=False)


def C1_1_3_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['f'] == True) | (df['j'] == False) | (df['i'] == True)].iterrows():
		add_sum = df[((df['f'] == False) & (df['e'] == False) & (df['d'] == row['d']) & (df['a'] == row['a'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == row['h']) & (df['j'] == True) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['f'] == False) & (df['j'] == True) & (df['i'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def C1_1_3_response_based_update():
	df = pd.read_csv('truth_table.csv')

	# j: True, i: False
	for index, row in df[(df['j'] == True) & (df['i'] == False)].iterrows():
		add_sum = df[((df['j'] == False) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['i'] == False) | (df['f'] == False) | (df['k'] == False) ].iterrows():
		add_sum = df[((df['f'] == True) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == row['a'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['h'] == True) & (df['i'] == True) & (df['j'] == row['j']) & (df['k'] == True))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['i'] == True) &  (df['f'] == True) & (df['k'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())

	
	df.to_csv('truth_table.csv', index=False)




def C1_2_1_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['d'] == True) | (df['i'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['d'] == False) & (df['a'] == row['a'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == row['h']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['d'] == False) & (df['i'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def C1_2_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, g: False
	for index, row in df[(df['g'] == False) & (df['i'] == False)].iterrows():
		add_sum = df[((df['g'] == True) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['h'] == row['h']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['g'] == False) | (df['d'] == False) | (df['j'] == False) ].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == True) & (df['a'] == row['a'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['i'] == row['i']) & (df['j'] == True) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['g'] == True) &  (df['d'] == True) & (df['j'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())

	
	df.to_csv('truth_table.csv', index=False)

def C1_2_2_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['d'] == True) | (df['i'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['d'] == False) & (df['a'] == row['a'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == row['h']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['d'] == False) & (df['i'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())




	df.to_csv('truth_table.csv', index=False)

def C1_2_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, d: False
	for index, row in df[(df['d'] == False) & (df['i'] == False)].iterrows():
		add_sum = df[((df['d'] == True) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['h'] == row['h']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['g'] == False) | (df['d'] == False) | (df['j'] == False) | (df['i'] == False) ].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == True) & (df['a'] == row['a'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['i'] == False) & (df['j'] == True) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['g'] == True) &  (df['d'] == True) & (df['j'] == True) & (df['i'] == True) , 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())

	
	df.to_csv('truth_table.csv', index=False)

def C1_2_3_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['d'] == True) | (df['i'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['d'] == False) & (df['a'] == row['a'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == row['h']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['d'] == False) & (df['i'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())


	df.to_csv('truth_table.csv', index=False)

def C1_2_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, d: False
	for index, row in df[(df['d'] == False) & (df['i'] == False)].iterrows():
		add_sum = df[((df['d'] == True) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['h'] == row['h']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['g'] == False) | (df['d'] == False) | (df['j'] == False) | (df['i'] == False) ].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == True) & (df['a'] == row['a'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['i'] == False) & (df['j'] == True) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['g'] == True) &  (df['d'] == True) & (df['j'] == True) & (df['i'] == True) , 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())

	df.to_csv('truth_table.csv', index=False)



def C1_3_1_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['a'] == True) | (df['i'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == row['h']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['a'] == False) & (df['i'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def C1_3_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, a: False
	for index, row in df[(df['a'] == False) & (df['i'] == False)].iterrows():
		add_sum = df[((df['a'] == True) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['h'] == row['h']) & (df['d'] == row['d']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['g'] == False) | (df['a'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['g'] == True) &  (df['a'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())

	
	df.to_csv('truth_table.csv', index=False)



def C1_3_2_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['a'] == True) | (df['i'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == row['h']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['a'] == False) & (df['i'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def C1_3_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, g: False
	for index, row in df[(df['g'] == False) & (df['i'] == False)].iterrows():
		add_sum = df[((df['g'] == True) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['h'] == row['h']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['g'] == False) | (df['a'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['g'] == True) &  (df['a'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())

	
	df.to_csv('truth_table.csv', index=False)



def C1_3_3_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['a'] == True) | (df['i'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == row['h']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['a'] == False) & (df['i'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def C1_3_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, a: False
	for index, row in df[(df['a'] == False) & (df['i'] == False)].iterrows():
		add_sum = df[((df['a'] == True) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['h'] == row['h']) & (df['d'] == row['d']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['g'] == False) | (df['a'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['g'] == True) &  (df['a'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())


	df.to_csv('truth_table.csv', index=False)


def C2_1_1_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['a'] == True) | (df['j'] == True)| (df['h'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == row['i']) & (df['h'] == False) & (df['j'] == False) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['a'] == False) & (df['j'] == False) & (df['h'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def C2_1_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# j: False, h: False
	for index, row in df[(df['j'] == False) & (df['h'] == False)].iterrows():
		add_sum = df[((df['j'] == True) | (df['h'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['g'] == row['g']) & (df['i'] == row['i']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['i'] == False) | (df['g'] == False) | (df['k'] == False) | (df['j'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == row['a'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['i'] == True) & (df['j'] == True) & (df['k'] == True))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['i'] == True) &  (df['g'] == True) & (df['k'] == True) & (df['j'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())
	
	df.to_csv('truth_table.csv', index=False)



def C2_1_2_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['a'] == True) | (df['j'] == False)| (df['i'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == row['h']) & (df['j'] == True) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['a'] == False) & (df['j'] == True) & (df['i'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())


	df.to_csv('truth_table.csv', index=False)

def C2_1_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# j: True, i: False
	for index, row in df[(df['j'] == True) & (df['i'] == False)].iterrows():
		add_sum = df[((df['j'] == False) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['i'] == False) | (df['g'] == False) | (df['k'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == row['a'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['i'] == True) & (df['j'] == row['j']) & (df['k'] == True))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['i'] == True) &  (df['g'] == True) & (df['k'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())

	
	df.to_csv('truth_table.csv', index=False)


def C2_1_3_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['a'] == True) | (df['j'] == False)| (df['i'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == row['h']) & (df['j'] == True) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['a'] == False) & (df['j'] == True) & (df['i'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def C2_1_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# j: True, i: False
	for index, row in df[(df['j'] == True) & (df['i'] == False)].iterrows():
		add_sum = df[((df['j'] == False) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['i'] == False) | (df['g'] == False) | (df['k'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == row['a'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['i'] == True) & (df['j'] == row['j']) & (df['k'] == True))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['i'] == True) &  (df['g'] == True) & (df['k'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())
	
	df.to_csv('truth_table.csv', index=False)


def C2_2_1_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['a'] == True) | (df['i'] == True)| (df['h'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == False) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['a'] == False) & (df['i'] == False) & (df['h'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def C2_2_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False (not spicy), h: False
	for index, row in df[(df['h'] == False) & (df['i'] == False)].iterrows():
		add_sum = df[((df['h'] == True) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['g'] == row['g']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['g'] == True) | (df['a'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['h'] == True) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['g'] ==False) &  (df['a'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())
	
	df.to_csv('truth_table.csv', index=False)


def C2_2_2_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['a'] == True) | (df['i'] == False)| (df['h'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == True) & (df['h'] == False) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['a'] == False) & (df['i'] == True) & (df['h'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)



def C2_2_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: True, h: False
	for index, row in df[(df['h'] == False) & (df['i'] == True)].iterrows():
		add_sum = df[((df['h'] == True) | (df['i'] == False)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['g'] == row['g']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['g'] == True) | (df['a'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['h'] == True) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['g'] ==False) &  (df['a'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())
	
	df.to_csv('truth_table.csv', index=False)


def C2_2_3_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['a'] == True) | (df['i'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == True) & (df['h'] == row['h']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['a'] == False) & (df['i'] == True), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())

	df.to_csv('truth_table.csv', index=False)


def C2_2_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: True, a: False
	for index, row in df[(df['a'] == False) & (df['i'] == True)].iterrows():
		add_sum = df[((df['a'] == True) | (df['i'] == False)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['h'] == row['h']) & (df['d'] == row['d']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['g'] == True) | (df['a'] == False) | (df['j'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['h'] == True) & (df['i'] == row['i']) & (df['j'] == True) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['g'] ==False) &  (df['a'] == True) &  (df['j'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())

	df.to_csv('truth_table.csv', index=False)

def C2_3_1_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['a'] == True) | (df['i'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == row['h']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['a'] == False) & (df['i'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def C2_3_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, a: False
	for index, row in df[(df['a'] == False) & (df['i'] == False)].iterrows():
		add_sum = df[((df['a'] == True) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['h'] == row['h']) & (df['d'] == row['d']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['g'] == False) | (df['a'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['g'] == True) &  (df['a'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())

	df.to_csv('truth_table.csv', index=False)


def C2_3_2_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['a'] == True) | (df['i'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == row['h']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['a'] == False) & (df['i'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def C2_3_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, g: False
	for index, row in df[(df['g'] == False) & (df['i'] == False)].iterrows():
		add_sum = df[((df['g'] == True) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['h'] == row['h']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['g'] == False) | (df['a'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['g'] == True) &  (df['a'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())
	
	df.to_csv('truth_table.csv', index=False)


def C2_3_3_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['a'] == True) | (df['i'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == row['h']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['a'] == False) & (df['i'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())


	df.to_csv('truth_table.csv', index=False)



def C2_3_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, a: False
	for index, row in df[(df['a'] == False) & (df['i'] == False)].iterrows():
		add_sum = df[((df['a'] == True) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['h'] == row['h']) & (df['d'] == row['d']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['g'] == False) | (df['a'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['g'] == True) &  (df['a'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())

	df.to_csv('truth_table.csv', index=False)


def C3_1_1_trust_based_update():
	df = pd.read_csv('truth_table.csv')


	for index, row in df[(df['f'] == True) | (df['g'] == True) |(df['j'] == True) & (df['h'] == True)].iterrows():
		add_sum = df[((df['f'] == False) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == row['i']) & (df['h'] == False) & (df['j'] == False) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['f'] == False) & (df['j'] == False) &  (df['h'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

# h, i, f
def C3_1_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# j: False, h: False
	for index, row in df[(df['j'] == False) & (df['h'] == False)].iterrows():
		add_sum = df[((df['j'] == True) | (df['h'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['g'] == row['g']) & (df['i'] == row['i']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['i'] == False) | (df['f'] == False) | (df['k'] == False) | (df['j'] == False)].iterrows():
		add_sum = df[((df['f'] == True) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == row['a'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['h'] == True) & (df['i'] == True) & (df['j'] == True) & (df['k'] == True))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['i'] == True) &  (df['f'] == True) & (df['k'] == True) & (df['j'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())

	
	df.to_csv('truth_table.csv', index=False)


def C3_1_2_trust_based_update():
	df = pd.read_csv('truth_table.csv')


	for index, row in df[(df['f'] == True) |(df['g'] == True) | (df['j'] == False) & (df['i'] == True)].iterrows():
		add_sum = df[((df['f'] == False) & (df['e'] == row['e']) & (df['a'] == row['a']) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == row['h']) & (df['j'] == True) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['f'] == False) & (df['g'] == False) & (df['j'] == True) &  (df['i'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)



def C3_1_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# j: True, i: False
	for index, row in df[(df['j'] == True) & (df['i'] == False)].iterrows():
		add_sum = df[((df['j'] == False) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['i'] == False) | (df['f'] == False) | (df['k'] == False)].iterrows():
		add_sum = df[((df['f'] == True) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == row['a'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['h'] == True) & (df['i'] == True) & (df['j'] == row['j']) & (df['k'] == True))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['i'] == True) &  (df['f'] == True) & (df['k'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())
	
	df.to_csv('truth_table.csv', index=False)


def C3_1_3_trust_based_update():
	df = pd.read_csv('truth_table.csv')


	for index, row in df[(df['g'] == True) |(df['f'] == True) | (df['j'] == False) & (df['i'] == True)].iterrows():
		add_sum = df[((df['f'] == False) & (df['e'] == row['e']) & (df['a'] == row['a']) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == row['h']) & (df['j'] == True) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['f'] == False) & (df['j'] == True) &  (df['i'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

# h: True, i: True, f: True
def C3_1_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# j: True, i: False
	for index, row in df[(df['j'] == True) & (df['i'] == False)].iterrows():
		add_sum = df[((df['j'] == False) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['i'] == False) | (df['f'] == False) | (df['k'] == False)].iterrows():
		add_sum = df[((df['f'] == True) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == row['a'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['h'] == True) & (df['i'] == True) & (df['j'] == row['j']) & (df['k'] == True))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['i'] == True) &  (df['f'] == True) & (df['k'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())
	
	
	df.to_csv('truth_table.csv', index=False)


def C3_2_1_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['a'] == True) | (df['i'] == True)| (df['h'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == False) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['a'] == False) & (df['i'] == False) & (df['h'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def C3_2_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False (not spicy), h: False
	for index, row in df[(df['h'] == False) & (df['i'] == False)].iterrows():
		add_sum = df[((df['h'] == True) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['g'] == row['g']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['g'] == True) | (df['a'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['h'] == True) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['g'] ==False) &  (df['a'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())
	
	df.to_csv('truth_table.csv', index=False)

def C3_2_2_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['a'] == True) | (df['i'] == False)| (df['h'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == True) & (df['h'] == False) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['a'] == False) & (df['i'] == True) & (df['h'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def C3_2_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: True, h: False
	for index, row in df[(df['h'] == False) & (df['i'] == True)].iterrows():
		add_sum = df[((df['h'] == True) | (df['i'] == False)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['g'] == row['g']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['g'] == True) | (df['a'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['h'] == True) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['g'] ==False) &  (df['a'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())
	
	df.to_csv('truth_table.csv', index=False)



def C3_2_3_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['a'] == True) | (df['i'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == True) & (df['h'] == row['h']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['a'] == False) & (df['i'] == True), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def C3_2_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: True, a: False
	for index, row in df[(df['a'] == False) & (df['i'] == True)].iterrows():
		add_sum = df[((df['a'] == True) | (df['i'] == False)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['h'] == row['h']) & (df['d'] == row['d']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['g'] == True) | (df['a'] == False) | (df['j'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['h'] == True) & (df['i'] == row['i']) & (df['j'] == True) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['g'] ==False) &  (df['a'] == True) &  (df['j'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def C3_3_1_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['a'] == True) | (df['i'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == row['h']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['a'] == False) & (df['i'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)





def C3_3_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, a: False
	for index, row in df[(df['a'] == False) & (df['i'] == False)].iterrows():
		add_sum = df[((df['a'] == True) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['h'] == row['h']) & (df['d'] == row['d']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['g'] == False) | (df['a'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['g'] == True) &  (df['a'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())

	df.to_csv('truth_table.csv', index=False)


def C3_3_2_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['a'] == True) | (df['i'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == row['h']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['a'] == False) & (df['i'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def C3_3_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, g: False
	for index, row in df[(df['g'] == False) & (df['i'] == False)].iterrows():
		add_sum = df[((df['g'] == True) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['h'] == row['h']) & (df['a'] == row['a']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())
	
	for index, row in df[(df['h'] == False) |(df['g'] == False) | (df['a'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['g'] == True) &  (df['a'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())

	df.to_csv('truth_table.csv', index=False)



def C3_3_3_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['a'] == True) | (df['i'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == row['e']) & (df['a'] == False) & (df['d'] == row['d'])) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['i'] == False) & (df['h'] == row['h']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_trust_based_updated'] = row['Fourth_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['a'] == False) & (df['i'] == False), 'Fourth_trust_based_updated'] *= (1 - s)

	# print(df['Fourth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def C3_3_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	for index, row in df[(df['a'] == False) & (df['i'] == False)].iterrows():
		add_sum = df[((df['a'] == True) | (df['i'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['e'] == row['e']) & (df['j'] == row['j']) & (df['h'] == row['h']) & (df['d'] == row['d']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_trust_based_updated'] + k * add_sum

	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']* (1 - k))
	
	# print(df['Fourth_response_based_updated'].sum())

	for index, row in df[(df['h'] == False) |(df['g'] == False) | (df['a'] == False)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] ==row['e']) & (df['d'] == row['d']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fourth_response_based_updated'] = row['Fourth_response_based_updated'] +  s * add_sum

	df.loc[(df['h'] == True) & (df['g'] == True) &  (df['a'] == True), 'Fourth_response_based_updated'] *= (1 - s)

	# print(df['Fourth_response_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)



def C1_1_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['l'] == True) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['l'] == False) & (df['g'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['l'] == False) & (df['g'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['l'] == True) & (df['g'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-1-1-1_1']), int(row['Ranking C-1-1-1_2']), int(row['Ranking C-1-1-1_3']), int(row['Ranking C-1-1-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C1_1_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == False) & (df['g'] == False) & (df['j'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['f'] == False) & (df['g'] == True) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['f'] == False) & (df['g'] == False) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['f'] == True) & (df['g'] == True) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-1-1-2_1']), int(row['Ranking C-1-1-2_2']), int(row['Ranking C-1-1-2_3']), int(row['Ranking C-1-1-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C1_1_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == False) & (df['g'] == False) & (df['j'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['f'] == False) & (df['g'] == True) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['f'] == False) & (df['g'] == False) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['f'] == True) & (df['g'] == True) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-1-1-3_1']), int(row['Ranking C-1-1-3_2']), int(row['Ranking C-1-1-3_3']), int(row['Ranking C-1-1-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C1_2_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == False) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['f'] == False) & (df['g'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['f'] == True) & (df['g'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-1-2-1_1']), int(row['Ranking C-1-2-1_2']), int(row['Ranking C-1-2-1_3']), int(row['Ranking C-1-2-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C1_2_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['l'] == True) & (df['f'] == True) & (df['h'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['l'] == True) & (df['f'] == True) & (df['h'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['l'] == False) & (df['f'] == False) & (df['h'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['l'] == False) & (df['f'] == True) & (df['h'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-1-2-2_1']), int(row['Ranking C-1-2-2_2']), int(row['Ranking C-1-2-2_3']), int(row['Ranking C-1-2-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C1_2_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['l'] == False) & (df['f'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['l'] == True) & (df['f'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['l'] == False) & (df['f'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['l'] == True) & (df['f'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-1-2-3_1']), int(row['Ranking C-1-2-3_2']), int(row['Ranking C-1-2-3_3']), int(row['Ranking C-1-2-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


def C1_3_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['e'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['e'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['e'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['a'] == True) & (df['e'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-1-3-1_1']), int(row['Ranking C-1-3-1_2']), int(row['Ranking C-1-3-1_3']), int(row['Ranking C-1-3-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C1_3_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['a'] == True) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['a'] == True) & (df['g'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-1-3-2_1']), int(row['Ranking C-1-3-2_2']), int(row['Ranking C-1-3-2_3']), int(row['Ranking C-1-3-2_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C1_3_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['e'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['e'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['e'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['e'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-1-3-3_1']), int(row['Ranking C-1-3-3_2']), int(row['Ranking C-1-3-3_3']), int(row['Ranking C-1-3-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C2_1_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['i'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['i'] == True) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['d'] == False) & (df['i'] == False) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['d'] == True) & (df['i'] == True) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-2-1-1_1']), int(row['Ranking C-2-1-1_2']), int(row['Ranking C-2-1-1_3']), int(row['Ranking C-2-1-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C2_1_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['j'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['j'] == True) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['d'] == False) & (df['j'] == False) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['d'] == True) & (df['j'] == True) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-2-1-2_1']), int(row['Ranking C-2-1-2_2']), int(row['Ranking C-2-1-2_3']), int(row['Ranking C-2-1-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C2_1_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == False) & (df['i'] == False) & (df['j'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['d'] == True) & (df['i'] == False) & (df['j'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['d'] == True) & (df['i'] == True) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['d'] == False) & (df['i'] == False) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-2-1-3_1']), int(row['Ranking C-2-1-3_2']), int(row['Ranking C-2-1-3_3']), int(row['Ranking C-2-1-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


def C2_2_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['g'] == False) & (df['h'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['g'] == True) & (df['h'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['h'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['g'] == True) & (df['h'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-2-2-1_1']), int(row['Ranking C-2-2-1_2']), int(row['Ranking C-2-2-1_3']), int(row['Ranking C-2-2-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C2_2_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['g'] == True) & (df['h'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['g'] == True) & (df['h'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['h'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['g'] == False) & (df['h'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-2-2-2_1']), int(row['Ranking C-2-2-2_2']), int(row['Ranking C-2-2-2_3']), int(row['Ranking C-2-2-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C2_2_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['g'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['g'] == True) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['d'] == True) & (df['g'] == True) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-2-2-3_1']), int(row['Ranking C-2-2-3_2']), int(row['Ranking C-2-2-3_3']), int(row['Ranking C-2-2-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C2_3_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-2-3-1_1']), int(row['Ranking C-2-3-1_2']), int(row['Ranking C-2-3-1_3']), int(row['Ranking C-2-3-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C2_3_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-2-3-2_1']), int(row['Ranking C-2-3-2_2']), int(row['Ranking C-2-3-2_3']), int(row['Ranking C-2-3-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C2_3_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-2-3-3_1']), int(row['Ranking C-2-3-3_2']), int(row['Ranking C-2-3-3_3']), int(row['Ranking C-2-3-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C3_1_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['g'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['d'] == True) & (df['g'] == True) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-3-1-1_1']), int(row['Ranking C-3-1-1_2']), int(row['Ranking C-3-1-1_3']), int(row['Ranking C-3-1-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C3_1_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['g'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['d'] == True) & (df['g'] == True) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-3-1-2_1']), int(row['Ranking C-3-1-2_2']), int(row['Ranking C-3-1-2_3']), int(row['Ranking C-3-1-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C3_1_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == False) & (df['g'] == False) & (df['j'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['f'] == False) & (df['g'] == True) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['f'] == False) & (df['g'] == False) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['f'] == True) & (df['g'] == True) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-3-1-3_1']), int(row['Ranking C-3-1-3_2']), int(row['Ranking C-3-1-3_3']), int(row['Ranking C-3-1-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C3_2_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['g'] == False) & (df['h'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['g'] == True) & (df['h'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['h'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['g'] == True) & (df['h'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-3-2-1_1']), int(row['Ranking C-3-2-1_2']), int(row['Ranking C-3-2-1_3']), int(row['Ranking C-3-2-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C3_2_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['g'] == True) & (df['h'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['g'] == True) & (df['h'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['h'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['g'] == False) & (df['h'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-3-2-2_1']), int(row['Ranking C-3-2-2_2']), int(row['Ranking C-3-2-2_3']), int(row['Ranking C-3-2-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C3_2_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['g'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['g'] == True) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['d'] == True) & (df['g'] == True) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-3-2-3_1']), int(row['Ranking C-3-2-3_2']), int(row['Ranking C-3-2-3_3']), int(row['Ranking C-3-2-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation
def C3_3_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['a'] == True) & (df['g'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-3-3-1_1']), int(row['Ranking C-3-3-1_2']), int(row['Ranking C-3-3-1_3']), int(row['Ranking C-3-3-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C3_3_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['a'] == True) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-3-3-2_1']), int(row['Ranking C-3-3-2_2']), int(row['Ranking C-3-3-2_3']), int(row['Ranking C-3-3-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


def C3_3_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking C-3-3-3_1']), int(row['Ranking C-3-3-3_2']), int(row['Ranking C-3-3-3_3']), int(row['Ranking C-3-3-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation
	

def fourth_response_update(num1, num2, num3):
	if num1 == 1:
		if num2 == 1:
			if num3 == 1:
				C1_1_1_response_based_update()
				#l, g, i: T, F, F/F, T, T/F, T, F/T, F, T
			elif num3 == 2:
				C1_1_2_response_based_update()
				# f, g, j: F, F, T/F, T, F/F, F, F/T, T, F
			elif num3 == 3:
				C1_1_3_response_based_update()
				# f, g, j: F, F, T/F, T, F/F, F, F/T, T, F
		elif num2 == 2:
			if num3 == 1:
				C1_2_1_response_based_update()
				# f, g, i: F, F, F/F, T ,T/T, F, F/T, T, T
			elif num3 == 2:
				C1_2_2_response_based_update()
				# l, f, h: T, T, T/T, T, F/F, F, F/F, T, T
			elif num3 == 3:
				C1_2_3_response_based_update()
				# l, f, i: F, T, F/T, F, T/F, F, F/T, T, F
		elif num2 == 3:
			if num3 == 1:
				C1_3_1_response_based_update()
				# a, e, i: F, F, F/F, T, T/F, F, T/T, T, T
			elif num3 == 2:
				C1_3_2_response_based_update()
				# a, g, i: F, F, F/T, F, F/T, T, T/F, T, F
			elif num3 == 3: 
				C1_3_3_response_based_update()
				# a, e, i: F, F, F/F, T, T/F, F, T/F, T, F
	elif num1 == 2:
		if num2 == 1:
			if num3 == 1:
				C2_1_1_response_based_update()
				# d, i, l: T, F, T/ F, T, F/F, F, F/ T, T, T
			elif num3 == 2:
				C2_1_2_response_based_update()
				# d, j, l: T, F, T/ F, T, F/F, F, F/ T, T, T
			elif num3 == 3:
				C2_1_3_response_based_update()
				# d, i, j: F, F, T/T, F, T/T, T, F/F, F, F
		elif num2 == 2:
			if num3 == 1:
				C2_2_1_response_based_update()
				# g, h, i: F, T, T/T, F, F/F, F, F/T, T, T
			elif num3 == 2:
				C2_2_2_response_based_update()
				# g, h, i: T, T, T/T, F, T/F, F, T/F, F, F
			elif num3 == 3:
				C2_2_3_response_based_update()
				# d, g, l: T, F, T/ F, T, F/F, F, F/ T, T, T
		elif num2 == 3:
			if num3 == 1:
				C2_3_1_response_based_update()
				# a, g, i: F, F, F/F, T, T/F, F, T/T, T, T
			elif num3 == 2:
				C2_3_2_response_based_update()
				# a, g, i: F, F, F/T, F, F/F, F, T/F, T, F
			elif num3 == 3:
				C2_3_3_response_based_update()
				# a, g, i: F, F, F/F, T, T/F, F, T/F, T, F
	elif num1 == 3:
		if num2 == 1:
			if num3 == 1:
				C3_1_1_response_based_update()
				# d, g, l: T, F, T/F, F, F/T, T, T/F, F, T
			elif num3 == 2:
				C3_1_2_response_based_update()
				# d, g, l: T, F, T/F, F, F/T, T, T/F, F, T
			elif num3 == 3:
				C3_1_3_response_based_update()
				# f, g, j: F, F, T/F, T, F/F, F, F/T, T, F
		elif num2 == 2:
			if num3 == 1:
				C3_2_1_response_based_update()
				# g, h, i: F, T, T/T, F, F/F, F, F/T, T, T
			elif num3 == 2:
				C3_2_2_response_based_update()
				# g, h, i: T, T, T/T, F, T/F, F, T/F, F, F
			elif num3 == 3:
				C3_2_3_response_based_update()
				# d, g, l: T, F, T/ F, T, F/F, F, F/ T, T, T
		elif num2 == 3:
			if num3 == 1:
				C3_3_1_response_based_update()
				# a,g,i:  F, F, F/F, T, T/F, F, T/T, T, T
			elif num3 == 2:
				C3_3_2_response_based_update()
				# a, g, i: F, F, F/T, F, F/F, F, T/F, T, F
			elif num3 == 3:
				C3_3_3_response_based_update()
				# a, g, i: F, F, F/F, T, T/F, F, T/F, T, F






