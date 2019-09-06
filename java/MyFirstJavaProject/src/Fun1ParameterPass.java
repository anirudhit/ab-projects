
public class Fun1ParameterPass {
	
	static int addition(int a, int b) {// Formal parameters : (Called function)
		int result = a+b;
		return result;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int sum = addition(10, 20);
		System.out.println("Sum is : "+sum);// Actual parameter : (Calling function)
	}

}
