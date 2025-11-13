'''
Instructions

    Define our function to accept a single number called rating.
    If the rating is equal to or less than 5, return "Avoid at all costs!"
    If the rating was less than 9, return "This one was fun."
    If neither of the if statement conditions were met, return "Outstanding!"
'''

def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif rating < 9:
        return "This one was fun."
    else:
        return "Outstanding!"


if __name__ == "__main__":
    print(movie_review(9))
    print(movie_review(4))
    print(movie_review(6))
