# https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/

'''
Managing a database connection
Global point access to writing log messages
File Manager
Print spooler
'''
class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


singleton = SingletonClass()
new_singleton = SingletonClass()

print(singleton is new_singleton)

singleton.singl_variable = "Singleton Variable"
print(new_singleton.singl_variable)
