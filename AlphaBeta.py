tree={
    'A' : ['B', 'C'],
    'B' : [3,5],
    'C' : [6,9]
}

def minmax_AB(node,depth,alpha,beta,max_player):
    if depth==0:
        if node in tree:
            return tree[node][0] if max_player else tree[node][0]
        else:
            return node

    if max_player:
        value=float('-inf')
        for child in tree[node]:
            value=max(value,minmax_AB(child,depth-1,alpha,beta,False))
            alpha=max(alpha,value)
            if alpha>=beta:
                print(f"Purning branch at node {node}")
                break
        return value

    else:
        value=float('inf')
        for child in tree[node]:
            value=min(value,minmax_AB(child,depth-1,alpha,beta,True))
            beta=min(beta,value)
            if beta<=alpha:
                print(f"Purning branch at node {node}")
                break
        return value

best_score=minmax_AB('A',2,float('-inf'),float('inf'),True)
print(f"The best score is : {best_score}")
