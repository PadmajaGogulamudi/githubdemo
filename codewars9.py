def is_age_diverse(lst):
    m=[]
    a1=[]
    a2=[]
    a3=[]
    a4=[]
    a5=[]
    a6=[]
    a7=[]
    a8=[]
    a9=[]
    a10=[]
    for i in lst:
         m.append(i['age'])
    for k in m:
        if k>=10 and k<20:
            a1.append(k)
        elif k>=20 and k<30:
            a2.append(k)
        elif k>=30 and k<40:
            a3.append(k)
        elif k>=40 and k<50:
            a4.append(k)
        elif k>=50 and k<60:
            a5.append(k)
        elif k>=60 and k<70:
            a6.append(k)
        elif k>=70 and k<80:
            a7.append(k)
        elif k>=80 and k<90:
            a8.append(k)
        elif k>=90 and k<100:
            a9.append(k)
        else:
            a10.append(k)
    if (len(a1)!=0 and len(a2)!=0 and len(a3)!=0 and len(a4)!=0 and len(a5)!=0 and len(a6)!=0 and
       len(a7)!=0 and len(a8)!=0 and len(a9)!=0 and len(a10)!=0)  :
        return True
    else:
        return False
    
        
list1 = [
  { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 19, 'language': 'Python' },
  { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 29, 'language': 'JavaScript' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
  { 'firstName': 'Noa', 'lastName': 'A.', 'country': 'Israel', 'continent': 'Asia', 'age': 40, 'language': 'Ruby' },
  { 'firstName': 'Andrei', 'lastName': 'E.', 'country': 'Romania', 'continent': 'Europe', 'age': 59, 'language': 'C' },
  { 'firstName': 'Maria', 'lastName': 'S.', 'country': 'Peru', 'continent': 'Americas', 'age': 60, 'language': 'C' },
  { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 75, 'language': 'Python' },
  { 'firstName': 'Chloe', 'lastName': 'K.', 'country': 'Guernsey', 'continent': 'Europe', 'age': 88, 'language': 'Ruby' },
  { 'firstName': 'Viktoria', 'lastName': 'W.', 'country': 'Bulgaria', 'continent': 'Europe', 'age': 98, 'language': 'PHP' },
  { 'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128, 'language': 'JavaScript' }
]
print(is_age_diverse(list1))