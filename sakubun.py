for i in range (20):
    name = ['あつひが','バカが','おっさんが','アOパOマOが']
    noun = ['あつひを','ライオンを','テレビを','アソコを']
    verb = ['舐めまわす','叩く','蹴る','つぶす']
    from random import randint
    def pick(words):
        num_words = len(words)
        num_picked = randint(0, num_words - 1)
        word_picked = words[num_picked]
        return word_picked
    print(pick(name), pick(noun), pick(verb))