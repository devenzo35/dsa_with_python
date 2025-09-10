S = "Hola buenos dias"
revertedS: list[str] = []

print("len", len(list(S)))


def reverseString(letterList: list[str]):
    for idx in range(len(letterList) - 1, -1, -1):
        print(idx)
        revertedS.append(letterList[idx])


reverseString(list(S))
print(revertedS)
print(S[::-1])
