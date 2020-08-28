package com.ruby.java.ch07.abstraction;

public class GalaxyMessenger implements Messenger {
	public String getMessage() {
		return "Galaxy";
	}
	
	public void setMessage(String msg) {
		System.out.println("Galaxy msg : " + msg);
	}
}
