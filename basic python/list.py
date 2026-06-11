food = ["sushi", "pizza", "pasta", "burger", "gelato"]
print(food[0])
print(food[-1])
food.append("noodles")
food.pop(1)
food.sort()
print(food)
# number 2
scores = [55, 72, 88, 43, 96, 61]
scores.sort()
print(scores[0])
print(scores[5])

abc = 0
for a in scores:
    if a > 70:
        abc +=  1
print(abc)
