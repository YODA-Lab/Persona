import pandas as pd
import itertools
import csv
import os
import random
from scipy import stats
import argparse
from scipy.optimize import fsolve
import time
import numpy as np


# Data location
current_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_directory, 'data', 'ChainA_data.csv')


# Representation of Chain1
# "a": Luminara Gardens is a suitable venue for parties
# "b": extensive advertising
# "c": 
# "d": 

# Combination of literals
num_variables = 7
variable_combinations = list(itertools.product([True, False], repeat=num_variables))

# Argument input
parser = argparse.ArgumentParser()
parser.add_argument('--s')
parser.add_argument('--r')
parser.add_argument('--check')
args = parser.parse_args()

s = float(args.s)
r = float(args.r)
data = args.check

# 
def inverse_function(y):
	if y <= s:
		x = 0.5 + np.sign(y - s) * np.abs(((y - s) / s))**(1/r) / 2
	else:
		x = 0.5 + np.sign(y - s) * ((y - s) / (1 - s))**(1/r) / 2
	return x

def sort_dict_by_values(d):
	sorted_keys = sorted(d, key=lambda x: (d[x], random.random()), reverse = True)
	sorted_dict = {k: d[k] for k in sorted_keys}
	return sorted_dict

def spearman_rank_correlation(x, y):
	n = len(x)
	rank_diff_squared = sum((x[i]- y[i]) ** 2 for i in range(n))
	correlation = 1 - (6 * rank_diff_squared) / (n * (n ** 2 - 1))
	return correlation

# 
def generate_variable_names(num_variables):
    return [chr(ord('a') + i) for i in range(num_variables)]

# 
def truth_table():
	truth_table = []
	initial_probability = 1 / (2 ** num_variables)
	variable_names = generate_variable_names(num_variables)
	for combination in variable_combinations:
		entry = dict(zip(variable_names, combination))
		entry['Initial'] = initial_probability
		truth_table.append(entry)
	df = pd.DataFrame(truth_table)
	df.to_csv('truth_table.csv', index=False)

def first_trust_based_update(trust_degree):
	# "They think Luminara Gardens is suitable for parties due to its extensive advertising, which highlights its moderate cost per person and delicious food offerings."
	# a: True, b: True, c: True, d: True
	# start_time = time.time()
	# print(start_time)
	df = pd.read_csv('truth_table.csv')
	real_prob = inverse_function(trust_degree)
	filtered_rows = df[(df['a'] == True) & (df['b'] == True) & (df['c'] == True) & (df['d'] == True)]
	sum_of_updated = filtered_rows['Initial'].sum()
	print(sum_of_updated)
	df.loc[(df['a'] == True) & (df['b'] == True) & (df['c'] == True) & (df['d'] == True), 'First_trust_based_updated'] = df['Initial']/sum_of_updated * real_prob
	df['First_trust_based_updated'] = df['First_trust_based_updated'].fillna(df['Initial']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)
	# end_time = time.time()
	# print(end_time)
	# print("First_trust_based_running_time: {:.6f}秒".format(end_time - start_time))


def first_response_based_update():
	# Response: But, since the moderate cost per person is only advertised, I'm not confident there won't be a high service fee.
	# e: False, c: False
	# Not confident -> High uncertainty -> 10%
	df = pd.read_csv('truth_table.csv')
	filtered_rows = df[(df['c'] == False) & (df['e'] == False)]
	sum_of_updated = filtered_rows['First_trust_based_updated'].sum()
	df.loc[(df['c'] == False) & (df['e'] == False), 'First_response_based_updated'] = df['First_trust_based_updated']/sum_of_updated * 0.1
	df['First_response_based_updated'] = df['First_response_based_updated'].fillna(df['First_trust_based_updated']/(1 - sum_of_updated) * 0.9)
	# print(df['First_response_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def first_trust_choose(keywords):
	if row[keywords] == "Almost Complete Trust (I believe Blitzcrank's assessment is well-founded and fully trust its insights almost completely)":
		first_trust_based_update(0.9)
		return 0.9

	elif row[keywords] == "High Trust (I have high confidence in Blitzcrank's explanation and find it to be very credible)":
		first_trust_based_update(0.7)
		return 0.7
	
	elif row[keywords] == "Average Trust (I find Blitzcrank's response to be reasonable, but I remain somewhat skeptical and would like more information)":
		first_trust_based_update(0.5)
		return 0.5
	
	elif row[keywords] == "Low Trust (I am skeptical of Blitzcrank's explanation and question the reliability of its assessment)":
		first_trust_based_update(0.2)
		return 0.2


