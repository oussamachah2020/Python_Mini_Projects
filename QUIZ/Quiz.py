from Questions import quiz
question = 1
score = 0
attempts = 3
answer = 1

while attempts > 0:
    print(quiz[question]["question"])
    ans = input("Enter your answer: ")
    print('/**********************/')
    
    if ans == quiz[answer]["answer"]:
        question += 1
        answer += 1
        score += 1 
        
        if question == 7:
            print("Congratulations Hero! your score is", score)
            break
        
    elif ans != quiz[answer]["answer"]:
        question += 1
        answer += 1
        attempts -= 1
        
    if attempts == 0:
        print("Not a true avenger! your score is", score)
        break