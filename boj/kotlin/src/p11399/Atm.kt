import java.util.*

// Condition
// - The number of people: 1 <= N <= 1000
// - Time duration: 1 <= P <= 1000
// Given
// - P_i = 1000, N = 1000
//   - Max result: 1000 * (1000 * 1001) /2

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
    val N = nextLine() // .trim().toInt()
    val arrString = nextLine()
    arrString.split(' ')
            .map(String::toInt)
            .sortedBy { -it }
            .run {
                println(this.solve())
            }
}

fun List<Int>.solve() =
        this.mapIndexed { index, t -> (index + 1) * t }
            .sum()