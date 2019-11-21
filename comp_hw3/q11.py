#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

no_of_poi = 0
no_total_payments = 0

for person in enron_data.keys():
    if enron_data[person]["poi"] == True: 
        no_of_poi += 1
        if math.isnan(float(enron_data[person]["total_payments"])):
            no_total_payments += 1

print("Number of POIs who have NaN for their total payments: {}".format(no_total_payments))
print("The percentage is: {}".format(no_total_payments * 100 / no_of_poi))
