def rhyme(txt):
    st = txt.lower().split()
    f = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
    tmp = f(st[0])
    if all([f(i) == tmp for i in st]):
        return 'Парам пам-пам'
    return 'Пам парам'

enter_user_rhyme=input("Enter your amazing rhyme")
rhyme(enter_user_rhyme)

# print(Rhyme("Хорошо-живет-на-свете-Винни-Пух!\
#  Оттого-поет-он-эти-Песни-вслух!"))
#
# print(Rhyme("пара-ра-рам рам-пам-папам па-ра-па-дам"))
#
# print(Rhyme("пара-ра-рам рам-пам-папам па-ра-па-дм"))