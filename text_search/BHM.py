# Boyer-Moore-Horspool算法
# Q: 函数deal_word的位置


def deco(*args, fmt=0):
    init = 0
    if fmt == 0:
        def wrapper(func):
            nonlocal init
            init += func(*args)
            return init
    else:
        def wrapper(func):
            nonlocal init
            init = func(*args)
            return init

    return wrapper


# Boyer-Moore-Horspool算法
def b_m_h(word, words):
    # 处理搜索的字符
    def deal_word():
        nonlocal word
        num = len(word) - 1
        var = {}
        for i in range(num):
            if var.get(word[num - 1 - i]) is None:
                var[word[num - 1 - i]] = i + 1
        return var

    pos, times = 0, 0
    var = deal_word()
    while pos <= len(words) - len(word):
        word_pos = len(word) - 1
        while word_pos >= 0 and word[word_pos] == words[pos + word_pos]:
            word_pos -= 1
        if word_pos == -1:
            print("搜索成功，起始位置是{}".format(pos + 1))
            times += 1
        if var.get(words[pos + len(word) - 1]) is not None:
            pos += var[words[pos + len(word) - 1]]
        else:
            pos += len(word)
    return times


# 按绝对位置进行搜索
def juedui_pos():
    ins = open('test/test1.txt', 'r', encoding='utf-8')
    keyword = '新手'
    while True:
        page = ins.read()
        if not page:
            ins.close()
            break
        f = deco(keyword, page, fmt=1)
        num = f(b_m_h)

    print('关键词：\'{}\'，共计出现{}次\n'.format(keyword, num))


# 按相对位置进行搜索
def xiangdui_pos():
    num = 0
    ins = open('test/test1.txt', 'r', encoding='utf-8')
    keyword = 'test'
    while True:
        page = ins.readline()
        if not page:
            ins.close()
            break
        f = deco(keyword, page, fmt=0)
        num += f(b_m_h)

    print('关键词：\'{}\'，共计出现{}次\n'.format(keyword, num))


juedui_pos()
xiangdui_pos()
