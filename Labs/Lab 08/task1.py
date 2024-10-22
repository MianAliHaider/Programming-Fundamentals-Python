file = open("records.txt","r")
best_average =0
high_score = 0
i = 1
num_players = int(file.readline())
while i<=num_players:
    run = 0
    j = 1
    number_of_matches = int(file.readline())
    print(f'Player{i} runs:', end = " ")
    while j <=number_of_matches:
        runs = int(file.readline())
        print(runs,end = ' ')
        if(runs>high_score):
            high_score = runs
        run = runs+run
        j = j+1
    print()
    avg = run/number_of_matches
    print("Average: ",avg)
    if(avg>best_average):
        best_average= avg
    i = i+1
print("best average",best_average)
print("high score",high_score)
file.close()

