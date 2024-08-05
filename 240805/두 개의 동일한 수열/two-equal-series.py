def isSequenceSame(seq1, seq2):
    seq1 = sorted(seq1)
    seq2 = sorted(seq2)

    if seq1 == seq2:
        print('Yes')
    else:
        print('No')

n = input()

A = list(map(int, input().split()))
B = list(map(int, input().split()))

isSequenceSame(A, B)