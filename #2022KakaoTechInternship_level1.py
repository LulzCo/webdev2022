# survey = ["RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"]
# chpice = [1,2,3,4,5,6,7,8]
# 1,2,3 ,4, 5,6,7
survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

R = 0
T = 0
C = 0
F = 0
J = 0
M = 0
A = 0
N = 0

def solution(survey, choices):
    answer = ''
    for x in range(len(survey)):
        if choices[x] == 1:
            globals()[survey[x][0]] += 3
        elif choices[x] == 2:
            globals()[survey[x][0]] += 2
        elif choices[x] == 3:
            globals()[survey[x][0]] += 1
        elif choices[x] == 5:
            globals()[survey[x][1]] += 1
        elif choices[x] == 6:
            globals()[survey[x][1]] += 2
        elif choices[x] == 7:
            globals()[survey[x][1]] += 3
        continue

    if R >= T:
        answer += "R"
    else:
        answer += "T"

    if C >= F:
        answer += "C"
    else:
        answer += "F"

    if J >= M:
        answer += "J"
    else:
        answer += "M"

    if A >= N:
        answer += "A"
    else:
        answer += "N"

    return answer

print(solution(survey, choices))