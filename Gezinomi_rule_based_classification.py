# Potential Customer Yield Calculation with Rule-Based Classification

# Business Problem
# Gezinomi wants to create new level-based sales definitions by using some features of the sales it makes,
# create segments according to these new sales definitions and estimate how much new customers can bring to
# the company on average based on these segments.
# For example: It is desired to determine how much a customer who wants to go to an All Inclusive hotel
# from Antalya during a busy period can earn on average.

# VARIABLES
# SaleId
# SaleDate
# CheckInDate : Customer's hotel check-in date
# Price : Price paid for sale
# ConceptName: Hotel concept information
# SaleCityName: Information about the city where the hotel is located
# CInDay: The day the customer checks in to the hotel
# SaleCheckInDayDiff
# Season: Season information on hotel check-in date


import pandas as pd
#pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

df = pd.read_excel('/Users/melihasecilozturk/Desktop/miuul/ödevler/gezinomi_tanıtım/miuul_gezinomi.xlsx')
pd.set_option('display.float_format', lambda x: '%.2f' % x)
print(df.head())
print(df.shape)

np.dot(A,B)

# How many unique cities are there? What are their frequencies?
print(df["SaleCityName"].nunique())
print(df["SaleCityName"].value_counts())

# How many unique Concepts are there??
df["ConceptName"].nunique()


# How many sales were made from which Concept?
df["ConceptName"].value_counts()

# How much was earned from sales in total by city?
df.groupby("SaleCityName").agg({"Price": "sum"})

# How much was earned according to concept types?
df.groupby("ConceptName").agg({"Price": "sum"})

# What are the PRICE averages by city?
df.groupby(by=['SaleCityName']).agg({"Price": "mean"})

# What are the PRICE averages according to concepts?
df.groupby(by=['ConceptName']).agg({"Price": "mean"})

# What are the PRICE averages in the City-Concept breakdown?
df.groupby(by=["SaleCityName", 'ConceptName']).agg({"Price": "mean"})



#############################################
#The sale_checkin_day_diff variable indicates how long before the CheckIn date the customer completed the purchase.
# Convert the sales_checkin_day_diff variable into a new categorical variable called EB_Score.
#############################################
bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)
df.head(50).to_excel("eb_scorew.xlsx", index=False)




#############################################
# See wage averages and frequencies by City, Concept, [EB_Score, Season, CInday]
#############################################
# Wage averages in City-Concept-EB Score breakdown
df.groupby(by=["SaleCityName", 'ConceptName', "EB_Score" ]).agg({"Price": ["mean", "count"]})

# Wage averages by City-Concept-Season breakdown
df.groupby(by=["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": ["mean", "count"]})

# Wage averages in City-Concept-Cinday breakdown
df.groupby(by=["SaleCityName", "ConceptName", "CInDay"]).agg({"Price": ["mean", "count"]})


#############################################
# Sort the output of the City-Concept-Season breakdown according to PRICE.
#############################################
# To better see the output in the previous question, apply the sort_values ​​method to PRICE in a decreasing order.
# Save the output as agg_df

agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"}).sort_values("Price", ascending=False)
agg_df.head(20)

#############################################
# Convert the names in the index into variable names.
#############################################
# All variables except PRICE in the output of the third question are index names.
# Convert these names to variable names.
# Hint: reset_index()
agg_df.reset_index(inplace=True)

agg_df.head()
#############################################
# Define new level based sales and add them to the data set as a variable.
#######################
# Define a variable called sales_level_based and add this variable to the data set.
agg_df['sales_level_based'] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: '_'.join(x).upper(), axis=1)


#############################################
# Divide the personas into segments.
#######################
# Segment by PRICE,
# add the segments to agg_df with the name "SEGMENT"
# describe the segments
agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"Price": ["mean", "max", "sum"]})

#############################################
# Sort the final df according to the price variable.
# In which segment is "ANTALYA_HERŞEY DAHIL_HIGH" and how much is expected?
#######################
agg_df.sort_values(by="Price")


new_user = "ANTALYA_HERŞEY DAHIL_HIGH"
agg_df[agg_df["sales_level_based"] == new_user]



num_list = [21,13,19,3,11,5,18]
num_list.sort()
num_list[len(num_list) // 2]

y = "stuff;thing;junk"
z = y.split(';')
len(z)




