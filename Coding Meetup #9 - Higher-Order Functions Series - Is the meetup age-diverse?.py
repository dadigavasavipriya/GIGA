'''You will be given an array of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next coding meetup that you are organising.

Your task is to return:

true if developers from all of the following age groups have signed up: teens, twenties, thirties, forties, fifties, sixties, seventies, eighties, nineties, centenarian (at least 100 years young).
false otherwise.
For example, given the following input array:

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
your function should return true as there is at least one developer from each age group.

Notes:

The input array will always be valid and formatted as in the example above.
Age is represented by a number which can be any positive integer up to 199.'''

def is_age_diverse(lst): 
    # your code here
    ages=[i['age'] for i in lst]
    ages.sort()
    if len(ages)<10:
        return False
    else:
        tens=0;twens=0;thir=0;four=0;fift=0;sixt=0;seven=0;eight=0;nine=0;cent=0
        for i in ages:
            if i in range(10,20):
                tens+=1
            elif i in range(20,30):
                twens+=1
            elif i in range(30,40):
                thir+=1
            elif i in range(40,50):
                four+=1
            elif i in range(50,60):
                fift+=1
            elif i in range(60,70):
                sixt+=1
            elif i in range(70,80):
                seven+=1
            elif i in range(80,90):
                eight+=1
            elif i in range(90,100):
                nine+=1
            else:
                cent+=1
        if tens>=1 and twens>=1 and thir>=1 and four>=1 and fift>=1 and sixt>=1 and seven>=1 and eight>=1 and nine>=1 and cent>=1:
            return True
        else:
            return False
                
            


