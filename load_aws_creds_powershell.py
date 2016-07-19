import pandas as pd
import boto
import matplotlib.pyplot as plt

import json 

with open('aws_creds.json') as f:
    data = json.load(f)
    access_key = data['access-key'] 
    access_secret_key = data['secret-access-key']