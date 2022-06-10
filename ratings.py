# """Restaurant rating lister."""
# filename = 'scores.txt'

# d = {}
# with open(filename) as f:
#     for line in f:
#         (key, val) = line.split(':')
#         d[key] = val

# print (d)

# put your code here





def resturant():

    rating = open('scores.txt')
    scores = {}

    for line in rating:
        line = line.rstrip()
        resturant, score = line.split(':')
        scores[resturant] = int(score)

    return scores

def addResturant(result):

    print('add a resturant')
    resturant = input('Name of Resturant > ')
    rating = input('resturant rating > ')

    result[resturant] = rating


def alphasort(result):

    for resturant, rating in sorted(result.items()):
        print(f'{resturant} has a rating of {rating}')


result = resturant()
addResturant(result)
alphasort(result)

# print(result)


