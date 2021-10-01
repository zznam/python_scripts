# Given a FileUtils class with statics methods:
# - listFiles(directory):  List<String> - return list of absolute path to all files in the directory
# - isDir(absolutePath): Boolean - return if the path is a directory/folder.
# - baseName(absoluteFilePath): String - return name of the file without the path.

# Complete the following function in any programming language:

# traverseDirectory(absolutePath, level): traverse the folder and subfolders (with level depth limit) and print out the files following the format in the following example:

# traverseDirectory("/home/user/awesome_user", 3)

# return:

# - file_a
# - file_b
# - file_c
# - sub_folder_level_1/
#   - file_a
#   - file_b
#   - file_c
#   - sub_folder_level_2
#     - file_a
#     - file_b
#     - sub_folder_level_3
#       - file_a
#       - file_b
#       - sub_folder_level_4/
#   - another_sub_folder_level_2/
#     - another_sub_folder_level_3
# - file_d 
# - file_e
# - another_sub_folder_level_1/
#   - file_a
#   - file_b
# Writing additional functions is allowed.

class FileUtils:
    def listFiles():
        pass
    def baseName():
        pass
    def isDir():
        pass

def traverseDirectory(absolutePath, level):
    traverseHelper(absolutePath, level, level)
        
def traverseHelper(absolutePath, level, baseLevel):
    fileUtils = FileUtils()
    l = fileUtils.listFiles(absolutePath)
    for file in l:
      if fileUtils.isDir(file):
          print(" " * (baseLevel-level) + "- " + fileUtils.baseName(file) +"/")
          if (level > 0): traverseHelper(file, level - 1, baseLevel)
      else:
        print(" " * (baseLevel-level) + "- " + fileUtils.baseName(file))