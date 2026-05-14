import pandas as pd

def create_and_display_df(inputs, output, input_columns, output_columns='output'):
    print_shapes(inputs, output)
    df = pd.DataFrame(inputs, columns=input_columns)
    df[output_columns] = output
    display(df)
    return

def print_shapes(inputs, output):
    print(f"Inputs shape: {inputs.shape}")
    print(f"Outputs shape: {output.shape}")
    return