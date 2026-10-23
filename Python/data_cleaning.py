# Import Libraries
import pandas as pd
import numpy as np

# Load Dataset

df = pd.read_excel('Ecommerce_Unclean_Project.xlsx')

# explore the dataset
# view first 5 Records
print(df.head())

#view dataset information
print(df.info())

# statical summary
print(df.describe())

#dataset shape
print(df.shape)

#Check Missing Values
print(df.isnull().sum())

# Check Duplicates
print(df.duplicated().sum())

# Remove Duplicate Records
print(df.drop_duplicates(inplace=True))

# Replace N/A and NULL
print(df.replace(["N/A","NULL"," "],np.nan,inplace=True))

print(df.isnull().sum())
print(df)
# remove extra spaces
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" and x.map(lambda v: isinstance(v, str) or pd.isna(v)).all() else x)

# standardize text format
# convert text into proper case
df['Customer_Name'] = df["Customer_Name"].str.title()
df['City'] = df["City"].str.title()
df['State'] = df["State"].str.title()

#validate email addresses
#keep only valid email addresses
df=df[df["Email"].str.contains("@",na=False)]

# Convert Date columns
df["Order_Date"]=pd.to_datetime(df["Order_Date"],errors="coerce")

df["Delivery_Date"]=pd.to_datetime(df["Delivery_Date"],errors="coerce")

# Convert Numeric Columns
cols = ['Qty','Unit_Price','Discount']

for c in cols:
    df[c]=pd.to_numeric(df[c],errors="coerce")

# remove invalid quantity           
# remove records having negative or zero quantity
df=df[df["Qty"]>0]

# Fill Missing Values
df["Discount"] = df["Discount"].fillna(0)
df["Phone"] = df["Phone"].fillna("Unknown")
df["Delivery_Date"] = df["Delivery_Date"].fillna(df["Order_Date"])

#feature engineering
#total sales
df["Sales"]=df["Qty"]*df["Unit_Price"]

# Net Amount
df["Net_Amount"]=df["Sales"]-(df["Sales"]*df["Discount"]/100)
# Profit 
df["Profit"]=df["Net_Amount"]*0.20
# Order Month
df["Month"]=df["Order_Date"].dt.month_name()
# Year
df["Year"]=df["Order_Date"].dt.year
# Weekday
df["Weekday"]=df["Order_Date"].dt.day_name()

# final data validation
df.info()
df.describe()
# Export Clean Data
df.to_excel("Clean_Ecommerce.xlsx",index=False)

# import data into mysql database
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:57575602@localhost/ecommerce')
#export dataframe to my sql
df.to_sql(
    name='orders',
    con=engine,
    if_exists='replace',
    index=False
)
df.shape()