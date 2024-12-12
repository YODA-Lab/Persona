from basic_function import confidence_choose
from basic_function import inverse_function
from basic_function import sort_dict_by_values
from basic_function import spearman_rank_correlation

import pandas as pd
import random


# B1 Response
def B1_trust_based_update(row,s,r):
	# f: True, e: True, d: True, a: True
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-1 confidence')
	real_prob = inverse_function(trust_degree, s, r)
	filtered_rows = df[(df['a'] == True) & (df['f'] == True) & (df['e'] == True) & (df['d'] == True)]
	sum_of_updated = filtered_rows['Second_response_based_updated'].sum()
	df.loc[(df['a'] == True) & (df['f'] == True) & (df['e'] == True) & (df['d'] == True), 'Third_trust_based_updated'] = df['Second_response_based_updated']/sum_of_updated * real_prob
	df['Third_trust_based_updated'] = df['Third_trust_based_updated'].fillna(df['Second_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B1_trust_update():
	# f: True, e: True, d: True, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['a'] == True) & (df['f'] == True) & (df['e'] == True) & (df['d'] == True)]
	sum_of_updated = filtered_rows['Second_response_based_updated'].sum()
	df.loc[(df['a'] == True) & (df['f'] == True) & (df['e'] == True) & (df['d'] == True), 'Third_trust_based_updated'] = df['Second_response_based_updated']/sum_of_updated * real_prob
	df['Third_trust_based_updated'] = df['Third_trust_based_updated'].fillna(df['Second_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


# B2 Response
def B2_trust_based_update(row,s,r):
	# f: True, e: True, a: True
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-2 confidence')
	real_prob = inverse_function(trust_degree, s, r)
	filtered_rows = df[(df['a'] == True) & (df['f'] == True) & (df['e'] == True)]
	sum_of_updated = filtered_rows['Second_response_based_updated'].sum()
	df.loc[(df['a'] == True) & (df['f'] == True) & (df['e'] == True), 'Third_trust_based_updated'] = df['Second_response_based_updated']/sum_of_updated * real_prob
	df['Third_trust_based_updated'] = df['Third_trust_based_updated'].fillna(df['Second_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B2_trust_update():
	# f: True, e: True, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['a'] == True) & (df['f'] == True) & (df['e'] == True)]
	sum_of_updated = filtered_rows['Second_response_based_updated'].sum()
	df.loc[(df['a'] == True) & (df['f'] == True) & (df['e'] == True), 'Third_trust_based_updated'] = df['Second_response_based_updated']/sum_of_updated * real_prob
	df['Third_trust_based_updated'] = df['Third_trust_based_updated'].fillna(df['Second_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

# B3 Response
def B3_trust_based_update(row,s,r):
	# f: True, e: True, a: True
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-3 confidence')
	real_prob = inverse_function(trust_degree, s, r)
	filtered_rows = df[(df['a'] == True) & (df['f'] == True) & (df['e'] == True)]
	sum_of_updated = filtered_rows['Second_response_based_updated'].sum()
	df.loc[(df['a'] == True) & (df['f'] == True) & (df['e'] == True), 'Third_trust_based_updated'] = df['Second_response_based_updated']/sum_of_updated * real_prob
	df['Third_trust_based_updated'] = df['Third_trust_based_updated'].fillna(df['Second_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B3_trust_update():
	# f: True, e: True, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['a'] == True) & (df['f'] == True) & (df['e'] == True)]
	sum_of_updated = filtered_rows['Second_response_based_updated'].sum()
	df.loc[(df['a'] == True) & (df['f'] == True) & (df['e'] == True), 'Third_trust_based_updated'] = df['Second_response_based_updated']/sum_of_updated * real_prob
	df['Third_trust_based_updated'] = df['Third_trust_based_updated'].fillna(df['Second_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def third_trust_update(num):
	if num == 1:
		B1_trust_based_update()
	elif num == 2:
		B2_trust_based_update()
	elif num == 3:
		B3_trust_based_update()

# B1_1_response
def B1_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# g: False, f: False
	real_prob = 0.9
	filtered_rows = df[(df['g'] == False) & (df['f'] == False)]
	sum_of_updated = filtered_rows['Third_trust_based_updated'].sum()
	df.loc[(df['g'] == False) & (df['f'] == False), 'Third_response_based_updated'] = df['Third_trust_based_updated']/sum_of_updated * real_prob
	df['Third_response_based_updated'] = df['Third_response_based_updated'].fillna(df['Third_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

# B1_2_response
def B1_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# g: False, d: False
	real_prob = 0.5
	filtered_rows = df[(df['g'] == False) & (df['d'] == False)]
	sum_of_updated = filtered_rows['Third_trust_based_updated'].sum()
	df.loc[(df['g'] == False) & (df['d'] == False), 'Third_response_based_updated'] = df['Third_trust_based_updated']/sum_of_updated * real_prob
	df['Third_response_based_updated'] = df['Third_response_based_updated'].fillna(df['Third_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

# B1_3_response
def B1_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# g: False, a: False
	real_prob = 0.7
	filtered_rows = df[(df['g'] == False) & (df['a'] == False)]
	sum_of_updated = filtered_rows['Third_trust_based_updated'].sum()
	df.loc[(df['g'] == False) & (df['a'] == False), 'Third_response_based_updated'] = df['Third_trust_based_updated']/sum_of_updated * real_prob
	df['Third_response_based_updated'] = df['Third_response_based_updated'].fillna(df['Third_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)



# B2_1_response
def B2_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# g: False, a: False
	real_prob = 0.5
	filtered_rows = df[(df['g'] == False) & (df['a'] == False)]
	sum_of_updated = filtered_rows['Third_trust_based_updated'].sum()
	df.loc[(df['g'] == False) & (df['a'] == False), 'Third_response_based_updated'] = df['Third_trust_based_updated']/sum_of_updated * real_prob
	df['Third_response_based_updated'] = df['Third_response_based_updated'].fillna(df['Third_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B2_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# g: False, a: False
	real_prob = 0.5
	filtered_rows = df[(df['g'] == False) & (df['a'] == False)]
	sum_of_updated = filtered_rows['Third_trust_based_updated'].sum()
	df.loc[(df['g'] == False) & (df['a'] == False), 'Third_response_based_updated'] = df['Third_trust_based_updated']/sum_of_updated * real_prob
	df['Third_response_based_updated'] = df['Third_response_based_updated'].fillna(df['Third_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B2_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# g: False, a: False
	real_prob = 0.7
	filtered_rows = df[(df['g'] == False) & (df['a'] == False)]
	sum_of_updated = filtered_rows['Third_trust_based_updated'].sum()
	df.loc[(df['g'] == False) & (df['a'] == False), 'Third_response_based_updated'] = df['Third_trust_based_updated']/sum_of_updated * real_prob
	df['Third_response_based_updated'] = df['Third_response_based_updated'].fillna(df['Third_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B3_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# g: False, f: False
	real_prob = 0.9
	filtered_rows = df[(df['g'] == False) & (df['f'] == False)]
	sum_of_updated = filtered_rows['Third_trust_based_updated'].sum()
	df.loc[(df['g'] == False) & (df['f'] == False), 'Third_response_based_updated'] = df['Third_trust_based_updated']/sum_of_updated * real_prob
	df['Third_response_based_updated'] = df['Third_response_based_updated'].fillna(df['Third_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B3_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# g: False, a: False
	real_prob = 0.5
	filtered_rows = df[(df['g'] == False) & (df['a'] == False)]
	sum_of_updated = filtered_rows['Third_trust_based_updated'].sum()
	df.loc[(df['g'] == False) & (df['a'] == False), 'Third_response_based_updated'] = df['Third_trust_based_updated']/sum_of_updated * real_prob
	df['Third_response_based_updated'] = df['Third_response_based_updated'].fillna(df['Third_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B3_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# g: False, a: False
	real_prob = 0.7
	filtered_rows = df[(df['g'] == False) & (df['a'] == False)]
	sum_of_updated = filtered_rows['Third_trust_based_updated'].sum()
	df.loc[(df['g'] == False) & (df['a'] == False), 'Third_response_based_updated'] = df['Third_trust_based_updated']/sum_of_updated * real_prob
	df['Third_response_based_updated'] = df['Third_response_based_updated'].fillna(df['Third_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)



def B1_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['e'] == True) & (df['f'] == False) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking2 = df[(df['e'] == False) & (df['f'] == False) & (df['g'] == False)]['Third_response_based_updated'].sum()
	ranking3 = df[(df['e'] == True) & (df['f'] == True) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking4 = df[(df['e'] == True) & (df['f'] == False) & (df['g'] == False)]['Third_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-1-1_2']), int(row['Ranking B-1-1_3']), int(row['Ranking B-1-1_4']), int(row['Ranking B-1-1_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B1_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == True) & (df['g'] == False) & (df['l'] == True)]['Third_response_based_updated'].sum()
	ranking2 = df[(df['f'] == False) & (df['g'] == True) & (df['l'] == False)]['Third_response_based_updated'].sum()
	ranking3 = df[(df['f'] == True) & (df['g'] == True) & (df['l'] == True)]['Third_response_based_updated'].sum()
	ranking4 = df[(df['f'] == False) & (df['g'] == False) & (df['l'] == False)]['Third_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-1-2_1']), int(row['Ranking B-1-2_2']), int(row['Ranking B-1-2_3']), int(row['Ranking B-1-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B1_3_calculation(row):

	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['e'] == True) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['e'] == False) & (df['g'] == False)]['Third_response_based_updated'].sum()
	ranking3 = df[(df['a'] == True) & (df['e'] == True) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['e'] == True) & (df['g'] == False)]['Third_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-1-3_1']), int(row['Ranking B-1-3_2']), int(row['Ranking B-1-3_3']), int(row['Ranking B-1-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B2_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['g'] == False) & (df['l'] == True)]['Third_response_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['g'] == True) & (df['l'] == False)]['Third_response_based_updated'].sum()
	ranking3 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == False)]['Third_response_based_updated'].sum()
	ranking4 = df[(df['d'] == True) & (df['g'] == True) & (df['l'] == True)]['Third_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-2-1_1']), int(row['Ranking B-2-1_2']), int(row['Ranking B-2-1_3']), int(row['Ranking B-2-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B2_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['g'] == False) & (df['l'] == True)]['Third_response_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['g'] == True) & (df['l'] == False)]['Third_response_based_updated'].sum()
	ranking3 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == False)]['Third_response_based_updated'].sum()
	ranking4 = df[(df['d'] == True) & (df['g'] == True) & (df['l'] == True)]['Third_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-2-2_1']), int(row['Ranking B-2-2_2']), int(row['Ranking B-2-2_3']), int(row['Ranking B-2-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B2_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == True) & (df['d'] == True) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['d'] == True) & (df['g'] == False)]['Third_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['d'] == False) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['d'] == False) & (df['g'] == False)]['Third_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-2-3_1']), int(row['Ranking B-2-3_2']), int(row['Ranking B-2-3_3']), int(row['Ranking B-2-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B3_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == False) & (df['f'] == False) & (df['g'] == False)]['Third_response_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['f'] == True) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking3 = df[(df['d'] == True) & (df['f'] == True) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking4 = df[(df['d'] == True) & (df['f'] == False) & (df['g'] == False)]['Third_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-3-1_2']), int(row['Ranking B-3-1_3']), int(row['Ranking B-3-1_4']), int(row['Ranking B-3-1_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B3_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['g'] == False) & (df['l'] == True)]['Third_response_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == False)]['Third_response_based_updated'].sum()
	ranking3 = df[(df['d'] == True) & (df['g'] == True) & (df['l'] == True)]['Third_response_based_updated'].sum()
	ranking4 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == True)]['Third_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-3-2_1']), int(row['Ranking B-3-2_2']), int(row['Ranking B-3-2_3']), int(row['Ranking B-3-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B3_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == True) & (df['c'] == False) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['c'] == True) & (df['g'] == True)]['Third_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['c'] == True) & (df['g'] == False)]['Third_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['c'] == False) & (df['g'] == False)]['Third_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-3-3_1']), int(row['Ranking B-3-3_2']), int(row['Ranking B-3-3_3']), int(row['Ranking B-3-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def third_response_update(num1, num2):
	if num1 == 1:
		if num2 == 1:
			B1_1_response_based_update()
			# e, f, g: T, F, T/ F, F, F/T, T, T/T, F, F
		elif num2 == 2:
			B1_2_response_based_update()
			# f, g, l: T, F, T/ F, T, F/T, T, T/ F, F, F
		elif num2 == 3:
			B1_3_response_based_update()
			# a, e, g: F, T, T/F, F, F/ T, T, T/F, T, F
	elif num1 == 2:
		if num2 == 1:
			B2_1_response_based_update()
			# d, g, l: T, F, T/ F, T, F/F, F, F/ T, T, T
		elif num2 == 2:
			B2_2_response_based_update()
			# d, g, l: T, F, T/ F, T, F/F, F, F/ T, T, T
		elif num2 == 3:
			B2_3_response_based_update()
			# a, d, g: T, T, T/ F,T,F/F, F, T/F, F, F
	elif num1 == 3:
		if num2 == 1:
			B3_1_response_based_update()
			# d, f, g: F, F, F/ F, T, T/T, T, T/T, F, F
		elif num2 == 2:
			B3_2_response_based_update()
			# d, g, l: T, F, T/F, F, F/T, T, T/F, F, T
		elif num2 == 3:
			B3_3_response_based_update()
			# a, c, g: T, T, T/ F,T,T/F, T, F/F, F, F




