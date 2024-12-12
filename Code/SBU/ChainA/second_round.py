from basic_function import confidence_choose
from basic_function import inverse_function
from basic_function import sort_dict_by_values
from basic_function import spearman_rank_correlation

import pandas as pd
import random

def second_trust_based_update(row, s, r):
	# c: False, d: True, a: True
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'Chain A confidence')
	real_prob = trust_degree
	filtered_rows = df[(df['a'] == True) & (df['d'] == True) & (df['c'] == False)]
	sum_of_updated = filtered_rows['First_response_based_updated'].sum()
	df.loc[(df['a'] == True) & (df['d'] == True) & (df['c'] == False), 'Second_trust_based_updated'] = df['First_response_based_updated']/sum_of_updated * real_prob
	df['Second_trust_based_updated'] = df['Second_trust_based_updated'].fillna(df['First_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def second_trust_update():
	# c: False, d: True, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['a'] == True) & (df['d'] == True) & (df['c'] == False)]
	sum_of_updated = filtered_rows['First_response_based_updated'].sum()
	df.loc[(df['a'] == True) & (df['d'] == True) & (df['c'] == False), 'Second_trust_based_updated'] = df['First_response_based_updated']/sum_of_updated * real_prob
	df['Second_trust_based_updated'] = df['Second_trust_based_updated'].fillna(df['First_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def A1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# e: False, d: False, a: False
	real_prob = 0.7
	filtered_rows = df[(df['d'] == False) & (df['a'] == False) & (df['e'] == False)]
	sum_of_updated = filtered_rows['Second_trust_based_updated'].sum()
	df.loc[(df['d'] == False) & (df['a'] == False) & (df['e'] == False), 'Second_response_based_updated'] = df['Second_trust_based_updated']/sum_of_updated * real_prob
	df['Second_response_based_updated'] = df['Second_response_based_updated'].fillna(df['Second_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def A2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# e: False, a: False
	real_prob = 0.5
	filtered_rows = df[(df['a'] == False) & (df['e'] == False)]
	sum_of_updated = filtered_rows['Second_trust_based_updated'].sum()
	df.loc[(df['a'] == False) & (df['e'] == False), 'Second_response_based_updated'] = df['Second_trust_based_updated']/sum_of_updated * real_prob
	df['Second_response_based_updated'] = df['Second_response_based_updated'].fillna(df['Second_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def A3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# e: False, a: False
	real_prob = 0.3
	filtered_rows = df[(df['a'] == False) & (df['e'] == False)]
	sum_of_updated = filtered_rows['Second_trust_based_updated'].sum()
	df.loc[(df['a'] == False) & (df['e'] == False), 'Second_response_based_updated'] = df['Second_trust_based_updated']/sum_of_updated * real_prob
	df['Second_response_based_updated'] = df['Second_response_based_updated'].fillna(df['Second_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

# def second_response_based_update(row):
# 	if row['Chain A choices'] == "The extra service fee results in high costs, making Luminara Gardens unsuitable for parties. (High Confidence)":
# 		A1_response_based_update()
# 	elif row['Chain A choices'] == "Luminara Gardens has no entertainment facilities that would make it unsuitable for parties. (Average Confidence)":
# 		A2_response_based_update()
# 	elif row['Chain A choices'] == "The unavailability of accommodation makes Luminara Gardens unsuitable for parties. (Low Confidence)":
# 		A3_response_based_update()

def A1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['d'] == False) & (df['e'] == False)]['Second_response_based_updated'].sum()
	ranking2 = df[(df['a'] == True) & (df['d'] == True) & (df['e'] == False)]['Second_response_based_updated'].sum()
	ranking3 = df[(df['a'] == True) & (df['d'] == False) & (df['e'] == False)]['Second_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['d'] == True) & (df['e'] == False)]['Second_response_based_updated'].sum()

	human_ranking = [int(row['Ranking A-1_2']), int(row['Ranking A-1_3']), int(row['Ranking A-1_4']), int(row['Ranking A-1_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)


	return correlation

def A2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['c'] == True) & (df['d'] == True) & (df['e'] == True)]['Second_response_based_updated'].sum()
	ranking2 = df[(df['c'] == False) & (df['d'] == True) & (df['e'] == True)]['Second_response_based_updated'].sum()
	ranking3 = df[(df['c'] == True) & (df['d'] == True) & (df['e'] == False)]['Second_response_based_updated'].sum()
	ranking4 = df[(df['c'] == False) & (df['d'] == True) & (df['e'] == False)]['Second_response_based_updated'].sum()

	human_ranking = [int(row['Ranking A-2_1']), int(row['Ranking A-2_2']), int(row['Ranking A-2_3']), int(row['Ranking A-2_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


def A3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['b'] == True) & (df['c'] == True) & (df['d'] == False)]['Second_response_based_updated'].sum()
	ranking2 = df[(df['b'] == True) & (df['c'] == False) & (df['d'] == True)]['Second_response_based_updated'].sum()
	ranking3 = df[(df['b'] == False) & (df['c'] == True) & (df['d'] == True)]['Second_response_based_updated'].sum()
	ranking4 = df[(df['b'] == True) & (df['c'] == False) & (df['d'] == False)]['Second_response_based_updated'].sum()
	
	human_ranking = [int(row['Ranking A-3_1']), int(row['Ranking A-3_2']), int(row['Ranking A-3_3']), int(row['Ranking A-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


# def round2_calculation(row):
# 	if row['Chain A choices'] == "The extra service fee results in high costs, making Luminara Gardens unsuitable for parties. (High Confidence)":
# 		return A1_calculation(row)
# 	elif row['Chain A choices'] == "Luminara Gardens has no entertainment facilities that would make it unsuitable for parties. (Average Confidence)":
# 		return A2_calculation(row)
# 	elif row['Chain A choices'] == "The unavailability of accommodation makes Luminara Gardens unsuitable for parties. (Low Confidence)":
# 		return A3_calculation(row)


def second_response_update(num):
	if num == 1:
		A1_response_based_update()
		# a, d, e: F, F, F/T, T, F/ T, F, F/F, T, F
	elif num == 2:
		A2_response_based_update()
		# c, d, e: T, T, T/F, T, T/T, T, F/F, T, F
	elif num == 3:
		A3_response_based_update()
		# b, c, d: T, T, F/T, F, T/F, T, T/T, F, F

