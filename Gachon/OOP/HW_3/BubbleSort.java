package HW_3;

public class BubbleSort {
    private static int num;

    static int[] sort(int[] arr){
        /** sort to bubble sort */
        for (int index = 0; index < arr.length - 1; index++){
            for (int i=arr.length - 1; i>index; i--){
                if (arr[i-1] > arr[i]){
                    /** swap the data arr[i-1], arr[i] */
                    num = arr[i-1];
                    arr[i-1] = arr[i];
                    arr[i] = num;
                }
            }
        }
        return arr;
    }
}
