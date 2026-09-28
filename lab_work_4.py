#array and matrix,2 by 2
import numpy as np
arr = np.array([[1,2],[3,4]])
print(arr)
#array and matrix,1by1 matrix
import numpy as np 
arr = np.array(42)
print(arr)
#array
import numpy as np 
arr = np.array([1,2])
print(arr)
#dimension of the matrix
import numpy as np 
arr = np.array(42)
print(arr.ndim)

import numpy as np 
arr = np.array([1,2])
print(arr.ndim)

#printing an element from defined array
import numpy as np
arr = np.array([[1,2],[2,3]])
print("this is the (0,0) element",arr[0][0])

#Addition of array
import numpy as np
arr = np.array([[1,2],[2,3]])
print("this is the (0,0) element",arr[0][0])

#printing the list of the elements  with respective indexes
import pandas as pd
a = [1,2,3,4]
myvar =pd.Series(a)
print(myvar)

#type of data
import numpy as np 
arr = np.array([1,2])
print(arr.dtype)

#inserting a .csv file
import pandas as pd
df = pd.read_csv("../Downloads/lab_work_4_CARS.csv")
print(df)





