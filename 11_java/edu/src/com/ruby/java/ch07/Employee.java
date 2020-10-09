package com.ruby.java.ch07;

public class Employee extends Person {
	private String dept;
	
	public Employee() {
		super();
		System.out.println(2);
	}
	
	public String getDept() {
		return dept;
	}
	
	public void setDept(String dept) {
		this.dept = dept;
	}
	
	public String toString() {
		return super.toString() + ":" + dept;
	}
}
