# Pick a n for an nxnxn cube

def populate_x(n):
    """
    Description: 
        Populates the x values of an array of nxnxn for matplot.
    Param:
        n.
    Return:
        x - array containing values
    """
    #Populate an x array
    x = []
    index_of_interest = -1
    count = 1
    for index in range(n*n*n):
        # if the index has reached 
        if (index)%(n*n) == 0:
            index_of_interest += 1

        x.append(index_of_interest)
        #print(f"count: {count}, index_of_interest: {index_of_interest}, \n")
        count += 1
    return x

def populate_y(n):
    """
    Description: 
        Populates the y values of an array of nxnxn for matplot.
    Param:
        n.
    Return:
        y - array containing values
    """
    # Populate a y array
    y = []
    index_of_interest = -1
    count = 1  
    for index in range(n*n*n):
        if (index) % (n) == 0:
            index_of_interest += 1
        if (index)%(n*n) == 0:
            index_of_interest = 0
        y.append(index_of_interest)
        #print(f"count: {count}, index_of_interest: {index_of_interest}, \n")
        count += 1
    return y

def populate_z(n):
    """
    Description: 
        Populates the z values of an array of nxnxn for matplot.
    Param:
        n.
    Return:
        z - array containing values
    """

    # Populate z array
    z = []
    index_of_interest = -1
    count = 1  
    for index in range(n*n*n):
        if (index) % (n) == 0:
            index_of_interest = 0

        z.append(index_of_interest)
        #print(f"count: {count}, index_of_interest: {index_of_interest}, \n")
        
        count += 1
        index_of_interest += 1

    return z


def create_cube(n):
    """
    Description: 
        Creates a matrix of a nxnxn cube suitable for maatplot 3d.
    Param:
        n.
    Return:
        x,y,z - arrays containing encoddings
    """
    return populate_x(n), populate_y(n), populate_z(n)