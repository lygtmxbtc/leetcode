a = [1,2,3]

tmp = []
res = []
mark = [0] * len(a)

def backtrace(cur_list, res_list, mark_list, n_length):
    if len(cur_list) == n_length:
        res_list.append([x for x in cur_list])
    else:
        for i in range(n_length):
            if mark_list[i] == 1:
                continue
            cur_list.append(a[i])
            mark_list[i] = 1
            backtrace(cur_list, res_list, mark_list, n_length)
            mark_list[i] = 0
            cur_list.pop()

backtrace(tmp,res,mark,len(a))


res = []
N = 4
def backtrace(s='',left=0,right=0):
    print(s)
    if len(s) == 2 * N:
        res.append(s)
        return
    if left < N:
        backtrace(s+'(',left+1,right)
    if right < left:
        backtrace(s+')',left,right+1)

backtrace()