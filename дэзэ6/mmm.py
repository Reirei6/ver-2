import re

text_to_correct = input()

change_to = "(TBD)"

res = re.sub(pattern="([0-1][0-9]|[2][0-3])(:[0-5][0-9]){1,2}",
                repl=change_to, string=text_to_correct)

print(res)