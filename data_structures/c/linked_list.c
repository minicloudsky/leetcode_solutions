/***
 * Single Linked List,implemented by @minicloudsky .
 *
 *
 */
#include<stdio.h>
#include<stdlib.h>

#define dtype int


typedef struct Node{
    dtype  data;
    Node  *next;
};

// insert val to node
Node _insert(Node *node, int position, dtype val){

}

Node _delete(Node *)

// traverse a linked list
void  traverse(Node *node){
    if(node==null){
        printf("node is empty .");
    }
    while(node->next!=null){
        printf("%d ",node->val);
    }
    printf("\n");
}





int main()
{
    printf("Hello world\n");
    return 0;
}

