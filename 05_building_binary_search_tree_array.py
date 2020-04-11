def GenerateBBSTArray(a):
    a.sort()
    spisok = [a]
    itogo = []
    while spisok:  # пожалуй, вместо массивов производительнее использовать связанные списки
        arr = spisok[0]
        itogo.append(arr[int(len(arr) // 2)])
        if arr[0:int(len(arr) // 2)]:
            spisok.append(arr[0:int(len(arr) // 2)])
        if arr[int(len(arr) // 2) + 1:]:
            spisok.append(arr[int(len(arr) // 2) + 1:])
        spisok.pop(0)
    return itogo
