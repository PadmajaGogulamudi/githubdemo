def greet_developers(lst):
    f=""
    l=""
    for i in lst:
        for  j in i:
            if j=='firstName':
                f=i['firstName']
            if j=='language':
                l=i['language']
        i['greeting']='Hi '+f+', what do you like the most about '+l+'?'  
    return lst
list1 = [
  { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java' },
  { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python' },
  { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby' } 
]
x=greet_developers(list1)
print(x)