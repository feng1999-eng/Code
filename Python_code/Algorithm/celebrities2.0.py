# coding=GBK


def bestToParty(sched):
    times = []
    for i in sched:
        times.append((i[0], 's'))
        times.append((i[1], 'e'))
    sortlist(times)
    maxcount, time = chooseTime(times)
    print('Best time to attend party is at', time, 'o\'clock', maxcount, 'celebrities will be attending!')


def sortlist(list):
    n = len(list)
    for i in range(n):
        for j in range(n - i - 1):
            if list[j][0] > list[j + 1][0]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def chooseTime(times):
    maxcount = 0
    rcount = 0
    time = times[0][0]
    for c in times:
        if c[1] == 's':
            rcount += 1
        elif c[1] == 'e':
            rcount -= 1
        if rcount > maxcount:
            maxcount = rcount
            time = c[0]
    return maxcount, time


sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0),
          (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
          (8.0, 10.0), (9.0, 12.0), (9.5, 10.0),
          (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]

bestToParty(sched2)
