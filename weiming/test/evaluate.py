from scrape import check_phrase
import time
import pandas as pd
import numpy as np

def check_all(file_path):
    interval = 0
    cnt = [0]*10
    acc = [0]*10

    with open(file_path, 'r') as file:
        for line in file:
            interval += 1
            score, phrase = line.strip().split('\t')
            score = float(score)
            exists = check_phrase(phrase)
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
    df_table.to_csv(f'./weiming/output/MyModel7A.csv', index=False)
    print(df_table)
    return df_table

file_path = './models/MyModel7A/AutoPhrase_multi-words.txt'
check_all(file_path)