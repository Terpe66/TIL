package edu;

public class BitPlus {

	public static void main(String[] args) {
		char c = 'A';
		/* 1 << 5 : 00001�� 10000����
		   c �� XOR(^)����
		 */
		c ^= (1 << 5);
		System.out.println(c);

	}

}
