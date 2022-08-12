class Stack:
    def __init__(self, length) -> None:
        self.__data = []
        self.__length = length

    def __getCurrentStack(self):
        return self.__data

    def push(self, data):
        if self.__isFull():
            print("stack is full, can\'t push")
        else:
            print("pushing item into stack with data ...", data)
            self.__getCurrentStack().append(data)
            self.print_stack()

    def pop(self):
        if self.__isEmpty():
            print('Stack is Empty, can\'t pop')
        else:
            print("removing item from stack...")
            item = self.__getCurrentStack().pop()
            print("Item removed into stack", item)
            self.print_stack()

    def __isFull(self):
        return len(self.__getCurrentStack()) == self.__length

    def __isEmpty(self):
        return len(self.__getCurrentStack()) == 0

    def print_stack(self):
        print(self.__data)
