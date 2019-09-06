
public class DemoFuctions {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Area of square:" + DemoFuctions.SquareArea(10));
		System.out.println("Area of rectangle: " + RectangleArea(10,20));
		System.out.println("Perimeter of rectangle: " + RectanglePerimeter(10,20));
	}
	
	public static int RectangleArea(int length, int breadth) {
		return length * breadth;
	}
	
	public static int RectanglePerimeter(int length, int breadth) {
		return 2*(length + breadth);
	}
	
	public static int SquareArea(int side) {
		return side*side;
	}
	

}
