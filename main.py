import os
import shutil

directory = r'C:\Feko Backup'
def items():
    return os.listdir(directory)

def numberOfItems(items):
    return len(items)

def copyItemsToDirectory():
    print("Copy items to new directory")

def checkItemsInFekoBackupDirectory():
    """
    items = os.listdir(r"\\192.168.1.133\Feko Backup")
    """
    items = os.listdir(r"C:\Users\opwikit\Desktop\Feko Backup")

    print(len(items))

    for item in items:
        print(item)

def checkNumberOfFiles(itemsNumber):

    if itemsNumber == 3:
        print("Perfect amount of files")
    elif itemsNumber > 3:
        print("Too many files")
        '''deleteFirstItem()'''
    elif itemsNumber < 3:
        print("Not enough files")

def copyFilesToDirectory(dstpath):
    src_path = r'C:\Feko Backup'
    dst_path = r"E:\demos\files\account\profit.txt"
    shutil.copy(src_path, dst_path)
    print('Copied')

if __name__ == '__main__':
    items = items()

    checkNumberOfFiles(numberOfItems(items))

    '''print("Number of items: " + str(itemsNumber))'''

    for item in items:
        print(item)

    print(directory + '\\' + items[0])


    '''def deleteFirstItem():
    # Get input.
    myfile = directory + '\\' + items[0]

    # Try to delete the file.
    try:
        os.remove(myfile)
        print("File deleted successfully")
    except OSError as e:
        # If it fails, inform the user.
        print("Error: %s - %s." % (e.filename, e.strerror))
        '''