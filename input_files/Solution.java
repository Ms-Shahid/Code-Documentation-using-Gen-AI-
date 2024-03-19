public class Solution {
    public int minDistance(String A, String B) {
        int n = A.length();
        int m = B.length();

        int[][] dp = initialize( n, m );

        return minimumStepsToConvertAToB( dp, A, B, n-1, m-1 );
    }

    private int[][] initialize( int n, int m ){

        int[][] dp = new int[n+1][m+1];

        for(int[] arr : dp ){
            Arrays.fill( arr, -1);
        }

        return dp;
    }

    private int minimumStepsToConvertAToB( int[][] dp, String A, String B, int i, int j ){

        if( i < 0  || j < 0 ){
            return Math.abs(i - j);
        }

        if( dp[i][j] != -1 ) return dp[i][j];

        if( A.charAt(i) == B.charAt(j) ){
            dp[i][j] = minimumStepsToConvertAToB(dp, A, B, i-1, j-1);
        }else{
            int value = Math.min( 
                minimumStepsToConvertAToB(dp, A, B, i-1, j-1), //replace
                minimumStepsToConvertAToB(dp, A, B, i, j-1 ) //insert
            );
            dp[i][j] = Math.min( value, minimumStepsToConvertAToB(dp, A, B, i-1, j ) ) + 1; //delete
        }
        return dp[i][j];
    }
}


/*
* Manifestation : editDistance(i, j ) -> min no. of steps required to convert A[0...j] -> B[0...j]

* Answer state : editDistance( n-1, m-1 )

* Elements of choice & Recursive relation : 
*    CASE 1 -> chars are matching => editDistance( i-1, j-1 ) contiue 
*    CASE 2 -> chars are not matching ={ 
*                                        -> replace : editDistance( i-1, j-1 ) replace the current char of A to B & contiue
*                                        -> insert  : editDistance( i, j-1 ) insert a char in A to make it equal to B, then decrement B's length 
*                                        -> delete  : editDistance( i-1, j ) delete a char from A to make it equal to B, then decrement A's length
*                                      }
* BASE case : if empty -> max of any 
*/
