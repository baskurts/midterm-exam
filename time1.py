class time1:
    
    
    def __init__(self, hour: int, minute: int, second: int):
        
        try:
            if not (0 <= hour <= 24):
                raise ValueError("Hour should be between 0 and 24")
            if not (0 <= minute < 60):
                raise ValueError("Minute should be between 0 and 59")
            if not (0 <= second < 60):
                raise ValueError("Second should be between 0 and 59")
        except ValueError as e:
            exit(e)
        else:
            self.__hour = hour
            self.__minute = minute
            self.__second = second
            self.__update_time()

    def __update_time(self):
        self.__time = f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"

    def getHour(self):
        return self.__hour

    def setHour(self, hour: int):
        try:
            if not (0 <= hour <= 24):
                raise ValueError("Hour should be between 0 and 24")
        except ValueError as e:
            exit(e)
        else:
            self.__hour = hour
            self.__update_time()

    def getMinute(self):
        return self.__minute

    def setMinute(self, minute: int):
        try:
            if not (0 <= minute < 60):
                raise ValueError("Minute should be between 0 and 59")
        except ValueError as e:
            exit(e)
        else:
            self.__minute = minute
            self.__update_time()

    def getSecond(self):
        return self.__second

    def setSecond(self, second: int):
        try:
            if not (0 <= second < 60):
                raise ValueError("Second should be between 0 and 59")
        except ValueError as e:
            exit(e)
        else:
            self.__second = second
            self.__update_time()

    def getTime(self):
        return self.__time

    def __str__(self):
        return self.__time

    def __eq__(self, other):
        if other is not None and isinstance(other, time1):
            return self.__time == other.getTime()
        return False

    @staticmethod
    def sort(data, first: int, last: int):
        i = 1 
        j = 0
        nextVal = 0

        while i <= last - first:
            nextVal = data[first + i]

            j = first + i
            while j > first and data[j - 1] > nextVal:
                data[j] = data[j - 1] 
                data[j - 1] = nextVal
                j = j - 1

            i = i + 1
    
    @staticmethod
    def search(a, first: int, last: int, target: str): 
        found = False 
        size = last - first + 1  
        middle = int(first + size / 2)

        if size <= 0:
            return -1
        else:
            while size > 0 and not found:
                if a[middle] == target:
                    found = True
                elif a[middle] > target:
                    size = int(size / 2)
                else:
                    first = middle + 1
                    size = int((size - 1) / 2)

                middle = int(first + size / 2)

        if found:
            return middle
        else:
            return -1
