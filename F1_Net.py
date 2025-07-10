import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader,TensorDataset
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt 
from tqdm import tqdm
from IPython import display
import sys


# Define the model class

class F1Net(nn.Module):
    def __init__(self,num_teams,num_driver):
        super().__init__()

        self.team_embedding = nn.Embedding(num_teams,4)
        self.driver_embedding = nn.Embedding(num_driver,4)

        self.fc1 = nn.Linear(4+4+4,64)
        self.fc2 = nn.Linear(64,64)
        self.output = nn.Linear(64,1)

        self.dropout = nn.Dropout(p=.25)

    def forward(self,team_idx,driver_idx,x):
        team_vec = self.team_embedding(team_idx)
        

       
        driver_vec = self.driver_embedding(driver_idx)
        
        x = torch.cat([team_vec,driver_vec,x],dim=1)
        
        x = self.dropout(F.leaky_relu( self.fc1(x) ))
        x = self.dropout(F.leaky_relu( self.fc2(x) ))

        x = self.output(x)

        return x

