function quickSort(arr){
    const left = []
    const right = []
    const equal = []
    const pivot = arr[arr.length - 1]
    if(arr.length <= 1) {
        return arr
    }
    for( let i=0; i< arr.length ; i++) {
        if (arr[i] < pivot) {
            left.push(arr[i])
        } else if(arr[i] > pivot) {
            right.push(arr[i])
        } else {
            equal.push(arr[i])
        }
    }
    return [...quickSort(left),...equal,...quickSort(right)]
}



const arr = [2,4,5,2,3,1,0,23,43,12,8,43,20]
console.log(quickSort(arr))