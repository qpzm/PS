class Solution {
    // Q. How to rotate in-place?
    public void rotate(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int[][] ret = new int[rows][cols];

        for(int i=0; i < rows; i++) {
            for(int j=0; j < cols; j++) {
                ret[j][rows - 1 - i] = matrix[i][j];
            }
        }

        for(int i=0; i < rows; i++) {
            for(int j=0; j < cols; j++) {
                matrix[i][j] = ret[i][j];
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
