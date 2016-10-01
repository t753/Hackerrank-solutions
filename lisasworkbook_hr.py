'''
Created on Sep 8, 2016

@author: Tom
'''
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
t = [int(c_temp) for c_temp in input().strip().split(' ')]

special = 0
start_page = 1
for i in range(n):
    
    full_pages, last_page = divmod(t[i],  k)
    if full_pages == 0:
        pages = 1
    else:
        if last_page > 0:
            last_page = 1
        pages = full_pages + last_page
    start_problem = 1
    for j in range(pages):
        page = j + start_page
        page_start_problem = (j * k)  + start_problem
        for m in range (page_start_problem, page_start_problem + k ):
            if m == page and m <= t[i]:
                special += 1
    start_page += pages
    
print(special)