def get_average(lst): 
    m=[]
    for i in lst:
            for j in i:
                if j=='age':
                    m.append(i['age'])
    n=len(m)
    r=sum(m)
    average = r/n
    return round(average)
list1 = [
  { 'firstName': 'Maria', 'lastName': 'Y.', 'country': 'Cyprus', 'continent': 'Europe', 'age': 30, 'language': 'Java' },
  { 'firstName': 'Victoria', 'lastName': 'T.', 'country': 'Puerto Rico', 'continent': 'Americas', 'age': 70, 'language': 'Python' },
]
print(get_average(list1))