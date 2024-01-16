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
