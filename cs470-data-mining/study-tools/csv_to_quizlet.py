#!/usr/bin/env python3

import pandas as pd
import numpy as np


if __name__ == "__main__":
    input_file = 'midterm.csv'
    output_file = 'output.txt'

    df = pd.read_csv(input_file)
    out = open(output_file, 'w')
    for index, row in df.iterrows():
        out.write(f'{row["Question"]}')
        
        for i in ['A','B','C','D','E']:
            out.write(f'\n{i.lower()}. {row[i]}')
        out.write(f',\t{row["Correct Answer"]}\n\n')
    out.close()
