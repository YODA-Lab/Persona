from basic_function import confidence_choose
from basic_function import inverse_function
from basic_function import sort_dict_by_values
from basic_function import spearman_rank_correlation

import pandas as pd
import random

def B1_1_trust_based_update(row, s, r):
	# h: True, i: True, f: True
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-1-1 confidence')
	real_prob = trust_degree
	filtered_rows = df[(df['h'] == True) & (df['i'] == True) & (df['f'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['h'] == True) & (df['i'] == True) & (df['f'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B1_1_trust_update():
	# h: True, i: True, f: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['h'] == True) & (df['i'] == True) & (df['f'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['h'] == True) & (df['i'] == True) & (df['f'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)



def B1_2_trust_based_update(row, s, r):
	# h: True, g: True, d: True
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-1-2 confidence')
	real_prob = trust_degree
	filtered_rows = df[(df['g'] == True) & (df['h'] == True) & (df['d'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['g'] == True) & (df['h'] == True) & (df['d'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B1_2_trust_update():
	# h: True, g: True, d: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['g'] == True) & (df['h'] == True) & (df['d'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['g'] == True) & (df['h'] == True) & (df['d'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B1_3_trust_based_update(row, s, r):
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-1-3 confidence')
	real_prob = trust_degree
	filtered_rows = df[(df['g'] == True) & (df['h'] == True) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['g'] == True) & (df['h'] == True) & (df['a'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B1_3_trust_update():
	# h: True, g: True, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['g'] == True) & (df['h'] == True) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['g'] == True) & (df['h'] == True) & (df['a'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)



def B2_1_trust_based_update(row, s, r):
	# h: True, i: True, g: True
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-2-1 confidence')
	real_prob = trust_degree
	filtered_rows = df[(df['h'] == True) & (df['i'] == True) & (df['g'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['h'] == True) & (df['i'] == True) & (df['g'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B2_1_trust_update():
	# h: True, i: True, g: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['h'] == True) & (df['i'] == True) & (df['g'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['h'] == True) & (df['i'] == True) & (df['g'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B2_2_trust_based_update(row, s, r):
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-2-2 confidence')
	real_prob = trust_degree
	filtered_rows = df[(df['g'] == False) & (df['h'] == True) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['g'] == False) & (df['h'] == True) & (df['a'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B2_2_trust_update():
	# g: False, h: True, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['g'] == False) & (df['h'] == True) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['g'] == False) & (df['h'] == True) & (df['a'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B2_3_trust_based_update(row, s, r):
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-2-3 confidence')
	real_prob = trust_degree
	filtered_rows = df[(df['g'] == True) & (df['h'] == True) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['g'] == True) & (df['h'] == True) & (df['a'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B2_3_trust_update():
	# h: True, g: True, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['g'] == True) & (df['h'] == True) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['g'] == True) & (df['h'] == True) & (df['a'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B3_1_trust_based_update(row, s, r):
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-3-1 confidence')
	real_prob = trust_degree
	filtered_rows = df[(df['h'] == True) & (df['i'] == True) & (df['f'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['h'] == True) & (df['i'] == True) & (df['f'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B3_1_trust_update():
	# h: True, i: True, f: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['h'] == True) & (df['i'] == True) & (df['f'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['h'] == True) & (df['i'] == True) & (df['f'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B3_2_trust_based_update(row, s, r):
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-3-2 confidence')
	real_prob = trust_degree
	filtered_rows = df[(df['g'] == False) & (df['h'] == True) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['g'] == False) & (df['h'] == True) & (df['a'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B3_2_trust_update():
	# g: False, h: True, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['g'] == False) & (df['h'] == True) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['g'] == False) & (df['h'] == True) & (df['a'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B3_3_trust_based_update(row, s, r):
	df = pd.read_csv('truth_table.csv')
	trust_degree = confidence_choose(row, 'B-3-3 confidence')
	real_prob = trust_degree
	filtered_rows = df[(df['g'] == True) & (df['h'] == True) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['g'] == True) & (df['h'] == True) & (df['a'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B3_3_trust_update():
	# h: True, g: True, a: True
	df = pd.read_csv('truth_table.csv')
	real_prob = 0.5
	filtered_rows = df[(df['g'] == True) & (df['h'] == True) & (df['a'] == True)]
	sum_of_updated = filtered_rows['Third_response_based_updated'].sum()
	df.loc[(df['g'] == True) & (df['h'] == True) & (df['a'] == True), 'Fourth_trust_based_updated'] = df['Third_response_based_updated']/sum_of_updated * real_prob
	df['Fourth_trust_based_updated'] = df['Fourth_trust_based_updated'].fillna(df['Third_response_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def fourth_trust_update(num1, num2):
	if num1 == 1:
		if num2 == 1:
			B1_1_trust_update()
		elif num2 == 2:
			B1_2_trust_update()
		elif num2 == 3:
			B1_3_trust_update()
	elif num1 == 2:
		if num2 == 1:
			B2_1_trust_update()
		elif num2 == 2:
			B2_2_trust_update()
		elif num2 == 3:
			B2_3_trust_update()
	elif num1 == 3:
		if num2 == 1:
			B3_1_trust_update()
		elif num2 == 2:
			B3_2_trust_update()
		elif num2 == 3:
			B3_3_trust_update()



def B1_1_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# j: False, h: False
	real_prob = 0.3
	filtered_rows = df[(df['j'] == False) & (df['h'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['j'] == False) & (df['h'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B1_1_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# j: True, i: False
	real_prob = 0.5
	filtered_rows = df[(df['j'] == True) & (df['i'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['j'] == True) & (df['i'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B1_1_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# j: True, i: False
	real_prob = 0.7
	filtered_rows = df[(df['j'] == True) & (df['i'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['j'] == True) & (df['i'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B1_2_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, g: False
	real_prob = 0.7
	filtered_rows = df[(df['i'] == False) & (df['g'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['i'] == False) & (df['g'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B1_2_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, d: False
	real_prob = 0.3
	filtered_rows = df[(df['i'] == False) & (df['d'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['i'] == False) & (df['d'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B1_2_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, d: False
	real_prob = 0.5
	filtered_rows = df[(df['i'] == False) & (df['d'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['i'] == False) & (df['d'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B1_3_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, a: False
	real_prob = 0.9
	filtered_rows = df[(df['i'] == False) & (df['a'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['i'] == False) & (df['a'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B1_3_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, g: False
	real_prob = 0.7
	filtered_rows = df[(df['i'] == False) & (df['g'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['i'] == False) & (df['g'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B1_3_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, a: False
	real_prob = 0.7
	filtered_rows = df[(df['i'] == False) & (df['a'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['i'] == False) & (df['a'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B2_1_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# j: False, h: False
	real_prob = 0.3
	filtered_rows = df[(df['j'] == False) & (df['h'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['j'] == False) & (df['h'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B2_1_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# j: True, i: False
	real_prob = 0.5
	filtered_rows = df[(df['j'] == True) & (df['i'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['j'] == True) & (df['i'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B2_1_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# j: True, i: False
	real_prob = 0.7
	filtered_rows = df[(df['j'] == True) & (df['i'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['j'] == True) & (df['i'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B2_2_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False (not spicy), h: False
	real_prob = 0.9
	filtered_rows = df[(df['i'] == False) & (df['h'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['i'] == False) & (df['h'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B2_2_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: True, h: False
	real_prob = 0.9
	filtered_rows = df[(df['i'] == True) & (df['h'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['i'] == True) & (df['h'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B2_2_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: True, a: False
	real_prob = 0.3
	filtered_rows = df[(df['i'] == True) & (df['a'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['i'] == True) & (df['a'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B2_3_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, a: False
	real_prob = 0.9
	filtered_rows = df[(df['i'] == False) & (df['a'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['i'] == False) & (df['a'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B2_3_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, g: False
	real_prob = 0.7
	filtered_rows = df[(df['i'] == False) & (df['g'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['i'] == False) & (df['g'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B2_3_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, a: False
	real_prob = 0.7
	filtered_rows = df[(df['i'] == False) & (df['a'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['i'] == False) & (df['a'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B3_1_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# j: False, h: False
	real_prob = 0.3
	filtered_rows = df[(df['j'] == False) & (df['h'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['j'] == False) & (df['h'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B3_1_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# j: True, i: False
	real_prob = 0.5
	filtered_rows = df[(df['j'] == True) & (df['i'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['j'] == True) & (df['i'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B3_1_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# j: True, i: False
	real_prob = 0.7
	filtered_rows = df[(df['j'] == True) & (df['i'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['j'] == True) & (df['i'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B3_2_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False (not spicy), h: False
	real_prob = 0.9
	filtered_rows = df[(df['i'] == False) & (df['h'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['i'] == False) & (df['h'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B3_2_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: True, h: False
	real_prob = 0.9
	filtered_rows = df[(df['i'] == True) & (df['h'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['i'] == True) & (df['h'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B3_2_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: True, a: False
	real_prob = 0.3
	filtered_rows = df[(df['i'] == True) & (df['a'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['i'] == True) & (df['a'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B3_3_1_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, a: False
	real_prob = 0.9
	filtered_rows = df[(df['i'] == False) & (df['a'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['i'] == False) & (df['a'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B3_3_2_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, g: False
	real_prob = 0.7
	filtered_rows = df[(df['i'] == False) & (df['g'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['i'] == False) & (df['g'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)

def B3_3_3_response_based_update():
	df = pd.read_csv('truth_table.csv')
	# i: False, a: False
	real_prob = 0.7
	filtered_rows = df[(df['i'] == False) & (df['a'] == False)]
	sum_of_updated = filtered_rows['Fourth_trust_based_updated'].sum()
	df.loc[(df['i'] == False) & (df['a'] == False), 'Fourth_response_based_updated'] = df['Fourth_trust_based_updated']/sum_of_updated * real_prob
	df['Fourth_response_based_updated'] = df['Fourth_response_based_updated'].fillna(df['Fourth_trust_based_updated']/(1 - sum_of_updated) * (1 - real_prob))
	df.to_csv('truth_table.csv', index=False)


def B1_1_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['l'] == True) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['l'] == False) & (df['g'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['l'] == False) & (df['g'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['l'] == True) & (df['g'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-1-1-1_1']), int(row['Ranking B-1-1-1_2']), int(row['Ranking B-1-1-1_3']), int(row['Ranking B-1-1-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B1_1_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['g'] == False) & (df['j'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['g'] == False) & (df['j'] == True) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['j'] == True) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['g'] == True) & (df['j'] == False) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-1-1-2_1']), int(row['Ranking B-1-1-2_2']), int(row['Ranking B-1-1-2_3']), int(row['Ranking B-1-1-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B1_1_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == False) & (df['g'] == False) & (df['j'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['f'] == False) & (df['g'] == True) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['f'] == False) & (df['g'] == False) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['f'] == True) & (df['g'] == True) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-1-1-3_1']), int(row['Ranking B-1-1-3_2']), int(row['Ranking B-1-1-3_3']), int(row['Ranking B-1-1-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B1_2_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['g'] == False) & (df['i'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['g'] == False) & (df['i'] == False) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['g'] == True) & (df['i'] == False) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['g'] == True) & (df['i'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-1-2-1_1']), int(row['Ranking B-1-2-1_2']), int(row['Ranking B-1-2-1_3']), int(row['Ranking B-1-2-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B1_2_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['l'] == True) & (df['f'] == True) & (df['h'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['l'] == True) & (df['f'] == True) & (df['h'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['l'] == False) & (df['f'] == False) & (df['h'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['l'] == False) & (df['f'] == True) & (df['h'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-1-2-2_1']), int(row['Ranking B-1-2-2_2']), int(row['Ranking B-1-2-2_3']), int(row['Ranking B-1-2-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B1_2_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['l'] == False) & (df['f'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['l'] == True) & (df['f'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['l'] == False) & (df['f'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['l'] == True) & (df['f'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-1-2-3_1']), int(row['Ranking B-1-2-3_2']), int(row['Ranking B-1-2-3_3']), int(row['Ranking B-1-2-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B1_3_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['c'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['c'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['c'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['a'] == True) & (df['c'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-1-3-1_1']), int(row['Ranking B-1-3-1_2']), int(row['Ranking B-1-3-1_3']), int(row['Ranking B-1-3-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B1_3_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['a'] == True) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['a'] == True) & (df['g'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-1-3-2_1']), int(row['Ranking B-1-3-2_2']), int(row['Ranking B-1-3-2_3']), int(row['Ranking B-1-3-2_5'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B1_3_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['e'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['e'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['e'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['e'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-1-3-3_1']), int(row['Ranking B-1-3-3_2']), int(row['Ranking B-1-3-3_3']), int(row['Ranking B-1-3-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B2_1_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['i'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['i'] == True) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['d'] == False) & (df['i'] == False) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['d'] == True) & (df['i'] == True) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-2-1-1_1']), int(row['Ranking B-2-1-1_2']), int(row['Ranking B-2-1-1_3']), int(row['Ranking B-2-1-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B2_1_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['j'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['j'] == True) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['d'] == False) & (df['j'] == False) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['d'] == True) & (df['j'] == True) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-2-1-2_1']), int(row['Ranking B-2-1-2_2']), int(row['Ranking B-2-1-2_3']), int(row['Ranking B-2-1-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B2_1_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == False) & (df['i'] == False) & (df['j'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['d'] == True) & (df['i'] == False) & (df['j'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['d'] == True) & (df['i'] == True) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['d'] == False) & (df['i'] == False) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-2-1-3_1']), int(row['Ranking B-2-1-3_2']), int(row['Ranking B-2-1-3_3']), int(row['Ranking B-2-1-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B2_2_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['g'] == False) & (df['h'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['g'] == True) & (df['h'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['h'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['g'] == True) & (df['h'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-2-2-1_1']), int(row['Ranking B-2-2-1_2']), int(row['Ranking B-2-2-1_3']), int(row['Ranking B-2-2-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B2_2_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['g'] == True) & (df['h'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['g'] == True) & (df['h'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['h'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['g'] == False) & (df['h'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-2-2-2_1']), int(row['Ranking B-2-2-2_2']), int(row['Ranking B-2-2-2_3']), int(row['Ranking B-2-2-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B2_2_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['g'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['g'] == True) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['d'] == True) & (df['g'] == True) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-2-2-3_1']), int(row['Ranking B-2-2-3_2']), int(row['Ranking B-2-2-3_3']), int(row['Ranking B-2-2-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B2_3_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-2-3-1_1']), int(row['Ranking B-2-3-1_2']), int(row['Ranking B-2-3-1_3']), int(row['Ranking B-2-3-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B2_3_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-2-3-2_1']), int(row['Ranking B-2-3-2_2']), int(row['Ranking B-2-3-2_3']), int(row['Ranking B-2-3-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B2_3_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-2-3-3_1']), int(row['Ranking B-2-3-3_2']), int(row['Ranking B-2-3-3_3']), int(row['Ranking B-2-3-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B3_1_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['g'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['d'] == True) & (df['g'] == True) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-3-1-1_1']), int(row['Ranking B-3-1-1_2']), int(row['Ranking B-3-1-1_3']), int(row['Ranking B-3-1-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B3_1_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['g'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['d'] == True) & (df['g'] == True) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-3-1-2_1']), int(row['Ranking B-3-1-2_2']), int(row['Ranking B-3-1-2_3']), int(row['Ranking B-3-1-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B3_1_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['f'] == False) & (df['g'] == False) & (df['j'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['f'] == False) & (df['g'] == True) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['f'] == False) & (df['g'] == False) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['f'] == True) & (df['g'] == True) & (df['j'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-3-1-3_1']), int(row['Ranking B-3-1-3_2']), int(row['Ranking B-3-1-3_3']), int(row['Ranking B-3-1-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B3_2_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['g'] == False) & (df['h'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['g'] == True) & (df['h'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['h'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['g'] == True) & (df['h'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-3-2-1_1']), int(row['Ranking B-3-2-1_2']), int(row['Ranking B-3-2-1_3']), int(row['Ranking B-3-2-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B3_2_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['g'] == True) & (df['h'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['g'] == True) & (df['h'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['g'] == False) & (df['h'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['g'] == False) & (df['h'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-3-2-2_1']), int(row['Ranking B-3-2-2_2']), int(row['Ranking B-3-2-2_3']), int(row['Ranking B-3-2-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B3_2_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['d'] == True) & (df['g'] == False) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['d'] == False) & (df['g'] == True) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['d'] == False) & (df['g'] == False) & (df['l'] == False)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['d'] == True) & (df['g'] == True) & (df['l'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-3-2-3_1']), int(row['Ranking B-3-2-3_2']), int(row['Ranking B-3-2-3_3']), int(row['Ranking B-3-2-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B3_3_1_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['a'] == True) & (df['g'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-3-3-1_1']), int(row['Ranking B-3-3-1_2']), int(row['Ranking B-3-3-1_3']), int(row['Ranking B-3-3-1_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def B3_3_2_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['a'] == True) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-3-3-2_1']), int(row['Ranking B-3-3-2_2']), int(row['Ranking B-3-3-2_3']), int(row['Ranking B-3-3-2_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation


def B3_3_3_calculation(row):
	df = pd.read_csv('truth_table.csv')

	ranking1 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	ranking2 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking3 = df[(df['a'] == False) & (df['g'] == False) & (df['i'] == True)]['Fourth_response_based_updated'].sum()
	ranking4 = df[(df['a'] == False) & (df['g'] == True) & (df['i'] == False)]['Fourth_response_based_updated'].sum()
	

	human_ranking = [int(row['Ranking B-3-3-3_1']), int(row['Ranking B-3-3-3_2']), int(row['Ranking B-3-3-3_3']), int(row['Ranking B-3-3-3_4'])]

	value_dict = {'R_1': ranking1, 'R_2': ranking2, 'R_3': ranking3, 'R_4': ranking4}
	sorted_dict = sort_dict_by_values(value_dict)
	calculated_ranking = [list(sorted_dict.keys()).index('R_1') + 1, list(sorted_dict.keys()).index('R_2') + 1, list(sorted_dict.keys()).index('R_3') + 1, list(sorted_dict.keys()).index('R_4') + 1]


	correlation = spearman_rank_correlation(calculated_ranking,human_ranking)

	return correlation

def fourth_response_update(num1, num2, num3):
	if num1 == 1:
		if num2 == 1:
			if num3 == 1:
				B1_1_1_response_based_update()
				#l, g, i: T, F, F/F, T, T/F, T, F/T, F, T
			elif num3 == 2:
				B1_1_2_response_based_update()
				# g, j, l: F, F, T/F, T, F/F, T, T/T, F, F
			elif num3 == 3:
				B1_1_3_response_based_update()
				# f, g, j: F, F, T/F, T, F/F, F, F/T, T, F
		elif num2 == 2:
			if num3 == 1:
				B1_2_1_response_based_update()
				# g, i, l: F, F, T/F, F, F/T, F, F/T, F, T
			elif num3 == 2:
				B1_2_2_response_based_update()
				# l, f, h: T, T, T/T, T, F/F, F, F/F, T, T
			elif num3 == 3:
				B1_2_3_response_based_update()
				# l, f, i: F, T, F/T, F, T/F, F, F/T, T, F
		elif num2 == 3:
			if num3 == 1:
				B1_3_1_response_based_update()
				# a, c, i: F, F, F/F, T, T/F, F, T/T, T, T
			elif num3 == 2:
				B1_3_2_response_based_update()
				# a, g, i: F, F, F/T, F, F/T, T, T/F, T, F
			elif num3 == 3: 
				B1_3_3_response_based_update()
				# a, e, i: F, F, F/F, T, T/F, F, T/F, T, F
	elif num1 == 2:
		if num2 == 1:
			if num3 == 1:
				B2_1_1_response_based_update()
				# d, i, l: T, F, T/ F, T, F/F, F, F/ T, T, T
			elif num3 == 2:
				B2_1_2_response_based_update()
				# d, j, l: T, F, T/ F, T, F/F, F, F/ T, T, T
			elif num3 == 3:
				B2_1_3_response_based_update()
				# d, i, j: F, F, T/T, F, T/T, T, F/F, F, F
		elif num2 == 2:
			if num3 == 1:
				B2_2_1_response_based_update()
				# g, h, i: F, T, T/T, F, F/F, F, F/T, T, T
			elif num3 == 2:
				B2_2_2_response_based_update()
				# g, h, i: T, T, T/T, F, T/F, F, T/F, F, F
			elif num3 == 3:
				B2_2_3_response_based_update()
				# d, g, l: T, F, T/ F, T, F/F, F, F/ T, T, T
		elif num2 == 3:
			if num3 == 1:
				B2_3_1_response_based_update()
				# a, g, i: F, F, F/F, T, T/F, F, T/F, T, F
			elif num3 == 2:
				B2_3_2_response_based_update()
				# a, g, i: F, F, F/T, F, F/F, F, T/F, T, F
			elif num3 == 3:
				B2_3_3_response_based_update()
				# a, g, i: F, F, F/F, T, T/F, F, T/F, T, F
	elif num1 == 3:
		if num2 == 1:
			if num3 == 1:
				B3_1_1_response_based_update()
				# d, g, l: T, F, T/F, F, F/T, T, T/F, F, T
			elif num3 == 2:
				B3_1_2_response_based_update()
				# d, g, l: T, F, T/F, F, F/T, T, T/F, F, T
			elif num3 == 3:
				B3_1_3_response_based_update()
				# f, g, j: F, F, T/F, T, F/F, F, F/T, T, F
		elif num2 == 2:
			if num3 == 1:
				B3_2_1_response_based_update()
				# g, h, i: F, T, T/T, F, F/F, F, F/T, T, T
			elif num3 == 2:
				B3_2_2_response_based_update()
				# g, h, i: T, T, T/T, F, T/F, F, T/F, F, F
			elif num3 == 3:
				B3_2_3_response_based_update()
				# d, g, l: T, F, T/ F, T, F/F, F, F/ T, T, T
		elif num2 == 3:
			if num3 == 1:
				B3_3_1_response_based_update()
				# a,g,i:  F, F, F/F, T, T/F, F, T/T, T, T
			elif num3 == 2:
				B3_3_2_response_based_update()
				# a, g, i: F, F, F/T, F, F/F, F, T/F, T, F
			elif num3 == 3:
				B3_3_3_response_based_update()
				# a, g, i: F, F, F/F, T, T/F, F, T/F, T, F






