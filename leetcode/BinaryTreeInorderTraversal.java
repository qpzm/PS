import java.util.List;
import java.util.ArrayList;

class BinaryTreeInorderTraversal {
    public List<Integer> inorderTraversal(TreeNode root) {
        if(root == null) {
            return new ArrayList<Integer>();
        }
        List<Integer> left = inorderTraversal(root.left);
        List<Integer> right = inorderTraversal(root.right);
        left.add(root.val);
        left.addAll(right);
        return left;
    }
}
