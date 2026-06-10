def subj():
    name = input("What is your name? ")
    subj_1 = int(input("What did you get in maths? "))  
    subj_2 = int(input("What did you get in science? "))
    subj_3 = int(input("What did you get in english? "))
    subj_4 = int(input("What did you get in hindi? "))  
    subj_5 = int(input("What did you get in spanish? "))
    subj_6 = int(input("What did you get in history? "))
    subj_7 = int(input("What did you get in geography? "))

    marks_dict = marks(subj_1, subj_2, subj_3, subj_4, subj_5, subj_6, subj_7)
    average(subj_1, subj_2, subj_3, subj_4, subj_5, subj_6, subj_7, name)
    return marks_dict

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

def average(subj_1, subj_2, subj_3, subj_4, subj_5, subj_6, subj_7, name):
    avg = (subj_1 + subj_2 + subj_3 + subj_4 + subj_5 + subj_6 + subj_7) / 7
    
    if avg >= 90:
        print(f"{name}, you have an average of {avg:.2f}% so you get an A+.")  
    elif avg >= 80:
        print(f"{name}, you have an average of {avg:.2f}% so you get a B+.") 
    elif avg >= 70:
        print(f"{name}, you have an average of {avg:.2f}% so you get a B-.")
    elif avg >= 60:
        print(f"{name}, you have an average of {avg:.2f}% so you get a C.")  
    elif avg >= 50:
        print(f"{name}, you have an average of {avg:.2f}% so you get a D.")
    elif avg >= 40:
        print(f"{name}, you have an average of {avg:.2f}% so you get a D-.")
    else:
        print(f"{name}, you have an average of {avg:.2f}% so you get an F.")  
subj()
