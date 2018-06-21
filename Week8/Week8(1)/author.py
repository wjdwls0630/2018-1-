def get_the_name(file) :
    file_name=open(file,'r')
    first=file_name.readline()
    author, name = first.split()
    file_name.close()
    return name

def all_author_name(L) :
    result=set()
    for i in L :
        name=get_the_name(i)
        result.add(name)

    return result

if __name__ == "__main__" :
    files=input()
    list_file=files.split()
    print(all_author_name(list_file))
