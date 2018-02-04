package com.example.puing.a2018codegate;

public class Main4Activity {
	static {
		System.load("/mnt/hgfs/Writeup/ctf/codegate/2018-Prequal/Reversing/Welcome to droid/Solve/libnative-lib.so");
	}
	
	public static void main(String[] args) {
		System.out.println(new Main4Activity().stringFromJNI());
	}
	
	public native String stringFromJNI();
}
