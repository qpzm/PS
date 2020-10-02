package p18258

import java.util.*

fun main() {
    val l = ArrayDeque<Int>()
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()

    var n = br.readLine().toInt()
    while(n-- != 0) {
        val str = br.readLine()
        val parsedList = str.split(' ')
        when(parsedList[0]) {
            "front" -> bw.write("${if(l.isEmpty()) -1 else l.peekFirst()}\n")
            "back" -> bw.write("${if(l.isEmpty()) -1 else  l.peekLast()}\n")
            "size" -> bw.write("${l.size}\n")
            "empty" -> bw.write("${if(l.isEmpty()) 1 else 0}\n")
            "pop" -> bw.write("${if(l.isEmpty()) -1 else l.removeFirst()}\n")
            "push" -> l.add(parsedList[1].toInt())
        }
    }

    br.close()
    bw.close()
}
