package com.ruby.java.ch07;

public class Student extends Person {
	private String major;
	
	public Student() {
		super();
		System.out.println(2);
	}
	
	public String getMajor() {
		return major;
	}
	
	public void setMajor(String major) {
		this.major = major;
	}
	
	public String toString() {
		return super.toString() + ":" + major;
	}
}
