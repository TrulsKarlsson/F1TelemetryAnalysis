import fastf1
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# To-Do list
#   Abstract code into functions
#   DONE Script to create one big dataframe containing all data from all races currently raced this season
#   DONE Fetch qualificiation data
#   Train model
#   Live training and prediction
#   Dashboard (Streamlit)