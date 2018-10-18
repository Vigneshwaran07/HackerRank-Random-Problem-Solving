import textwrap
def merge_the_tools(string, k):
    l = textwrap.wrap(string, k)
    t = []
    for i in l:
        for j in i:
            if j not in t:
                t.append(j)
        print("".join(t))
        t =[]
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)        
