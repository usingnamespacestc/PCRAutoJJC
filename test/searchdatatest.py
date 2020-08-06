import os
import pcrdata
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import cpu_count

unitsIcons = []


def searchKeyByName(name):
    for key in pcrdata.CHARA_NAME:
        if name in pcrdata.CHARA_NAME[key]:
            return key

'''#日后再说多线程优化
def searchSingle(i_group):
    print(i_group)

def searchMulti(task):
    pool = ThreadPoolExecutor(cpu_count())
    list(pool.map(searchSingle, task))
    pool.shutdown()
'''
if __name__ == '__main__':
    unitsIcons = os.listdir('units')
    '''#日后再说多线程优化
    cpu = cpu_count() - 1
    pool = ProcessPoolExecutor(cpu)
    L = unitsIcons
    F = int(len(L) / cpu)
    task_assign = [L[n * F:] if (n + 1) == cpu else L[n * F:(n + 1) * F] for n in range(cpu)]
    list(pool.map(searchMulti, task_assign))
    pool.shutdown()
    '''
    searchKeyByName("望")