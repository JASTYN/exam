import pandas as pd
import matplotlib.pyplot as plt

def read_vegetable_data(filename):
	df = pd.DataFrame()

	# Please, introduce your answer here

	return df

def generate_plot_1(df):
	# Code to generate Plot 1 (show or save to file)

	# Please, introduce your answer here
	
	print('Plot 1 not completed yet.') # Remove this line when completed.

def generate_plot_2(df, vegetable):
	# Code to generate Plot 2 (show or save to file)
	
	# Please, introduce your answer here
	
	print('Plot 2 not completed yet.') # Remove this line when completed.


def find_cheapest_month(df, vegetable, organic):
	cheapest_month = 'Not completed yet'  # Change/remove this line
	
	# Please, introduce your answer here
	
	return cheapest_month




if __name__ == '__main__':
	''' You might modify the values of
	these variables to try different aspects
	of your code. You might also want to try
	different files that have the same format
	but different numbers for the prices.
	Running this file should produce all the
	outputs you need, two plots and the desired value'''

	filename = 'data/Vegetables.csv' # You can change this value for testing

	# Parameters for plot 2
	vegetable_for_plot_2 = 'Lettuce' # You can change this value for testing

	# Parameters for finding the cheapest month:
	vegetable_for_cheapest_month = 'Carrots' # You can change this value for testing
	organic_for_cheapest_month = False # You can change this value for testing


	# The code below is for your reference, so you can visualise your answer
	df = read_vegetable_data(filename)

	# Generate plots:
	generate_plot_1(df)
	generate_plot_2(df, vegetable_for_plot_2)

	# Cheapest month info:
	cheapest_month = find_cheapest_month(df, 
										 vegetable_for_cheapest_month, 
										 organic_for_cheapest_month)

	print('For', vegetable_for_cheapest_month, 
		  '(organic =', organic_for_cheapest_month,
		  ') the cheapest month was:', cheapest_month)
