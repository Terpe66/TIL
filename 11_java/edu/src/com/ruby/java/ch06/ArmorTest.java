package com.ruby.java.ch06;

public class ArmorTest {

	public static void main(String[] args) {
		Armor suit1 = new Armor();
		Armor suit2 = new Armor();
		Armor suit3 = new Armor();
		
		suit1.setName("mark42");
		suit1.setHeight(180);
		
		suit2.setName("mark43");
		suit2.setHeight(200);
		
		suit3.setName("mark50");
		suit3.setHeight(220);
		
		System.out.println(suit1.getName() + " : " + suit1.getHeight());
		System.out.println(suit2.getName() + " : " + suit2.getHeight());
		System.out.println(suit3.getName() + " : " + suit3.getHeight());
	}

}
