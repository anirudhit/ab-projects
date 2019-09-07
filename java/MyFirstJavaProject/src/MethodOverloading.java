class Area{
	void calculate(int side) {
		int area = side * side;
		System.out.println("Area of square: "+area);
	}
	
	void calculate(int length, int breadth) {
		int area = length * breadth;
		System.out.println("Area of rectangle: "+area);
	}
}
public class MethodOverloading {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Area area = new Area();
		area.calculate(10);
		area.calculate(10, 20);
	}

}
