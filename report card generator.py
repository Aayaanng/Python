def subj():
    name = input("What is your name? ")
    subj_1 = input("What did you get in maths? ")
    subj_2 = input("What did you get in science? ")
    subj_3 = input("What did you get in english? ")
    subj_4 = input("What did you get in hindi? ")
    subj_5 = input("What did you get in spanish? ")
    subj_6 = input("What did you get in history? ")
    subj_7 = input("What did you get in geography? ")

    marks(subj_1, subj_2, subj_3, subj_4, subj_5, subj_6, subj_7)
def marks(subj_1, subj_2, subj_3, subj_4, subj_5, subj_6, subj_7):
    mks = {
        "math": subj_1,
        "science": subj_2,
        "english": subj_3,
        "hindi": subj_4,
        "spanish": subj_5,
        "history": subj_6,
        "geography": subj_7
    } 
    return mks
subj()
def average(subj_1, subj_2, subj_3, subj_4, subj_5, subj_6, subj_7):
    avg = subj_1 + subj_2 + subj_3 + subj_4 + subj_5 + subj_6 + subj_7 / 7
    