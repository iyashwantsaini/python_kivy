import time

gen_start=time.time()
print(sum(n for n in range(100000000)))
gen_time=time.time()-gen_start

list_start=time.time()
print(sum([n for n in range(100000000)]))
list_time=time.time()-list_start

print(f'Gen_time={gen_time}')
print(f'List_time={list_time}')