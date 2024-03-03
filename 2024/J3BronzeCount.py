N = int(input())
scores = []
counter = 0
for i in range(N):
    S = int(input())
    scores.append(S)

scores.sort(reverse=True)
scores_ = set(scores)
scores_ = list(scores_)
scores_.sort(reverse=True)

for i in range(len(scores)):
    if scores[i] == scores_[2]:
        counter += 1

print(scores_[2], " ", counter)