def is_same_language(lst): 
    m=''
    for i in lst:
        for j in i:
            if j=='language':
                m=i['language']
                break
    for i in lst:
        for j in i:
            if j=='language':
                if i['language']==m:
                    continue
                else:
                    return False
    return True
list1 = [
  { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'JavaScript' },
  { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'JavaScript' },
  { 'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary', 'continent': 'Europe', 'age': 65, 'language': 'JavaScript' },
]
print(is_same_language(list1))