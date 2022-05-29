import java.util.*;
class bubques{
   public static int[] sort(int[] arr,int n,int num){
    for(int i=num;i<n;i+=2){
        for(int j=num;j<n-i;j+=2){
            if(arr[j]>arr[j+2]){
                int temp=arr[j];
                arr[j]= arr[j+2];
                arr[j+2]=temp;
            }
        }
    }
    
    return arr;
   }

   public static void main(String[] args){
    int[] arr={4,2,5,1};
    int n= arr.length;
    if ((n-1)%2==0) {
    arr= sort(arr,n-1,0); //even
    arr= sort(arr,n-1,1); //odd
    }
    else{
        arr= sort(arr,n-2,0); //even
        arr= sort(arr,n-2,1); //odd  
    }
    System.out.println("Sorted Array");
    for(int i=0;i<n;i++){
        System.out.print(arr[i]+" ");
    } 
   }
}