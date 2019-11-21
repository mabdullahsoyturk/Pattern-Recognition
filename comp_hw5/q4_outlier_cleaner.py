#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    diff = abs(predictions - net_worths)

    sorted_diff = sorted(diff)[:81]

    for i in range(81):
        for k in range(90):
            if diff[k] == sorted_diff[i]:
                cleaned_data.append((ages[k], net_worths[k], diff[k]))

    return cleaned_data

