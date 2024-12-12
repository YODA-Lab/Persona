from basic_function import confidence_choose
from basic_function import inverse_function
from basic_function import sort_dict_by_values
from basic_function import spearman_rank_correlation

import pandas as pd
import random

def first_trust_based_update(row, s, r):
	# a: True, b: True
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'Overall confidence')
	real_prob = trust_degree
	filtered_rows = df[(df['a'] == True) & (df['b'] == True)]
	sum_of_updated = filtered_rows['Initial'].sum()
	df.loc[(df['a'] == True) & (df['b'] == True), 'First_trust_based_updated'] = df['Initial']/sum_of_updated * real_prob
	df['First_trust_based_updated'] = df['First_trust_based_updated'].fillna(df['Initial']/(1 - sum_of_updated) * (1 - real_prob))
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
	real_prob = 0.7
	filtered_rows = df[(df['c'] == False) & (df['a'] == False)]
	sum_of_updated = filtered_rows['First_trust_based_updated'].sum()
	df.loc[(df['c'] == False) & (df['a'] == False), 'First_response_based_updated'] = df['First_trust_based_updated']/sum_of_updated * real_prob
	df['First_response_based_updated'] = df['First_response_based_updated'].fillna(df['First_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
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


	human_ranking = [int(row['Ranking B_1']), int(row['Ranking B_2']), int(row['Ranking B_3']), int(row['Ranking B_4'])]

	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation




# def round1_ranking(row):
# a, b, c: T, T, F/F, T, F/ T, F, F/ F, F, F
	