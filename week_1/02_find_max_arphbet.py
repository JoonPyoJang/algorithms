# Q.  다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오


def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1
    max_num = 0
    for i,j in enumerate(alphabet_occurrence_array):
        if  max_num < j:
            max_num = j
            alphbet_index = i
    return chr(ord("a") + alphbet_index)

print("정답 = a 현재 풀이 값 =", find_alphabet_occurrence_array("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", find_alphabet_occurrence_array("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", find_alphabet_occurrence_array("best of best sparta"))

