#include <stdio.h>
#include <stdlib.h>

typedef struct bTreeNode
{
    char data;
    struct bTreeNode *left;
    struct bTreeNode *right;
} BTreeNode;

BTreeNode *setNode(char data)
{
    BTreeNode *node = (BTreeNode*)malloc(sizeof(BTreeNode));
    node->left = NULL;
    node->right = NULL;
    node->data = data;

    return node;
}

void preorder(BTreeNode* node) {
    if (node == NULL)
        return;

    printf("%c", node->data);
    preorder(node->left);
    preorder(node->right);
}

void inorder(BTreeNode* node) {
    if (node == NULL)
        return;

    inorder(node->left);
    printf("%c", node->data);
    inorder(node->right);
}

void postorder(BTreeNode* node) {
    if (node == NULL)
        return;

    postorder(node->left);
    postorder(node->right);
    printf("%c", node->data);
}

int main()
{
    int N;
    scanf("%d", &N);

    char arr[N][2];
    BTreeNode *bt[N];
    char root, left, right;
    for(int i=0; i<N; i++){
        scanf(" %c %c %c", &root, &left, &right);
        arr[i][0] = left;
        arr[i][1] = right;

        bt[i] = setNode(root);
    }

    for(int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            if(arr[i][0] == bt[j]->data){
                bt[i]->left = bt[j];
            }

            if(arr[i][1] == bt[j]->data){
                bt[i]->right = bt[j];
            }
        }
    }

    preorder(bt[0]);
    printf("\n");
    inorder(bt[0]);
    printf("\n");
    postorder(bt[0]);
}
