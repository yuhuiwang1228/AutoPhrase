from scrape import is_valid
import time
import pandas as pd
import numpy as np
import os

def check_all(file_path,grade,term):
    interval = 0
    cnt = [0]*10
    acc = [0]*10

    with open(file_path, 'r') as file:
        for line in file:
            interval += 1
            score, phrase = line.strip().split('\t')
            score = float(score)
            exists = is_valid(phrase)
            for i in range(int(score*10)+1):
                if exists:
                    acc[i] += 1
                cnt[i] += 1
            # print(f"'{phrase}' exists in Cambridge Dictionary: {exists}")
        if interval%50==0: 
            time.sleep(1)  

    threshold = [round(0.1*i,1) for i in range(1,10)]
    precision = [round(acc[i]/cnt[i],2) for i in range(1,10)]
    recall = [round(acc[i]/acc[0],2) for i in range(1,10)]

    df_table = pd.DataFrame( np.array([threshold, precision, recall]).T, columns = ['threshold', 'precision', 'recall'])  
    df_table['threshold'] = df_table['threshold'].astype(float)
    df_table.to_csv(f'./weiming/output/threshold/MyModel{grade}{term}.csv', index=False)
    print(df_table)
    return df_table

if __name__ == "__main__":
    grades = ['1','2','3','4','5','6','7','8','9','R','E']
    terms = ['A','B','C','D']
    for grade in grades:
        for term in terms:
            file_path = f'./models/MyModel{grade}{term}/AutoPhrase_multi-words.txt'
            if os.path.exists(file_path):
                print(f"Processing file: {file_path}")
                check_all(file_path,grade,term)