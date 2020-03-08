from random import randint
def numbering(kuchi, numCount, minNum, maxNum):
    print("口数：", kuchi, " 文字数：", numCount, " 最小文字：", minNum, " 最大文字：", maxNum)
    print(numbering)
    for i in range (kuchi):
        numlist = list()
        while len(numlist) < numCount:
            number = randint(minNum, maxNum)
            if not number in numlist:
                numlist.append(number)
        numlist.sort()
        print(numlist)


while True:
    kind = int(input("下記のメニューを確認し、１から５の数字を入力してください。\n\
    １．ロト７のナンバーズを生成する\n\
    ２．ロト６のナンバーズを生成する\n\
    ３．ミニロトのナンバーズを生成する\n\
    ４．ナンバーズ４のナンバーズを生成する\n\
    ５．ナンバーズ３のナンバーズを生成する\n\
    ※１から５以外の文字が入力されると終了\n\
メニューの数字を入力してください："))
    if kind == 0 or kind > 5:
        break
    kuchi = int(input("口数を入力してください："))

    if kind == 1:
        print("====== ロト７のナンバーズを", kuchi, "口生成します。 ======")
        numbering(kuchi, 7, 1, 37)
    elif kind == 2:
        print("====== ロト６のナンバーズを", kuchi, "口生成します。 ======")
        numbering(kuchi, 6, 1, 34)
    elif kind == 3:
        print("====== ミニロトのナンバーズを", kuchi, "口生成します。 ======")
        numbering(kuchi, 5, 1, 31)
    elif kind == 4:
        print("====== ナンバーズ４のナンバーズを", kuchi, "口生成します。 ======")
        numbering(kuchi, 4, 0, 9)
    elif kind == 5:
        print("====== ナンバーズ３のナンバーズを", kuchi, "口生成します。 ======")
        numbering(kuchi, 3, 0, 9)
    