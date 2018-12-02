import sys


def one_diff(box1, box2):
    diffs = 0
    for i in range(len(box1)):
        if box1[i] != box2[i]:
            diffs += 1
    return False if diffs > 1 else True
    

def common(box1, box2):
    for i in range(len(box1)):
        if box1[i] != box2[i]:
            return box1[0:i] + box1[i + 1:]


lines = sys.stdin.readlines()
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        if one_diff(lines[i], lines[j]):
            print (common(lines[i], lines[j]))
            exit(0)