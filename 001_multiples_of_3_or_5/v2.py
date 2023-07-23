n = 1000

no_threes = (n-1)//3
no_fives = (n-1)//5
no_fifteens = (n-1)//15

tot_threes = no_threes*(no_threes+1)/2 * 3
tot_fives = no_fives*(no_fives+1)/2 * 5
tot_fifteens = no_fifteens*(no_fifteens+1)/2 * 15

print(tot_threes+tot_fives-tot_fifteens)
