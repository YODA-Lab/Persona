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
import basic_function
import first_round
import second_round
import third_round
import fourth_round
import fifth_round
from basic_function import remain_update


# Data location
current_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_directory, 'data', 'ChainA_data.csv')


# Argument input
# parser = argparse.ArgumentParser()
# parser.add_argument('--s')
# parser.add_argument('--r')
# args = parser.parse_args()

# s = float(args.s)
# r = float(args.r)

num_variables = 11


def compare_distribution(lists):
	devision = [-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75]
	distribution_list = []
	def count_close_to_1(lst):
		count1 = sum(1 for x in lst if 0.75 <= x <= 1)
		count2 = sum(1 for x in lst if 0.5 <= x <= 1)
		count3 = sum(1 for x in lst if 0.25 <= x <= 1)
		count4 = sum(1 for x in lst if 0 <= x <= 1)
		count5 = sum(1 for x in lst if -0.25 <= x <= 1)
		count6 = sum(1 for x in lst if -0.5 <= x <= 1)
		count7 = sum(1 for x in lst if -0.75 <= x <= 1)
		return [count1, count2, count3, count4, count5, count6, count7]

	for i in range(len(lists)):
		distribution_list.append(count_close_to_1(lists[i]))


	return distribution_list

def compare_lists(lists):
    max_list = lists[0]
    for i in range(1, len(lists)):
        max_list = compare_two_lists(max_list, lists[i])
    print(max_list)
    return max_list

def compare_two_lists(list1, list2):
    for num1, num2 in zip(list1, list2):
        if num1 > num2:
            return list1
        elif num2 > num1:
            return list2
    return random.choice([list1, list2])


s_values=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
r_values=[1, 2, 3, 4, 5, 6, 7, 8]

parameter_set = [[s, r] for s in s_values for r in r_values]

# Read the file and process each line
rowlist = []

