package p10799

import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

internal class MainKtTest {
    @Test
    fun solveExample1() {
        val input = "()(((()())(())()))(())"
        assertEquals(17, solve(input))
    }

    @Test
    fun solveExample2() {
        val input = "(()())"
        assertEquals(3, solve(input))
    }

    @Test
    fun solveExample3() {
        val input = "(((()(()()))(())()))(()())"
        assertEquals(24, solve(input))
    }
}