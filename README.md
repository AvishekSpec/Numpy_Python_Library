# Numpy_Python_Library

Numpy
NumPy is a Python package that stands for ‘Numerical Python’. It is the core library for scientific computing, which contains a powerful n-dimensional array object.
Numpy array is a powerful N-dimensional array object which is in the form of rows and columns. We can initialize NumPy arrays from nested Python lists and access it elements.

Single dimensional array and Multi-dimensional array:
 

Numpy Operations

1. Array Creation
-	np.array(): Create an array from a list or tuple.
- np.zeros(): Create an array filled with zeros.
- np.ones(): Create an array filled with ones.
•	np.arange(): Create an array with a specified range.
•	np.linspace(): Create an array with evenly spaced values.
•	np.eye(): Create an identity matrix.
•	np.random.rand(): Create an array with random values (uniform distribution).
•	np.random.randint(): Create an array with random integers.

3. Array Properties and Inspection
•	array.shape: Get the shape of an array.
•	array.size: Get the total number of elements.
•	array.ndim: Get the number of dimensions.
•	array.dtype: Get the data type of elements.

5. Array Reshaping and Transposing
•	np.reshape(): Change the shape of an array.
•	array.T: Transpose an array (swap rows and columns).
•	np.ravel(): Flatten an array to 1D.

7. Array Indexing and Slicing
•	Indexing: Access elements using [row, column] syntax.
•	Slicing: Extract subarrays with array[start:stop] syntax.
•	Fancy Indexing: Access specific elements using lists of indices.
•	Boolean Indexing: Filter elements based on conditions.

9. Mathematical Operations
•	Arithmetic operations: +, -, *, / for element-wise operations.
•	np.add(), np.subtract(), np.multiply(), np.divide(): Element-wise operations as functions.
•	np.exp(): Exponential (e^x) of each element.
•	np.sqrt(): Square root of each element.
•	np.log(): Natural logarithm of each element.
•	np.sin(), np.cos(), np.tan(): Trigonometric functions.

10. Aggregate Functions
•	np.sum(): Sum of elements.
•	np.min(), np.max(): Minimum and maximum values.
•	np.mean(): Mean of elements.
•	np.median(): Median of elements.
•	np.std(), np.var(): Standard deviation and variance.
•	np.argmin(), np.argmax(): Index of min and max values.

11. Linear Algebra Operations
•	np.dot(): Dot product of two arrays.
•	np.linalg.inv(): Inverse of a matrix.
•	np.linalg.det(): Determinant of a matrix.
•	np.linalg.eig(): Eigenvalues and eigenvectors.
•	np.linalg.norm(): Norm (e.g., Euclidean distance).

12. Random Number Generation
•	np.random.rand(): Generate random values (uniform distribution).
•	np.random.randn(): Generate random values (normal distribution).
•	np.random.randint(): Generate random integers.
•	np.random.choice(): Randomly select elements.
•	np.random.shuffle(): Shuffle elements.

13. Set Operations
•	np.unique(): Find unique elements in an array.
•	np.intersect1d(): Intersection of two arrays.
•	np.union1d(): Union of two arrays.
•	np.setdiff1d(): Difference of two arrays.

14. Array Manipulation
•	np.concatenate(): Concatenate arrays along a specific axis.
•	np.vstack(), np.hstack(): Stack arrays vertically or horizontally.
•	np.split(): Split an array into multiple parts.
•	np.resize(): Resize an array.










ndim, itemsize & dtype
 

Reshaping
 
 

Slicing
 
Explanation:
Here, the colon (:) in a[0:, 2] selects all rows starting from row 0.The 2 after the comma specifies column 2.So, a[0:, 2] retrieves the third element (index 2) from each row.
When you use b[0:2, 3], here's how each part is interpreted:
1.	0:2 (Rows): Selects rows starting from index 0 up to, but not including, index 2—so it includes rows 0 and 1 only.
2.	3 (Column): Specifies column 3 for each selected row.
So, a[0:2, 3] means:
•	Select rows 0 and 1.
•	Within these rows, select the element at column 3.




Linespace
•	returns evenly spaced numbers over a specified interval
 
Min/Max
 
Standard Deviation & Square Root
 
Mathematical Operation
 

Python Numpy Special Functions
There are various special functions available in numpy such as sine, cosine, tan, log etc. First, let’s begin with sine function where we will learn to plot its graph. 
For that, we need to import a module called matplotlib. Moving ahead with python numpy tutorial, let’s see how these graphs are plotted.

 
 
Solution
 
 



Using tan function
 
