import java.util.*;
public class RemoveDuplicatesArray
{
    public static int removeDuplicates(int[] nums) {
        ArrayList<Integer> al=new ArrayList<>();
        for (int i=0;i<nums.length;i++){
            if(al.contains(nums[i])){
            }
            else{
                al.add(nums[i]);
            }
        }
        return al.size();
    }
	public static void main(String[] args) {
		int[] nums={1,1,2,2,2,3};
		int ans=removeDuplicates(nums);
		System.out.println(ans);
		
	}
}
