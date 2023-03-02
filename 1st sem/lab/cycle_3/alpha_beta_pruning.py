 # Initial values of Alpha and Beta
MAX, MIN = 1000, -1000
#function for minimax
def minimax(depth, node, maximizer,
            value, alpha, beta):
    #checking if leaf node
    if depth == 3:
        return value[node]
 
    if maximizer:
      
        best_val = MIN
 
        for i in range(0, 2):
            #recursive calling of function for left and right child
            val = minimax(depth + 1, node * 2 + i,
                          False, values, alpha, beta)
            best_val = max(best_val, val)
            alpha = max(alpha, best_val)
 
            # Alpha Beta Prunning
            if beta <= alpha:
                break
          
        return best_val
      
    else:
        best_val = MAX
        #recursive calling of function for left and right child
        # right children
        for i in range(0, 2):
          
            val = minimax(depth + 1, node * 2 + i,
                            True, values, alpha, beta)
            best_val = min(best_val, val)
            beta = min(beta, best_val)
 
            # Alpha Beta Pruning
            if beta <= alpha:
                break
          
        return best_val

#input values for alpha beta pruning 
values = [3, 5, 6, 9, 1, 2, 0, -1] 

print("\nvalues for prunning :\n",values)
#call and print minimax function for alpha beta prunning
print("\nThe optimal value using alpha beta prunning is :", minimax(0, 0, True, values, MIN, MAX))