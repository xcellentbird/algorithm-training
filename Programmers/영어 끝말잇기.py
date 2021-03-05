def solution(n, words):
    talked = [words[0]]
    for i, word in enumerate(words[1:]):
        if word in talked or word[0] != words[i][-1]:
            ret = [(i+2)%n, (i+n+1)//n]
            if ret[0] == 0:
                ret[0] = n
            return ret
        talked.append(word)
    return [0, 0]
