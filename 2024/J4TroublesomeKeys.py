A = list(input())

B = list(input())

silly_letter = ""
silent_letter = ""
actual_letter = ""

for i in range(len(A)):
    try:
        if B[i] != A[i] and B[i] in A:
            B.insert(i, " ")
    except IndexError:
        break

for i in range(len(B)):
    try:

        if B[i] not in A and B[i] != " ":
            actual_letter = A[i]
            silly_letter = B[i]

        elif B[i] == " ":
            silent_letter = A[i]

    except IndexError:
        silent_letter = A[i]
        break

print(f"{actual_letter} {silly_letter}")

if silent_letter == '':
    print("-")
else:
    print(silent_letter)