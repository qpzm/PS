import java.util.*

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
    val N = nextInt()
    val K = nextInt()
    println(solve(N, K).myToString())
}

fun List<Int>.myToString(prefix: String = "<", postFix: String = ">") =
    prefix + this.map(Int::toString).reduce { acc, x ->  acc + ", " + x } + postFix

/*
 * 1. remove 한 값을 결과 리스트에 더함.
 * 2. 다음 candidate 선정: k - 1 만큼 계속 더해주거나 종료 조건 체크.
 */
fun solve(n: Int, k: Int): List<Int> {
    val nums = (1..n).toMutableList()
    var pickIndex = k - 1
    val l = mutableListOf<Int>()

    while(!nums.isEmpty()) {
        val (v, j) = pickOne(nums, pickIndex)
        // println(v to j)
        l.add(v)
        pickIndex = j + k - 1
    }

    return l
}

/*
 * l에서 index k를 remove. 자체적으로 overflow 처리
 * k > lastIndex 이면 넘치는 만큼 처음부터 다시 시작. 즉, k = k - size
 */
fun pickOne(l: MutableList<Int>, k: Int): Pair<Int, Int> =
    if(l.size <= k) {
        pickOne(l, k - l.size)
    } else {
        l.removeAt(k) to k
    }
