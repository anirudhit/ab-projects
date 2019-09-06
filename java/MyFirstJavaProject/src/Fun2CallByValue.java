
public class Fun2CallByValue {
	
	static void increment(int p) {
		p = p+1;
		System.out.println("P value in increment function (Called function): "+ p);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int p = 10;
		increment(p);
		System.out.println("P value in main function (Calling function): " + (p));

	}

}
