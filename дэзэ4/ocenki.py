film = ['Зеленная книга', 'Интерстеллар', 'Бойцовский клуб', 'Шрек']
mentions = dict()
with open('Оценки фильмов.txt', encoding='utf-8') as file:
    for line in file.readlines():
        line_list = line.replace('\n', '').split(', ')
        mentions[line_list[0]] = list(map(int, line_list[1:]))

put_rating = list(map(int, input('Оценки (Зеленная книга, Интерстеллар, Бойцовский клуб, Шрек): ').split(', ')))

res = []
for name, ratings in mentions.items():

    scalar = sum([my_rating*user_rating for my_rating, user_rating in zip(put_rating, ratings)])
    len_put_rating = sum([my_rating**2 for my_rating in put_rating])
    len_rating = sum([user_rating**2 for user_rating in ratings])

    res.append((name, scalar / len_put_rating**0.5 / len_rating**0.5))

best_matches = sorted(res, key=lambda x: x[1], reverse=True)[:5]
best_matches = dict([x for x in best_matches if x[1] > 0])

print('\nТоп-5 похожих пользователей:')
for name, matches  in best_matches.items():
    print(f'{name}: {matches}')

print('\nРекомендации:')

recomended_films = dict()
for name in best_matches:
    for i, my_u_rating in enumerate(zip(put_rating, mentions[name])):
        my_rating, user_rating = my_u_rating
        if my_rating == 0:
            if films[i] not in recomended_films:
                recomended_films[films[i]] = 0
            recomended_films[films[i]] += user_rating * best_matches[name]

best_recomendation = sorted(recomended_films.items(), key=lambda x: x[1], reverse=True)[:5]

for film, rate in best_recomendation:
    print(f'{film}: коэффициент {rate}')