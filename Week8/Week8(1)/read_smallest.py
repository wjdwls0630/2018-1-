import time_series

def smallest_value(reader):
    """ (file open for reading) -> NoneType
    Read and process reader and return the smallest value after the
    time_series header.
    """
    
    line = time_series.skip_header(reader).strip()
    
    # Now line contains the first data value; this is also the smallest value
    # found so far, because it is the only one we have seen.
    smallest = int(line)
    
    for line in reader:
        if line.isdigit() :
            value = int(line.strip())
            smallest = min(smallest, value)







    return smallest


if __name__ == '__main__':
    input_file =  open('hopedale.txt', 'r')
    print(smallest_value(input_file))
    input_file.close()


    
