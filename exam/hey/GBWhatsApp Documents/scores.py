def scores(temp_list):
    sentinel = -1
    temp_list = []

    while True:
        score = int(input("Enter score: "))
        if score == sentinel:
            break
        temp_list.append(score)
    
    # print(temp_list)
    avarage = sum(temp_list) / len(temp_list)
    if avarage >= 90:
        print(f"The avarage score of the class is: {avarage}.\nWell done class!")
    else:
        print(f"The avarage score of the class is: {avarage}.")
        

if __name__ == '__main__':
    scores_list = []
    scores(scores_list)