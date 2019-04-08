import numpy as np


class AlgorithmChapter2(object):
    def __init__(self):
        pass

    @staticmethod
    def algorithm_2_2(A):
        n = len(A)
        P, L, U = [np.eye(n), np.eye(n), np.zeros((n, n))]

        for i in range(n - 1):

            m = np.argmax(np.abs(A[i:, i])) + i

            if A[m, i] == 0:
                raise ValueError("matrix is singular.")
            else:
                if m != i:
                    A[[i, m], :] = A[[m, i], :]
                    P[[i, m], :] = P[[m, i], :]
                for j in range(i + 1, n):
                    L[j, i] = A[j, i] / A[i, i]
                    A[j, i] = A[j, i] / A[i, i]

                for j in range(i, n):
                    U[i, j] = A[i, j]

                for j in range(i + 1, n):
                    for k in range(i + 1, n):
                        A[j, k] -= L[j, i] * U[i, k]

        P = P.T
        L = np.tril(A, -1) + np.eye(n)
        U[-1, -1] = A[-1, -1]
        return A, P, L, U

    @staticmethod
    def algorithm_2_3(A):
        n = len(A)
        P = np.eye(n)

        for i in range(n - 1):

            m = np.argmax(np.abs(A[i:, i])) + i

            if A[m, i] == 0:
                raise ValueError("matrix is singular.")
            else:
                if m != i:
                    A[[i, m], :] = A[[m, i], :]
                    P[[i, m], :] = P[[m, i], :]

                for j in range(i + 1, n):
                    A[j, i] = A[j, i] / A[i, i]

                for j in range(i + 1, n):
                    for k in range(i + 1, n):
                        A[j, k] -= A[j, i] * A[i, k]

        P = P.T
        L = np.tril(A, -1) + np.eye(n)
        U = np.triu(A, 0)
        return A, P, L, U

    @staticmethod
    def algorithm_2_4(A):
        n = len(A)
        P = np.eye(n)

        for i in range(n - 1):

            m = np.argmax(np.abs(A[i:, i])) + i

            if A[m, i] == 0:
                raise ValueError("matrix is singular.")
            else:
                if m != i:
                    A[[i, m], :] = A[[m, i], :]
                    P[[i, m], :] = P[[m, i], :]

                A[(i + 1):, i] = A[(i + 1):, i] / A[i, i]
                A[(i + 1):, (i + 1):] -= A[(i + 1):, i][:, None] * A[i, (i + 1):]

        P = P.T
        L = np.tril(A, -1) + np.eye(n)
        U = np.triu(A, 0)
        return A, P, L, U

    @staticmethod
    def test(algorithm, A=None, random=False):
        if A is None:
            if random:
                A = np.random.rand(5, 5)
            else:
                A = np.array([[4, 2, 1, 5], [8, 7, 2, 10], [4, 8, 3, 6], [6, 8, 4, 9]], dtype=float)
        elif not isinstance(A, np.ndarray):
            raise ValueError('vararg input is not a n-by-n matrix.')
        elif len(A) != len(A[0]):
            raise ValueError('vararg input is not a n-by-n matrix.')

        print('A_0 = \n', A)
        A, P, L, U = algorithm(A)
        print('A = \n', A)
        print('P = \n', P)
        print('L = \n', L)
        print('U = \n', U)
        print('Check = \n', P.dot(L.dot(U)))


if __name__ == '__main__':
    obj = AlgorithmChapter2()
    obj.test(algorithm=obj.algorithm_2_2)
    obj.test(algorithm=obj.algorithm_2_3)
    obj.test(algorithm=obj.algorithm_2_4)
