def getUniqueLargeNumber(string, pattern):
    answer = ''
    if pattern[-1] == "#":

        for i in range(len(string) - len(pattern) + 1):

            if string[i:i + len(pattern) - 1] == pattern[:-1]:
                answer = answer + str(i + 1)



    else:
        for i in range(len(string) - len(pattern) + 1):
            if string[i:i + len(pattern)] == pattern:
                answer = answer + str(i + 1)



    if len(answer) > 0:
        return int(answer)
    else:
        return 0


print(getUniqueLargeNumber('abcdabghabd', 'abssdsdsd#'))
# print(getUniqueLargeNumber("abcdefabc", "abc"))
