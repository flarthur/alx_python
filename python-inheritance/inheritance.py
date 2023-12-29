# Python
#!! Inheritance

# * Python has two built-in functions that will work with inheritance:

# * 1. isinstance()
#########to check an instance's type: isinstance(obj, int), will only
##return true if obj.__class__ is int or some class derived from int
# * 2. issubclass()
#########to check for inheritance: issubclass(bool, int) is True since bool is
##is a subclass of int but issubclass(float, int) would return False

# *Subclass - class that is inheriting, superclass - class being inherited from


class Animal:
    def __init__(self, birthType="Unknown", appearance="Unknows", blooded="Unknown"):
        self.birthType = birthType
        self.appearance = appearance
        self.blooded = blooded

    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    #! Magic Methods
    # First well continue with the code and use string magic methods
    # This magic method casts our object as a string (__str__)

    def __str__(self):
        return "A {} is {} it is {} it is{}".format(
            type(self).__name__, self.birthType, self.appearance, self.blooded
        )


class Mammal(Animal):
    def __init__(
        self,
        birthType="born alive",
        appearance="hair or fur",
        blooded="warm blooded",
        nurseYoung=True,
    ):
        Animal.__init__(self, birthType, appearance, blooded)
        self.__nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    def __str__(self):
        return super().__str__() + " and it is {} they " "nurse their young".format(
            self.nurseYoung
        )


class Reptile(Animal):
    def __init__(
        self,
        birthType="born in egg or born alive",
        appearance="dry scales",
        blooded="cold blooded",
    ):
        Animal.__init__(self, birthType, appearance, blooded)

    def sumAll(self, *args):
        sum = 0

        for i in args:
            sum += i

        return sum

    ####*             Polymorphism                #####


def getBirthType(theObject):
    print("the {} is {}".format(type(theObject).__name__, theObject.birthType))


def main():
    animal1 = Animal("born alive")

    print(animal1.birthType)
    print(animal1)
    print()

    mammal1 = Mammal()

    print(mammal1.birthType)
    print(mammal1.appearance)
    print(mammal1.blooded)
    print(mammal1.nurseYoung)
    print(mammal1)
    print()

    reptile1 = Reptile()

    print(reptile1.birthType)
    print(reptile1)

    print("Sum : {}".format(reptile1.sumAll(1, 2, 3, 4, 5, 6)))

    getBirthType(mammal1)
    getBirthType(reptile1)


main()


#!!!                   Magic Methods            #######
# Are surrounded by double underscores
# __eq__	: Equal
# __ne__	: Not Equal
# __lt__	: Less Than
# __gt__	: Greater Than
# __ge__	: Greater than or equal to
# __le__	:Less than or Equal To
# __add__	:Addition
# __sub__	:Subtraction
# __mul__	:Multiplication
# __div__	:Division
# __mod__	:Modulus

# * TIME


class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def __add__(self, other_time):
        new_time = Time()

        # Add second and correct if sum >= 60
        if (self.second + other_time.second) >= 60:
            self.minute += 1
            new_time.second = (self.second + other_time.second) - 60
        else:
            new_time.second = self.second + other_time.second

        # Add minutes and correct if sum >= 60
        if (self.minute + other_time.minute) >= 60:
            self.hour += 1
            new_time.minute = (self.minute + other_time.minute) - 60
        else:
            new_time.minute = self.minute + other_time.minute

        # Add hours and correct if sum >= 24
        if (self.hour + other_time.hour) >= 24:
            new_time.hour = (self.hour + other_time.hour) - 24
        else:
            new_time.hour = self.hour + other_time.hour

        return new_time


def main():
    time1 = Time(23, 9, 30)
    print(time1)

    time2 = Time(4, 28, 30)
    print(time1 + time2)


main()
