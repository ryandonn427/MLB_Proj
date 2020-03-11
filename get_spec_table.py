all_cols,all_vals = [],[]
with open('queries_test_small.txt','r') as file:
    for i in file.readlines():
        if 'liveData.plays.pitch' in i:
            cols = i.split('(')[1].split(')')[0].split(',')
            vals = i.split('VALUES ')[1].replace('(','').replace(')','').split(',')
            all_cols.append(cols)
            all_vals.append(vals)

for i,j in zip(all_cols,all_vals):
    for k,l in zip(i,j):
        if k == 'isPitch':
            print((k,l))
        
    