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

no_quantified_salary = 0
no_known_email = 0

for person in enron_data.keys():
    if math.isnan(float(enron_data[person]["salary"])) == False:
        no_quantified_salary += 1

    if enron_data[person]['email_address'] != 'NaN':
        no_known_email += 1

print(no_quantified_salary)
print(no_known_email)