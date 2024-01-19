def is_ruby_coming(lst): 
    l= False
    for i in lst:
        for  j in i:
            if j=='language':
                 if i['language']=='Ruby':
                        l= True
    return l
list1 = [
    { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java' },
    { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python' },
    { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby' } 
    ]
print(is_ruby_coming(list1))