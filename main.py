from heapq import merge
from pick import pick
import splitter
import merge

title = 'Select a service: '
options = ['Merge multiple files', 'Split pages in half', 'Rotate']
option, index = pick(options, title)

if(index == 1):
    splitter.main()
elif(index == 2):
    merge.main()
else:
    exit()