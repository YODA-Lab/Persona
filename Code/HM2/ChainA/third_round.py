from basic_function import confidence_choose
from basic_function import inverse_function
from basic_function import sort_dict_by_values
from basic_function import spearman_rank_correlation

import pandas as pd
import random

k = 1
s = 1
# A1 Response
def A1_trust_based_update(row, s, r):
	# f: True, e: True, d: True, a: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)].iterrows():
		add_sum = df[((df['f'] == False) | (df['e'] == False) | (df['d'] == False)| (df['a'] == False)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Second_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_trust_based_updated'] = row['Second_response_based_updated'] +  k * add_sum

	df['Third_trust_based_updated'] = df['Third_trust_based_updated'].fillna(df['Second_response_based_updated']* (1 - k))
	# print(df['Third_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def A1_trust_update():
	# f: True, e: True, d: True, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['a'] == True) & (df['f'] == True) & (df['e'] == True) & (df['d'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['a'] == True) & (df['f'] == True) & (df['e'] == True) & (df['d'] == True), 'Third_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Third_trust_based_updated'] = df['Third_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


# A2 Response
def A2_trust_based_update(row, s, r):
	# f: True, e: True, a: True
	df = pd.read_csv('truth_table.csv')
	for index, row in df[(df['f'] == True) & (df['e'] == True) & (df['a'] == True)].iterrows():
		add_sum = df[((df['f'] == False) | (df['e'] == False) | (df['a'] == False)) & ((df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Second_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_trust_based_updated'] = row['Second_response_based_updated'] +  k * add_sum

	df['Third_trust_based_updated'] = df['Third_trust_based_updated'].fillna(df['Second_response_based_updated']* (1 - k))
	# print(df['Third_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def A2_trust_update():
	# f: True, e: True, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['a'] == True) & (df['f'] == True) & (df['e'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['a'] == True) & (df['f'] == True) & (df['e'] == True), 'Third_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Third_trust_based_updated'] = df['Third_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

# A3 Response
def A3_trust_based_update(row, s, r):
	# f: True, e: True, a: True
	df = pd.read_csv('truth_table.csv')
	for index, row in df[(df['f'] == True) & (df['e'] == True) & (df['a'] == True)].iterrows():
		add_sum = df[((df['f'] == False) | (df['e'] == False) | (df['a'] == False)) & ((df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Second_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_trust_based_updated'] = row['Second_response_based_updated'] +  k * add_sum

	df['Third_trust_based_updated'] = df['Third_trust_based_updated'].fillna(df['Second_response_based_updated']* (1 - k))
	# print(df['Third_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def A3_trust_update():
	# f: True, e: True, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['a'] == True) & (df['f'] == True) & (df['e'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['a'] == True) & (df['f'] == True) & (df['e'] == True), 'Third_trust_based_updated'] = df['Second_response_based_updated']/sum_of_updated * real_prob
	df['Third_trust_based_updated'] = df['Third_trust_based_updated'].fillna(df['Second_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


# def third_trust_based_update(row, s, r):
# 	if row['Chain A choices'] == "The extra service fee results in high costs, making Luminara Gardens unsuitable for parties. (High Confidence)":
# 		A1_trust_based_update(row, s, r)
# 	elif row['Chain A choices'] == "Luminara Gardens has no entertainment facilities that would make it unsuitable for parties. (Average Confidence)":
# 		A2_trust_based_update(row, s, r)
# 	elif row['Chain A choices'] == "The unavailability of accommodation makes Luminara Gardens unsuitable for parties. (Low Confidence)":
# 		A3_trust_based_update(row, s, r)


def third_trust_update(num):
	if num == 1:
		A1_trust_update()
	elif num == 2:
		A2_trust_update()
	elif num == 3:
		A3_trust_update()


def A1_1_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) | (df['f'] == True) | (df['e'] == True) | (df['d'] == True) | (df['a'] == True)].iterrows():
		add_sum = df[((df['f'] == False) & (df['e'] == False) & (df['d'] == False) & (df['a'] == False)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_trust_based_updated'] = row['Third_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['f'] == False) & (df['e'] == False) & (df['d'] == False) & (df['a'] == False), 'Third_trust_based_updated'] *= (1 - s)


	# print(df['Third_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

# A1_1_response
def A1_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# g: False, f: False
	for index, row in df[(df['g'] == False) & (df['f'] == False)].iterrows():
		add_sum = df[((df['g'] == True) | (df['f'] == True)) & ((df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['a'] == row['a']) & (df['e'] == row['e']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_response_based_updated'] = row['Third_trust_based_updated'] + k * add_sum

	df['Third_response_based_updated'] = df['Third_response_based_updated'].fillna(df['Third_trust_based_updated']* (1 - k))
	
	# print(df['Third_response_based_updated'].sum())

	for index, row in df[(df['f'] == False) | (df['e'] == False) | (df['d'] == False) | (df['a'] == False) | (df['h'] == False) | (df['i'] == False)].iterrows():
		add_sum = df[((df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['h'] == True) & (df['i'] == True) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_response_based_updated'] = row['Third_response_based_updated'] +  s * add_sum

	df.loc[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True) & (df['h'] == True) & (df['i'] == True), 'Third_response_based_updated'] *= (1 - s)


	# print(df['Third_response_based_updated'].sum())

	
	df.to_csv('truth_table.csv', index=False)


def A1_2_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['e'] == True) | (df['d'] == True) | (df['a'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == False) & (df['d'] == False) & (df['a'] == False)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_trust_based_updated'] = row['Third_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['e'] == False) & (df['d'] == False) & (df['a'] == False), 'Third_trust_based_updated'] *= (1 - s)


	# print(df['Third_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

# A1_2_response
def A1_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# g: False, d: False
	for index, row in df[(df['g'] == False) & (df['d'] == False)].iterrows():
		add_sum = df[((df['g'] == True) | (df['d'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['a'] == row['a']) & (df['e'] == row['e']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_response_based_updated'] = row['Third_trust_based_updated'] + k * add_sum

	df['Third_response_based_updated'] = df['Third_response_based_updated'].fillna(df['Third_trust_based_updated']* (1 - k))
	
	# print(df['Third_response_based_updated'].sum())

	for index, row in df[(df['f'] == False) | (df['e'] == False) | (df['d'] == False) | (df['a'] == False) | (df['h'] == False) | (df['g'] == False)].iterrows():
		add_sum = df[((df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_response_based_updated'] = row['Third_response_based_updated'] +  s * add_sum

	df.loc[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True) & (df['h'] == True) & (df['g'] == True), 'Third_response_based_updated'] *= (1 - s)


	# print(df['Third_response_based_updated'].sum())

	
	df.to_csv('truth_table.csv', index=False)


def A1_3_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['e'] == True) | (df['d'] == True) | (df['a'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == False) & (df['d'] == False) & (df['a'] == False)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_trust_based_updated'] = row['Third_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['e'] == False) & (df['d'] == False) & (df['a'] == False), 'Third_trust_based_updated'] *= (1 - s)


	# print(df['Third_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

# A1_3_response
def A1_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# g: False, a: False
	for index, row in df[(df['g'] == False) & (df['a'] == False)].iterrows():
		add_sum = df[((df['g'] == True) | (df['a'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_response_based_updated'] = row['Third_trust_based_updated'] + k * add_sum

	df['Third_response_based_updated'] = df['Third_response_based_updated'].fillna(df['Third_trust_based_updated']* (1 - k))
	
	# print(df['Third_response_based_updated'].sum())
	
	for index, row in df[(df['f'] == False) | (df['e'] == False) | (df['d'] == False) | (df['a'] == False) | (df['h'] == False) | (df['g'] == False)].iterrows():
		add_sum = df[((df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_response_based_updated'] = row['Third_response_based_updated'] +  s * add_sum

	df.loc[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True) & (df['h'] == True) & (df['g'] == True), 'Third_response_based_updated'] *= (1 - s)


	# print(df['Third_response_based_updated'].sum())

	df.to_csv('truth_table.csv', index=False)



def A2_1_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['e'] == True) | (df['a'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == False) & (df['d'] == row['d']) & (df['a'] == False)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_trust_based_updated'] = row['Third_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['e'] == False) & (df['a'] == False), 'Third_trust_based_updated'] *= (1 - s)


	# print(df['Third_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

# A2_1_response
def A2_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# g: False, a: False
	for index, row in df[(df['g'] == False) & (df['a'] == False)].iterrows():
		add_sum = df[((df['g'] == True) | (df['a'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_response_based_updated'] = row['Third_trust_based_updated'] + k * add_sum

	df['Third_response_based_updated'] = df['Third_response_based_updated'].fillna(df['Third_trust_based_updated']* (1 - k))
	
	# print(df['Third_response_based_updated'].sum())

	for index, row in df[(df['f'] == False) | (df['e'] == False) | (df['i'] == False) | (df['a'] == False) | (df['h'] == False) | (df['g'] == False)].iterrows():
		add_sum = df[((df['f'] == True) & (df['e'] == True) & (df['i'] == True) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['d'] == row['d']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_response_based_updated'] = row['Third_response_based_updated'] +  s * add_sum

	df.loc[(df['f'] == True) & (df['e'] == True) & (df['i'] == True) & (df['a'] == True) & (df['h'] == True) & (df['g'] == True), 'Third_response_based_updated'] *= (1 - s)


	# print(df['Third_response_based_updated'].sum())



	
	df.to_csv('truth_table.csv', index=False)


def A2_2_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['e'] == True) | (df['a'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == False) & (df['d'] == row['d']) & (df['a'] == False)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_trust_based_updated'] = row['Third_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['e'] == False) & (df['a'] == False), 'Third_trust_based_updated'] *= (1 - s)


	# print(df['Third_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def A2_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# g: False, a: False
	for index, row in df[(df['g'] == False) & (df['a'] == False)].iterrows():
		add_sum = df[((df['g'] == True) | (df['a'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_response_based_updated'] = row['Third_trust_based_updated'] + k * add_sum

	df['Third_response_based_updated'] = df['Third_response_based_updated'].fillna(df['Third_trust_based_updated']* (1 - k))
	
	# print(df['Third_response_based_updated'].sum())
	
	for index, row in df[(df['f'] == False) | (df['e'] == False) | (df['a'] == False) | (df['h'] == False) | (df['g'] == True)].iterrows():
		add_sum = df[((df['f'] == True) & (df['e'] == True) & (df['i'] == row['i']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['h'] == True) & (df['d'] == row['d']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_response_based_updated'] = row['Third_response_based_updated'] +  s * add_sum

	df.loc[(df['f'] == True) & (df['e'] == True) & (df['a'] == True) & (df['h'] == True) & (df['g'] == False), 'Third_response_based_updated'] *= (1 - s)


	# print(df['Third_response_based_updated'].sum())

	df.to_csv('truth_table.csv', index=False)


def A2_3_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['e'] == True) | (df['a'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == False) & (df['d'] == row['d']) & (df['a'] == False)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_trust_based_updated'] = row['Third_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['e'] == False) & (df['a'] == False), 'Third_trust_based_updated'] *= (1 - s)


	# print(df['Third_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def A2_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# g: False, a: False
	for index, row in df[(df['g'] == False) & (df['a'] == False)].iterrows():
		add_sum = df[((df['g'] == True) | (df['a'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_response_based_updated'] = row['Third_trust_based_updated'] + k * add_sum

	df['Third_response_based_updated'] = df['Third_response_based_updated'].fillna(df['Third_trust_based_updated']* (1 - k))
	
	# print(df['Third_response_based_updated'].sum())
	
	for index, row in df[(df['f'] == False) | (df['e'] == False) | (df['a'] == False) | (df['h'] == False) | (df['g'] == False)].iterrows():
		add_sum = df[((df['f'] == True) & (df['e'] == True) & (df['i'] == row['i']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['d'] == row['d']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_response_based_updated'] = row['Third_response_based_updated'] +  s * add_sum

	df.loc[(df['f'] == True) & (df['e'] == True) & (df['a'] == True) & (df['h'] == True) & (df['g'] == True), 'Third_response_based_updated'] *= (1 - s)


	# print(df['Third_response_based_updated'].sum())

	df.to_csv('truth_table.csv', index=False)


def A3_1_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['e'] == True) | (df['a'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == False) & (df['d'] == row['d']) & (df['a'] == False)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_trust_based_updated'] = row['Third_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['e'] == False) & (df['a'] == False), 'Third_trust_based_updated'] *= (1 - s)


	# print(df['Third_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def A3_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# g: False, a: False
	for index, row in df[(df['g'] == False) & (df['a'] == False)].iterrows():
		add_sum = df[((df['g'] == True) | (df['a'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_response_based_updated'] = row['Third_trust_based_updated'] + k * add_sum

	df['Third_response_based_updated'] = df['Third_response_based_updated'].fillna(df['Third_trust_based_updated']* (1 - k))
	
	# print(df['Third_response_based_updated'].sum())

	for index, row in df[(df['f'] == False) | (df['e'] == False) | (df['i'] == False) | (df['a'] == False) | (df['h'] == False) | (df['g'] == False)].iterrows():
		add_sum = df[((df['f'] == True) & (df['e'] == True) & (df['i'] == True) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['d'] == row['d']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_response_based_updated'] = row['Third_response_based_updated'] +  s * add_sum

	df.loc[(df['f'] == True) & (df['e'] == True) & (df['i'] == True) & (df['a'] == True) & (df['h'] == True) & (df['g'] == True), 'Third_response_based_updated'] *= (1 - s)


	# print(df['Third_response_based_updated'].sum())


	
	df.to_csv('truth_table.csv', index=False)



def A3_2_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['e'] == True) | (df['a'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == False) & (df['d'] == row['d']) & (df['a'] == False)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_trust_based_updated'] = row['Third_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['e'] == False) & (df['a'] == False), 'Third_trust_based_updated'] *= (1 - s)


	# print(df['Third_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def A3_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# g: False, a: False
	for index, row in df[(df['g'] == False) & (df['a'] == False)].iterrows():
		add_sum = df[((df['g'] == True) | (df['a'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_response_based_updated'] = row['Third_trust_based_updated'] + k * add_sum

	df['Third_response_based_updated'] = df['Third_response_based_updated'].fillna(df['Third_trust_based_updated']* (1 - k))
	
	# print(df['Third_response_based_updated'].sum())

	for index, row in df[(df['f'] == False) | (df['e'] == False) | (df['a'] == False) | (df['h'] == False) | (df['g'] == True)].iterrows():
		add_sum = df[((df['f'] == True) & (df['e'] == True) & (df['i'] == row['i']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['h'] == True) & (df['d'] == row['d']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_response_based_updated'] = row['Third_response_based_updated'] +  s * add_sum

	df.loc[(df['f'] == True) & (df['e'] == True) & (df['a'] == True) & (df['h'] == True) & (df['g'] == False), 'Third_response_based_updated'] *= (1 - s)


	# print(df['Third_response_based_updated'].sum())
	
	df.to_csv('truth_table.csv', index=False)


def A3_3_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) |(df['e'] == True) | (df['a'] == True)].iterrows():
		add_sum = df[((df['f'] == row['f']) & (df['e'] == False) & (df['d'] == row['d']) & (df['a'] == False)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == False) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_trust_based_updated'] = row['Third_trust_based_updated'] +  s * add_sum

	df.loc[(df['g'] == False) & (df['e'] == False) & (df['a'] == False), 'Third_trust_based_updated'] *= (1 - s)


	# print(df['Third_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def A3_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# g: False, a: False
	for index, row in df[(df['g'] == False) & (df['a'] == False)].iterrows():
		add_sum = df[((df['g'] == True) | (df['a'] == True)) & ((df['f'] == row['f']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_response_based_updated'] = row['Third_trust_based_updated'] + k * add_sum

	df['Third_response_based_updated'] = df['Third_response_based_updated'].fillna(df['Third_trust_based_updated']* (1 - k))
	
	# print(df['Third_response_based_updated'].sum())
	
	for index, row in df[(df['f'] == False) | (df['e'] == False) | (df['a'] == False) | (df['h'] == False) | (df['g'] == False)].iterrows():
		add_sum = df[((df['f'] == True) & (df['e'] == True) & (df['i'] == row['i']) & (df['a'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == True) & (df['h'] == True) & (df['d'] == row['d']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Third_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Third_response_based_updated'] = row['Third_response_based_updated'] +  s * add_sum

	df.loc[(df['f'] == True) & (df['e'] == True) & (df['a'] == True) & (df['h'] == True) & (df['g'] == True), 'Third_response_based_updated'] *= (1 - s)


	# print(df['Third_response_based_updated'].sum())

	df.to_csv('truth_table.csv', index=False)
	



def third_response_based_update(row):
	if row['Chain A choices'] == "The extra service fee results in high costs, making Luminara Gardens unsuitable for parties. (High Confidence)":
		if row['Chain A-1 choices'] == "The information on the official website is outdated and not accurate. (Very High Confidence)":
			A1_1_response_based_update()
		elif row['Chain A-1 choices'] == "The hidden fees might arise due to various conditions not listed on the website, potentially leading to high costs. (Average Confidence)":
			A1_2_response_based_update()
		elif row['Chain A-1 choices'] == "The lack of diverse entertainment facilities makes Luminara Gardens unsuitable for parties. (High Confidence)":
			A1_3_response_based_update()
	elif row['Chain A choices'] == "Luminara Gardens has no entertainment facilities that would make it unsuitable for parties. (Average Confidence)":
		if row['Chain A-2 choices'] == "The insufficient number of entertainment facilities makes Luminara Gardens unsuitable for parties. (Average Confidence)":
			A2_1_response_based_update()
		elif row['Chain A-2 choices'] == "The limited variety of cuisine at Luminara Gardens makes it unsuitable for parties. (Average Confidence)":
			A2_2_response_based_update()
		elif row['Chain A-2 choices'] == "The lack of diverse entertainment facilities makes Luminara Gardens unsuitable for parties. (High Confidence)":
			A2_3_response_based_update()
	elif row['Chain A choices'] == "The unavailability of accommodation makes Luminara Gardens unsuitable for parties. (Low Confidence)":
		if row['Chain A-3 choices'] == "The poor accommodation conditions make Luminara Gardens unsuitable for parties. (High Confidence)":
			A3_1_response_based_update()
		elif row['Chain A-3 choices'] == "The limited variety of cuisine at Luminara Gardens makes it unsuitable for parties. (Average Confidence)":
			A3_2_response_based_update()
		elif row['Chain A-3 choices'] == "The lack of diverse entertainment facilities makes Luminara Gardens unsuitable for parties. (High Confidence)":
			A3_3_response_based_update()

def A1_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['e'] == True) & (df['f'] == False) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking2 = df[(df['e'] == False) & (df['f'] == False) & (df['g'] == False)]['Third_response_based_updated'].sum()
	ranking3 = df[(df['e'] == True) & (df['f'] == True) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking4 = df[(df['e'] == True) & (df['f'] == False) & (df['g'] == False)]['Third_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-1-1_2']), int(row['Ranking A-1-1_3']), int(row['Ranking A-1-1_4']), int(row['Ranking A-1-1_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation



def A1_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == False) & (df['f'] == True) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking2 = df[(df['c'] == True) & (df['f'] == False) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking3 = df[(df['c'] == False) & (df['f'] == True) & (df['g'] == False)]['Third_response_based_updated'].sum()
	ranking4 = df[(df['c'] == True) & (df['f'] == True) & (df['g'] == False)]['Third_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-1-2_1']), int(row['Ranking A-1-2_2']), int(row['Ranking A-1-2_3']), int(row['Ranking A-1-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def A1_3_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['e'] == True) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['e'] == False) & (df['g'] == False)]['Third_response_based_updated'].sum()
	ranking3 = df[(df['a'] == True) & (df['e'] == True) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['e'] == True) & (df['g'] == False)]['Third_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-1-3_1']), int(row['Ranking A-1-3_2']), int(row['Ranking A-1-3_3']), int(row['Ranking A-1-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


def A2_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == True) & (df['f'] == False) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking2 = df[(df['c'] == False) & (df['f'] == True) & (df['g'] == False)]['Third_response_based_updated'].sum()
	ranking3 = df[(df['c'] == False) & (df['f'] == False) & (df['g'] == False)]['Third_response_based_updated'].sum()
	ranking4 = df[(df['c'] == True) & (df['f'] == True) & (df['g'] == False)]['Third_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-2-1_1']), int(row['Ranking A-2-1_2']), int(row['Ranking A-2-1_3']), int(row['Ranking A-2-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def A2_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == True) & (df['f'] == True) & (df['g'] == False)]['Third_response_based_updated'].sum()
	ranking2 = df[(df['c'] == True) & (df['f'] == False) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking3 = df[(df['c'] == False) & (df['f'] == True) & (df['g'] == False)]['Third_response_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['f'] == False) & (df['g'] == False)]['Third_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-2-2_1']), int(row['Ranking A-2-2_2']), int(row['Ranking A-2-2_3']), int(row['Ranking A-2-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


def A2_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == True) & (df['c'] == False) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['c'] == False) & (df['g'] == False)]['Third_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['c'] == True) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['c'] == True) & (df['g'] == False)]['Third_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-2-3_1']), int(row['Ranking A-2-3_2']), int(row['Ranking A-2-3_3']), int(row['Ranking A-2-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def A3_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['c'] == False) & (df['g'] == False)]['Third_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['c'] == True) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['c'] == True) & (df['g'] == False)]['Third_response_based_updated'].sum()
	ranking4 = df[(df['a'] == True) & (df['c'] == False) & (df['g'] == True)]['Third_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-3-1_1']), int(row['Ranking A-3-1_2']), int(row['Ranking A-3-1_3']), int(row['Ranking A-3-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def A3_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == False) & (df['d'] == False) & (df['g'] == False)]['Third_response_based_updated'].sum()
	ranking2 = df[(df['c'] == False) & (df['d'] == True) & (df['g'] == False)]['Third_response_based_updated'].sum()
	ranking3 = df[(df['c'] == True) & (df['d'] == True) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking4 = df[(df['c'] == True) & (df['d'] == False) & (df['g'] == False)]['Third_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-3-2_1']), int(row['Ranking A-3-2_2']), int(row['Ranking A-3-2_3']), int(row['Ranking A-3-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def A3_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == True) & (df['c'] == False) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['c'] == False) & (df['g'] == False)]['Third_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['c'] == True) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['c'] == True) & (df['g'] == False)]['Third_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-3-3_1']), int(row['Ranking A-3-3_2']), int(row['Ranking A-3-3_3']), int(row['Ranking A-3-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


def third_response_update(num1, num2):
	if num1 == 1:
		if num2 == 1:
			A1_1_response_based_update()
			# e, f, g: T, F, T/ F, F, F/T, T, T/T, F, F
		elif num2 == 2:
			A1_2_response_based_update()
			# c, f, g: F, T, T/T, F, T/F, T, F/T, T, F
		elif num2 == 3:
			A1_3_response_based_update()
			# a, e, g: F, T, T/F, F, F/ T, T, T/F, T, F
	elif num1 == 2:
		if num2 == 1:
			A2_1_response_based_update()
			# c, f, g: T, F, T/ F, T, F/F, F, F/ T, T, F
		elif num2 == 2:
			A2_2_response_based_update()
			# c, f, g: T, T, F/ T, F, T/F, T, F/ F. F. F
		elif num2 == 3:
			A2_3_response_based_update()
			# a, c, g: T, F, T/ F,F,F/F, T, T/F, T, F
	elif num1 == 3:
		if num2 == 1:
			A3_1_response_based_update()
			# a, c, g: F, F, F/ F, T, T/F, T, F/T, F, T
		elif num2 == 2:
			A3_2_response_based_update()
			# c, d, g: F, F, F/F, T, F/T, T, T/ T, F, F
		elif num2 == 3:
			A3_3_response_based_update()
			# a, c, g: T, F, T/ F,F,F/F, T, T/F, T, F




