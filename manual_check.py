import pandas as pd
enables=pd.read_csv('/Users/youssrarebboud/PycharmProjects/GPT3DataAugmentation/generated_dataset/enabling_clean.csv')
correct_ones=[]
correct_trigger1=0
correct_trigger2=0
correct_Sentenecs=0

for idx, row in enables.iloc[:2].iterrows():


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
                correct1=row['trigger1']

            else:
                correct1=input('correct please trigger1')

            if inp3 == '1':
                correct2=row['trigger2']
                correct_trigger2 += 1
            else:
                correct2=input('correct please')
            correct_ones.append([row['sentence'],correct1,correct2])






print('correct_Sentenecs: ',correct_Sentenecs)
print('correct_trigger1',correct_trigger1)
print('correct_trigger2',correct_trigger2)