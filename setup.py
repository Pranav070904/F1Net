import os


req_dirs = [
    "encoders","saved_Models","visualizations"
]


for directory in req_dirs:
    os.makedirs(directory,exist_ok=True)