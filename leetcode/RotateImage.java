class Solution {
    /* in-place rotate : (i,j) -> (j, N - 1 - i)
     * 1. transpose : (i, j) -> (j, i)
     * 2. symmetric transposition(대칭 이동)
     *    reverse columns through swap i-th col & (N-1-i)th col
     *    i.e. (j, i) -> (j, N - 1 - i)
     */
    public void rotate(int[][] matrix) {
        transpose(matrix);
        reverseColumns(matrix);
    }

    // This is not the answer
    public void rotateNotInPlace(int[][] matrix) {
        int rows = matrix.length;
        int[][] ret = new int[rows][rows];

        for(int i=0; i < rows; i++) {
            for(int j=0; j < rows; j++) {
                ret[j][rows - 1 - i] = matrix[i][j];
            }
        }

        for(int i=0; i < rows; i++) {
            for(int j=0; j < rows; j++) {
                matrix[i][j] = ret[i][j];
            }
        }
    }

    private void transpose(int[][] matrix) {
        int rows = matrix.length;
        int tmp;
        for(int i=0; i < rows; i++) {
            for(int j=i+1; j < rows; j++) {
                tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        }
    }

    private void reverseColumns(int[][] matrix) {
        int N = matrix.length;
        int tmp;
        for(int j=0; j < N/2; j++) {
            int symmetric_col = N - 1 - j;
            for(int i=0; i < N; i++) {
                tmp = matrix[i][j];
                matrix[i][j] = matrix[i][symmetric_col];
                matrix[i][symmetric_col] = tmp;
            }
        }
    }
}

class RotateImage {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] input = {{1,2},{3,4}};
        int[][] output = {{3,1},{4,2}};
        sol.rotate(input);
        printMatrix(input);
        System.out.println(testEqual(input, output));

        int[][] input2 = {{1,2,3},{4,5,6},{7,8,9}};
        int[][] output2 = {{7,4,1},{8,5,2},{9,6,3}};
        sol.rotate(input2);
        printMatrix(input2);
        System.out.println(testEqual(input2, output2));
    }

    private static void printMatrix(int[][] x) {
        int rows = x.length;
        for(int i=0; i < rows; i++) {
            for(int j=0; j < rows; j++) {
                System.out.println(String.format("%d, %d: %d", i, j, x[i][j]));
            }
        }
    }

    private static boolean testEqual(int[][] x, int[][] y) {
        int rows = x.length;
        for(int i=0; i < rows; i++) {
            for(int j=0; j < rows; j++) {
                if(x[i][j] != y[i][j]) {
                    System.out.println(String.format("%d, %d", x[i][j], y[i][j]));
                    return false;
                }
            }
        }

        return true;
    }
}
