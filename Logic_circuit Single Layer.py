def update_weights(w,b,x,y,o,i):
    w[0] = w[0] + (y[i] - o[i])*x[i][0]
    w[1] = w[1] + (y[i] - o[i])*x[i][1]
    #b = b + (y[i] - o[i])
    return w,b

x = [(0,0),(0,1),(1,0),(1,1)]
y = [1,0,0,1]
w = [0,0]
b = 0
o = [None,None,None,None]
epoch = 0

while True:
    epoch += 1
    # training Function

    for i in range(len(x)):
        z = w[0]*x[i][0] + w[1]*x[i][1] + b

    #threshold check

        if z > 0:
            o[i] = 1
        else:
            o[i] = 0
    #Updating weights

        if o[i] != y[i]:
            w,b = update_weights(w,b,x,y,o,i)
    
    print(f"""
        After {epoch} iterations:
        x: {x}
        y: {y}
        o: {o}
        w: {w}, b: {b}""")

    #terminating condition

    if o == y or epoch == 100:
        break