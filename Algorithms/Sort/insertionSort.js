const insertionSort = (arr) => {
    for(let i = 0 ; i< arr.length ; i++) {
        while(i > 0 && arr[i-1] > arr[i]) {
            const temp = arr[i-1]
            arr[i-1] = arr[i];
            arr[i] = temp
            i--
        }
    }
}

const arr = [2,4,5,2,3,1,0,23,43,12,8,43,20]
insertionSort(arr)
console.log(arr)