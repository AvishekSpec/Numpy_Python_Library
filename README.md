**NumpyPython Library** 

<mark>Numpy</mark>

NumPy is a Python package that stands for ‘Numerical Python’. It is the core library for scientific computing, which contains a powerful n-dimensional array object.
Numpy array is a powerful N-dimensional array object which is in the form of rows and columns. We can initialize NumPy arrays from nested Python lists and access it elements.

<mark>Single dimensional array and Multi-dimensional array:</mark>

![image](https://github.com/user-attachments/assets/9be44f66-612b-4590-ac12-53d6a79703d8)


<mark>Numpy Operations</mark>

**1. Array Creation**
-	np.array(): Create an array from a list or tuple.
-	np.zeros(): Create an array filled with zeros.
-	np.ones(): Create an array filled with ones.
-	np.arange(): Create an array with a specified range.
-	np.linspace(): Create an array with evenly spaced values.
-	np.eye(): Create an identity matrix.
-	np.random.rand(): Create an array with random values (uniform distribution).
-	np.random.randint(): Create an array with random integers.

**2. Array Properties and Inspection**
-	array.shape: Get the shape of an array.
-	array.size: Get the total number of elements.
-	array.ndim: Get the number of dimensions.
-	array.dtype: Get the data type of elements.

**3. Array Reshaping and Transposing**
-	np.reshape(): Change the shape of an array.
-	array.T: Transpose an array (swap rows and columns).
-	np.ravel(): Flatten an array to 1D.

**4. Array Indexing and Slicing**
-	Indexing: Access elements using [row, column] syntax.
-	Slicing: Extract subarrays with array[start:stop] syntax.
-	Fancy Indexing: Access specific elements using lists of indices.
-	Boolean Indexing: Filter elements based on conditions.

**5. Mathematical Operations**
-	Arithmetic operations: +, -, *, / for element-wise operations.
-	np.add(), np.subtract(), np.multiply(), np.divide(): Element-wise operations as functions.
-	np.exp(): Exponential (e^x) of each element.
-	np.sqrt(): Square root of each element.
-	np.log(): Natural logarithm of each element.
-	np.sin(), np.cos(), np.tan(): Trigonometric functions.

**6. Aggregate Functions**
-	np.sum(): Sum of elements.
-	np.min(), np.max(): Minimum and maximum values.
-	np.mean(): Mean of elements.
-	np.median(): Median of elements.
-	np.std(), np.var(): Standard deviation and variance.
-	np.argmin(), np.argmax(): Index of min and max values.

**7. Linear Algebra Operations**
-	np.dot(): Dot product of two arrays.
-	np.linalg.inv(): Inverse of a matrix.
-	np.linalg.det(): Determinant of a matrix.
-	np.linalg.eig(): Eigenvalues and eigenvectors.
-	np.linalg.norm(): Norm (e.g., Euclidean distance).

**8. Random Number Generation**
-	np.random.rand(): Generate random values (uniform distribution).
-	np.random.randn(): Generate random values (normal distribution).
-	np.random.randint(): Generate random integers.
-	np.random.choice(): Randomly select elements.
-	np.random.shuffle(): Shuffle elements.

**9. Set Operations**
-	np.unique(): Find unique elements in an array.
-	np.intersect1d(): Intersection of two arrays.
-	np.union1d(): Union of two arrays.
-	np.setdiff1d(): Difference of two arrays.

**10. Array Manipulation**
-	np.concatenate(): Concatenate arrays along a specific axis.
-	np.vstack(), np.hstack(): Stack arrays vertically or horizontally.
-	np.split(): Split an array into multiple parts.
-	np.resize(): Resize an array.

**ndim, itemsize & dtype**

![image](https://github.com/user-attachments/assets/adc1d602-392c-4744-9f5a-7918ec7a303c)
 
**Reshaping**

![image](https://github.com/user-attachments/assets/2a847f3b-f1bd-4348-b2dd-3b4100c319e1)

![image](https://github.com/user-attachments/assets/029dc48a-e8de-4d8a-bd32-8174860118f5)


**Slicing**

![image](https://github.com/user-attachments/assets/666dbe08-b4ad-4230-ad18-b322a41eaf5a)

**Explanation:**
Here, the colon (:) in a[0:, 2] selects all rows starting from row 0.
The 2 after the comma specifies column 2.So, a[0:, 2] retrieves the third element (index 2) from each row.

When you use b[0:2, 3], here's how each part is interpreted:
1.	0:2 (Rows): Selects rows starting from index 0 up to, but not including, index 2—so it includes rows 0 and 1 only.
2.	3 (Column): Specifies column 3 for each selected row.
So, a[0:2, 3] means:
-	Select rows 0 and 1.
-	Within these rows, select the element at column 3.

**Linespace**
-	returns evenly spaced numbers over a specified interval

![image](https://github.com/user-attachments/assets/afead951-10b0-43bd-b978-e061a3abfe04)

**Min/Max**

![image](https://github.com/user-attachments/assets/6725e324-10ec-4c3f-a2a0-6f508f9d1954)

**Standard Deviation & Square Root**

![image](https://github.com/user-attachments/assets/f01ed759-1d28-4afb-91de-5c8fbc7cf952)

**Mathematical Operation**

![image](https://github.com/user-attachments/assets/8019155c-c2aa-44ba-9759-a57abbe86ccc)
 

