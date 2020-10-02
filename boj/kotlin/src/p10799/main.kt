package p10799

import java.util.*

fun main(args: Array<String>) {
    with(Scanner(System.`in`)) {
        val input = this.nextLine()
        println(solve(input))
    }
}

fun solve(input: String): Int {
    var height = 0
    var res = 0
    var i = 0

    while(i < input.length) {
        if(input[i] == '(') {
            if(input[i + 1] == ')') {
                res += height
                i += 2
            } else {
                height += 1
                i += 1
            }
        } else {
            height -= 1
            res += 1
            i += 1
        }
    }

    return res
}
