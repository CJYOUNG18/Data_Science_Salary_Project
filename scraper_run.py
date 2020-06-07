# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 00:05:42 2020

@author: carso
"""
import scraper as scrape
import pandas as pd

df = scrape.get_jobs("data scientist", 1000, False, "D:\Github\Data Science Project\chromedriver.exe")

df.to_csv("data_science_jobs.csv", index = False)