import java.util.*;
public class ArraySum {
	
	public static void main(String[] Args)
	{
		int[][] arr1 = {{1,2},{3,4}};
		int[][] arr2 = {{1,2},{3,4}};
		
		System.out.println("***First Array***");
		
		for(int[] i: arr1)
		{
			for(int j: i)
			{
				System.out.print(j+" ");
			}
			System.out.println("");
		}
		
		System.out.println("***Second Array***");
		
		for(int[] i: arr2)
		{
			for(int j: i)
			{
				System.out.print(j+" ");
			}
			System.out.println("");
		}
		System.out.println("***Sum Array***");
		
		for(int i=0;i<arr1.length;i++)
		{
			for(int j=0;j<arr1[0].length;j++)
			{
				arr1[i][j] +=arr2[i][j];
				System.out.print(arr1[i][j]+" ");
			}
			System.out.println("");
		}
	}

}
