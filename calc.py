# get two integer parameters
# return sum
def plus(x, y):
    return x+y

# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:
        print("0: exit, 1: plus")
        try: # Added try-except function to deal with exceptions
            check = int(input())
            if check == 1:
                print("First Number")
                x = int(input())
                print("Second Number")
                y = int(input())
                print("answer : ", plus(x,y))
            elif check > 1:
                print("Unsupported")
            else:
                print("Thank you")
        except:
            print("Please check your input. Only 'NUMBERS' supported!")

if __name__ == "__main__":
    main()
