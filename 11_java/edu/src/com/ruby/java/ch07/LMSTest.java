package com.ruby.java.ch07;

public class LMSTest {
	
	public static void main(String[] args) {
		Employee emp = new Employee();
		Professor pro = new Professor();
		Student stu = new Student();
		
		emp.setName("우너");
		emp.setAge(123);
		emp.setDept("집");
		
		pro.setName("우너");
		pro.setAge(123);
		pro.setSubject("자바");
		
		stu.setName("우너");
		stu.setAge(123);
		stu.setMajor("컴퓨터");

		System.out.println(emp.toString());
		System.out.println(pro.toString());
		System.out.println(stu.toString());
	}

}
