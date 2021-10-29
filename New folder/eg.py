#!/bin/python3


def theHackathon(n, m, a, b, f, s, t):
    fn = len
    deptmax = {"1": f, "2": s, "3": t}
    dict = {}
    for i in range(n):
        mem, team = input().split()
        dict[mem] = team
    list = []
    for i in range(m):
        mem1, mem2 = input().split()
        index = -1
        index1 = -1
        for i in range(fn(list)):
            if mem1 in list[i]:
                index = i
                break
        for i in range(fn(list)):
            if mem2 in list[i]:
                index1 = i
                break
        if (index == -1 and index1 == -1):
            list.append({mem1, mem2})

        elif (index == -1 or index1 == -1):
            if (index != -1):
                domsum = 0
                for i in list[index]:
                    if (dict[i] == dict[mem2]):
                        domsum += 1
                if (fn(list[index]) + 1 <= b and domsum + 1 <= deptmax[dict[mem2]]):
                    list[index].add(mem2)
            else:
                domsum = 0
                for i in list[index1]:
                    if (dict[i] == dict[mem1]):
                        domsum += 1
                if (fn(list[index1]) + 1 <= b and domsum + 1 <= deptmax[dict[mem1]]):
                    list[index1].add(mem1)
        elif (index != -1 and index1 != -1):
            if(fn(list[index])>b or fn(list[index1])>b):
                continue
            if (index != index1):
                dept1 = 0
                dept2 = 0
                dept3 = 0
                # print(list[index].union(list[index1]))
                list3 = list[index].union(list[index1])
                x = fn(list3)
                if (x <= b):
                    for i in list3:
                        if (dict[i] == "1"):
                            dept1 += 1
                        elif (dict[i] == "2"):
                            dept2 += 1
                        elif (dict[i] == "3"):
                            dept3 += 1
                    if (dept1 <= f and dept2 <= s and dept3 <= t):
                        list[index1] = list[index1].union(list[index])
                        list.remove(list[index])
    list.sort(key=lambda x: fn(x))
    if fn(list) == 0 or fn(list[-1]) < a:
        print("no groups")
    else:
        list4 = []
        for i in range(fn(list) - 1, -1, -1):
            if (fn(list[i]) < fn(list[-1])):
                break
            if (fn(list[i]) == fn(list[-1])):
                for j in list[i]:
                    list4.append(j)
    [print(i) for i in sorted(list4)]
    # Participant code here


if __name__ == '__main__':
    inputdata = input().split()

    n = int(inputdata[0])

    m = int(inputdata[1])

    a = int(inputdata[2])

    b = int(inputdata[3])

    f = int(inputdata[4])

    s = int(inputdata[5])

    t = int(inputdata[6])

    theHackathon(n, m, a, b, f, s, t)