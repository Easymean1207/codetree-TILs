class Sequence:
    def __init__(self, element, index):
        self.element, self.index = element, index


# 원래 수열과 정렬된 수열을 비교하여 index를 출력하는 함수
def findAterIndex(origin, after):
    for i, element in enumerate(origin):
        # 정렬된 수열에서 값 기반으로 index 찾기
        after_idx = after.index(element)+1
        print(after_idx, end = ' ')


length_of_sequence = int(input())
given_element = list(map(int, input().split()))
sequences = []

for i in range(length_of_sequence):
    given_index = i+1
    sequences.append(Sequence(given_element[i], given_index))

# 정렬된 sequence를 변수에 할당
after_sorted = sorted(sequences, key= lambda x:(x.element, x.index))

findAterIndex(sequences, after_sorted)