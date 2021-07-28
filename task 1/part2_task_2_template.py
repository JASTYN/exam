# Dice rolling
import numpy as np

def dice_probabilities(n_dice, replications):
	dice_values = np.zeros(1) # Change/remove this line
	dice_probabilities = np.zeros(1)  # Change/remove this line

	# Please, introduce your answer here

	return dice_values, dice_probabilities


if __name__ == '__main__':
	n_dice = 2  # You can change this value for testing
	replications = 1000000  # You can change this value for testing


	# The code below is for your reference, so you can visualise your answer	
	dv, dp = dice_probabilities(n_dice, replications)

	n = len(dv)
	print('Rolling', n_dice, 'dice has', n, 'possible outcomes:')
	print('With', replications, 'replications, the estimated probabilities are:')
	print('Outcome', 'Prob:', sep='\t')
	for i in range(n):
		print(dv[i], '', np.round(dp[i], 8), sep='\t')
