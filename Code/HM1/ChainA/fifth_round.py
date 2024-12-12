from basic_function import confidence_choose
from basic_function import inverse_function
from basic_function import sort_dict_by_values
from basic_function import spearman_rank_correlation

import pandas as pd
import random

k = 1
def A1_1_1_trust_based_update(row, s, r):
	# k: True, j: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['k'] == True) & (df['j'] == True)].iterrows():
		add_sum = df[((df['k'] == False) | (df['j'] == False)) & ((df['a'] == row['a'])&  (df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['i'] == row['i']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['g'] == row['g']) & (df['h'] == row['h']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fifth_trust_based_updated'] = row['Fourth_response_based_updated'] +  k * add_sum

	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']* (1 - k))
	# print(df['Fifth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def A1_1_1_trust_update():
	# k: True, j: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['k'] == True) & (df['j'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['j'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def A1_1_2_trust_based_update(row, s, r):
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['k'] == True) & (df['i'] == True)].iterrows():
		add_sum = df[((df['k'] == False) | (df['i'] == False)) & ((df['a'] == row['a'])&  (df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['j'] == row['j']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['g'] == row['g']) & (df['h'] == row['h']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fifth_trust_based_updated'] = row['Fourth_response_based_updated'] +  k * add_sum

	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']* (1 - k))
	# print(df['Fifth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def A1_1_2_trust_update():
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['k'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def A1_1_3_trust_based_update(row, s, r):
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['k'] == True) & (df['i'] == True)].iterrows():
		add_sum = df[((df['k'] == False) | (df['i'] == False)) & ((df['a'] == row['a'])&  (df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['j'] == row['j']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['g'] == row['g']) & (df['h'] == row['h']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fifth_trust_based_updated'] = row['Fourth_response_based_updated'] +  k * add_sum

	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']* (1 - k))
	# print(df['Fifth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def A1_1_3_trust_update():
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['k'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def A1_2_1_trust_based_update(row, s, r):
	# j: True, g: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['g'] == True) & (df['j'] == True)].iterrows():
		add_sum = df[((df['g'] == False) | (df['j'] == False)) & ((df['a'] == row['a'])&  (df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['i'] == row['i']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['k'] == row['k']) & (df['h'] == row['h']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fifth_trust_based_updated'] = row['Fourth_response_based_updated'] +  k * add_sum

	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']* (1 - k))
	# print(df['Fifth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def A1_2_1_trust_update():
	# j: True, g: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['j'] == True) & (df['g'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['j'] == True)  & (df['g'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def A1_2_2_trust_based_update(row, s, r):
	# j: True, i: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['i'] == True) & (df['j'] == True)].iterrows():
		add_sum = df[((df['i'] == False) | (df['j'] == False)) & ((df['a'] == row['a'])&  (df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['k'] == row['k']) & (df['h'] == row['h']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fifth_trust_based_updated'] = row['Fourth_response_based_updated'] +  k * add_sum

	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']* (1 - k))
	# print(df['Fifth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def A1_2_2_trust_update():
	# j: True, i: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['j'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['j'] == True)  & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def A1_2_3_trust_based_update(row, s, r):
	# j: True, i: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['i'] == True) & (df['j'] == True)].iterrows():
		add_sum = df[((df['i'] == False) | (df['j'] == False)) & ((df['a'] == row['a'])&  (df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['k'] == row['k']) & (df['h'] == row['h']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fifth_trust_based_updated'] = row['Fourth_response_based_updated'] +  k * add_sum

	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']* (1 - k))
	# print(df['Fifth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)



def A1_2_3_trust_update():
	# j: True, i: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['j'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['j'] == True)  & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def A2_1_1_trust_based_update(row, s, r):
	# k: True, j: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['k'] == True) & (df['j'] == True)].iterrows():
		add_sum = df[((df['k'] == False) | (df['j'] == False)) & ((df['a'] == row['a'])&  (df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['i'] == row['i']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['g'] == row['g']) & (df['h'] == row['h']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fifth_trust_based_updated'] = row['Fourth_response_based_updated'] +  k * add_sum

	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']* (1 - k))
	# print(df['Fifth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def A2_1_1_trust_update():
	# k: True, j: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['k'] == True) & (df['j'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['j'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def A2_1_2_trust_based_update(row, s, r):
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['i'] == True) & (df['j'] == True)].iterrows():
		add_sum = df[((df['i'] == False) | (df['j'] == False)) & ((df['a'] == row['a'])&  (df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['k'] == row['k']) & (df['h'] == row['h']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fifth_trust_based_updated'] = row['Fourth_response_based_updated'] +  k * add_sum

	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']* (1 - k))
	# print(df['Fifth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)
	
def A2_1_2_trust_update():
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['k'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def A2_1_3_trust_based_update(row, s, r):
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['i'] == True) & (df['j'] == True)].iterrows():
		add_sum = df[((df['i'] == False) | (df['j'] == False)) & ((df['a'] == row['a'])&  (df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['k'] == row['k']) & (df['h'] == row['h']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fifth_trust_based_updated'] = row['Fourth_response_based_updated'] +  k * add_sum

	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']* (1 - k))
	# print(df['Fifth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def A2_1_3_trust_update():
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['k'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def A2_2_3_trust_based_update(row, s, r):
	# j: False, a: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['a'] == True) & (df['j'] == False)].iterrows():
		add_sum = df[((df['a'] == False) | (df['j'] == True)) & ((df['i'] == row['i'])&  (df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['k'] == row['k']) & (df['h'] == row['h']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fifth_trust_based_updated'] = row['Fourth_response_based_updated'] +  k * add_sum

	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']* (1 - k))
	# print(df['Fifth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def A2_2_3_trust_update():
	# j: False, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['j'] == False) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['j'] == False) & (df['a'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def A3_1_1_trust_based_update(row, s, r):
	# k: True, j: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['k'] == True) & (df['j'] == True)].iterrows():
		add_sum = df[((df['k'] == False) | (df['j'] == False)) & ((df['a'] == row['a'])&  (df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['i'] == row['i']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['g'] == row['g']) & (df['h'] == row['h']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fifth_trust_based_updated'] = row['Fourth_response_based_updated'] +  k * add_sum

	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']* (1 - k))
	# print(df['Fifth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def A3_1_1_trust_update():
	# k: True, j: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['k'] == True) & (df['j'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['j'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def A3_1_2_trust_based_update(row, s, r):
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['i'] == True) & (df['j'] == True)].iterrows():
		add_sum = df[((df['i'] == False) | (df['j'] == False)) & ((df['a'] == row['a'])&  (df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['k'] == row['k']) & (df['h'] == row['h']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fifth_trust_based_updated'] = row['Fourth_response_based_updated'] +  k * add_sum

	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']* (1 - k))
	# print(df['Fifth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)
	

def A3_1_3_trust_based_update(row, s, r):

	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['i'] == True) & (df['j'] == True)].iterrows():
		add_sum = df[((df['i'] == False) | (df['j'] == False)) & ((df['a'] == row['a'])&  (df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['k'] == row['k']) & (df['h'] == row['h']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fifth_trust_based_updated'] = row['Fourth_response_based_updated'] +  k * add_sum

	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']* (1 - k))
	# print(df['Fifth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)
	


def A3_1_2_trust_update():
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['k'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def A3_1_3_trust_update():
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['k'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def A3_2_3_trust_based_update(row, s, r):

	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['a'] == True) & (df['j'] == False)].iterrows():
		add_sum = df[((df['a'] == False) | (df['j'] == True)) & ((df['i'] == row['i'])&  (df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['g'] == row['g']) & (df['f'] == row['f']) & (df['e'] == row['e']) & (df['k'] == row['k']) & (df['h'] == row['h']))]['Fourth_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Fifth_trust_based_updated'] = row['Fourth_response_based_updated'] +  k * add_sum

	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']* (1 - k))
	# print(df['Fifth_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def A3_2_3_trust_update():
	# j: False, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['j'] == False) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['j'] == False) & (df['a'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def A1_1_1_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == False) & (df['g'] == False) & (df['i'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['c'] == True) & (df['g'] == True) & (df['i'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['c'] == False) & (df['g'] == False) & (df['i'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == True) & (df['g'] == False) & (df['i'] == True)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-1-1-1 F_1']), int(row['Ranking A-1-1-1 F_2']), int(row['Ranking A-1-1-1 F_3']), int(row['Ranking A-1-1-1 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def A1_1_1_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['e'] == False) & (df['d'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking A-1-1-1 A_1']), int(row['Ranking A-1-1-1 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [1, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter



def A1_1_2_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == False) & (df['g'] == False) & (df['h'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['c'] == True) & (df['g'] == True) & (df['h'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['c'] == False) & (df['g'] == False) & (df['h'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == True) & (df['g'] == False) & (df['h'] == False)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-1-1-2 F_1']), int(row['Ranking A-1-1-2 F_2']), int(row['Ranking A-1-1-2 F_3']), int(row['Ranking A-1-1-2 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def A1_1_2_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['e'] == False) & (df['d'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking A-1-1-2 A_1']), int(row['Ranking A-1-1-2 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [1, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def A1_1_3_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == False) & (df['g'] == False) & (df['k'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['c'] == True) & (df['g'] == True) & (df['k'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['c'] == False) & (df['g'] == False) & (df['k'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == True) & (df['g'] == True) & (df['k'] == True)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-1-1-3 F_1']), int(row['Ranking A-1-1-3 F_2']), int(row['Ranking A-1-1-3 F_3']), int(row['Ranking A-1-1-3 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def A1_1_3_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['e'] == False) & (df['d'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking A-1-1-3 A_1']), int(row['Ranking A-1-1-3 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [1, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter



def A1_2_1_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == False) & (df['f'] == True) & (df['j'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['c'] == True) & (df['f'] == True) & (df['j'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['c'] == False) & (df['f'] == True) & (df['j'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == True) & (df['f'] == True) & (df['j'] == True)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-1-2-1 F_1']), int(row['Ranking A-1-2-1 F_2']), int(row['Ranking A-1-2-1 F_3']), int(row['Ranking A-1-2-1 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def A1_2_1_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['e'] == False) & (df['d'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking A-1-2-1 A_1']), int(row['Ranking A-1-2-1 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [1, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter



def A1_2_2_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == False) & (df['f'] == True) & (df['h'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['c'] == True) & (df['f'] == False) & (df['h'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['c'] == False) & (df['f'] == True) & (df['h'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['f'] == False) & (df['h'] == False)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-1-2-2 F_1']), int(row['Ranking A-1-2-2 F_2']), int(row['Ranking A-1-2-2 F_3']), int(row['Ranking A-1-2-2 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


def A1_2_2_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['e'] == False) & (df['d'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking A-1-2-2 A_1']), int(row['Ranking A-1-2-2 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [1, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def A1_2_3_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == False) & (df['f'] == True) & (df['j'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['c'] == False) & (df['f'] == True) & (df['j'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['c'] == True) & (df['f'] == False) & (df['j'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == True) & (df['f'] == True) & (df['j'] == True)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-1-2-3 F_1']), int(row['Ranking A-1-2-3 F_2']), int(row['Ranking A-1-2-3 F_3']), int(row['Ranking A-1-2-3 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def A1_2_3_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['e'] == False) & (df['d'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking A-1-2-3 A_1']), int(row['Ranking A-1-2-3 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [1, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def A1_3_1_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()


	human_ranking = [int(row['Ranking A-1-3-1 A_2']), int(row['Ranking A-1-3-1 A_3']), int(row['Ranking A-1-3-1 A_4']), int(row['Ranking A-1-3-1 A_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 2, 4, 3]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def A1_3_2_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()


	human_ranking = [int(row['Ranking A-1-3-2 A_2']), int(row['Ranking A-1-3-2 A_3']), int(row['Ranking A-1-3-2 A_4']), int(row['Ranking A-1-3-2 A_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [2, 1, 4, 3]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def A1_3_3_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()


	human_ranking = [int(row['Ranking A-1-3-3 A_1']), int(row['Ranking A-1-3-3 A_2']), int(row['Ranking A-1-3-3 A_3']), int(row['Ranking A-1-3-3 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [2, 1, 4, 3]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def A2_1_1_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == False) & (df['i'] == True) & (df['k'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['c'] == False) & (df['i'] == True) & (df['k'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['c'] == True) & (df['i'] == False) & (df['k'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == True) & (df['i'] == True) & (df['k'] == True)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-2-1-1 F_1']), int(row['Ranking A-2-1-1 F_2']), int(row['Ranking A-2-1-1 F_3']), int(row['Ranking A-2-1-1 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def A2_1_1_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['e'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['h'] == True) & (df['i'] == True) & (df['g'] == True)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking A-2-1-1 A_1']), int(row['Ranking A-2-1-1 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [2, 1]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def A2_1_2_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['e'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['h'] == True) & (df['i'] == True) & (df['g'] == True)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking A-2-1-2 A_1']), int(row['Ranking A-2-1-2 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [2, 1]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def A2_1_2_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == False) & (df['h'] == True) & (df['k'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['c'] == False) & (df['h'] == True) & (df['k'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['c'] == True) & (df['h'] == False) & (df['k'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['h'] == False) & (df['k'] == False)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-2-1-2 F_1']), int(row['Ranking A-2-1-2 F_2']), int(row['Ranking A-2-1-2 F_3']), int(row['Ranking A-2-1-2 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def A2_1_3_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == False) & (df['j'] == False) & (df['k'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['c'] == False) & (df['j'] == True) & (df['k'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['c'] == False) & (df['j'] == False) & (df['k'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == True) & (df['j'] == True) & (df['k'] == True)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-2-1-3 F_1']), int(row['Ranking A-2-1-3 F_2']), int(row['Ranking A-2-1-3 F_3']), int(row['Ranking A-2-1-3 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


def A2_1_3_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['e'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['h'] == True) & (df['i'] == True) & (df['g'] == True)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking A-2-1-3 A_1']), int(row['Ranking A-2-1-3 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [2, 1]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def A2_2_3_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == True) & (df['g'] == True) & (df['h'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['c'] == True) & (df['g'] == False) & (df['h'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['c'] == False) & (df['g'] == False) & (df['h'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['g'] == True) & (df['h'] == False)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-2-2-3 F_1']), int(row['Ranking A-2-2-3 F_2']), int(row['Ranking A-2-2-3 F_3']), int(row['Ranking A-2-2-3 F_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


def A2_2_1_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['h'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['g'] == False) & (df['h'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()


	human_ranking = [int(row['Ranking A-2-2-1 A_1']), int(row['Ranking A-2-2-1 A_2']), int(row['Ranking A-2-2-1 A_3']), int(row['Ranking A-2-2-1 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 4, 3, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def A2_2_2_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == True) & (df['h'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['g'] == False) & (df['h'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()


	human_ranking = [int(row['Ranking A-2-2-2 A_1']), int(row['Ranking A-2-2-2 A_2']), int(row['Ranking A-2-2-2 A_3']), int(row['Ranking A-2-2-2 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 4, 3, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def A2_2_3_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['j'] == False) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['g'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking A-2-2-3 A_1']), int(row['Ranking A-2-2-3 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [1, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def A2_3_1_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['e'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()

	human_ranking = [int(row['Ranking A-2-3-1 A_1']), int(row['Ranking A-2-3-1 A_2']), int(row['Ranking A-2-3-1 A_3']), int(row['Ranking A-2-3-1 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 2, 3, 4]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def A2_3_2_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['e'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()

	human_ranking = [int(row['Ranking A-2-3-2 A_1']), int(row['Ranking A-2-3-2 A_2']), int(row['Ranking A-2-3-2 A_3']), int(row['Ranking A-2-3-2 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 2, 3, 4]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def A2_3_3_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['e'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()

	human_ranking = [int(row['Ranking A-2-3-3 A_1']), int(row['Ranking A-2-3-3 A_2']), int(row['Ranking A-2-3-3 A_3']), int(row['Ranking A-2-3-3 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 2, 3, 4]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter



def A3_1_1_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == False) & (df['i'] == True) & (df['k'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['c'] == False) & (df['i'] == True) & (df['k'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['c'] == True) & (df['i'] == False) & (df['k'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == True) & (df['i'] == True) & (df['k'] == True)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-3-1-1 F_1']), int(row['Ranking A-3-1-1 F_2']), int(row['Ranking A-3-1-1 F_3']), int(row['Ranking A-3-1-1 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def A3_1_1_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['g'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['h'] == True) & (df['i'] == True) & (df['g'] == True)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking A-3-1-1 A_1']), int(row['Ranking A-3-1-1 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [2, 1]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter



def A3_1_2_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['g'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['h'] == True) & (df['i'] == True) & (df['g'] == True)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking A-3-1-2 A_1']), int(row['Ranking A-3-1-2 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [2, 1]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter



def A3_1_3_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['g'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['h'] == True) & (df['i'] == True) & (df['g'] == True)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking A-3-1-3 A_1']), int(row['Ranking A-3-1-3 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [2, 1]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def A3_1_2_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == False) & (df['h'] == True) & (df['k'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['c'] == False) & (df['h'] == True) & (df['k'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['c'] == True) & (df['h'] == False) & (df['k'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['h'] == False) & (df['k'] == False)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-3-1-2 F_1']), int(row['Ranking A-3-1-2 F_2']), int(row['Ranking A-3-1-2 F_3']), int(row['Ranking A-3-1-2 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


def A3_1_3_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == False) & (df['j'] == False) & (df['k'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['c'] == False) & (df['j'] == True) & (df['k'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['c'] == False) & (df['j'] == False) & (df['k'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == True) & (df['j'] == True) & (df['k'] == True)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-3-1-3 F_1']), int(row['Ranking A-3-1-3 F_2']), int(row['Ranking A-3-1-3 F_3']), int(row['Ranking A-3-1-3 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


def A3_2_3_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == True) & (df['g'] == True) & (df['h'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['c'] == True) & (df['g'] == False) & (df['h'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['c'] == False) & (df['g'] == False) & (df['h'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['g'] == True) & (df['h'] == False)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking A-3-2-3 F_1']), int(row['Ranking A-3-2-3 F_2']), int(row['Ranking A-3-2-3 F_3']), int(row['Ranking A-3-2-3 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation



def A3_2_1_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['h'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['g'] == False) & (df['h'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()


	human_ranking = [int(row['Ranking A-3-2-1 A_1']), int(row['Ranking A-3-2-1 A_2']), int(row['Ranking A-3-2-1 A_3']), int(row['Ranking A-3-2-1 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 4, 3, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def A3_2_2_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['h'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['g'] == False) & (df['h'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()


	human_ranking = [int(row['Ranking A-3-2-2 A_1']), int(row['Ranking A-3-2-2 A_2']), int(row['Ranking A-3-2-2 A_3']), int(row['Ranking A-3-2-2 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 4, 3, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def A3_2_3_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['j'] == False) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['g'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()

	human_ranking = [int(row['Ranking A-3-2-3 A_1']), int(row['Ranking A-3-2-3 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [1, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def A3_3_1_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['e'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()

	human_ranking = [int(row['Ranking A-3-3-1 A_1']), int(row['Ranking A-3-3-1 A_2']), int(row['Ranking A-3-3-1 A_3']), int(row['Ranking A-3-3-1 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 2, 3, 4]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def A3_3_2_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['e'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()

	human_ranking = [int(row['Ranking A-3-3-2 A_1']), int(row['Ranking A-3-3-2 A_2']), int(row['Ranking A-3-3-2 A_3']), int(row['Ranking A-3-3-2 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 2, 3, 4]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def A3_3_3_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['e'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()

	human_ranking = [int(row['Ranking A-3-3-3 A_1']), int(row['Ranking A-3-3-3 A_2']), int(row['Ranking A-3-3-3 A_3']), int(row['Ranking A-3-3-3 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 2, 3, 4]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter




def fifth_trust_update(num1, num2, num3):
	if num1 == 1:
		if num2 == 1:
			if num3 == 1:
				A1_1_1_trust_update()
				# c, g, i: F, F, F/T, T, F/F, F, T/T, F, T
			elif num3 == 2:
				A1_1_2_trust_update()
				# c, g, h: F, F, T/T, T, F/F, F, F/T, F, F
			elif num3 == 3:
				A1_1_3_trust_update()
				# c, g, k: F, F, T/T, T, F/F, F, F/T, T, T
		elif num2 == 2:
			if num3 == 1:
				A1_2_1_trust_update()
				# c, f, j: F, T, T/T, T, F/F, T, F/ T, T, T
			elif num3 == 2:
				A1_2_2_trust_update()
				# c, f, h: F, T, F/T, F, F/F, T, T/F, F, F
			elif num3 == 3:
				A1_2_3_trust_update()
				# c, f, j: F, T, T/F, T ,F/T, F, F/T, T, T
	elif num1 == 2:
		if num2 == 1:
			if num3 == 1:
				A2_1_1_trust_update()
				# c, i, k: F, T, T/F, T, F/T, F, F/T, T, T
			elif num3 == 2:
				A2_1_2_trust_update()
				# c, h, k: F,T ,T/F, T, F/T, F, F/F, F, F
			elif num3 == 3:
				A2_1_3_trust_update()
				# c, j, k: F, F, F/F, T, T/F, F, T/T, T, T
		elif num2 == 2:
			if num3 == 3:
				A2_2_3_trust_update()
				# c, g, h: T, T, T/T, F, T/F, F, T/F, T, F
	elif num1 == 3:
		if num2 == 1:
			if num3 == 1:
				A3_1_1_trust_update()
				# c, i, k: F, T, T/F, T, F/T, F, F/T, T, T
			elif num3 == 2:
				A3_1_2_trust_update()
				# c, h, k: F,T ,T/F, T, F/T, F, F/F, F, F
			elif num3 == 3:
				A3_1_3_trust_update()
				# c, j, k: F, F, F/F, T, T/F, F, T/T, T, T
		elif num2 == 2:
			if num3 == 3:
				A3_2_3_trust_update()
				# c, g, h: T, T, T/T, F, T/F, F, T/F, T, F