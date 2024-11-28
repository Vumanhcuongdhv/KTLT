print("Vũ Mạnh Cường")
print("235752021610030")
with open('D:/a.txt', 'r') as file:
    char = 0  
    wc = 0     
    lc = 0
    
    for line in file:
        lc += 1 
        char += len(line)  
        
        words = line.split()
        wc += len(words)
        
    # In kết quả
    print("The no. of chars is %d" % char)
    print("The no. of words is %d" % wc)
    print("The no. of lines is %d" % lc)
