package edu;

public class For {

	public static void main(String[] args) {
		int[][] testArr = new int[5][2];
		
		int i = 0;
		for (int j = 0; j < testArr.length; ++j)
		{
			testArr[i][0] = ++i;
			testArr[j][1] = j;
		}
		
		for (int j = 0; j < testArr.length; ++j)
		{
			System.out.print(testArr[j][0]);
			System.out.print(", ");
			System.out.println(testArr[j][1]);
		}
	}

}
