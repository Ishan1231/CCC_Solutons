A = list(input())
B = list(input())

actual_letter = ''
silly_letter = ''
silent_letter = ''

for i in range(len(A)):
    try:
        if A[i] == B[i]:
            continue
        elif A[i + 1] == B[i]:
            B.insert(i, ' ')
            silent_letter = A[i]
        actual_letter = A[i]
        silly_letter = B[i]
    except IndexError:
        silent_letter = A[i]
        break
print(f"{A}\n{B}")
print(f'{actual_letter} {silly_letter}')
if silent_letter == '':
    print('-')
else:
    print(silent_letter)
