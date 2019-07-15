import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)
data_array = []


#Path to data files
target_file = "data/adult.data"
target_file_header = "data/column_names.data"

# load header data and actual data into panda dataframe
framed_data_header = pd.read_csv(target_file_header)
framed_data = pd.read_csv(target_file, names = framed_data_header)


# print(framed_data)
# print(framed_data['age'])
#
# age_list = list(framed_data['age'])
#
# print(age_list)


##Statsitical details

framed_data['age'].plot()

statistical_details = framed_data['age'].describe()
print(statistical_details)
print(framed_data['age'].mean())

print(type(framed_data['age'].astype(int).mean()))
framed_age_int = int(framed_data['age'].mean())

print(type(framed_age_int))


plt.show()



#
#
# def sum(passed_array):  # A helper function that adds the value of the elements of an array and return their total sum
#     sum = 0
#     for datapoint in range(0, len(passed_array)):
#         sum = sum + int(passed_array[datapoint])
#     return sum
#
#
# def mean(
#         passed_array):  ## Statistical mean is obtained by adding all the data points and dividing the result by the number of data points
#     passed_array_sum = sum(passed_array)
#     number_of_data_points = len(passed_array)
#     mean = 0
#     print("Sum of the total values in the array ", passed_array_sum)
#     print("number of data points", number_of_data_points)
#     mean = passed_array_sum / number_of_data_points
#     print("Mean of the received data points: ", mean)
#     return mean
#
#
# def median(
#         passed_array):  ## Statistical median is the middle of the data set . 50% of the data are smaller and 50% are larger than the median
#     sorted_array = sorted(passed_array, key=int)  # first let's sort the array
#
#     print("First we sort the received array: ", sorted_array)
#     if len(sorted_array) % 2 == 0:  # if the length of the array is even
#         print(
#             "we are dealing with an even number of data elements, hence the average of the two middle points is the median")
#         middle_point_lower = sorted_array[int((len(sorted_array) / 2)) - 1]
#         middle_point_larger = sorted_array[int((len(sorted_array) / 2))]
#         median = (int(middle_point_lower) + int(middle_point_larger)) / 2
#         print("Median is: ", median)
#     else:
#         print("we are dealing with an odd number of data elements, hence the middle point is the median")
#         middle_point = math.ceil(len(sorted_array) / 2)
#         print("Median is: ", passed_array[middle_point])
#
#
# def mode(passed_array):  # The most repeated value(s) in the data set (some data sets may not have mode)
#     mode_of_dataset = stats.mode(passed_array, axis=None)
#     print(mode_of_dataset)
#
#
# def variance(passed_array):
#     tmp_var = 0
#     tmp_sum = 0
#     length_of_passed_array = len(passed_array)
#     calculated_mean = mean(passed_array)
#     for datapoint in range(0, length_of_passed_array):
#         tmp_var = math.pow((int((passed_array[datapoint])) - int(calculated_mean)), 2)  # raised to the power of 2
#         tmp_sum = tmp_sum + tmp_var
#     variance = tmp_sum/(length_of_passed_array-1)
#     print("variance", variance)
#     return variance
#
#
# def stdv(passed_array):
#     calculated_variance = variance(passed_array)
#     stdv = math.sqrt(calculated_variance)
#     print("standard deviation is: ", stdv)
#     return stdv
#
#
# ## TO do:  add range, and z-score
#
#
#
# mean(data_array)
# median(data_array)
# mode(data_array)
# variance(data_array)
# stdv(data_array)