def round1_ranking(row):

	# b: True, c: True, d: True
	# b: True, c: False, d: True
	# b: True, c: True, d: False
	# b: False, c: False, d: False

	trust_level = first_trust_choose('Overall trust degree')
	
	first_response_based_update()

	df = pd.read_csv('truth_table.csv')
	filter_row_ranking1_1= df[(df['b'] == True) & (df['c'] == True) & (df['d'] == True)]
	ranking1_1 = filter_row_ranking1_1['First_response_based_updated'].sum()

	filter_row_ranking1_2= df[(df['b'] == True) & (df['c'] == False) & (df['d'] == True)]
	ranking1_2 = filter_row_ranking1_2['First_response_based_updated'].sum()

	filter_row_ranking1_3= df[(df['b'] == True) & (df['c'] == True) & (df['d'] == False)]
	ranking1_3 = filter_row_ranking1_3['First_response_based_updated'].sum()

	filter_row_ranking1_4= df[(df['b'] == False) & (df['c'] == False) & (df['d'] == False)]
	ranking1_4 = filter_row_ranking1_4['First_response_based_updated'].sum()



	with open(csv_file_path, newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		human_ranking = [int(row['Ranking 1_1']), int(row['Ranking 1_2']), int(row['Ranking 1_3']), int(row['Ranking 1_4'])]
		# print(human_ranking)

	value_dict = {'Ranking 1_1': ranking1_1, 'Ranking 1_2': ranking1_2, 'Ranking 1_3': ranking1_3, 'Ranking 1_4': ranking1_4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('Ranking 1_1') + 1, list(sorted_dict.keys()).index('Ranking 1_2') + 1, list(sorted_dict.keys()).index('Ranking 1_3') + 1, list(sorted_dict.keys()).index('Ranking 1_4') + 1]
		

	# print(calculated_ranking)

	# print(spearman_rank_correlation(calculated_ranking,human_ranking))

	return sorted_dict, calculated_ranking, human_ranking, spearman_rank_correlation(calculated_ranking,human_ranking), trust_level


def second_trust_based_update(trust_degree):
	# Actually, I have consulted with the manager of Luminara Gardens, and they assured me of a low service fee, resulting in a moderate cost per person.
	# f: True, e: True, c: True
	df = pd.read_csv('truth_table.csv')
	real_prob = inverse_function(trust_degree)
	filtered_rows = df[(df['f'] == True) & (df['e'] == True) & (df['c'] == True)]
	sum_of_updated = filtered_rows['First_response_based_updated'].sum()
	df.loc[(df['f'] == True) & (df['e'] == True) & (df['c'] == True), 'Second_trust_based_updated'] = df['First_response_based_updated']/sum_of_updated * real_prob
	df['Second_trust_based_updated'] = df['Second_trust_based_updated'].fillna(df['First_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def second_response_based_update():
	# Response: But it's quite likely that the manager of Luminara Gardens may be exaggerating to attract customers.
	# f: False, e: False, c: False
	# Quite likely ->  70%
	df = pd.read_csv('truth_table.csv')
	filtered_rows = df[(df['f'] == False) & (df['c'] == False) & (df['e'] == False)]
	sum_of_updated = filtered_rows['Second_trust_based_updated'].sum()
	df.loc[(df['f'] == False) & (df['c'] == False) & (df['e'] == False), 'Second_response_based_updated'] = df['Second_trust_based_updated']/sum_of_updated * 0.7
	df['Second_response_based_updated'] = df['Second_response_based_updated'].fillna(df['Second_trust_based_updated']/(1 - sum_of_updated) * 0.3)
	# print(df['Second_response_based_updated'].sum())
	df.to_csv('truth_table.csv', index=False)

def second_trust_choose(keywords):
	if row[keywords] == "Almost Complete Trust (I believe Blitzcrank's assessment is well-founded and fully trust its insights almost completely)":
		second_trust_based_update(0.9)
		return 0.9

	elif row[keywords] == "High Trust (I have high confidence in Blitzcrank's explanation and find it to be very credible)":
		second_trust_based_update(0.7)
		return 0.7
	
	elif row[keywords] == "Average Trust (I find Blitzcrank's response to be reasonable, but I remain somewhat skeptical and would like more information)":
		second_trust_based_update(0.5)
		return 0.5
	
	elif row[keywords] == "Low Trust (I am skeptical of Blitzcrank's explanation and question the reliability of its assessment)":
		second_trust_based_update(0.2)
		return 0.2

def round2_ranking(row):
	# c: T, e: T, f: T
	# c: T, e: F, f: F
	# c: F, e: F, f: T
	# c: F, e: F, f: F


	trust_level = second_trust_choose('Chain 1 trust')
	
	second_response_based_update()

	df = pd.read_csv('truth_table.csv')
	filter_row_ranking1_1= df[(df['c'] == True) & (df['e'] == True) & (df['f'] == True)]
	ranking1_1 = filter_row_ranking1_1['Second_response_based_updated'].sum()

	filter_row_ranking1_2= df[(df['c'] == True) & (df['e'] == False) & (df['f'] == False)]
	ranking1_2 = filter_row_ranking1_2['Second_response_based_updated'].sum()

	filter_row_ranking1_3= df[(df['c'] == False) & (df['e'] == False) & (df['f'] == True)]
	ranking1_3 = filter_row_ranking1_3['Second_response_based_updated'].sum()

	filter_row_ranking1_4= df[(df['c'] == False) & (df['e'] == False) & (df['f'] == False)]
	ranking1_4 = filter_row_ranking1_4['Second_response_based_updated'].sum()


	with open(csv_file_path, newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		human_ranking = [int(row['Ranking 1-1_1']), int(row['Ranking 1-1_2']), int(row['Ranking 1-1_3']), int(row['Ranking 1-1_4'])]
		# print(human_ranking)

	value_dict = {'Ranking 1-1_1': ranking1_1, 'Ranking 1-1_2': ranking1_2, 'Ranking 1-1_3': ranking1_3, 'Ranking 1-1_4': ranking1_4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('Ranking 1-1_1') + 1, list(sorted_dict.keys()).index('Ranking 1-1_2') + 1, list(sorted_dict.keys()).index('Ranking 1-1_3') + 1, list(sorted_dict.keys()).index('Ranking 1-1_4') + 1]

	# print(calculated_ranking)

	# print(spearman_rank_correlation(calculated_ranking,human_ranking))

	return sorted_dict, calculated_ranking, human_ranking, spearman_rank_correlation(calculated_ranking,human_ranking), trust_level

def third_trust_based_update(trust_degree):
	# "Actually, the authoritative professional website details the approved fees, confirming that the service fee is low."
	# g: True, e: True, c: True, f: True

	df = pd.read_csv('truth_table.csv')

	real_prob = inverse_function(trust_degree)
	filtered_rows = df[(df['g'] == True) & (df['e'] == True) & (df['f'] == True) & (df['c'] == True)]
	sum_of_updated = filtered_rows['Second_response_based_updated'].sum()
	df.loc[(df['g'] == True) & (df['e'] == True) & (df['f'] == True) & (df['c'] == True), 'Third_trust_based_updated'] = df['Second_response_based_updated']/sum_of_updated * real_prob
	df['Third_trust_based_updated'] = df['Third_trust_based_updated'].fillna(df['Second_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	# print(df['Third_trust_based_updated'].sum())

	df.to_csv('truth_table.csv', index=False)

def third_trust_choose(keywords):
	if row[keywords] == "Almost Complete Trust (I believe Blitzcrank's assessment is well-founded and fully trust its insights almost completely)":
		third_trust_based_update(0.9)
		return 0.9

	elif row[keywords] == "High Trust (I have high confidence in Blitzcrank's explanation and find it to be very credible)":
		third_trust_based_update(0.7)
		return 0.7
	
	elif row[keywords] == "Average Trust (I find Blitzcrank's response to be reasonable, but I remain somewhat skeptical and would like more information)":
		third_trust_based_update(0.5)
		return 0.5
	
	elif row[keywords] == "Low Trust (I am skeptical of Blitzcrank's explanation and question the reliability of its assessment)":
		third_trust_based_update(0.2)
		return 0.2


def round3_ranking(row):
	# a: T, b: T, g: T
	# a: T, b: T, g: F
	# a: T, b: F, g: T
	# a: F, b: F, g: F


	trust_level = third_trust_choose('1-1 trust')


	df = pd.read_csv('truth_table.csv')
	filter_row_ranking1_1= df[(df['a'] == True) & (df['b'] == True) & (df['g'] == True)]
	ranking1_1 = filter_row_ranking1_1['Third_trust_based_updated'].sum()

	filter_row_ranking1_2= df[(df['a'] == True) & (df['b'] == True) & (df['g'] == False)]
	ranking1_2 = filter_row_ranking1_2['Third_trust_based_updated'].sum()

	filter_row_ranking1_3= df[(df['a'] == True) & (df['b'] == False) & (df['g'] == True)]
	ranking1_3 = filter_row_ranking1_3['Third_trust_based_updated'].sum()

	filter_row_ranking1_4= df[(df['a'] == False) & (df['b'] == False) & (df['g'] == False)]
	ranking1_4 = filter_row_ranking1_4['Third_trust_based_updated'].sum()

	
	with open(csv_file_path, newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		human_ranking = [int(row['Ranking 1-1 final_1']), int(row['Ranking 1-1 final_2']), int(row['Ranking 1-1 final_3']), int(row['Ranking 1-1 final_4'])]
		# print(human_ranking)



	# print(calculated_ranking)
	value_dict = {'Ranking 1-1 final_1': ranking1_1, 'Ranking 1-1 final_2': ranking1_2, 'Ranking 1-1 final_3': ranking1_3, 'Ranking 1-1 final_4': ranking1_4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('Ranking 1-1 final_1') + 1, list(sorted_dict.keys()).index('Ranking 1-1 final_2') + 1, list(sorted_dict.keys()).index('Ranking 1-1 final_3') + 1, list(sorted_dict.keys()).index('Ranking 1-1 final_4') + 1]

	# print(spearman_rank_correlation(calculated_ranking,human_ranking))

	return sorted_dict, calculated_ranking, human_ranking, spearman_rank_correlation(calculated_ranking,human_ranking), trust_level

def calculation_probability():

	df = pd.read_csv('truth_table.csv')
	filtered_rows_A = df[(df['a'] == True) & ( df['b'] == True) & (df['c'] == True) & (df['d'] == True)]
	Argument_A = filtered_rows_A['Third_trust_based_updated'].sum()
	
	filtered_rows_B = df[(df['c'] == False) & (df['e'] == False)]
	Argument_B = filtered_rows_B['Third_trust_based_updated'].sum()

	filtered_rows_C = df[(df['f'] == True) & (df['e'] == True) & (df['c'] == True)]
	Argument_C = filtered_rows_C['Third_trust_based_updated'].sum()
	
	filtered_rows_D = df[(df['f'] == False) & (df['c'] == False) & (df['e'] == False)]
	Argument_D = filtered_rows_D['Third_trust_based_updated'].sum()

	filtered_rows_E = df[(df['g'] == True) & (df['e'] == True) & (df['f'] == True) & (df['c'] == True)]
	Argument_E = filtered_rows_E['Third_trust_based_updated'].sum()

	print('Argument A: ', Argument_A)
	print('Argument B: ', Argument_B)
	print('Argument C: ', Argument_C)
	print('Argument D: ', Argument_D)
	print('Argument E: ', Argument_E)

rowlist = []
with open(csv_file_path, 'r') as file:
	csv_iterator = pd.read_csv(file, iterator=True)
	for chunk in csv_iterator:
		for _, row in chunk.iterrows():
			start_time = time.time()
			# print(start_time)
			truth_table()
			sorted_dict1, calculated_ranking1, human_ranking1, rank_correlation1, trust_level1 = round1_ranking(row)
			# print(rank_correlation1)
			sorted_dict2, calculated_ranking2, human_ranking2, rank_correlation2, trust_level2 = round2_ranking(row)
			# print(rank_correlation2)
			sorted_dict3, calculated_ranking3, human_ranking3, rank_correlation3, trust_level3 = round3_ranking(row)
			# print(rank_correlation3)
			rowlist.append([sorted_dict1, calculated_ranking1, human_ranking1, rank_correlation1, sorted_dict2, calculated_ranking2, human_ranking2, rank_correlation2,sorted_dict3, calculated_ranking3, human_ranking3, rank_correlation3, trust_level1, trust_level2, trust_level3])
			end_time = time.time()
			calculation_probability()
			# print(end_time)
			print("One Row: {:.6f}秒".format(end_time - start_time))


with open('chain1-1_correlation.csv', 'w', newline='') as csvfile:
	fieldnames = ['Chain_number', 'Sorted_dict1', 'Calculated_ranking1', 'Human_ranking1', 'Rank_correlation1', 'Sorted_dict2', 'Calculated_ranking2', 'Human_ranking2', 'Rank_correlation2', 'Sorted_dict3', 'Calculated_ranking3', 'Human_ranking3', 'Rank_correlation3', 'Trust_level1', 'Trust_level2', 'Trust_level3']

	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	writer.writeheader()

	for i in range(len(rowlist)):
		writer.writerow({'Chain_number': 'Chain1-1', 'Sorted_dict1': rowlist[i][0], 'Calculated_ranking1': rowlist[i][1], 'Human_ranking1': rowlist[i][2], 'Rank_correlation1': rowlist[i][3], 'Sorted_dict2': rowlist[i][4], 'Calculated_ranking2': rowlist[i][5], 'Human_ranking2': rowlist[i][6], 'Rank_correlation2': rowlist[i][7], 'Sorted_dict3': rowlist[i][8], 'Calculated_ranking3': rowlist[i][9], 'Human_ranking3': rowlist[i][10], 'Rank_correlation3': rowlist[i][11], 'Trust_level1': rowlist[i][12], 'Trust_level2': rowlist[i][13], 'Trust_level3': rowlist[i][14]})


