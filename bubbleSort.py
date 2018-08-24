def bubbleSort( lst ):
    '''
    sorts the elements in the list passed as parameter using the traditional bubble sort
    parameter:
        lst - list of elements (list)
    return:
        newlst - sorted list (list)
    '''
    newlst = []
    for idx in range( len( lst )):
        smallest = 1000
        for element in lst:
            if element <= smallest:
                smallest = element
        lst.remove( smallest )
        newlst.append( smallest )
    return newlst

