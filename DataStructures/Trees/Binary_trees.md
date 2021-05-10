
**Trees:** Unlike Arrays, Linked Lists, Stack and queues, which are linear data structures,
trees are hierarchical data structures.


**Why Trees?** 
1. One reason to use trees might be because you want to store information that naturally forms a hierarchy.
 For example, the file system on a computer. 
2. Trees (with some ordering e.g., BST) provide moderate access/search (quicker than Linked List and slower than arrays). 
3. Trees provide moderate insertion/deletion (quicker than Arrays and slower than Unordered Linked Lists). 
4. Like Linked Lists and unlike Arrays, Trees don’t have an upper limit on number of nodes as nodes are linked using pointers.


### Binary Trees
**Binary Tree:** A tree whose elements have at most 2 children is called a binary tree. 
Since each element in a binary tree can have only 2 children, we typically name them the left and right child.


#### Properties of a Binary Tree

1. **The maximum number of nodes at level ‘l’ of a binary tree is 2^l.** 
2. **The Maximum number of nodes in a binary tree of height ‘h’ is 2^h – 1.**
   sometimes the height of the root is considered as 0. In this convention, the above formula becomes 2^(h+1) – 1  
3. **In a Binary Tree with N nodes, minimum possible height or the minimum number of levels is Log2(N+1)**
4. **A Binary Tree with L leaves has at least | Log2L |+ 1   levels**