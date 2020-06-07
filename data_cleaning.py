# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 21:28:46 2020

@author: carso
"""


import pandas as pd
from us_state_convert import us_state_abbrev

df = pd.read_csv("data_science_jobs.csv")

#Remove all job listings without a rating
df.drop(df[df.Rating == -1].index, inplace = True)

#salary parsing
salary = df["Salary Estimate"].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace("K", " ").replace("$", " "))

df["min_salary"] = minus_Kd.apply(lambda x: int(x.split("-")[0]))
df["max_salary"] = minus_Kd.apply(lambda x: int(x.split("-")[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

#state field
df["job_state"] = df["Location"].apply(lambda x: x.split(", ")[1] if "," in x else us_state_abbrev[x] if x in us_state_abbrev.keys() else x)

df["same_state"] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#age of company
df["age"] = df.Founded.apply(lambda x: x if x < 0 else 2020 - x)

#parsing of job description (python, (etc.))
df['python_yn'] = df["Job Description"].apply(lambda x: 1 if "python" in x.lower() else 0)

df['r_yn'] = df["Job Description"].apply(lambda x: 1 if "r studio" in x.lower() or "r-studio" in x.lower() else 0)

df['spark'] = df["Job Description"].apply(lambda x: 1 if "spark" in x.lower() else 0)

df['aws'] = df["Job Description"].apply(lambda x: 1 if "aws" in x.lower() else 0)

df['excel'] = df["Job Description"].apply(lambda x: 1 if "excel" in x.lower() else 0)

df.to_csv("salary_data_cleaned.csv", index = False)