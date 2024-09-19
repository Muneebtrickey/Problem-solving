"""
# finding the size of a directory 

so this we are interacting with the system so for this we will will the os module which help us to interact
with the operating system. 

so we will be using 4 main function for this task :
 1. os.path.getsize(path) -> which will return the size of directory
 2. os.path.isdir(path) -> this is will  check if the 
                           is a directory or not 

3. os.listdir(path) -> this will return the list of directory within the path 

4. os.path.join(path,filename) -> this function compose the path and the filename. 
for example :     /file/course , /khan so it combine this

/file/course/khan   . 



"""
import os

def disk_usage(path):

    total = os.path.getsize(path) # return size in bytes

    # now we will check that if the current path is a 
    # directory if it is so will also return the size of 
    # its directories

    if os.path.isdir(path): # checking the path is directory or not 
        # if the path is a directory so will return the 
        # the list of all the directory

        for filename in os.listdir(path): # return list of directory
            # we will combine the file with the path so
            # so that we calculate the size of the file
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    print ( "{0:<7}" .format(total), path)
    return total


path = r"C:\Users\muni1\Downloads\Dhr_v T_me M_nag_ent"

print(disk_usage(path))  # 7940083222
