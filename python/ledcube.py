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
        x, y, z, b= self.create_cube(n)
        self.n = n
        self.brightness = b
        self.x = x
        self.y = y
        self.z = z

    def show(self):
        """
        Description:
            Method that diplays the object using matplot.
        """
        plt.style.use('_mpl-gallery')

        # Plot
        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
        ax.scatter(self.x, self.y, self.z,c = self.brightness)

        ax.set(xticklabels=[],
        yticklabels=[],
        zticklabels=[])

        plt.show()

    def create_cube(self, n):
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

        b = []
        for i in range(n**3):
            b.append(0)

        return x, y, z, b

    def change_led(self, led_xyz, brightness):
        """
        Description:
            Changes one of the desired leds accessed like a numpy matrix. 
            Assumes a valid location is chosen.
        Param:
            led_xyz - tuple containing the xyz location of the led to change. Ex: (x, y, z).
            brightness - to set the led to. 0 = off, 1 = max.
        Returns:
            Changes the brightness of the specified led.
        """
        x, y, z = led_xyz

        possible_x_index = []
        for index, entry in enumerate (self.x):
            if entry == x:
                possible_x_index.append(index)

        possible_y_index = []
        for index, entry in enumerate (self.y):
            if entry == y:
                possible_y_index.append(index)
        
        possible_z_index = []
        for index, entry in enumerate (self.z):
            if entry == z:
                possible_z_index.append(index)
        
        for index in possible_x_index:
            if index in possible_y_index and index in possible_z_index:
                cube_index = index

        self.brightness[cube_index] = brightness
