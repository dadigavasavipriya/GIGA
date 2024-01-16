'''You will be given an array of objects representing data about developers who have signed up to attend the next coding meetup that you are organising.

Your task is to return an object which includes the count of food options selected by the developers on the meetup sign-up form..

For example, given the following input array:

list1 = [
    { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C', 'meal': 'vegetarian' },
    { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript', 'meal': 'standard' },
    { 'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby', 'meal': 'vegan' },
    { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C', 'meal': 'vegetarian' },
]
your function should return the following object (the order of properties does not matter):

{ 'vegetarian': 2, 'standard': 1, 'vegan': 1 }
Notes:

The order of the meals count in the object does not matter.
The count value should be a valid number.
The input array will always be valid and formatted as in the example above.
there are 5 possible meal options and the strings representing the selected meal option will always be formatted in the same way, as follows: 'standard', 'vegetarian', 'vegan', 'diabetic', 'gluten-intolerant'.'''

'''import string
from collections import defaultdict

@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        list1 = [
            { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C', 'meal': 'vegetarian' },
            { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript', 'meal': 'standard' },
            { 'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby', 'meal': 'vegan' },
            { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C', 'meal': 'vegetarian' },
        ]
        
        answer = { 'vegetarian': 2, 'standard': 1, 'vegan': 1 }
        
        test.assert_equals(order_food(list1), answer)
        
        
@test.describe('Random Tests')'''
def order_food(lst): 
    # your code here
    d={}
    meal={'vegetarian':0,'vegan':0,'diabetic':0,'standard':0,'gluten-intolerant':0}
    for i in lst:
        if i['meal']=='vegetarian':
            a=meal['vegetarian']+1
            meal.update({'vegetarian':a})
            d.update({'vegetarian':a})
        elif i['meal']=='vegan':
            a=meal['vegan']+1
            meal.update({'vegan':a})
            d.update({'vegan':a})
        elif i['meal']=='diabetic':
            a=meal['diabetic']+1
            meal.update({'diabetic':a})
            d.update({'diabetic':a})
        elif i['meal']=='standard':
            a=meal['standard']+1
            meal.update({'standard':a})
            d.update({'standard':a})
        else:
            a=meal['gluten-intolerant']+1
            meal.update({'gluten-intolerant':a})
            d.update({'gluten-intolerant':a})
    return d
