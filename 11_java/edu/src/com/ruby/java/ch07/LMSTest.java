package com.ruby.java.ch07;

public class LMSTest {
	
	public static void main(String[] args) {
		Employee emp = new Employee();
		Professor pro = new Professor();
		Student stu = new Student();
		
		emp.setName("���");
		emp.setAge(123);
		emp.setDept("��");
		
		pro.setName("���");
		pro.setAge(123);
		pro.setSubject("�ڹ�");
		
		stu.setName("���");
		stu.setAge(123);
		stu.setMajor("��ǻ��");

		System.out.println(emp.toString());
		System.out.println(pro.toString());
		System.out.println(stu.toString());
	}

}
