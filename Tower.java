import java.util.*;
public class Tower {

	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);
		int n;
		n=sc.nextInt();
		int a=1;
		for(int i=0;i<n;i++)
			{
			for(int j=1;j<n-i;j++)
			{
				System.out.print(" ");
			}
			for(int k=0	;k<i+1;k++)
			{
				System.out.print(a);
			}
			a++;
			System.out.println(" ");
			}
		
	}
}
