class Queue:
    index = None
    nextQueue = None
    sameRotation = None
    outQueue = None
    server = None
    capacity = None
    states = {}
    min_arrival = None
    max_arrival = None
    min_exit = None
    max_exit = None
    
    currentState = 0
    loss = 0
    
    def __init__(self,index,nextQueue,sameRotation,outQueue,server,capacity,arrival,exitTime):
        self.index = index
        self.nextQueue = float(nextQueue)
        self.sameRotation = float(sameRotation)
        self.outQueue = float(outQueue)
        self.server = int(server)
        self.capacity = int(capacity)
        for i in range(self.capacity+1):
            self.states[i] = 0
        self.min_arrival = int(arrival[0])
        self.max_arrival = int(arrival[1])
        self.min_exit = int(exitTime[0])
        self.max_exit = int(exitTime[1])
        print(self.min_exit)
        print(self.states)

    def getId(self):
        return self.index
