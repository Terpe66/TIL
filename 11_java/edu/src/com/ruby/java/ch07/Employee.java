package com.ruby.java.ch07;

public class Employee extends Person {
	private String dept;
	
	public String getDept() {
		return dept;
	}
	
	public void setDept(String dept) {
		this.dept = dept;
	}
	
	public String toString() {
		return this.getName() + ":" + this.getAge() + ":" + this.dept;
	}
}
