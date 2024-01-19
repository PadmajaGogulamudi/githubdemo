def count_languages(lst): 
    d=dict()
    for i in lst:
        for key in i:
            if i['language'] not in d.keys():
                d[i['language']]=0
            if key == 'language':
                if i['language'] in d.keys():
                    d[i['language']]= d[i['language']]+1
    return d
list1 = [
            { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C' },
            { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript' },
            { 'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby' },
            { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C' },
            ]  
print(count_languages(list1))