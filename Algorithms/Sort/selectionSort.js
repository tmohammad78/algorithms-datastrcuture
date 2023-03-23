const selectionSort = (arr) => {
    for(let i = 0 ; i< arr.length ; i++) {
        let minIndex = i
        for(let j=i+1 ; j < arr.length ; j++){
            if(arr[j] < arr[minIndex]) minIndex = j
        }
        const temp = arr[minIndex]
        arr[minIndex] = arr[i];
        arr[i] = temp
    }
}

const arr = [2,4,5,2,3,1,0,23,43,12,8,43,20]
selectionSort(arr)
console.log(arr)