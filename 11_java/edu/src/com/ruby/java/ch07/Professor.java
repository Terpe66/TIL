package com.ruby.java.ch07;

public class Professor extends Person {
	private String subject;
	
	public Professor() {
		super();
		System.out.println(2);
	}
	
	public String getSubject() {
		return subject;
	}
	
	public void setSubject(String subject) {
		this.subject = subject;
	}
	
	public String toString() {
		return super.toString() + ":" + subject;
	}
}
