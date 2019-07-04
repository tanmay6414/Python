import ftplib
import os

contents = []

def deletefile(ftp,file_name):
    try:
        ftp.delete(file_name)
        print ' File Deleted '
    except:
        print ' Error '

def deletefolder(ftp,folder_name):
    try:
        ftp.rmd(folder_name)
        print 'Folder Deleted.'
    except:
        print 'Error'


def rename(ftp,from_name,to_name):
    try:
        ftp.rename(from_name,to_name)
        print 'File Renamed.'
    except:
        print 'Error'

def newfolder(ftp,folder_name):
    try:
        ftp.mkd(folder_name)
        print 'Folder Created.'
        
    except:
        print 'Error'



def download(ftp,filename):
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
        print 'File Successfully Downloaded. Check The Program Directory.'
    except:
        print "Error"

ftp = ftplib.FTP("127.0.0.1")
ftp.login("mayur","mayur")

print ">> Successfully Connected With FTP Server.\n>> Connection Is Now Live."
print ">> Welcome To Filezilla FTP Server."

while 1==1:
    print '----------------------------------------------------'
    print '======================= Menu ======================='
    print '1. Upload'
    print '2. Download'
    print '3. Rename'
    print '4. Create A Folder'
    print '5. Delete Folder/File'
    print '6. Exit'
    print '----------------------------------------------------'
    choice = input('Enter Your Choice :-\n')
    
    if choice == 1:
        #directory = raw_input('Enter The Directory To Upload :-\n')
        file_name = raw_input('Enter The File Name :-\n')
        file = open(file_name ,'rb')                  # file to send
        ftp.storbinary('STOR ' + file_name , file)     # send the file
        file.close()                                    # close file and FTP
        ftp.quit()

    elif choice==2:
        directory = raw_input('Enter The Directory To Download :-\n')
        ftp.cwd(directory)
        contents = ftp.retrlines('LIST')
        file_name = raw_input('Enter The File Name :-\n')
        download(ftp,file_name)

    elif choice == 3:
        directory = raw_input('Enter The Directory Name :-\n')
        ftp.cwd(directory)
        contents = ftp.retrlines('LIST')
        from_name = raw_input('Enter The File Name To Be Renamed :-\n')
        to_name = raw_input('Enter The New File Name :-\n')
        rename(ftp,from_name,to_name)

    elif choice == 4:
        directory = raw_input('Enter The Directory Name :-\n')
        ftp.cwd(directory)
        folder_name = raw_input('Enter The New Folder Name :-\n')
        newfolder(ftp,folder_name)

    elif choice == 5:

        print '    1. Delete Folder \n    2. Delete File \n'

        subchoice = int(raw_input('Enter Your Choice :- \n'))
        directory = raw_input('Enter The Directory Name :-\n')
        ftp.cwd(directory)
        contents = ftp.retrlines('LIST')

        if subchoice == 1:
            
            folder_name = raw_input('Enter The Folder Name To Delete :-\n')
            deletefolder(ftp,folder_name)

        elif subchoice==2:
            
            file_name = raw_input('Enter The File Name To Delete :-\n')
            deletefile(ftp,file_name)

    elif choice==6:
        break

