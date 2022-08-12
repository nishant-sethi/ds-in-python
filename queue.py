class Queue:
    def __init__(self, length) -> None:
        self.__data = []
        self.__length = length

    def __isFull(self):
        return len(self.__getCurrentQueue()) == self.__length

    def __isEmpty(self):
        return len(self.__getCurrentQueue()) == 0

    def __getCurrentQueue(self):
        return self.__data

    def print_Queue(self):
        print(self.__getCurrentQueue())

    def enqueue(self, data):
        if self.__isFull():
            print('Queue is full, can\'t add')
        else:
            print("pushing item into queue with data ...", data)
            self.__getCurrentQueue().append(data)
            self.print_Queue()

    def dequeue(self):
        if self.__isEmpty():
            print('Queue is Empty, can\'t remove')
        else:
            print("removing item from queue ...")
            self.__getCurrentQueue().pop(0)
            self.print_Queue()
