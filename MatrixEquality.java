import java.util.*;
public class MatrixEquality {

	public static void  checkEqual(int[][] a,int[][] b)
	{
		int res=0;
		for(int i=0;i<a.length;i++)
		{
			for(int j=0;j<a[0].length;j++)
			{
				if(a[i][j]==b[i][j])
				{
					a[i][j]=0;
					res++;
				}
				
			}
		}
		if(res==a.length*a.length) System.out.println("Equal");
		else
		{
			for(int[] n:a)
			{
				for(int m : n) System.out.print(m);
			 System.out.println("");
			}
		}
	}
	public static void main(String[] args)
	{
		int[][] arr1 = {{1,2,3},{-5,4,6}};
		int[][] arr2 = {{1,4,5,6},{0,8,9}};
		int[][] arr3 = {{1,2,3},{-5,4,6}};
		
		checkEqual(arr1,arr2);
	    System.out.println("");
		checkEqual(arr1,arr3);
	}
}
