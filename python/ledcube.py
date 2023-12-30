# Pick a n for an nxnxn cube
import numpy as np
import matplotlib.pyplot as plt
class LedCube:
    def __init__(self, n):
        """
        Description:
            Constructor that creates an led cube object that is nxnxn.
        Parameters:
            n - int that defines the size of the cube (nxnxn).
        Returns:
            An LedCube object.
        """
        x, y, z = self.create_xyz(n)
        self.n = n
        self.x = x
        self.y = y
        self.z = z

    def view(self):
        """
        Description:
            Method that diplays the object using matplot.
        """
        plt.style.use('_mpl-gallery')

        # Assign the plot values
        xs = self.x
        ys = self.y
        zs = self.z

        # Assign the color
        color = np.ones(self.n**3)

        # Plot
        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
        ax.scatter(xs, ys, zs,c = color)

        ax.set(xticklabels=[],
        yticklabels=[],
        zticklabels=[])

        plt.show()

    def create_xyz(self, n):
        """
        Description: 
            Creates a matrix of a nxnxn cube suitable for maatplot 3d.
        Param:
            n.
        Return:
            x,y,z - arrays containing encoddings

        """
        """
        Description: 
            Populates the x values of an array of nxnxn for matplot.
        Return:
            x - array containing values
        """
        #Populate an x array
        x = []
        index_of_interest = -1
        count = 1
        for index in range(n**3):
            # if the index has reached 
            if (index)%(n**2) == 0:
                index_of_interest += 1

            x.append(index_of_interest)
            #print(f"count: {count}, index_of_interest: {index_of_interest}, \n")
            count += 1
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
        for index in range(n**3):
            if (index) % (n) == 0:
                index_of_interest += 1
            if (index)%(n**2) == 0:
                index_of_interest = 0
            y.append(index_of_interest)
            #print(f"count: {count}, index_of_interest: {index_of_interest}, \n")
            count += 1
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
        for index in range(n**3):
            if (index) % (n) == 0:
                index_of_interest = 0

            z.append(index_of_interest)
            #print(f"count: {count}, index_of_interest: {index_of_interest}, \n")
            
            count += 1
            index_of_interest += 1

        return x, y, z

    def change_led(x_a,y_a,z_a, x,y,z):
        """
        Description:
            Changes one of the desired leds accessed like a numpy matrix.
        Param:

        """