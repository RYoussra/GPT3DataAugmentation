import pandas as pd
enables=pd.read_csv('/Users/youssrarebboud/Desktop/generated_dataset/enabling_clean.csv')
correct_ones=[]
correct_trigger1=0
correct_trigger2=0
correct_Sentenecs=0
for idx, row in enables.iterrows():
    print(row['sentence'])
    print(row['trigger1'])
    print(row['trigger2'])
    inp = input('is the sentence correct?')
    if inp=='1':
        correct_Sentenecs+=1
        inp2 = input('is trigger1 correct?')
        inp3 = input('is trigger2 correct?')
        if inp2=='1':
            correct_trigger1 += 1
        if inp2=='1':
            correct_trigger2 += 1






    break

