age = 33
count = 0
while count < 3:
    guess_age = int(input("Guess the age: "))
    if guess_age == age:
        print("You guess right")
        break
    count+=1
    if count == 3:
        conti_play = input("还有继续玩吗？（y/n）")
        if conti_play == 'y':
            count = 0


