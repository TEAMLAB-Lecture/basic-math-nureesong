#######################
# Basic Math          #
#######################

def get_greatest(number_list):
    greatest_number = max(number_list)
    return greatest_number


def get_smallest(number_list):
    smallest_number = min(number_list)
    return smallest_number


def get_mean(number_list):
    mean = sum(number_list)/len(number_list)
    return mean


def get_median(number_list):
    number_list.sort()
    n = len(number_list)
    if n % 2 == 1:
        median = number_list[(n-1)//2]
    else:
        median = (number_list[n//2-1] + number_list[n//2])/2
    return median