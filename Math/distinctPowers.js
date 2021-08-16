let arr = []
let value;
for (let i = 2; i < 101; i++) {
    for (let j = 2; j < 101; j++) {
        value = i ** j
        arr.indexOf(value) === -1 && arr.push(value)
    }
}
console.log(arr.length);

