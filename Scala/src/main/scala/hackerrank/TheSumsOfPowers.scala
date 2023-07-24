package hackerrank

// https://www.hackerrank.com/challenges/functional-programming-the-sums-of-powers/problem

import scala.io.StdIn.readInt

object Solution {

    // Helper function.
    def getNumberOfWaysHelper(remainingSum:Int, power:Int, base:Int):Int = {
        //calculate power
        val result: Int = math.pow(base, power).toInt

        if(remainingSum == result)  return 1
        else if(remainingSum < result) return 0
        else {
            //Two recursive calls one to include current base's power in sum another to exclude
            val x: Int = getNumberOfWaysHelper(remainingSum - result, power, base + 1)
            val y: Int = getNumberOfWaysHelper(remainingSum, power, base + 1)

            return x + y
        }
    }

    def numberOfWays(X:Int,N:Int):Int = {
        getNumberOfWaysHelper(X, N, 1)
    }

    def main(args: Array[String]) {
        println(numberOfWays(readInt(),readInt()))
    }
}
