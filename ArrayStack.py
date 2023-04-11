
class ArrayStack:

    def __init__(self):
        self.data=[]

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self,e):
        self.data.append(e)

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.data[-1]

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.data.pop()

    def reverse_file(filename):
        S=ArrayStack()
        original = open(filename)
        for line in original:
            S.push(line.rstrip("\n"))
        original.close()

        output=open(filename,"w")
        while not S.is_empty():
            output.write(S.pop() + "\n")
        output.close()



        


            
