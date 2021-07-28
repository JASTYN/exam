import numpy as np

def read_data(file_patients, file_centres):
	patients = np.zeros((1, 4))  # Change/remove this line
	centres = np.zeros((1, 4))  # Change/remove this line

    # Please, introduce your answer here

	return patients, centres

def euclidean_distance(x1, y1, x2, y2):
    d = 0.0

    # Please, introduce your answer here

    return d

def allocation(patients, centres, days):
	centre_usage = np.zeros((1, days))  # Change/remove this line
	patient_allocation = np.zeros((1, 4))  # Change/remove this line
	total_distance = 0  # Change/remove this line
	
    # Please, introduce your answer here

	return patient_allocation, centre_usage, total_distance


if __name__ == '__main__':
	file_patients = 'data/t3_patients_example.csv'  # You can change this value for testing
	file_centres = 'data/t3_centres_example.csv'  # You can change this value for testing
	days = 3  # You can change this value for testing


	# The code below is for your reference, so you can visualise your answer
	patients, centres = read_data(file_patients, file_centres)
	patient_allocation, centre_usage, total_distance = allocation(patients, centres, days)
	print('Centre usage matrix:')
	print(centre_usage)
	
	print('Patient allocation matrix:')
	print(patient_allocation)

	print('Total allocation distance:', total_distance)