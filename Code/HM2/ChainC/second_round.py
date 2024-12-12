from basic_function import confidence_choose
from basic_function import inverse_function
from basic_function import sort_dict_by_values
from basic_function import spearman_rank_correlation

import pandas as pd
import random

k = 1
s = 1
def second_trust_based_update(row, s, r):
	# c: True, d: True, a: True, l: True
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['c'] == True) & (df['d'] == True) & (df['a'] == True) & (df['l'] == True)].iterrows():
		add_sum = df[((df['c'] == False) | (df['d'] == False)| (df['a'] == False) | (df['l'] == False)) & ((df['b'] == row['b']) & (df['e'] == row['e']) & (df['f'] == row['f']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['First_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Second_trust_based_updated'] = row['First_response_based_updated'] +  k * add_sum

	df['Second_trust_based_updated'] = df['Second_trust_based_updated'].fillna(df['First_response_based_updated']* (1 - k))
	# print(df['Second_trust_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)


def second_trust_update():
	# c: True, d: True, a: True, l: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['c'] == True) & (df['d'] == True) & (df['a'] == True) & (df['l'] == True)]
	sum_of_updated = filtered_rows['First_response_based_updated'].sum()
	df.loc[(df['c'] == True) & (df['d'] == True) & (df['a'] == True) & (df['l'] == True), 'Second_trust_based_updated'] = df['First_response_based_updated']/sum_of_updated * real_prob
	df['Second_trust_based_updated'] = df['Second_trust_based_updated'].fillna(df['First_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def C1_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['c'] == True) | (df['a'] == True)| (df['e'] == True)| (df['d'] == True)].iterrows():
		add_sum = df[((df['a'] == False) & (df['c'] == False)) & ((df['b'] == row['b']) & (df['d'] == False) & (df['e'] == False) & (df['f'] == row['f']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Second_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Second_trust_based_updated'] = row['Second_trust_based_updated'] + s * add_sum

	df.loc[(df['a'] == False) & (df['c'] == False) & (df['d'] == False) & (df['e'] == False), 'Second_trust_based_updated'] *= (1 - s)
	
	# print(df['Second_trust_based_updated'].sum())

def C2_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['c'] == True) | (df['a'] == True)| (df['e'] == True)].iterrows():
		add_sum = df[((df['a'] == False) & (df['c'] == False)) & ((df['b'] == row['b']) & (df['d'] == row['d']) & (df['e'] == False) & (df['f'] == row['f']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Second_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Second_trust_based_updated'] = row['Second_trust_based_updated'] + s * add_sum

	df.loc[(df['a'] == False) & (df['c'] == False) & (df['e'] == False), 'Second_trust_based_updated'] *= (1 - s)
	
	# print(df['Second_trust_based_updated'].sum())

def C3_trust_based_update():
	df = pd.read_csv('truth_table.csv')

	for index, row in df[(df['c'] == True) | (df['a'] == True)| (df['e'] == True)].iterrows():
		add_sum = df[((df['a'] == False) & (df['c'] == False)) & ((df['b'] == row['b']) & (df['d'] == row['d']) & (df['e'] == False) & (df['f'] == row['f']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Second_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Second_trust_based_updated'] = row['Second_trust_based_updated'] + s * add_sum

	df.loc[(df['a'] == False) & (df['c'] == False) & (df['e'] == False), 'Second_trust_based_updated'] *= (1 - s)
	
	# print(df['Second_trust_based_updated'].sum())


def C1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# e: False, d: False, a: False
	for index, row in df[(df['d'] == False) & (df['a'] == False) & (df['e'] == False)].iterrows():
		add_sum = df[((df['d'] == True) | (df['a'] == True) | (df['e'] == True)) & ((df['b'] == row['b']) & (df['c'] == row['c']) & (df['f'] == row['f']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Second_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Second_response_based_updated'] = row['Second_trust_based_updated'] + k * add_sum

	df['Second_response_based_updated'] = df['Second_response_based_updated'].fillna(df['Second_trust_based_updated']* (1 - k))
	
	# print(df['Second_response_based_updated'].sum())

	for index, row in df[(df['c'] == True) | (df['d'] == False) | (df['a'] == False)| (df['f'] == False) | (df['e'] == False) | (df['l'] == False)].iterrows():
		add_sum = df[((df['d'] == True) & (df['a'] == True) & (df['e'] == True)) & ((df['b'] == row['b']) & (df['c'] == False) & (df['l'] == True) & (df['f'] == True) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Second_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Second_response_based_updated'] = row['Second_response_based_updated'] + s * add_sum

	df.loc[(df['c'] == False) & (df['d'] == True) & (df['a'] == True) & (df['f'] == True) & (df['e'] == True) & (df['l'] == True), 'Second_response_based_updated'] *= (1 - s)


	# print(df['Second_response_based_updated'].sum())

	
	df.to_csv('truth_table.csv', index=False)


def C2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# e: False, a: False
	for index, row in df[(df['a'] == False) & (df['e'] == False)].iterrows():
		add_sum = df[((df['a'] == True) | (df['e'] == True)) & ( (df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['f'] == row['f']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Second_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Second_response_based_updated'] = row['Second_trust_based_updated'] + k * add_sum

	df['Second_response_based_updated'] = df['Second_response_based_updated'].fillna(df['Second_trust_based_updated']* (1 - k))
	
	# print(df['Second_response_based_updated'].sum())

	for index, row in df[(df['c'] == True) | (df['d'] == False) | (df['a'] == False)| (df['f'] == False) | (df['e'] == False) | (df['l'] == False)].iterrows():
		add_sum = df[((df['d'] == True) & (df['a'] == True) & (df['e'] == True)) & ((df['b'] == row['b']) & (df['c'] == False) & (df['f'] == True) & (df['l'] == True) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Second_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Second_response_based_updated'] = row['Second_response_based_updated'] + k * add_sum

	df.loc[(df['c'] == False) & (df['d'] == True) & (df['a'] == True) & (df['f'] == True) & (df['e'] == True) &  (df['l'] == True), 'Second_response_based_updated'] *= (1 - s)

	# print(df['Second_response_based_updated'].sum())
	
	df.to_csv('truth_table.csv', index=False)

def C3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# e: False, a: False
	# e: False, a: False
	for index, row in df[(df['a'] == False) & (df['e'] == False)].iterrows():
		add_sum = df[((df['a'] == True) | (df['e'] == True)) & ((df['d'] == row['d']) & (df['b'] == row['b']) & (df['c'] == row['c']) & (df['f'] == row['f']) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']) & (df['l'] == row['l']))]['Second_trust_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Second_response_based_updated'] = row['Second_trust_based_updated'] + k * add_sum

	df['Second_response_based_updated'] = df['Second_response_based_updated'].fillna(df['Second_trust_based_updated']* (1 - k))
	
	# print(df['Second_response_based_updated'].sum())

	for index, row in df[(df['c'] == True) | (df['d'] == False) | (df['a'] == False)| (df['f'] == False) | (df['e'] == False) | (df['l'] == False)].iterrows():
		add_sum = df[((df['d'] == True) & (df['a'] == True) & (df['e'] == True)) & ((df['b'] == row['b']) & (df['c'] == False) & (df['f'] == True) &  (df['l'] == True) & (df['g'] == row['g']) & (df['h'] == row['h']) & (df['i'] == row['i']) & (df['j'] == row['j']) & (df['k'] == row['k']))]['Second_response_based_updated'].sum()
		# print(add_sum)
		df.at[index, 'Second_response_based_updated'] = row['Second_response_based_updated'] + k * add_sum

	df.loc[(df['c'] == False) & (df['d'] == True) & (df['a'] == True) & (df['f'] == True) & (df['e'] == True) &  (df['l'] == True), 'Second_response_based_updated'] *= (1 - s)

	# print(df['Second_response_based_updated'].sum())
	
	df.to_csv('truth_table.csv', index=False)


def C1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['d'] == False) & (df['e'] == False)]['Second_response_based_updated'].sum()
	ranking2 = df[(df['a'] == True) & (df['d'] == True) & (df['e'] == False)]['Second_response_based_updated'].sum()
	ranking3 = df[(df['a'] == True) & (df['d'] == False) & (df['e'] == False)]['Second_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['d'] == True) & (df['e'] == False)]['Second_response_based_updated'].sum()

	human_ranking = [int(row['Ranking C-1_2']), int(row['Ranking C-1_3']), int(row['Ranking C-1_4']), int(row['Ranking C-1_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)


	return correlation

def C2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['e'] == True) & (df['l'] == True)]['Second_response_based_updated'].sum()
	ranking2 = df[(df['d'] == True) & (df['e'] == True) & (df['l'] == False)]['Second_response_based_updated'].sum()
	ranking3 = df[(df['d'] == False) & (df['e'] == False) & (df['l'] == True)]['Second_response_based_updated'].sum()
	ranking4 = df[(df['d'] == True) & (df['e'] == False) & (df['l'] == False)]['Second_response_based_updated'].sum()

	human_ranking = [int(row['Ranking C-2_1']), int(row['Ranking C-2_2']), int(row['Ranking C-2_3']), int(row['Ranking C-2_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def C3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['b'] == True) & (df['d'] == True) & (df['l'] == True)]['Second_response_based_updated'].sum()
	ranking2 = df[(df['b'] == False) & (df['d'] == True) & (df['l'] == True)]['Second_response_based_updated'].sum()
	ranking3 = df[(df['b'] == False) & (df['d'] == False) & (df['l'] == False)]['Second_response_based_updated'].sum()
	ranking4 = df[(df['b'] == True) & (df['d'] == True) & (df['l'] == False)]['Second_response_based_updated'].sum()
	
	human_ranking = [int(row['Ranking C-3_2']), int(row['Ranking C-3_3']), int(row['Ranking C-3_4']), int(row['Ranking C-3_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


def second_response_update(num):
	if num == 1:
		C1_response_based_update()
		# a, d, e: F, F, F/T, T, F/ T, F, F/F, T, F
	elif num == 2:
		C2_response_based_update()
		# l, d, e: T, T, T/F, T, T/T, F, F/F, T, F
	elif num == 3:
		C3_response_based_update()
		# b, d, l: T, T, T/F, T, T/F, F, F/T, T, F

