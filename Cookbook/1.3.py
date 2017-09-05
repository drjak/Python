from collections import deque

def search(file_content, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in file_content:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, '10.50.51.6',7):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)

