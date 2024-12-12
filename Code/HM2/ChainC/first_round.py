from basic_function import confidence_choose
from basic_function import inverse_function
from basic_function import sort_dict_by_values
from basic_function import spearman_rank_correlation

import pandas as pd
import random

k = 1
s = 1
def first_trust_based_update(row, s, r):
	# a: True, b: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['a'] == True) & (df['b'] == True)].iterrows():
		add_sum = df[((df['a'] == False) | (df['b'] == False)) & ((df['c'] == row['c']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['f'] == row['f']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Initial'].sum()
		# print(add_sum)
		df.at[index, 'First_trust_based_updated'] = row['Initial'] +  k * add_sum

	df['First_trust_based_updated'] = df['First_trust_based_updated'].fillna(df['Initial']* (1 - k))
	# print(df['First_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

	for index, row in df[(df['c'] == True) | (df['a'] == True)].iterrows():
		add_sum = df[((df['a'] == False) & (df['c'] == False)) & ((df['b'] == row['b']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['f'] == row['f']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['First_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'First_trust_based_updated'] = row['First_trust_based_updated'] + s * add_sum

	df.loc[(df['c'] == False) & (df['a'] == False), 'First_trust_based_updated'] *= (1 - s)
	
	# print(df['First_trust_based_updated'].sum())

	df.to_csv('truth_table.csv', index=False)

def first_trust_update():
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['a'] == True) & (df['b'] == True)]
	sum_of_updated = filtered_rows['Initial'].sum()
	df.loc[(df['a'] == True) & (df['b'] == True), 'First_trust_based_updated'] = df['Initial']/sum_of_updated * real_prob
	df['First_trust_based_updated'] = df['First_trust_based_updated'].fillna(df['Initial']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def first_response_based_update():
	# c: False, a: False
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['c'] == False) & (df['a'] == False)].iterrows():
		add_sum = df[((df['a'] == True) | (df['c'] == True)) & ((df['b'] == row['b']) & (df['d'] == row['d']) & (df['e'] == row['e']) & (df['f'] == row['f']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['First_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'First_response_based_updated'] = row['First_trust_based_updated'] + k * add_sum

	df['First_response_based_updated'] = df['First_response_based_updated'].fillna(df['First_trust_based_updated']* (1 - k))
	
	# print(df['First_response_based_updated'].sum())

	for index, row in df[(df['b'] == False) | (df['a'] == False) | (df['c'] == True)| (df['d'] == False) | (df['l'] == False)].iterrows():
		add_sum = df[((df['a'] == True) & (df['c'] == False)) & ((df['b'] == True) & (df['d'] == True) & (df['l'] == True) & (df['e'] == row['e']) & (df['f'] == row['f']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['First_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'First_response_based_updated'] = row['First_response_based_updated'] + s * add_sum

	df.loc[(df['a'] == True) & (df['c'] == False) & (df['b'] == True) & (df['d'] == True) & (df['l'] == True), 'First_response_based_updated'] *= (1 - s)
	
	# print(df['First_response_based_updated'].sum())

	
	df.to_csv('truth_table.csv', index=False)
def round1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == True) & (df['b'] == True) & (df['c'] == False)]['First_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['b'] == True) & (df['c'] == False)]['First_response_based_updated'].sum()
	ranking3 = df[(df['a'] == True) & (df['b'] == False) & (df['c'] == False)]['First_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['b'] == False) & (df['c'] == False)]['First_response_based_updated'].sum()
	
	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	human_ranking = [int(row['Ranking C_1']), int(row['Ranking C_2']), int(row['Ranking C_3']), int(row['Ranking C_4'])]

	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation




# def round1_ranking(row):
# a, b, c: T, T, F/F, T, F/ T, F, F/ F, F, F
	