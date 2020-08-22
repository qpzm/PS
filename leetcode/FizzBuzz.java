import java.util.List;
import java.util.ArrayList;

class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> arr = new ArrayList<String>();
        for(int i=1; i <= n; i++) {
            arr.add(_fizzBuzz(i));
        }
        return arr;
    }

    private String _fizzBuzz(int n) {
        String ret = "";
        if(n % 3 == 0) {
            ret += "Fizz";
        }
        if (n % 5 == 0) {
            ret += "Buzz";
        }
        return ret == "" ? String.valueOf(n) : ret;
    }
}