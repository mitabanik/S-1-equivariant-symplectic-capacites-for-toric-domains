import numpy as np

def GH_capacities_concave(it,x,f):
    # computing Gutt-Hutchings capacities upto it iterations for concave toric domains
    cap=[]
    for n in range(1,it+1):
        Max=0;m=len(x);
        for i in range(n):
            A=[i,n-i+1]; Min=1e09;
            Min=min(min(np.dot(A,[x,f])),Min)
            
            if Max<Min:
                Max=Min
                
        cap.append(Max)
    return cap