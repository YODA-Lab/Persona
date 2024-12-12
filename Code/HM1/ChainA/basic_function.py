import itertools
import pandas as pd
import random
import numpy as np
import pandas as pd

def truth_table(num_variables):
	truth_table = []
	initial_probability = 1 / (2 ** num_variables)
	variable_names = [chr(ord('a') + i) for i in range(num_variables)]
	variable_combinations = list(itertools.product([True, False], repeat=num_variables))
	for combination in variable_combinations:
		entry = dict(zip(variable_names, combination))
		entry['Initial'] = initial_probability
		truth_table.append(entry)
	df = pd.DataFrame(truth_table)
	df.to_csv('truth_table.csv', index=False)

def remain_update():
	df = pd.read_csv('truth_table.csv')
	df['Fifth_trust_based_updated'] = df['Fourth_response_based_updated']
	df.to_csv('truth_table.csv', index=False)

def inverse_function(y, s, r):
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


def confidence_choose(row, keywords):
	full_confidence = "I believe Blitzcrank's argument is exceptionally well-founded and entirely convincing. (Very High Confidence)"
	high_confidence = "I believe Blitzcrank's argument to be credible and well-supported. (High Confidence)"
	average_confidence = "I believe Blitzcrank's argument is reasonable, but I remain somewhat skeptical and would like more information. (Average Confidence)"
	low_confidence = "I believe Blitzcrank's argument is doubtful and question the reliability of its assessment. (Low Confidence)"
	no_confidence = "I believe Blitzcrank's argument is unconvincing and see little value in its insights. (Very Low Confidence)"
	
	if row[keywords] == full_confidence:
		return 0.9
	elif row[keywords] == high_confidence:
		return 0.7
	elif row[keywords] == average_confidence:
		return 0.5
	elif row[keywords] == low_confidence:
		return 0.3
	elif row[keywords] == no_confidence:
		return 0.1

def literal_calculation(variables, probability_keywords):
	df = pd.read_csv('truth_table.csv')

	true_value = [True, False]

	probability_list = {}
	for i in variables:
		filter_row_ranking = df[df[i] == True]
		probability_variable = filter_row_ranking[probability_keywords].sum()
		probability_list[i] = probability_variable

	random.shuffle(variables)

	true_values_list = list(probability_list.values())

	difference_list = [abs(2*true_values_list[i] - 1) for i in range(len(true_values_list))]

	max_three = sorted(difference_list, reverse=True)[:3]

	max_keys = []

	for i in range(len(variables)):
		if max_three != []:
			if abs(2*probability_list[variables[i]]-1) in max_three:
				max_keys.append(variables[i])
				max_three.remove(abs(2*probability_list[variables[i]]-1))
	
	max_three_dic = {key: probability_list [key] for key in max_keys}

	max_three_keys = sorted(list(max_three_dic.keys()))

	record_max_probability = []

	record_list = []
	for x in true_value:
		for y in true_value:
			for z in true_value:
				max_filtered_rows = df[(df[max_three_keys[0]] == x) & (df[max_three_keys[1]] == y) & (df[max_three_keys[2]] == z)]
				max_corresponding_probability = max_filtered_rows[probability_keywords].sum()
				record_max_probability.append([x, y, z, max_corresponding_probability])
	
	print(max_three_keys)

	for element in record_max_probability:
		print(element)
	# print(record_max_probability)

	return max_three_keys, record_max_probability







