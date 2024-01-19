def get_first_python(lst):
    l= 'There will be no Python developers'
    m=""
    n=""
    for i in lst:
        for  j in i:
            if j=='language':
                 if i['language']=='Python':
                        m= i['first_name']
                        n= i['country']
                        return m+', '+n
    return l
list1= [
          { "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },
          { "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },
          { "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" }
        ]
print(get_first_python(list1))