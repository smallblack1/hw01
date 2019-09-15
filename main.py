for i in range(1,10):
    for a in range(0,i-1):
        print(4*"  ",end=''),
    for j in range(i,10):
        
        print(f"{i:2d}x{j:<2d}={i*j:2d}",end='')
    print()
    
