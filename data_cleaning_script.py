import pandas as pd

#Loaded all the CSV files into separate DataFrames

divvy_tripdata_202504 = pd.read_csv('data/202504-divvy-tripdata.csv')
divvy_tripdata_202505 = pd.read_csv('data/202505-divvy-tripdata.csv')
divvy_tripdata_202506 = pd.read_csv('data/202506-divvy-tripdata.csv')
divvy_tripdata_202507 = pd.read_csv('data/202507-divvy-tripdata.csv')
divvy_tripdata_202508 = pd.read_csv('data/202508-divvy-tripdata.csv')
divvy_tripdata_202509 = pd.read_csv('data/202509-divvy-tripdata.csv')
divvy_tripdata_202510 = pd.read_csv('data/202510-divvy-tripdata.csv')
divvy_tripdata_202511 = pd.read_csv('data/202511-divvy-tripdata.csv')
divvy_tripdata_202512 = pd.read_csv('data/202512-divvy-tripdata.csv')
divvy_tripdata_202601 = pd.read_csv('data/202601-divvy-tripdata.csv')
divvy_tripdata_202602 = pd.read_csv('data/202602-divvy-tripdata.csv')
divvy_tripdata_202603 = pd.read_csv('data/202603-divvy-tripdata.csv')

### Check the columns of each DataFrame###

print("Columns for 202504:", divvy_tripdata_202504.columns)
print("Columns for 202505:", divvy_tripdata_202505.columns)
print("Columns for 202506:", divvy_tripdata_202506.columns)
print("Columns for 202507:", divvy_tripdata_202507.columns)
print("Columns for 202508:", divvy_tripdata_202508.columns)
print("Columns for 202509:", divvy_tripdata_202509.columns)
print("Columns for 202510:", divvy_tripdata_202510.columns)
print("Columns for 202511:", divvy_tripdata_202511.columns)
print("Columns for 202512:", divvy_tripdata_202512.columns)
print("Columns for 202601:", divvy_tripdata_202601.columns)
print("Columns for 202602:", divvy_tripdata_202602.columns)
print("Columns for 202603:", divvy_tripdata_202603.columns)
#All the columns are the same across all DataFrames, so we can concatenate them together

#Check the first and last few rows of each DataFrame to ensure they are loaded correctly and to check for any inconsistencies in the data
print("First few rows of 202504:")
print(divvy_tripdata_202504.head())
print("Last few rows of 202504:")
print(divvy_tripdata_202504.tail())
print("First few rows of 202505:")
print(divvy_tripdata_202505.head())
print("Last few rows of 202505:")
print(divvy_tripdata_202505.tail())
print("First few rows of 202506:")
print(divvy_tripdata_202506.head())
print("Last few rows of 202506:")
print(divvy_tripdata_202506.tail())
print("First few rows of 202507:")
print(divvy_tripdata_202507.head())
print("Last few rows of 202507:")
print(divvy_tripdata_202507.tail())
print("First few rows of 202508:")
print(divvy_tripdata_202508.head())
print("Last few rows of 202508:")
print(divvy_tripdata_202508.tail())
print("First few rows of 202509:")
print(divvy_tripdata_202509.head())
print("Last few rows of 202509:")
print(divvy_tripdata_202509.tail())
print("First few rows of 202510:")
print(divvy_tripdata_202510.head())
print("Last few rows of 202510:")
print(divvy_tripdata_202510.tail())
print("First few rows of 202511:")
print(divvy_tripdata_202511.head())
print("Last few rows of 202511:")
print(divvy_tripdata_202511.tail())
print("First few rows of 202512:")
print(divvy_tripdata_202512.head())
print("Last few rows of 202512:")
print(divvy_tripdata_202512.tail())
print("First few rows of 202601:")
print(divvy_tripdata_202601.head())
print("Last few rows of 202601:")
print(divvy_tripdata_202601.tail())
print("First few rows of 202602:")
print(divvy_tripdata_202602.head())
print("Last few rows of 202602:")
print(divvy_tripdata_202602.tail())
print("First few rows of 202603:")
print(divvy_tripdata_202603.head())
print("Last few rows of 202603:")
print(divvy_tripdata_202603.tail())


#Concatenate all DataFrames into a single DataFrame
divvy_tripdata_all = pd.concat([divvy_tripdata_202504, divvy_tripdata_202505, divvy_tripdata_202506, divvy_tripdata_202507, divvy_tripdata_202508, divvy_tripdata_202509, divvy_tripdata_202510, divvy_tripdata_202511, divvy_tripdata_202512, divvy_tripdata_202601, divvy_tripdata_202602, divvy_tripdata_202603], ignore_index=True) 

#Save the combined DataFrame to a new CSV file
divvy_tripdata_all.to_csv('data/divvy_tripdata_all.csv', index=False)

print("Data cleaning and merging completed. Combined data saved to 'data/divvy_tripdata_all.csv'.")
print("Total number of rows in the combined DataFrame:", len(divvy_tripdata_all))

#Load the combined CSV file into a new DataFrame to ensure it has been saved correctly
divvy_tripdata_all = pd.read_csv('data/divvy_tripdata_all.csv')
print("Columns in the combined DataFrame:")
print(divvy_tripdata_all.columns)

