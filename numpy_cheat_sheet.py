'''

The NumPy library is the core library for scientific computing in Python. It provides a
high-performance multidimensional array object, and tools for working with these arrays.

'''

import numpy as np

# creating arrays
#a = np.array([1,2,3])
#b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
#c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]],dtype = float)

# initial placeholders
#array = np.zeros((3, 4))
#array = np.ones((2,3,4),dtype=np.int16)
#array = np.arange(10, 25, 5)
#array = np.linspace(0,2,50)
#array = np.full((2, 2), 7)
#array = np.eye(8)
#array = np.random.random((2, 2))
#array = np.empty((3, 2))

#IO
#np.save('my_array', a)
#np.savez('array.npz', a, b)
#np.load('my_array.npy')
#np.loadtxt("myfile.txt")
#np.genfromtxt("my_file.csv", delimiter=',')
#np.savetxt("myarray.txt", a, delimiter=" ")


#data types
np.int64    #Signed 64-bit integer types
np.float32  #Standard double-precision floating point
np.complex  #Complex numbers represented by 128 floats
np.bool     #Boolean type storing TRUE and FALSE values
np.object   #Python object type
np.string_  #Fixed-length string type
np.unicode_ #Fixed-length unicode type



#array = np.array([(1.5,2,3), (4,5,6)], dtype = float)

#print(array.shape)    #Array dimensions
#print(len(array))     #Length of array
#print(array.ndim)     #Number of array dimensions
#print(array.size)     #Number of array elements
#print(array.dtype)    #Data type of array elements
#print(array.dtype.name)  #Name of data type
#print(array.astype(int)) #Convert an array to a different type

# we can apply arithmatic operations like -,+ and other functions like np.exp(), np.cos() and etc on numpy arrays

# comparison

#a = np.array([(1,5,3),(8,7,9)],dtype=int)
#b = np.array([(1,7,1),(8,9,3)],dtype=int)

#a == b   #array([[False,  True,  True], [False, False, False]], dtype=bool)

#a < 2    #array([True, False, False], dtype=bool) >> > np.array_equal(a, b)

#np.array_equal(a, b)

#aggregate functions

#a = np.array([(1,5,3),(8,7,9)],dtype=int)

#a.sum()                     #Array-wise sum
#a.min()                     #Array-wise minimum value
#b.max(axis=0)               #Maximum value of an array row
#b.cumsum(axis=1)            #Cumulative sum of the elements
#a.mean()                    #Mean
#b.median()                  #Median
#a.corrcoef()                #Correlation coefficient
#np.std(b)                   #Standard deviation

# copying arrays

#a = np.array([(1,5,3),(8,7,9)],dtype=int)

#h = a.view()     #Create a view of the array with the same data
#b = np.copy(a)       #Create a copy of the array
#h = a.copy()     #Create a deep copy of the array

# sorting arrays
#a.sort()
#c.sort(axis=0)

# subsetting, slicing, indexing
#a[2]
#b[1,2]
#a[0:2] # return elements of 0 and 1
#b[0:2,1]
#b[:1]
#a[a>2]  # Boolean Indexing
#a[[0, 0, 1, 1],[0, 1, 1, 2]]  # fancy indexing  = [a[0,0], a[0,1], a[1,1], a[1,2]]

#a = np.transpose(b) #Transposing Array
#a.T                 #Transposing Array

#b.ravel() #Flatten the array
#g.reshape(3, -2)  #reshape but dont change data

#h.resize((2,6)) # Return a new array with shape (2,6)
#np.append(h,g)
#np.insert(a, 1, 5)
#np.delete(a,[1])

#np.concatenate((a,d),axis=0)
#np.vstack((a, b)) # Stack arrays vertically (row-wise)
#np.r_[e, f] #  Stack arrays vertically (row-wise)
#np.hstack((e, f)) # Stack arrays horizontally (column-wise)
#np.column_stack((a,d)) #Create stacked column-wise arrays
#np.c_[a,d] # Create stacked column-wise arrays

#np.hsplit(a, 3) #Split the array horizontally at the 3rd index
#np.vsplit(c, 2) #Split the array vertically at the 2nd index
