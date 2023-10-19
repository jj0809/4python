def myName(a, b):
    print(f"{a + b} from {__name__}")

def myChange(a, b):
    print(a+b)

if __name__ == '__main__':
    myName(4,6)

myChange(2,4)