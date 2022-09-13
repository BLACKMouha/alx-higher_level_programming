#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0

    sum_weights = 0
    sum_score_weighted = 0
    score_weighted = 1
    average_weighted = 0

    for item in my_list:
        sum_weights += item[1]

    for item in my_list:
        score_weighted = 1
        for i in range(len(item)):
            score_weighted *= item[i]
        sum_score_weighted += score_weighted
    average_weighted = sum_score_weighted / sum_weights

    return average_weighted
