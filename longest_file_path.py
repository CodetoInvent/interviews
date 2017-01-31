# 388. Longest Absolute File Path

# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext



def path_depth(str): return str.count('\t')

def file_name(file): return file.replace('\t', '')

path = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext\n'.split('\n')

stack = []
depth = 1

maximum = path[0]
current_path = path[0]

for i in path[1:]:
    if path_depth(i) < depth:
        if stack: stack.pop()
        current_path = '/'.join(stack)
        print current_path
    depth = path_depth(i)
    current_path += '/' + file_name(i)
    if current_path.endswith('.ext'):
        maximum = max(maximum, current_path)

print maximum
