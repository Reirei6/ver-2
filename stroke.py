f open("train.csv", "r") = list = f.readlines()
f.close()

count = 0
male = 0
female = 0
k = []
for i in range(1, len(list)):
    k = list[i].strip().split(',')
   if k[1] == '1' and k[5] == 'male':
    male += 1
    if k[1] == '1' and k[5] == 'female':

    female += 1
count = male + female
print("Общее число выживших