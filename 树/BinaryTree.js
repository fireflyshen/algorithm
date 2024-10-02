class TreeNode{
    constructor(value){
        this.value = value;
        this.left = null;
        this.right = null;
    }
}


class BinaryTree {
    constructor(){
        this.root = null;
    }


    // 插入节点;
    insert(value){
        let newNode = new TreeNode(value);

        if (this.root === null) {
            this.root = newNode;
            return this;
        } else {
            this._insertNode(this.root, newNode);
            return this;
        }
    }

    _insertNode(node, newNode){
        if (newNode.value < node.value){
            if (node.left === null) {
                node.left = newNode;
            } else {
                this._insertNode(node.left, newNode);
            }
        } else {  
            if (node.right === null) {
                node.right = newNode;
            } else {
                this._insertNode(node.right, newNode);
            }
        }
    }

    // 遍历
    preOrderTraverse(){
        this._preOrderTraverse(this.root);
    }

    _preOrderTraverse(node){
        if (node === null) return;
        console.log("前序遍历",node.value);
        this._preOrderTraverse(node.left);
        console.log("中序遍历：",node.value);
        this._preOrderTraverse(node.right);
        console.log("后序遍历：",node.value);
    }    
}


new BinaryTree().insert(1).insert(2).insert(3).insert(4).insert(5).insert(6).insert(7).inOrderTraverse();