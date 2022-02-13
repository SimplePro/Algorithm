N = int(input())

def isitright(sequence):
    for i in range(len(sequence)-1, len(sequence) // 2-1, -1):
        check_len = len(sequence) - i

        if sequence[i-check_len:i] == sequence[i:]:
            return False

    return True

def dfs(sequence):

    if len(sequence) == N:
        print(sequence)
        exit()

    else:
        for i in ['1', '2', '3']:
            if isitright(sequence + str(i)):
                dfs(sequence + str(i))

dfs("1")