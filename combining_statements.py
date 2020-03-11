
def get_bulk_queries():
    with open('queries.txt','r') as file:
        split_data = [i.split(' VALUES ') for i in file.readlines()]

    tables = set([i[0] for i in split_data])
    dict={}
    for i in tables:
        for j in split_data:
            if i == j[0]:
                if j[0] in dict:
                    dict[j[0]].append(j[1].replace('\n',''))
                else:
                    dict[j[0]] = [j[1].replace('\n','')]
    with open('combined_queries.txt','w') as file:
        for i in dict:
            file.write("{} VALUES {};".format(i,','.join(dict[i])))
            yield "{} VALUES {};".format(i,','.join(dict[i]))
        