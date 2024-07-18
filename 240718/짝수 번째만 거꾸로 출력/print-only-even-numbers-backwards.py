string = input()

# 짝수번째 원소만 추출 후, 슬라이싱으로 뒤집기
even_elem = string[1::2][::-1]

print(even_elem)