from basic_function import confidence_choose
from basic_function import inverse_function
from basic_function import sort_dict_by_values
from basic_function import spearman_rank_correlation

import pandas as pd
import random


def B1_1_1_trust_based_update(row, s, r):
	# k: True, j: True
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-1-1-1 confidence')
	real_prob = inverse_function(trust_degree, s, r)
	filtered_rows = df[(df['k'] == True) & (df['j'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['j'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B1_1_1_trust_update():
	# k: True, j: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['k'] == True) & (df['j'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['j'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B1_1_2_trust_based_update(row, s, r):
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-1-1-2 confidence')
	real_prob = inverse_function(trust_degree, s, r)
	filtered_rows = df[(df['k'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B1_1_2_trust_update():
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['k'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B1_1_3_trust_based_update(row, s, r):
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-1-1-3 confidence')
	real_prob = inverse_function(trust_degree, s, r)
	filtered_rows = df[(df['k'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B1_1_3_trust_update():
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['k'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B1_2_1_trust_based_update(row, s, r):
	# j: True, g: True
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-1-2-1 confidence')
	real_prob = inverse_function(trust_degree, s, r)
	filtered_rows = df[(df['j'] == True) & (df['g'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['j'] == True)  & (df['g'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B1_2_1_trust_update():
	# j: True, g: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['j'] == True) & (df['g'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['j'] == True)  & (df['g'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B1_2_2_trust_based_update(row, s, r):
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-1-2-2 confidence')
	real_prob = inverse_function(trust_degree, s, r)
	filtered_rows = df[(df['j'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['j'] == True)  & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B1_2_2_trust_update():
	# j: True, i: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['j'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['j'] == True)  & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B1_2_3_trust_based_update(row, s, r):
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-1-2-3 confidence')
	real_prob = inverse_function(trust_degree, s, r)
	filtered_rows = df[(df['j'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['j'] == True)  & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B1_2_3_trust_update():
	# j: True, i: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['j'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['j'] == True)  & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B2_1_1_trust_based_update(row, s, r):
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-2-1-1 confidence')
	real_prob = inverse_function(trust_degree, s, r)
	filtered_rows = df[(df['k'] == True) & (df['j'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['j'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B2_1_1_trust_update():
	# k: True, j: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['k'] == True) & (df['j'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['j'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B2_1_2_trust_based_update(row, s, r):
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-2-1-2 confidence')
	real_prob = inverse_function(trust_degree, s, r)
	filtered_rows = df[(df['k'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B2_1_2_trust_update():
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['k'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B2_1_3_trust_based_update(row, s, r):
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-2-1-3 confidence')
	real_prob = inverse_function(trust_degree, s, r)
	filtered_rows = df[(df['k'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B2_1_3_trust_update():
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['k'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B2_2_3_trust_based_update(row, s, r):
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-2-2-3 confidence')
	real_prob = inverse_function(trust_degree, s, r)
	filtered_rows = df[(df['j'] == False) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['j'] == False) & (df['a'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B2_2_3_trust_update():
	# j: False, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['j'] == False) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['j'] == False) & (df['a'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B3_1_1_trust_based_update(row, s, r):
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-3-1-1 confidence')
	real_prob = inverse_function(trust_degree, s, r)
	filtered_rows = df[(df['k'] == True) & (df['j'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['j'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B3_1_1_trust_update():
	# k: True, j: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['k'] == True) & (df['j'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['j'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B3_1_2_trust_based_update(row, s, r):
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-3-1-2 confidence')
	real_prob = inverse_function(trust_degree, s, r)
	filtered_rows = df[(df['k'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B3_1_2_trust_update():
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['k'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B3_1_3_trust_based_update(row, s, r):
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-3-1-3 confidence')
	real_prob = inverse_function(trust_degree, s, r)
	filtered_rows = df[(df['k'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B3_1_3_trust_update():
	# k: True, i: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['k'] == True) & (df['i'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['k'] == True) & (df['i'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B3_2_3_trust_based_update(row, s, r):
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-3-2-3 confidence')
	real_prob = inverse_function(trust_degree, s, r)
	filtered_rows = df[(df['j'] == False) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['j'] == False) & (df['a'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B3_2_3_trust_update():
	# j: False, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['j'] == False) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Fourth_response_based_updated'].sum()
	df.loc[(df['j'] == False) & (df['a'] == True), 'Fifth_trust_based_updated'] = df['Fourth_response_based_updated']/sum_of_updated * real_prob
	df['Fifth_trust_based_updated'] = df['Fifth_trust_based_updated'].fillna(df['Fourth_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B1_1_1_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['l'] == True) & (df['g'] == False) & (df['i'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['l'] == False) & (df['g'] == True) & (df['i'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['l'] == False) & (df['g'] == True) & (df['i'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['l'] == True) & (df['g'] == False) & (df['i'] == True)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-1-1-1 F_1']), int(row['Ranking B-1-1-1 F_2']), int(row['Ranking B-1-1-1 F_3']), int(row['Ranking B-1-1-1 F_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B1_1_1_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['e'] == False) & (df['d'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking B-1-1-1 A_1']), int(row['Ranking B-1-1-1 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [1, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def B1_1_2_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['g'] == True) & (df['h'] == False) & (df['l'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['g'] == False) & (df['h'] == False) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['h'] == False) & (df['l'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['g'] == False) & (df['h'] == True) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-1-1-2 F_1']), int(row['Ranking B-1-1-2 F_2']), int(row['Ranking B-1-1-2 F_3']), int(row['Ranking B-1-1-2 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B1_1_2_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['e'] == False) & (df['d'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking B-1-1-2 A_1']), int(row['Ranking B-1-1-2 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [1, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def B1_1_3_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['g'] == True) & (df['h'] == False) & (df['k'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['g'] == False) & (df['h'] == False) & (df['k'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['h'] == False) & (df['k'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['g'] == False) & (df['h'] == True) & (df['k'] == True)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-1-1-3 F_1']), int(row['Ranking B-1-1-3 F_2']), int(row['Ranking B-1-1-3 F_3']), int(row['Ranking B-1-1-3 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B1_1_3_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['e'] == False) & (df['d'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking B-1-1-3 A_1']), int(row['Ranking B-1-1-3 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [1, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def B1_2_1_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['l'] == False) & (df['f'] == True) & (df['j'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['l'] == True) & (df['f'] == True) & (df['j'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['l'] == False) & (df['f'] == True) & (df['j'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['l'] == True) & (df['f'] == True) & (df['j'] == True)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-1-2-1 F_1']), int(row['Ranking B-1-2-1 F_2']), int(row['Ranking B-1-2-1 F_3']), int(row['Ranking B-1-2-1 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B1_2_1_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['e'] == False) & (df['d'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking B-1-2-1 A_1']), int(row['Ranking B-1-2-1 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [1, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def B1_2_2_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['l'] == True) & (df['f'] == True) & (df['h'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['l'] == True) & (df['f'] == True) & (df['h'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['l'] == False) & (df['f'] == False) & (df['h'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['l'] == False) & (df['f'] == True) & (df['h'] == True)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-1-2-2 F_1']), int(row['Ranking B-1-2-2 F_2']), int(row['Ranking B-1-2-2 F_3']), int(row['Ranking B-1-2-2 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B1_2_2_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['e'] == False) & (df['d'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking B-1-2-2 A_1']), int(row['Ranking B-1-2-2 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [1, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def B1_2_3_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['l'] == False) & (df['f'] == True) & (df['j'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['l'] == False) & (df['f'] == True) & (df['j'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['l'] == True) & (df['f'] == False) & (df['j'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['l'] == True) & (df['f'] == True) & (df['j'] == True)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-1-2-3 F_1']), int(row['Ranking B-1-2-3 F_2']), int(row['Ranking B-1-2-3 F_3']), int(row['Ranking B-1-2-3 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B1_2_3_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['e'] == False) & (df['d'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking B-1-2-3 A_1']), int(row['Ranking B-1-2-3 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [1, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def B1_3_1_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()


	human_ranking = [int(row['Ranking B-1-3-1 A_2']), int(row['Ranking B-1-3-1 A_3']), int(row['Ranking B-1-3-1 A_4']), int(row['Ranking B-1-3-1 A_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 3, 4, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def B1_3_2_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()


	human_ranking = [int(row['Ranking B-1-3-2 A_2']), int(row['Ranking B-1-3-2 A_3']), int(row['Ranking B-1-3-2 A_4']), int(row['Ranking B-1-3-2 A_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 3, 4, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def B1_3_3_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['e'] == True) & (df['d'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()


	human_ranking = [int(row['Ranking B-1-3-3 A_1']), int(row['Ranking B-1-3-3 A_2']), int(row['Ranking B-1-3-3 A_3']), int(row['Ranking B-1-3-3 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 3, 4, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def B2_1_1_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['i'] == False) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['i'] == True) & (df['l'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['d'] == False) & (df['i'] == False) & (df['l'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['d'] == True) & (df['i'] == True) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-2-1-1 F_1']), int(row['Ranking B-2-1-1 F_2']), int(row['Ranking B-2-1-1 F_3']), int(row['Ranking B-2-1-1 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


def B2_1_1_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['e'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['h'] == True) & (df['i'] == True) & (df['g'] == True)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking B-2-1-1 A_1']), int(row['Ranking B-2-1-1 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [2, 1]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def B2_1_2_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['h'] == True) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['h'] == False) & (df['l'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['d'] == True) & (df['h'] == False) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['d'] == True) & (df['h'] == True) & (df['l'] == False)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-2-1-2 F_1']), int(row['Ranking B-2-1-2 F_2']), int(row['Ranking B-2-1-2 F_3']), int(row['Ranking B-2-1-2 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


def B2_1_2_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['e'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['h'] == True) & (df['i'] == True) & (df['g'] == True)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking B-2-1-2 A_1']), int(row['Ranking B-2-1-2 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [2, 1]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def B2_1_3_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['k'] == True) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['k'] == False) & (df['l'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['d'] == True) & (df['k'] == False) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['d'] == True) & (df['k'] == True) & (df['l'] == False)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-2-1-3 F_1']), int(row['Ranking B-2-1-3 F_2']), int(row['Ranking B-2-1-3 F_3']), int(row['Ranking B-2-1-3 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


def B2_1_3_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['e'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['h'] == True) & (df['i'] == True) & (df['g'] == True)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking B-2-1-3 A_1']), int(row['Ranking B-2-1-3 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [2, 1]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def B2_2_3_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['g'] == False) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['g'] == True) & (df['l'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['d'] == True) & (df['g'] == True) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-2-2-3 F_1']), int(row['Ranking B-2-2-3 F_2']), int(row['Ranking B-2-2-3 F_3']), int(row['Ranking B-2-2-3 F_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B2_2_1_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['h'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['g'] == False) & (df['h'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()


	human_ranking = [int(row['Ranking B-2-2-1 A_1']), int(row['Ranking B-2-2-1 A_2']), int(row['Ranking B-2-2-1 A_3']), int(row['Ranking B-2-2-1 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 4, 3, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def B2_2_2_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == True) & (df['h'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['g'] == False) & (df['h'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()


	human_ranking = [int(row['Ranking B-2-2-2 A_1']), int(row['Ranking B-2-2-2 A_2']), int(row['Ranking B-2-2-2 A_3']), int(row['Ranking B-2-2-2 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 4, 3, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def B2_2_3_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['j'] == False) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['g'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking B-2-2-3 A_1']), int(row['Ranking B-2-2-3 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [1, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def B2_3_1_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['e'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()

	human_ranking = [int(row['Ranking B-2-3-1 A_1']), int(row['Ranking B-2-3-1 A_2']), int(row['Ranking B-2-3-1 A_3']), int(row['Ranking B-2-3-1 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 2, 3, 4]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def B2_3_2_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['e'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()

	human_ranking = [int(row['Ranking B-2-3-2 A_1']), int(row['Ranking B-2-3-2 A_2']), int(row['Ranking B-2-3-2 A_3']), int(row['Ranking B-2-3-2 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 2, 3, 4]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter



def B2_3_3_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['e'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()

	human_ranking = [int(row['Ranking B-2-3-3 A_1']), int(row['Ranking B-2-3-3 A_2']), int(row['Ranking B-2-3-3 A_3']), int(row['Ranking B-2-3-3 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 2, 3, 4]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def B3_1_1_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['g'] == False) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['d'] == True) & (df['g'] == True) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-3-1-1 F_1']), int(row['Ranking B-3-1-1 F_2']), int(row['Ranking B-3-1-1 F_3']), int(row['Ranking B-3-1-1 F_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


def B3_1_1_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['g'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['h'] == True) & (df['i'] == True) & (df['g'] == True)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking B-3-1-1 A_1']), int(row['Ranking B-3-1-1 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [2, 1]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def B3_1_2_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['g'] == False) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['d'] == True) & (df['g'] == True) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-3-1-2 F_1']), int(row['Ranking B-3-1-2 F_2']), int(row['Ranking B-3-1-2 F_4']), int(row['Ranking B-3-1-2 F_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B3_1_2_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['g'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['h'] == True) & (df['i'] == True) & (df['g'] == True)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking B-3-1-2 A_1']), int(row['Ranking B-3-1-2 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [2, 1]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def B3_1_3_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['g'] == False) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['d'] == True) & (df['g'] == True) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking B-3-1-3 F_1']), int(row['Ranking B-3-1-3 F_2']), int(row['Ranking B-3-1-3 F_3']), int(row['Ranking B-3-1-3 F_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B3_1_3_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['g'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['h'] == True) & (df['i'] == True) & (df['g'] == True)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking B-3-1-3 A_1']), int(row['Ranking B-3-1-3 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [2, 1]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def B3_2_3_F_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['g'] == False) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['g'] == True) & (df['l'] == False)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['d'] == True) & (df['g'] == True) & (df['l'] == True)]['Fifth_trust_based_updated'].sum()
	
	human_ranking = [int(row['Ranking B-3-2-3 F_1']), int(row['Ranking B-3-2-3 F_2']), int(row['Ranking B-3-2-3 F_3']), int(row['Ranking B-3-2-3 F_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B3_2_1_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['h'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['g'] == False) & (df['h'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()


	human_ranking = [int(row['Ranking B-3-2-1 A_1']), int(row['Ranking B-3-2-1 A_2']), int(row['Ranking B-3-2-1 A_3']), int(row['Ranking B-3-2-1 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 4, 3, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def B3_2_2_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['h'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['g'] == False) & (df['h'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()


	human_ranking = [int(row['Ranking B-3-2-2 A_1']), int(row['Ranking B-3-2-2 A_2']), int(row['Ranking B-3-2-2 A_3']), int(row['Ranking B-3-2-2 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 4, 3, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def B3_2_3_A_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['j'] == False) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['g'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()

	human_ranking = [int(row['Ranking B-3-2-3 A_1']), int(row['Ranking B-3-2-3 A_2'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1]

	hunter_ranking = [1, 2]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter

def B3_3_1_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['e'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()

	human_ranking = [int(row['Ranking B-3-3-1 A_1']), int(row['Ranking B-3-3-1 A_2']), int(row['Ranking B-3-3-1 A_3']), int(row['Ranking B-3-3-1 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 2, 3, 4]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def B3_3_2_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['e'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()

	human_ranking = [int(row['Ranking B-3-3-2 A_1']), int(row['Ranking B-3-3-2 A_2']), int(row['Ranking B-3-3-2 A_3']), int(row['Ranking B-3-3-2 A_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]

	hunter_ranking = [1, 2, 3, 4]

	correlation_calculated = spearman_rank_correlation(calculated_ranking,human_ranking)
	correlation_hunter = spearman_rank_correlation(hunter_ranking,human_ranking)

	return correlation_calculated, correlation_hunter


def B3_3_3_A_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['i'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['e'] == True) & (df['a'] == True)]['Fifth_trust_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['a'] == False)]['Fifth_trust_based_updated'].sum()

	human_ranking = [int(row['Ranking B-3-3-3 A_1']), int(row['Ranking B-3-3-3 A_2']), int(row['Ranking B-3-3-3 A_3']), int(row['Ranking B-3-3-3 A_4'])]

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
				B1_1_1_trust_update()
				#l, g, i: T, F, F/F, T, T/F, T, F/T, F, T
			elif num3 == 2:
				B1_1_2_trust_update()
				# g, h, l: T, F, F/F, F, T/F, F, F/ F, T, T
			elif num3 == 3:
				B1_1_3_trust_update()
				# g, h, k: T, F, F/F, F, T/F, F, F/ F, T, T
		elif num2 == 2:
			if num3 == 1:
				B1_2_1_trust_update()
				# l, f, j: F, T, T/T, T, F/F, T, F/ T, T, T
			elif num3 == 2:
				B1_2_2_trust_update()
				# l, f, h: T, T, T/T, T, F/F, F, F/F, T, T
			elif num3 == 3:
				B1_2_3_trust_update()
				# l, f, j: F, T, T/F, T ,F/T, F, F/T, T, T
	elif num1 == 2:
		if num2 == 1:
			if num3 == 1:
				B2_1_1_trust_update()
				# d, i, l: T, F, T/ F, T, F/F, F, F/ T, T, T
			elif num3 == 2:
				B2_1_2_trust_update()
				# d, h, l: T, T, T/F, F, F/T, F, T/T, T, F
			elif num3 == 3:
				B2_1_3_trust_update()
				# d, k, l: T, T, T/F, F, F/T, F, T/T, T, F
		elif num2 == 2:
			if num3 == 3:
				B2_2_3_trust_update()
				# d, g, l: T, F, T/ F, T, F/F, F, F/ T, T, T
	elif num1 == 3:
		if num2 == 1:
			if num3 == 1:
				B3_1_1_trust_update()
				# d, g, l: T, F, T/F, F, F/T, T, T/F, F, T
			elif num3 == 2:
				B3_1_2_trust_update()
				# d, g, l: T, F, T/F, F, F/T, T, T/F, F, T
			elif num3 == 3:
				B3_1_3_trust_update()
				# d, g, l: T, F, T/F, F, F/T, T, T/F, F, T
		elif num2 == 2:
			if num3 == 3:
				B3_2_3_trust_update()
				# d, g, l: T, F, T/ F, T, F/F, F, F/ T, T, T
