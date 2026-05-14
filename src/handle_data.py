import numpy as np
import pandas as pd
import ast
import re
import os
import shutil

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
    with open(f"../data/week{week}/processed/inputs.txt", "r") as f:
        arrays = [parse_input_content(line) for line in f if line.strip()]
        for i in range(len(arrays)):
            # append arrays all the weeks results into initial array
            input_list = np.vstack((input_list, arrays[i][function_id - 1]))

    # append new outputs to output_list
    with open(f"../data/week{week}/processed/outputs.txt", "r") as f:
        parsed = [np.array(parse_output_content(line)) for line in f if line.strip()]
        arrays = np.vstack(parsed)
        for i in range(len(arrays)):
            # append arrays all the weeks results into initial array
            output_list =  np.hstack((output_list, arrays[i][function_id - 1]))

    return input_list, output_list

# -- PROCESS INPUTS FOR WEEKLY SETUP ----------------------------------------------------

def setup_week_folders(week_number: int, base_dir="data"):
    """ Create data/week<n>/raw and data/week<n>/processed if not yet present """
    week= "week" + str(week_number)
    for sub in ("raw", "processed"):
        path=os.path.join(base_dir, week, sub)
        os.makedirs(path, exist_ok=True,)
    print_dir_tree(base_dir + f"/{week}", basedir = base_dir[3:])
    
def print_dir_tree(startpath, basedir=None):
    print(f"[Weekly setup] --- Paths created:")

    if basedir != None:
        print(f"../{basedir}/")
    
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        if basedir != None:
            level+=1
        originalI = ' ' * 4 * (level)
        indent = f"{originalI}" + "\u2514\u2500\u2500" + " "
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

def is_already_processed(output_path: str) -> bool:
    return os.path.exists(output_path)

def process_raw(input_path: str, output_path: str):
    """
    Read inputs.txt, join mid-array line breaks, write cleaned file.
    Each list ends up on a single unbroken line.
    Moves outputs.txt to same dir
    """
    with open(input_path, "r") as f:
        raw = f.read()
 
    lines = raw.splitlines()
    merged_lines = []
    buffer = ""
 
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("["):
            if buffer:
                merged_lines.append(buffer)
            buffer = stripped
        else:
            buffer = buffer + " " + stripped
 
    if buffer:
        merged_lines.append(buffer)
 
    move_lines_to_output_path(merged_lines, output_path)

def move_lines_to_output_path(merged_lines, output_path):
    with open(output_path, "w") as f:
        f.write("\n".join(merged_lines) + "\n")
