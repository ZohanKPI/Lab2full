class Rectangle:
    def __init__(self): # default values
        self.__length = 1
        self.__width = 1
    def get_length(self): # getter functions for length and width
        return self.__length
    def get_width(self):
        return self.__width
    def set_length(self,length): # setter functions that also checks values according to the task and throws exceptions
        try:
            if 0.0 <= length <= 20.0:
                self.__length = length
                return True
        except:
            return None

    def set_width(self,width):
        try:
            if 0.0 <= width <= 20.0:
                self.__width = width
                return True
        except:
            return None
    def perimeter(self): # calculation functions
        p = (self.__width+self.__length)*2
        return p
    def area(self):
        a = self.__length*self.__width
        return a
rectangle = Rectangle() # class instance
rectangle.set_length(-1)
rectangle.set_width(2)
print(rectangle.get_length(), rectangle.get_width())
print(rectangle.perimeter(), rectangle.area())