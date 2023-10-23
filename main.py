from time1 import *

def main():
    # Creating time objects
    t1 = time1(2, 30, 5)
    t2 = time1(12, 25, 42)
    t3 = time1(1, 20, 22)
    t4 = time1(11, 45, 50)
    t5 = time1(3, 25, 25)

    # Displaying string representation of time objects
    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print(t5)

    # Testing equality of time objects
    print('Is t1 equal to t5?', t1.__eq__(t5))

    # Updating t1 to make it equal to t5
    t1.setHour(t5.getHour())
    t1.setMinute(t5.getMinute())
    t1.setSecond(t5.getSecond())
    print('Is t1 equal to t5?', t1.__eq__(t5))

    # Storing times in a list and displaying it
    times = [str(t1), str(t2), str(t3), str(t4), str(t5)]
    print(times)

    # Sorting times list partially and fully, then displaying it
    time1.sort(times, 1, 3)
    print(times)
    time1.sort(times, 0, 4)
    print(times)

    # Searching for specific times in the sorted list
    print(time1.search(times, 0, 4, str(t2)))
    print(time1.search(times, 0, 4, str(t3)))
    print(time1.search(times, 1, 3, str(t2)))
    print(time1.search(times, 1, 3, str(t3)))

if __name__ == "__main__":
    main()
