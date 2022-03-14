from pick import pick

title = 'Select a service: '
options = ['Merge multiple files', 'Split pages in half', 'Rotate']
option, index = pick(options, title)
