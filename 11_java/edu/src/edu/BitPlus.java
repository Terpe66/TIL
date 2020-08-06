package edu;

public class BitPlus {

	public static void main(String[] args) {
		char c = 'A';
		/* 1 << 5 : 00001을 10000으로
		   c 와 XOR(^)연산
		 */
		c ^= (1 << 5);
		System.out.println(c);

	}

}
