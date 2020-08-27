package com.ruby.java.ch06;

public class Member {
	private String name;
	private int age;
	
	public Member() {
		System.out.println("Member() 생성자");
	}
	
	public void setName(String name) {
	}
	
	
	public static void main(String[] args) {
		System.out.println("실행");
		new Member();

	}

}
