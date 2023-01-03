def count_positives_sum_negatives(arr):
  # initialize variables to store the count and sum
  count_positives = 0
  sum_negatives = 0

  # check if the input is an empty array or is null
  if not arr or len(arr) == 0:
    # return an empty array
    return []

  # iterate over the elements of the list
  for n in arr:
    # check the sign of the number
    if n > 0:
      # increment the count of positives
      count_positives += 1
    else:
      # add the negative number to the sum
      sum_negatives += n

  # return an array with the count and sum
  return [count_positives, sum_negatives]

# test the function
print(count_positives_sum_negatives([1, -2, 3, -4, 5])) # prints [3, -6]
print(count_positives_sum_negatives([-1, -2, -3, -4, -5])) # prints [0, -15]
print(count_positives_sum_negatives([1, 2, 3, 4, 5])) # prints [5, 0]
print(count_positives_sum_negatives([0, 0, 0])) # prints [0, 0]
print(count_positives_sum_negatives([])) # prints []
print(count_positives_sum_negatives(None)) # prints []
