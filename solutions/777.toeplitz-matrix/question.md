A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return&nbsp;True&nbsp;if and only if the matrix is Toeplitz.
&nbsp;

Example 1:


Input:
matrix = [
&nbsp; [1,2,3,4],
&nbsp; [5,1,2,3],
&nbsp; [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the&nbsp;diagonals are:
&quot;[9]&quot;, &quot;[5, 5]&quot;, &quot;[1, 1, 1]&quot;, &quot;[2, 2, 2]&quot;, &quot;[3, 3]&quot;, &quot;[4]&quot;.
In each diagonal all elements are the same, so the answer is True.


Example 2:


Input:
matrix = [
&nbsp; [1,2],
&nbsp; [2,2]
]
Output: False
Explanation:
The diagonal &quot;[1, 2]&quot; has different elements.



Note:


	matrix will be a 2D array of integers.
	matrix will have a number of rows and columns in range [1, 20].
	matrix[i][j] will be integers in range [0, 99].



Follow up:


	What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
	What if the matrix is so large that you can only load up a partial row into the memory at once?

