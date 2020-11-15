import os
def soldier(directery,filename,filetype):
    os.chdir(directery)
    files=os.listdir(directery)
    i=1
    with open(filename) as f:
        filelists=f.read().split('\n')

    for file in files:

        if file not in filelists:
            os.rename(file,file.capitalize())

        if os.path.splitext(file)[1] == filetype:
            os.rename(file,f'{i}{filetype}')
            i+=1

soldier(r'C:\xyz',r'C:\Users\rajma\PycharmProjects\tuts\ext.txt','.png')