df = pd.read_csv(csv_file_path)
for _, row in df.iterrows():
	compare_rank_correlation = []
	temp_list = []
	break_or_not = False

	for parameter in parameter_set:
		s = parameter[0]
		r = parameter[1]
	# Part 1
		basic_function.truth_table(num_variables)
		first_round.first_trust_based_update(row, s, r)
		first_round.first_response_based_update()

		correlation1 = first_round.round1_calculation(row)
		# print(correlation1)

		# Part 2
		second_round.second_trust_based_update(row, s, r)
		if row['Chain A choices'] == "The extra service fee results in high costs, making Luminara Gardens unsuitable for parties. (High Confidence)":
			second_round.A1_response_based_update()
			correlation2 = second_round.A1_calculation(row)

			third_round.A1_trust_based_update(row, s, r)
			if row['Chain A-1 choices'] == "The information on the official website is outdated and not accurate. (Very High Confidence)":
				third_round.A1_1_response_based_update()
				correlation3 = third_round.A1_1_calculation(row)

				fourth_round.A1_1_trust_based_update(row, s, r)
				if row['Chain A-1-1 choices'] == "The high ratings were artificially generated through automated processes to attract customers, which could make the high rankings unreliable. (Low Confidence)":
					fourth_round.A1_1_1_response_based_update()
					correlation4 = fourth_round.A1_1_1_calculation(row)

					fifth_round.A1_1_1_trust_based_update(row, s, r)
					correlation5 = fifth_round.A1_1_1_F_calculation(row)

					correlation_calculated, correlation_hunter = fifth_round.A1_1_1_A_calculation(row)

				elif row['Chain A-1-1 choices'] == "Luminara Gardens may receive positive reviews by offering discounts, which could make those reviews unreliable. (Average Confidence)":
					fourth_round.A1_1_2_response_based_update()
					correlation4 = fourth_round.A1_1_2_calculation(row)

					fifth_round.A1_1_2_trust_based_update(row, s, r)
					correlation5 = fifth_round.A1_1_2_F_calculation(row)

					correlation_calculated, correlation_hunter = fifth_round.A1_1_2_A_calculation(row)

				elif row['Chain A-1-1 choices'] == "The positive reviews are due to Luminara Gardens offering coupons, which could make the reviews unreliable. (High Confidence)":
					fourth_round.A1_1_3_response_based_update()
					correlation4 = fourth_round.A1_1_3_calculation(row)

					fifth_round.A1_1_3_trust_based_update(row, s, r)
					correlation5 = fifth_round.A1_1_3_F_calculation(row)

					correlation_calculated, correlation_hunter = fifth_round.A1_1_3_A_calculation(row)

			elif row['Chain A-1 choices'] == "The hidden fees might arise due to various conditions not listed on the website, potentially leading to high costs. (Average Confidence)":
				third_round.A1_2_response_based_update()
				correlation3 = third_round.A1_2_calculation(row)

				fourth_round.A1_2_trust_based_update(row, s, r)
				if row['Chain A-1-2 choices'] == "The manager might be dishonest about the absence of hidden fees to attract customers. (High Confidence)":
					fourth_round.A1_2_1_response_based_update()
					correlation4 = fourth_round.A1_2_1_calculation(row)

					fifth_round.A1_2_1_trust_based_update(row, s, r)
					correlation5 = fifth_round.A1_2_1_F_calculation(row)

					correlation_calculated, correlation_hunter = fifth_round.A1_2_1_A_calculation(row)


				elif row['Chain A-1-2 choices'] == "The cost may vary between peak and off-peak seasons, but the current peak season may result in higher costs. (Low Confidence)":
					fourth_round.A1_2_2_response_based_update()
					correlation4 = fourth_round.A1_2_2_calculation(row)

					fifth_round.A1_2_2_trust_based_update(row, s, r)
					correlation5 = fifth_round.A1_2_2_F_calculation(row)

					correlation_calculated, correlation_hunter = fifth_round.A1_2_2_A_calculation(row)



				elif row['Chain A-1-2 choices'] == "The additional expenses for entertainment could lead to higher costs. (Average Confidence)":
					fourth_round.A1_2_3_response_based_update()
					correlation4 = fourth_round.A1_2_3_calculation(row)

					fifth_round.A1_2_3_trust_based_update(row, s, r)
					correlation5 = fifth_round.A1_2_3_F_calculation(row)

					correlation_calculated, correlation_hunter = fifth_round.A1_2_3_A_calculation(row)

					# correlation_calculated, correlation_hunter = 'None', 'None'

			elif row['Chain A-1 choices'] == "The lack of diverse entertainment facilities makes Luminara Gardens unsuitable for parties. (High Confidence)":
				third_round.A1_3_response_based_update()
				correlation3 = third_round.A1_3_calculation(row)

				fourth_round.A1_3_trust_based_update(row, s, r)
				if row['Chain A-1-3 choices'] == "The outdated facilities make Luminara Gardens unsuitable for parties. (Very High Confidence)":
					fourth_round.A1_3_1_response_based_update()
					correlation4 = fourth_round.A1_3_1_calculation(row)

					correlation5 = 'None'
					remain_update()
					correlation_calculated, correlation_hunter = fifth_round.A1_3_1_A_calculation(row)


				elif row['Chain A-1-3 choices'] == "Luminara Gardens lacks standard party facilities like KTV or Xbox, making its entertainment options insufficiently diverse. (High Confidence)":
					fourth_round.A1_3_2_response_based_update()
					correlation4 = fourth_round.A1_3_2_calculation(row)

					correlation5 = 'None'
					remain_update()
					correlation_calculated, correlation_hunter = fifth_round.A1_3_2_A_calculation(row)


				elif row['Chain A-1-3 choices'] == "The comments in the apps describe that most board games are boring, making Luminara Gardens unsuitable for parties. (High Confidence)":
					fourth_round.A1_3_3_response_based_update()
					correlation4 = fourth_round.A1_3_3_calculation(row)

					correlation5 = 'None'
					remain_update()
					correlation_calculated, correlation_hunter = fifth_round.A1_3_3_A_calculation(row)

		elif row['Chain A choices'] == "Luminara Gardens has no entertainment facilities that would make it unsuitable for parties. (Average Confidence)":
			second_round.A2_response_based_update()
			correlation2 = second_round.A2_calculation(row)

			third_round.A2_trust_based_update(row, s, r)
			if row['Chain A-2 choices'] == "The insufficient number of entertainment facilities makes Luminara Gardens unsuitable for parties. (Average Confidence)":
				third_round.A2_1_response_based_update()
				correlation3 = third_round.A2_1_calculation(row)

				fourth_round.A2_1_trust_based_update(row, s, r)
				if row['Chain A-2-1 choices'] == "The high ratings were artificially generated through automated processes to attract customers, which could make the high rankings unreliable. (Low Confidence)":
					fourth_round.A2_1_1_response_based_update()
					correlation4 = fourth_round.A2_1_1_calculation(row)


					fifth_round.A2_1_1_trust_based_update(row, s, r)
					correlation5 = fifth_round.A2_1_1_F_calculation(row)

					correlation_calculated, correlation_hunter = fifth_round.A2_1_1_A_calculation(row)

				elif row['Chain A-2-1 choices'] == "Luminara Gardens may receive positive reviews by offering discounts, which could make those reviews unreliable. (Average Confidence)":
					fourth_round.A2_1_2_response_based_update()
					correlation4 = fourth_round.A2_1_2_calculation(row)

					fifth_round.A2_1_2_trust_based_update(row, s, r)
					correlation5 = fifth_round.A2_1_2_F_calculation(row)

					correlation_calculated, correlation_hunter = fifth_round.A2_1_2_A_calculation(row)

				elif row['Chain A-2-1 choices'] == "The positive reviews are due to Luminara Gardens offering coupons, which could make the reviews unreliable. (High Confidence)":
					fourth_round.A2_1_3_response_based_update()
					correlation4 = fourth_round.A2_1_3_calculation(row)

					fifth_round.A2_1_3_trust_based_update(row, s, r)
					correlation5 = fifth_round.A2_1_3_F_calculation(row)

					correlation_calculated, correlation_hunter = fifth_round.A2_1_3_A_calculation(row)

			elif row['Chain A-2 choices'] == "The limited variety of cuisine at Luminara Gardens makes it unsuitable for parties. (Average Confidence)":
				third_round.A2_2_response_based_update()
				correlation3 = third_round.A2_2_calculation(row)

				fourth_round.A2_2_trust_based_update(row, s, r)
				if row['Chain A-2-2 choices'] == "My friend visited Luminara Gardens last month, and most of the cuisine is too spicy, which cannot cater to most people's tastes. (Very High Confidence)":
					fourth_round.A2_2_1_response_based_update()
					correlation4 = fourth_round.A2_2_1_calculation(row)

					correlation5 = 'None'
					remain_update()
					correlation_calculated, correlation_hunter = fifth_round.A2_2_1_A_calculation(row)


				elif row['Chain A-2-2 choices'] == "The cuisine cannot cater to most people's tastes since people come from different areas and countries. (Very High Confidence)":
					fourth_round.A2_2_2_response_based_update()
					correlation4 = fourth_round.A2_2_2_calculation(row)

					correlation5 = 'None'
					remain_update()
					correlation_calculated, correlation_hunter = fifth_round.A2_2_2_A_calculation(row)

				elif row['Chain A-2-2 choices'] == "I’ve visited Solaria Fields, known for its exceptional cuisine, so Luminara Gardens is less suitable for parties in comparison. (Low Confidence)":
					fourth_round.A2_2_3_response_based_update()
					correlation4 = fourth_round.A2_2_3_calculation(row)

					fifth_round.A2_2_3_trust_based_update(row, s, r)
					correlation5 = fifth_round.A2_2_3_F_calculation(row)

					correlation_calculated, correlation_hunter = fifth_round.A2_2_3_A_calculation(row)



			elif row['Chain A-2 choices'] == "The lack of diverse entertainment facilities makes Luminara Gardens unsuitable for parties. (High Confidence)":
				third_round.A2_3_response_based_update()
				correlation3 = third_round.A2_3_calculation(row)

				fourth_round.A2_3_trust_based_update(row, s, r)
				if row['Chain A-2-3 choices'] == "The outdated facilities make Luminara Gardens unsuitable for parties. (Vey High Confidence)":
					fourth_round.A2_3_1_response_based_update()
					correlation4 = fourth_round.A2_3_1_calculation(row)

					correlation5 = 'None'
					remain_update()
					correlation_calculated, correlation_hunter = fifth_round.A2_3_1_A_calculation(row)

				elif row['Chain A-2-3 choices'] == "Luminara Gardens lacks standard party facilities like KTV or Xbox, making its entertainment options insufficiently diverse. (High Confidence)":
					fourth_round.A2_3_2_response_based_update()
					correlation4 = fourth_round.A2_3_2_calculation(row)

					correlation5 = 'None'
					remain_update()
					correlation_calculated, correlation_hunter = fifth_round.A2_3_2_A_calculation(row)

				elif row['Chain A-2-3 choices'] ==  "The comments in the apps describe that most board games are boring, making Luminara Gardens unsuitable for parties. (High Confidence)":
					fourth_round.A2_3_3_response_based_update()
					correlation4 = fourth_round.A2_3_3_calculation(row)

					correlation5 = 'None'
					remain_update()
					correlation_calculated, correlation_hunter = fifth_round.A2_3_3_A_calculation(row)
		
		elif row['Chain A choices'] == "The unavailability of accommodation makes Luminara Gardens unsuitable for parties. (Low Confidence)":
			second_round.A3_response_based_update()
			correlation2 = second_round.A3_calculation(row)

			third_round.A3_trust_based_update(row, s, r)
			if row['Chain A-3 choices'] == "The poor accommodation conditions make Luminara Gardens unsuitable for parties. (High Confidence)":
				third_round.A3_1_response_based_update()
				correlation3 = third_round.A3_1_calculation(row)

				fourth_round.A3_1_trust_based_update(row, s, r)
				if row['Chain A-3-1 choices'] == "The high ratings were artificially generated through automated processes to attract customers, which could make the high rankings unreliable. (Low Confidence)":
					fourth_round.A3_1_1_response_based_update()
					correlation4 = fourth_round.A3_1_1_calculation(row)

					fifth_round.A3_1_1_trust_based_update(row, s, r)
					correlation5 = fifth_round.A3_1_1_F_calculation(row)

					correlation_calculated, correlation_hunter = fifth_round.A3_1_1_A_calculation(row)


				elif row['Chain A-3-1 choices'] == "Luminara Gardens may receive positive reviews by offering discounts, which could make those reviews unreliable. (Average Confidence)":
					fourth_round.A3_1_2_response_based_update()
					correlation4 = fourth_round.A3_1_2_calculation(row)

					fifth_round.A3_1_2_trust_based_update(row, s, r)
					correlation5 = fifth_round.A3_1_2_F_calculation(row)

					correlation_calculated, correlation_hunter = fifth_round.A3_1_2_A_calculation(row)

				elif row['Chain A-3-1 choices'] == "The positive reviews are due to Luminara Gardens offering coupons, which could make the reviews unreliable. (High Confidence)":
					fourth_round.A3_1_3_response_based_update()
					correlation4 = fourth_round.A3_1_3_calculation(row)

					fifth_round.A3_1_3_trust_based_update(row, s, r)
					correlation5 = fifth_round.A3_1_3_F_calculation(row)
					
					correlation_calculated, correlation_hunter = fifth_round.A3_1_3_A_calculation(row)

			elif row['Chain A-3 choices'] == "The limited variety of cuisine at Luminara Gardens makes it unsuitable for parties. (Average Confidence)":
				third_round.A3_2_response_based_update()
				correlation3 = third_round.A3_2_calculation(row)

				fourth_round.A3_2_trust_based_update(row, s, r)
				if row['Chain A-3-2 choices'] == "My friend visited Luminara Gardens last month, and most of the cuisine is too spicy, which cannot cater to most people's tastes. (Very High Confidence)":
					fourth_round.A3_2_1_response_based_update()
					correlation4 = fourth_round.A3_2_1_calculation(row)

					correlation5 = 'None'
					remain_update()
					correlation_calculated, correlation_hunter = fifth_round.A3_2_1_A_calculation(row)


				elif row['Chain A-3-2 choices'] == "The cuisine cannot cater to most people's tastes since people come from different areas and countries. (Very High Confidence)":
					fourth_round.A3_2_2_response_based_update()
					correlation4 = fourth_round.A3_2_2_calculation(row)

					correlation5 = 'None'
					remain_update()
					correlation_calculated, correlation_hunter = fifth_round.A3_2_2_A_calculation(row)

				elif row['Chain A-3-2 choices'] == "I’ve visited Solaria Fields, known for its exceptional cuisine, so Luminara Gardens is less suitable for parties in comparison. (Low Confidence)":
					fourth_round.A3_2_3_response_based_update()
					correlation4 = fourth_round.A3_2_3_calculation(row)

					fifth_round.A3_2_3_trust_based_update(row, s, r)

					correlation5 = fifth_round.A3_2_3_F_calculation(row)
					correlation_calculated, correlation_hunter = fifth_round.A3_2_3_A_calculation(row)


			elif row['Chain A-3 choices'] == "The lack of diverse entertainment facilities makes Luminara Gardens unsuitable for parties. (High Confidence)":
				third_round.A3_3_response_based_update()
				correlation3 = third_round.A3_3_calculation(row)

				fourth_round.A3_3_trust_based_update(row, s, r)
				if row['Chain A-3-3 choices'] == "The outdated facilities make Luminara Gardens unsuitable for parties. (Vey High Confidence)":
					fourth_round.A3_3_1_response_based_update()
					correlation4 = fourth_round.A3_3_1_calculation(row)

					correlation5 = 'None'
					remain_update()
					correlation_calculated, correlation_hunter = fifth_round.A3_3_1_A_calculation(row)

				elif row['Chain A-3-3 choices'] == "Luminara Gardens lacks standard party facilities like KTV or Xbox, making its entertainment options insufficiently diverse. (High Confidence)":
					fourth_round.A3_3_2_response_based_update()
					correlation4 = fourth_round.A3_3_2_calculation(row)

					correlation5 = 'None'
					remain_update()
					correlation_calculated, correlation_hunter = fifth_round.A3_3_2_A_calculation(row)

				elif row['Chain A-3-3 choices'] ==  "The comments in the apps describe that most board games are boring, making Luminara Gardens unsuitable for parties. (High Confidence)":
					fourth_round.A3_3_3_response_based_update()
					correlation4 = fourth_round.A3_3_3_calculation(row)

					correlation5 = 'None'
					remain_update()
					correlation_calculated, correlation_hunter = fifth_round.A3_3_3_A_calculation(row)

		if correlation5 == 'None':
			compare_rank_correlation.append([correlation1, correlation2, correlation3])
		else:
			compare_rank_correlation.append([correlation1, correlation2, correlation3, correlation4])
		

		temp_list.append([correlation1, correlation2, correlation3, correlation4, correlation5, correlation_calculated, correlation_hunter])

	distribution_list = compare_distribution(compare_rank_correlation)
	max_distribution = compare_lists(distribution_list)

	for i in range(len(distribution_list)):
		if distribution_list[i] == max_distribution:
			max_list = compare_rank_correlation[i]

		
	for i in range(len(temp_list)):
		if break_or_not == False:
			if len(max_list) == 3:
				if temp_list[i][0] == max_list[0] and temp_list[i][1] == max_list[1] and temp_list[i][2] == max_list[2]:
					rowlist.append(temp_list[i])
					break_or_not = True
			else:
				if temp_list[i][0] == max_list[0] and temp_list[i][1] == max_list[1] and temp_list[i][2] == max_list[2] and temp_list[i][3] == max_list[3]:
					rowlist.append(temp_list[i])
					break_or_not = True
	
