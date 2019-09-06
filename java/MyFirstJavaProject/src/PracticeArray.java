
public class PracticeArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int a[] = new int[]{10,20,30,40,50};
		System.out.println(a[1]);
		System.out.println(a[4]);
		int i;
		for (i=0; i<5; i++) {
			System.out.println(a[i]);
		}
		
		int b[][]= {{1,2,3},{4,5,6},{7,8,9}};
		for(int j=0; j<3; j++) {
			for(int k=0;k<3;k++) {
				System.out.print(b[j][k]+ " ");
			}
			System.out.println();
		}
	}

}
