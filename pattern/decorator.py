# https://www.geeksforgeeks.org/decorator-method-python-design-patterns/

# Advantages
# Single Responsibility Principle
# Runtime Responsibilities
# SubClassing

# Disadvantages
# Removing Wrapper hard
# Complicated Decorators
# Ugly Configuration

# Applicability
# Incapable Inheritance
# Runtime Assignment


class WrittenText:
    """Represents a Written text """
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class UnderlineWrapper(WrittenText):
    """Wraps a tag in <u>"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<u>{}</u>".format(self._wrapped.render())


class ItalicWrapper(WrittenText):
    """Wraps a tag in <i>"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())


class BoldWrapper(WrittenText):
    """Wraps a tag in <b>"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())


""" main method """

if __name__ == '__main__':

    before_gfg = WrittenText("GeeksforGeeks")
    temp1 =  BoldWrapper(before_gfg)
    temp2 =  UnderlineWrapper(temp1)
    after_gfg =  ItalicWrapper(temp2)
    # after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg)))

    print("before :", before_gfg.render())
    print("after :", after_gfg.render())
