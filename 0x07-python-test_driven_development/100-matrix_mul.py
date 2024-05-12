#!/usr/bin/python3
"""
a function that multiplies 2 matrices
"""
def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        list of lists: Resulting matrix after multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, or if an element in the list of lists is not an integer or float.
        ValueError: If m_a or m_b is empty, or if the matrices cannot be multiplied.

    """
    # Validate input matrices
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    
    if not all(isinstance(val, (int, float)) for row in m_a for val in row) or not all(isinstance(val, (int, float)) for row in m_b for val in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    
    # Check if matrices can be multiplied
    cols_a = len(m_a[0])
    rows_b = len(m_b)
    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Initialize result matrix
    result = [[0] * len(m_b[0]) for _ in range(len(m_a))]
    
    # Perform matrix multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    
    return result
