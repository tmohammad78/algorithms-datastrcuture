const combineArr = (leftOne,rightOne) => {
    let i = 0;
    let j = 0;
    const mergedArr = [];
    
    while (i < leftOne.length && j < rightOne.length) {
        if (leftOne[i] < rightOne[j]) {
        mergedArr.push(leftOne[i]);
        i++;
        } else {
        mergedArr.push(rightOne[j]);
        j++;
        }
    }
    console.log(leftOne,leftOne.slice(i),'this is ')
    return mergedArr.concat(leftOne.slice(i)).concat(rightOne.slice(j))
}
const mergSort = (arr) => {
    if(arr.length <= 1) {
        return arr
    }
    const middle  = Math.floor(arr.length / 2)
    const leftSide = arr.slice(0,middle)
    const rightSide = arr.slice(middle)
    const leftSorted = mergSort(leftSide)
    const rightSorted = mergSort(rightSide)
    return combineArr(leftSorted,rightSorted)
}

const arr = [2,4,5,2,3,1,0,23,43,12,8,43,20]
console.log(mergSort(arr))