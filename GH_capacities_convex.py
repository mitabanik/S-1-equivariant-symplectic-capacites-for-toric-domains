import numpy as np

def GH_capacities_convex(it,x,f):
    # computing Gutt-Hutchings capacities upto it iterations for convex toric domains
    # input : it = iterations ; x = point in [0,1] ; f = convex function 
    # returns array of GH capacities
    
    cap = []
    for n in range( 1, it+1 ):
        Min = 1e09; m = len(x);
        for i in range(n):
            A=[i,n-i]; Max = np.dot(A, [0 ,1]);
            Max=max(max(np.dot( A,[x,f] )), Max)
            
            if Max <= Min:
                Min = Max
                
        cap.append( Min )
        
    return cap
