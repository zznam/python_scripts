class Tea:
    """Represents a cup of tea object """
    def __init__(self, name, origin):
        self._name = name
        self._origin = origin

    def getRecipe(self):
        return self._name

    def getOrigin(self):
        return self._origin


class MilkWrapper(Tea):
    """Use to add tea to our cups """
    def __init__(self, wrapped, volume):
        self._wrapped = wrapped
        self._volume = volume

    def getRecipe(self):
        return self._wrapped.getRecipe() + " + " + str(
            self._volume) + "ml Milk"

    def getOrigin(self):
        return self._wrapped.getOrigin()


class IceWrapper(Tea):
    """Use to add ice to our cups """
    def __init__(self, wrapped, percent):
        self._wrapped = wrapped
        self._percent = percent

    def getRecipe(self):
        return self._wrapped.getRecipe() + " + " + str(self._percent) + "% Ice"

    def getOrigin(self):
        return self._wrapped.getOrigin()


class SugarWrapper(Tea):
    """Use to add sugar to our cups """
    def __init__(self, wrapped, percent):
        self._wrapped = wrapped
        self._percent = percent

    def getRecipe(self):
        return self._wrapped.getRecipe() + " + " + str(
            self._percent) + "% Sugar"

    def getOrigin(self):
        return self._wrapped.getOrigin()


""" main method """

if __name__ == '__main__':

    # let's create a recipe for bubble tea
    # first let choose type of tea
    originCup = Tea("Black Tea", "Ha Giang")
    # then add some milk
    cupAfStep1 = MilkWrapper(originCup, 200)
    # then add some ice
    cupAfStep2 = IceWrapper(cupAfStep1, 30)
    # then specify that the recipe don't use sugar
    cupAfStep3 = SugarWrapper(cupAfStep2, 0)

    print("before :", originCup.getRecipe())
    print("after :", cupAfStep3.getRecipe())
    print("get tea origin :", cupAfStep3.getOrigin())
