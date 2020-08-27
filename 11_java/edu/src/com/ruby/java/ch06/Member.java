package com.ruby.java.ch06;

public class Member {
	private String name;
	private int age;
	
	public Member() {
		this("guest");
	}
	
	public Member(String name) {
		this(name, 0);
	}
	
	public Member(String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	public String toString() {
		return name + ":" + age;
	}
	
	
	public static void main(String[] args) {
		Member m1 = new Member();
		Member m2 = new Member("wooner");
		Member m3 = new Member("wooner", 123);
		
		System.out.println(m1.toString());
		System.out.println(m2.toString());
		System.out.println(m3.toString());
	}

}
