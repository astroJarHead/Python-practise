"""

An object oriented path management program

>>> import sharePath
Instantiate a sharePath object as pm
>>> pm = sharePath.sharePath()
>>> help(pm)
... the help on this was returned :)
>>>

>>> pm.get_path()
'/mnt/nofs/projects/gaiaWds/WDS_Gaia-main/test-code'
>>> sharePath.function_a(pm)
Function A is using the path:
  /mnt/nofs/projects/gaiaWds/WDS_Gaia-main/test-code
>>> sharePath.function_b(pm)
Function B is using the path:
  /mnt/nofs/projects/gaiaWds/WDS_Gaia-main/test-code

Son-of-a-gun, this works!

Or:

>>> from sharePath import *
>>> pm = sharePath()
>>> function_a(pm)
Function A is using the path:
     /mnt/nofs/projects/gaiaWds/WDS_Gaia-main/test-code

Or:

>>> import sharePath
Pass in a sharePath object instantiating it via the argument to
the function function_a and it looks like a method:
>>> sharePath.function_a(sharePath.sharePath())
Function A is using the path:
     /mnt/nofs/projects/gaiaWds/WDS_Gaia-main/test-code

"""
import os


class sharePath:
    def __init__(self):
        self.shared_path = os.getcwd()

    def set_path(self, path):
        self.shared_path = os.getcwd()

    def get_path(self):
        return self.shared_path


# Example functions interacting with PathManager
def function_a(path_manager):
    path = path_manager.get_path()
    print(f"Function A is using the path: {path}")
    pathy_string = 'Function A is using the path: '+path
    with open(path+'/example.txt', 'w') as file:
        file.write(pathy_string)


def function_b(path_manager):
    path = path_manager.get_path()
    print(f"Function B is using the path: {path}")


# Main part of the code
if __name__ == "__main__":
    # Create an instance of class sharePath
    path_manager = sharePath()
    # Set the shared path
    # path_manager.set_path("/mnt/nofs/projects/gaiaWds/WDS_Gaia-main/test-code")
    # set an arbitrary path in the current working directory
    path_manager.set_path()

    # The user can now call function_a and function_b as needed
    # Example of how the user would call these functions:
    # function_a(path_manager)
    # function_b(path_manager)
