
class Node { 
    constructor(value) {
        this.value = value;
        this.left = null
        this.right = null
    }
}

class BinarySearchTree {
    constructor(){
        this.root = null
    }
    insert(value) {
        const newNode = new Node(value)
        if(!this.root) {
            this.root = newNode
            return this;
        }
        
        let current = this.root;

        while(true) {
            if(current.value === value) {
                return undefined
            }
            if(value > current.value) {
                if(!current.right) {
                    current.right = newNode;
                    return this;
                }
                current = current.right
            }
            if(value < current.value) {
                if(!current.left) {
                    current.left = newNode;
                    return this;
                }
                current  = current.left
            }
        }
    }
    preOrder() {
        const data = []
        function travers(node) {
            data.push(node.value)
            if(node.left) travers(node.left)
            if(node.right) travers(node.right)
        }
        travers(this.root)
        return data
    }
    inOrder() {
        const data = []
        function travers(node) {
            if(node.left) travers(node.left)
            data.push(node.value)
            if(node.right) travers(node.right)
        }
        travers(this.root)
        return data
    }
    postOrder() {
        const data = []
        function travers(node) {
            if(node.left) travers(node.left)
            if(node.right) travers(node.right)
            data.push(node.value)
        }
        travers(this.root)
        return data
    }
}





////// TEST ///////


const expect = (realValue) => {
    const isEqual = (expectedValue) => {
        if(typeof realValue === typeof expectedValue) {
            if(Array.isArray(realValue)) {
                const result = realValue.every((item,index) => item === expectedValue[index])
                console.log(`${result}`)
                return
            }
            realValue === expectedValue ? console.log('true') : console.log('false')
            return;
        }
        console.log('false')
    }
    return {
        isEqual,
    }
}

const describe = (name,callbackTest) => {
    callbackTest()
    console.log(`Test for ${name}:`)
}



describe('BinarySearchTree', () => { 
    const binaryTree = new BinarySearchTree()
    binaryTree.insert(12)
    expect(binaryTree.root.value).isEqual(12)
    expect(binaryTree.root.right).isEqual(null)
    expect(binaryTree.root.left).isEqual(null)
})

describe('BinarySearchTree preOrder', () => { 
    const binaryTree = new BinarySearchTree()
    binaryTree.insert(12)
    binaryTree.insert(3)
    binaryTree.insert(20)
    binaryTree.insert(2)
    binaryTree.insert(4)
    expect(binaryTree.preOrder()).isEqual([12,3,2,4,20])
})

describe('BinarySearchTree inOrder', () => { 
    const binaryTree = new BinarySearchTree()
    binaryTree.insert(12)
    binaryTree.insert(3)
    binaryTree.insert(20)
    binaryTree.insert(2)
    binaryTree.insert(4)
    expect(binaryTree.inOrder()).isEqual([2,3,4,12,20])
})

describe('BinarySearchTree postOrder', () => { 
    const binaryTree = new BinarySearchTree()
    binaryTree.insert(12)
    binaryTree.insert(3)
    binaryTree.insert(20)
    binaryTree.insert(2)
    binaryTree.insert(4)
    expect(binaryTree.postOrder()).isEqual([2,4,3,20,12])
})
