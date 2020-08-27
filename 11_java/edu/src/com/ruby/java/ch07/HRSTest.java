package com.ruby.java.ch07;

abstract class Employee {
	String name;
	int salary;
	
	public abstract void calcSalary();
}

class Salesman extends Employee {
	public void calcSalary() {
		System.out.println("Salesman : 기본 + 수당");
	}
}

class Consultant extends Employee {
	public void calcSalary() {
		System.out.println("Consultant : 기본 + 특별");
	}
}

class Manager extends Employee {
	public void calcSalary () {
		System.out.println("Manager : 기본 + 팀");
	}
}


public class HRSTest {
	public static void main(String[] args) {
		Salesman slm = new Salesman();
		Consultant cst = new Consultant();
		Manager mgr = new Manager();
		
		slm.calcSalary();
		cst.calcSalary();
		mgr.calcSalary();
	}
}