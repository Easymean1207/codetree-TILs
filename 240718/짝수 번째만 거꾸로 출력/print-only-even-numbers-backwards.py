string = input()

# 짝수번째 원소만 추출
even_elem = string[1::2][::-1]

print(even_elem)