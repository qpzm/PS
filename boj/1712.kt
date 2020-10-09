import java.util.*

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
    val fixedCost = nextInt()
    val costPerProduct = nextInt()
    val reveneuePerProduct = nextInt()
    val profitPerProduct = reveneuePerProduct - costPerProduct

    if(profitPerProduct <= 0) {
        println(-1)
    } else {
        println(fixedCost / profitPerProduct + 1)
    }
}
