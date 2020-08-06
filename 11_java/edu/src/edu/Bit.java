package edu;

public class Bit {

	public static void main(String[] args) {
		byte a = 0b00010001, b = 0b00100010;
		int c = a & b;
		int d = a | b;
		int e = a ^ b;
		System.out.println(Integer.toBinaryString(c));
		System.out.println(Integer.toBinaryString(d));
		System.out.println(Integer.toBinaryString(e));
		
		int f = 12;
		int g = (~f) + 1;
		System.out.println(g);
		
		int h = f << 1;
		int i = f >> 1;
		System.out.println(h);
		System.out.println(Integer.toBinaryString(f));
		System.out.println(Integer.toBinaryString(h));
		System.out.println(i);
	}

}
