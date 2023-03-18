# python3
# Aleksandra Červinska 221RDB069 12.grupa
def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    p = [(0,i) for i in range(n)]
    for i in range(m):
        sak, ti = min(p)
        output.append((ti,sak))
        p.remove((sak,ti))
        p.append((sak+data[i],ti))

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n,m= map(int,input("input integers: ").split())
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    data=list(map(int, input("input time: ").split()))
    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for pair in result:
        print(pair[0],pair[1])


if __name__ == "__main__":
    main()