with open('ChainA_correlation.csv', 'w', newline='') as csvfile:
	fieldnames = ['Chain_number', 'Correlation 1', 'Correlation 2', 'Correlation 3', 'Correlation 4', 'Correlation 5', 'Correlation Argument', 'Correlation Hunter']

	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	writer.writeheader()

	for i in range(len(rowlist)):
		writer.writerow({'Chain_number': 'ChainA', 'Correlation 1': rowlist[i][0], 'Correlation 2': rowlist[i][1], 'Correlation 3': rowlist[i][2], 'Correlation 4': rowlist[i][3], 'Correlation 5': rowlist[i][4], 'Correlation Argument': rowlist[i][5], 'Correlation Hunter': rowlist[i][6]})

	# print(correlation2)


	# third_round.third_trust_based_update(row, s, r)
	# third_round.third_response_based_update(row)





# 	if row['Chain A choices'] == "But it's quite likely that the extra service fee results in high costs, making Luminara Gardens unsuitable for parties.":
# 		second_round.A1_response_based_update()
# 		# ranking here
# 		third_round.A1_trust_based_update(row)
# 		if row['Chain A-1 choices'] == "But I am certain that the information on the official website is outdated and not accurate.":
# 			third_round.A1_1_response_based_update()

			





# basic_function.truth_table(num_variables)
# first_round.first_trust_update()
# first_round.first_response_based_update()
# basic_function.literal_calculation(['a', 'b', 'c'], 'First_response_based_updated')

# second_round.second_trust_update()
# second_round.second_response_update(3)
# basic_function.literal_calculation(['a', 'b', 'c', 'd', 'e'], 'Second_response_based_updated')

# third_round.third_trust_update(3)
# third_round.third_response_update(3,3)
# basic_function.literal_calculation(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 'Third_response_based_updated')


# fourth_round.fourth_trust_update(3, 3)
# fourth_round.fourth_response_update(3, 3, 3)
# basic_function.literal_calculation(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 'Fourth_response_based_updated')

# fifth_round.fifth_trust_update(3, 2, 3)
# basic_function.literal_calculation(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 'Fifth_trust_based_updated')

