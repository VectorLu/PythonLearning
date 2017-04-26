def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0, nextY-i):
            return True
    return False

def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num -1:
                yield (pos, )
            else:
                for result in queens(num, state + (pos, )):
                    yield (pos, ) + result

def prettyPrint(solution):
    def line(pos, length=len(solution)):
        return '. '*(pos) + 'X ' + '. '*(length-pos-1)
    for pos in solution:
        print line(pos)

if __name__ == '__main__':
    import random
    prettyPrint(random.choice(list(queens(8))))

    for solution in queens(8):
        print solution

    '''
    作者：est
    链接：https://www.zhihu.com/question/37046157/answer/70747261
    来源：知乎
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    '''
    # 这是一个一行的解法
    _=[__import__('sys').stdout.write("\n".join('.' * i + 'Q' + '.' * (8-i-1) for i in vec) + "\n===\n") for vec in __import__('itertools').permutations(xrange(8)) if 8 == len(set(vec[i]+i for i in xrange(8))) == len(set(vec[i]-i for i in xrange(8)))]
