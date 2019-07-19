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


print(framed_data)
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
# Computing IQR
Q1 = framed_data['age'].quantile(0.25)
Q2 = framed_data['age'].quantile(0.50)
Q3 = framed_data['age'].quantile(0.75)
IQR = Q3 - Q1
print("Q1=",Q1,"Q@=",Q2,"Q3=",Q3)
print("IQR=", IQR)

framed_data['age'].plot()
# framed_data['age'].boxplot()
fig1, ax1 = plt.subplots()
ax1.set_title('Basic Plot')
ax1.boxplot(framed_data['age'])

plt.show()