#Inspect the new table that has been created
print("Columns in the combined DataFrame:")
print(divvy_tripdata_all.columns)
print("Data types of each column in the combined DataFrame:")
print(divvy_tripdata_all.dtypes)
print("First few rows of the combined DataFrame:")
print(divvy_tripdata_all.head())
print("Last few rows of the combined DataFrame:")
print(divvy_tripdata_all.tail())
print("Number of rows and columns in the combined DataFrame:")
print(divvy_tripdata_all.shape)

#Inspect the data frames and look for incongruities
print("Summary of the combined DataFrame:")
print(divvy_tripdata_all.info())

# Statistical summary of data (mainly for numerics)
print("Statistical summary of the combined DataFrame:")
print(divvy_tripdata_all.describe())

#Check for unique values in categorical columns
print("Unique values in 'member_casual' column:")
print(divvy_tripdata_all['member_casual'].unique())
print("Unique values in 'rideable_type' column:")
print(divvy_tripdata_all['rideable_type'].unique())

#Inspect the data frame and look for any missing values or inconsistencies
print("Checking for missing values in the combined DataFrame:")
print(divvy_tripdata_all.isnull().sum())

#Convert 'started_at' and 'ended_at' to datetime objects
divvy_tripdata_all['started_at'] = pd.to_datetime(divvy_tripdata_all['started_at'])
divvy_tripdata_all['ended_at'] = pd.to_datetime(divvy_tripdata_all['ended_at'])

#Add columns that list the date, month, day, and year of each ride
divvy_tripdata_all['started_date'] = divvy_tripdata_all['started_at'].dt.date
divvy_tripdata_all['ended_date'] = divvy_tripdata_all['ended_at'].dt.date
divvy_tripdata_all['started_month'] = divvy_tripdata_all['started_at'].dt.month
divvy_tripdata_all['ended_month'] = divvy_tripdata_all['ended_at'].dt.month
divvy_tripdata_all['started_day'] = divvy_tripdata_all['started_at'].dt.day
divvy_tripdata_all['ended_day'] = divvy_tripdata_all['ended_at'].dt.day
divvy_tripdata_all['started_year'] = divvy_tripdata_all['started_at'].dt.year
divvy_tripdata_all['ended_year'] = divvy_tripdata_all['ended_at'].dt.year
divvy_tripdata_all['day_of_week'] = divvy_tripdata_all['started_at'].dt.day_name()

#Add a column that calculates the length of each ride
divvy_tripdata_all['ride_length'] = (divvy_tripdata_all['ended_at'] - divvy_tripdata_all['started_at']).dt.total_seconds()

#Inspect the structure of the new DataFrame with the added columns
print("Columns in the combined DataFrame after adding new columns:")
print(divvy_tripdata_all.info())

#Remove "bad" data
#The data frame includes entries where bikes were taken out of docks for quality checks or ride_length was negative
#Create a new version of the data frame (v2) since data is being removed
divvy_tripdata_all_v2 = divvy_tripdata_all[(divvy_tripdata_all['start_station_name'] != "HQ QR") & (divvy_tripdata_all['ride_length'] >= 0)].copy()

#Read the new data frame to ensure it has been saved correctly
divvy_tripdata_all_v2.to_csv('data/divvy_tripdata_all_v2.csv', index=False)
divvy_tripdata_all_v2 = pd.read_csv('data/divvy_tripdata_all_v2.csv')
print("Columns in the cleaned DataFrame:")
print(divvy_tripdata_all_v2.columns)
print("Data types of each column in the cleaned DataFrame:")
print(divvy_tripdata_all_v2.dtypes)


#==============================
# CONDUCT DESCRIPTIVE ANALYSIS
#==============================

#Descriptive analysis of ride_length
print("Statistical summary of 'ride_length' column:")
print(divvy_tripdata_all_v2['ride_length'].describe())

#Compare members and casual riders
print("Average ride length by member type:")
print(divvy_tripdata_all_v2.groupby('member_casual')['ride_length'].agg(['mean', 'median', 'max', 'min']))

# See the average ride time by each day for members vs casual users
print("Average ride length by day of the week:")
print(divvy_tripdata_all_v2.groupby(['member_casual', 'started_day'])['ride_length'].mean())

# Order the days of the week for correct sorting for analysis
days_order = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
divvy_tripdata_all_v2['day_of_week'] = pd.Categorical(divvy_tripdata_all_v2['day_of_week'], categories=days_order, ordered=True)
# Now, run the aggregation again to see the sorted result
print("\nAverage ride length (sorted by day of week):\n", divvy_tripdata_all_v2.groupby(['member_casual', 'day_of_week'])['ride_length'].mean())
# Analyze ridership data by type and weekday
summary_stats = divvy_tripdata_all_v2.groupby(['member_casual', 'day_of_week']).agg( number_of_rides=('ride_id', 'count'), average_duration=('ride_length', 'mean') ).reset_index()
print("\nSummary of rides and duration by rider type and weekday:\n", summary_stats)

#==========================================
# EXPORT SUMMARY FILE FOR FURTHER ANALYSIS
#==========================================

# Export the summary statistics to a new CSV file for further analysis
summary_stats.to_csv('data/summary_stats_by_member_and_day.csv', index=False)
print("Summary statistics exported to 'data/summary_stats_by_member_and_day.csv'.")