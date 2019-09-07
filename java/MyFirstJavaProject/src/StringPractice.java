
public class StringPractice {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s1 = "Words are words";
		String s2 = "They are always words";
		String s3 = "Words are words";
		String s4 = "WORDS are words";
		String s5 = "   WORDS are words and many spaces     ";
		System.out.println("Length of string: "+s1.length());
		System.out.println("Character at an index: "+s1.charAt(1));
		System.out.println("Concatenated string: "+s1.concat(" "+s2));
		System.out.println("String are equal: "+s1.equals(s2));
		System.out.println("String are equal: "+s1.equals(s3));
		System.out.println("String are equal case: "+s1.equals(s4));
		System.out.println("String are equal case ignore: "+s1.equalsIgnoreCase(s4));
		System.out.println("Character index in the string: "+s1.indexOf('d'));
		System.out.println("Replace characters in string: "+s1.replace("d", "D"));
		System.out.println("Converting to uppercase: "+s4.toUpperCase());
		System.out.println("Converting to lowercase: "+s4.toLowerCase());
		System.out.println("Trim the spaces in the string: "+s5.trim());
		
		StringBuffer sb1 = new StringBuffer("Hello");
		StringBuffer sb2 = new StringBuffer("World");
		System.out.println("Before string append: "+sb1);
		sb1.append(" "+ sb2);
		System.out.println("After string append: "+sb1);
		
	}

}
