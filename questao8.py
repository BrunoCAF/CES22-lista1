from math import log10, floor

def ssum(sl):
    S = ""
    for w in sl:
        S += w
    return S

def print_neat_table(n):
    l = floor(log10(n))+1
    m = floor(2*log10(n))+1
    cell_block = lambda x: (" "*m + f"{x}")[-m-1:]
    begin_block = lambda x: (" "*l + f"{x}")[-l:]
    
    # 1a Linha:
    print(begin_block(" ")+"   "+ssum(cell_block(k) for k in range(1, n+1)))
    # 2a Linha:
    print(begin_block(" ")+":--"+("-")*n*(m+1))
    # Linhas seguintes:
    for i in range(1, n+1):
        print(begin_block(i)+":  "+ssum(cell_block(i*k) for k in range(1, n+1)))
    
    return

print_neat_table(12)

