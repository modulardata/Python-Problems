# word = input()
# spaces = int(input())
# space = " " * spaces
# print(space.join([word[i] for i in range(len(word))]))


print(*input(), sep=int(input()) * ' ')
