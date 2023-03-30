class Node {
    constructor(value){
        this.value = value;
        this.next = null
    }
}

class LinkedList { 
    constructor(){
        this.head = null
        this.tail = null
    }

    append(value) {
        const newNode = new Node(value)
        if(!this.head) {
            this.head  = newNode
            this.tail  = newNode
        } else {
            this.head.tail = newNode;
            this.tail = newNode;
        }
    }
}

const a = new LinkedList()
a.append(10)
a.append(12)