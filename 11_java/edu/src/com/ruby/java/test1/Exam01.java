package com.ruby.java.test1;

class Test {
	static void testF(int ... ints) {
		for (int i = 0; i < ints.length; ++i) {
			System.out.println(ints[i]);
		}
	}
}

public class Exam01 {
	public static void main(String[] args) {
		System.out.println(1234);
		Test.testF(1, 2, 3, 4);
	}	
}
