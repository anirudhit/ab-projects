class Sample{
	int data;
	public Sample(int p) {
		data = p;
	}
	
	void showIncrementedValue() {
		System.out.println("Incremented Value: "+data);
	}
	
	
}


public class Fun3CallByReference {
	
	static void increment(Sample p) {
		p.data = p.data + 1;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Sample obj1 = new Sample(15);
		
		increment(obj1);
		obj1.showIncrementedValue();

	}

}
