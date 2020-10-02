import java.util.*

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
    val N = nextInt()
    val K = nextInt()
    println(solve(N, K).myToString())
}

fun List<Int>.myToString(prefix: String = "<", postFix: String = ">") =
    prefix + this.map(Int::toString).reduce { acc, x ->  acc + ", " + x } + postFix

fun solve(n: Int, k: Int): List<Int> {
    val nums = (1..n).toMutableList()
    var i = 0
    val l = mutableListOf<Int>()

    while(true) {
        // index 기준으로 맞춤.
        val (v, j) = pickOne(nums, k - 1, i)
        if(v == -1) {
            break
        }
        //println(v to j)
        l.add(v)
        i = j
    }

    return l
}

fun pickOne(l: MutableList<Int>, k: Int, i: Int): Pair<Int, Int> {
    if(l.size == 0) {
        return -1 to -1
    }

    val candidate = i + k
    if(l.size <= candidate) {
        return pickOne(l, candidate - l.size, 0)
    }

    return l.removeAt(candidate) to candidate
}
