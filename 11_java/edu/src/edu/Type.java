package edu;

public class Type {

	public static void main(String[] args) {
		byte age;
		short point;
		int price;
		long totalSales;
		
		age = 23;
		point = 32000;
		price = 3500000;
		totalSales = 2147483648L;
		
		System.out.println(age);
		System.out.println(point);
		System.out.println(price);
		System.out.println(totalSales);
		
		
		float exchangeRate = 1136.50f;
		double USDAmount = 600.50;
		double KRWAmount = 282468.25;
		
		System.out.println(exchangeRate);
		System.out.println(USDAmount);
		System.out.println(KRWAmount);
	}

}
