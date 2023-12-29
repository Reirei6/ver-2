f = open("train.csv", "r")
lst = list(f.readlines())
f.close()

all = 0
male = 0
female = 0

m = []
for i in range(1, len (spisok)):
    m = lst[i].split(',')
    if m[1] == '1' and m[5] == 'male':
       male += 1
    if m[1] == '1' and m[5] == 'female':
        female += 1
all = male + female
print("общее число выживших:", all , "," " выживших мужчин:", male , "," " выживших женщин:", female)