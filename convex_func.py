import math
def convex_func_lin (x, pts , val):
    #pts= points in interval [0,1]
    #example pts= [.2,.3,.4,.5]
    # val function values on pts, should be a decresing sequence between 0 and 1.
    #example val=[0.9,0.8,.6,.5]
    # returns piece-wise linear function joining (pts(i),vals(i) starting from (0,1) and ending at (1,0)
    if (len(pts) != len(val)): 
        raise "Wrong inputs."
    pts=[0]+pts+[1]
    val=[1]+val+[0]
    for i in range(1,len(pts)-1):
        pts_val= ((val[i+1]-val[i-1])*pts[i] + (val[i-1]*pts[i+1] - val[i+1]*pts[i-1]))/(pts[i+1]-pts[i-1])
        if pts_val > val[i]:
            raise "Not a convex function."

    i=0;
    for pt in pts:
        if pt>=x:
            break
        i+=1
    value=((val[i]-val[i-1])*x + (val[i-1]*pts[i] - val[i]*pts[i-1]))/(pts[i]-pts[i-1])
    return value

def convex_func_smooth(x,a):
    # we use the cosine convex, one can use other convex smooth functions
    if a<1:
        raise "a should be atleast 1"
    return math.cos(math.pi/2 * x**a)

    
            
            