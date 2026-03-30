import numpy as np
import pandas as pd
import ast
import re

def load_data(function_id, week):
    base = f"../data/initial/function{function_id}/week{week}"
    X = np.load(f"{base}/initial_inputs.npy")
    Y = np.load(f"{base}/initial_outputs.npy")
    return X, Y

def parse_input_content(content):
    # Normalize the content: remove 'array(' and ')' wrappers
    cleaned = re.sub(r'array\(', '', content.strip())
    cleaned = re.sub(r'\)', '', cleaned)
    
    # Safely evaluate the cleaned string as a Python literal
    parsed = ast.literal_eval(cleaned)
    
    # Convert each inner list to a numpy array
    arrays = [np.array(row) for row in parsed]
    
    return arrays

def parse_output_content(content):
    # Parse a line of text into numpy arrays
    try:
        # Clean the line and convert to a list of floats
        # This assumes each line contains a list of numbers in string format
        content = content.strip()

        # remove np.float64(...) wrapper
        content = re.sub(r'np\.float64\((.*?)\)', r'\1', content)

        # safely parse the list
        values = ast.literal_eval(content)

        return np.array(values, dtype=float)

    except Exception as e:
        print(f"Error parsing line: {content}")
        print(f"Error details: {e}")
        return np.array([[]])  # Return empty array on error


def load_and_append(function_id, week):
    # Loads selected function by week inputs.txt and outputs.txt
    # Parses the txts - manually for now, would like to automate the process and make it cleaner
    # Appends relative data to corresponding list
    # Returns complete lists
    print(f"Retrieving inputs/outputs for function {function_id}, week {week}")
    input_list, output_list = load_data(function_id, 1)
    
    if week==1:
        return input_list, output_list
    
    print(f"*** Loading new inputs for function {function_id}, week {week} ***")
    # append new inputs to input_list 
    with open(f"../data/week{week}/inputs.txt", "r") as f:
        arrays = [parse_input_content(line) for line in f if line.strip()]
        for i in range(len(arrays)):
            # append arrays all the weeks results into initial array
            input_list = np.vstack((input_list, arrays[i][function_id - 1]))

    # append new outputs to output_list
    with open(f"../data/week{week}/outputs.txt", "r") as f:
        parsed = [np.array(parse_output_content(line)) for line in f if line.strip()]
        arrays = np.vstack(parsed)
        for i in range(len(arrays)):
            # append arrays all the weeks results into initial array
            output_list =  np.hstack((output_list, arrays[i][function_id - 1]))

    return input_list, output_list