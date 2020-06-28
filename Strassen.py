def matrix_plus(A, B):
    length = len(A)
    C = [[0 for i in range(length)] for j in range(length)]
    for i in range(length):
        for j in range(length):
            C[i][j] = A[i][j] + B[i][j]
    return C

def matrix_sub(A, B):
    length = len(A)
    C = [[0 for i in range(length)] for j in range(length)]
    for i in range(length):
        for j in range(length):
            C[i][j] = A[i][j] - B[i][j]
    return C

def combine(A11, A12, A21, A22):
    length = (int)(2*len(A11))
    half = len(A11)
    A = [[0 for i in range(length)] for j in range(length)]
    for i in range(length):
        for j in range(length):
            if i < half and j < half:
                A[i][j] = A11[i][j]
            elif i < half and j >= half:
                A[i][j] = A12[i][j-half]
            elif i >= half and j < half:
                A[i][j] = A21[i-half][j]
            else:
                A[i][j] = A22[i-half][j-half]
    return A


def split_to_4(A):
    half = (int)(len(A)/2)
    A11 = [[0 for i in range(half)] for j in range(half)]
    A12 = [[0 for i in range(half)] for j in range(half)]
    A21 = [[0 for i in range(half)] for j in range(half)]
    A22 = [[0 for i in range(half)] for j in range(half)]
    for i in range(len(A)):
        for j in range(len(A)):
            if i < half and j < half:
                A11[i][j] = A[i][j]
            elif i < half and j >= half:
                A12[i][j-half] = A[i][j]
            elif i >= half and j < half:
                A21[i-half][j] = A[i][j]
            else:
                A22[i-half][j-half] = A[i][j]
    return A11, A12, A21, A22

def strassen(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    if n == 1:
        C[0][0] = A[0][0]*B[0][0]
    else:
        A11, A12, A21, A22 = split_to_4(A)
        B11, B12, B21, B22 = split_to_4(B)
        S1 = matrix_sub(B12, B22)
        S2 = matrix_plus(A11, A12)
        S3 = matrix_plus(A21, A22)
        S4 = matrix_sub(B21, B11)
        S5 = matrix_plus(A11, A22)
        S6 = matrix_plus(B11, B22)
        S7 = matrix_sub(A12, A22)
        S8 = matrix_plus(B21, B22)
        S9 = matrix_sub(A11, A21)
        S10 = matrix_plus(B11, B12)
        
        P1 = strassen(A11, S1)
        P2 = strassen(S2, B22)
        P3 = strassen(S3, B11)
        P4 = strassen(A22, S4)
        P5 = strassen(S5, S6)
        P6 = strassen(S7, S8)
        P7 = strassen(S9, S10)

        C11, C12, C21, C22 = split_to_4(C)
        res = matrix_plus(P5, P4)
        res = matrix_sub(res, P2)
        res = matrix_plus(res, P6)
        C11 = res

        C12 = matrix_plus(P1, P2)

        C21 = matrix_plus(P3, P4)

        res = matrix_plus(P5, P1)
        res = matrix_sub(res, P3)
        res = matrix_sub(res, P7)
        C22 = res

        C = combine(C11, C12, C21, C22)
    return C



if __name__ == "__main__":
    A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    B = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
    C = strassen(A, B)
    print(C)