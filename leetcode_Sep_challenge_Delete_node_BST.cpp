
//  Definition for a binary tree node.
  struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  };
 
class Solution {
public:
    TreeNode* findMax(TreeNode* root){
        TreeNode* max = root;
        while(max && max->right){
            max = max->right;
        }
        return max;
    } // find the max vertex in the left subtree
    TreeNode* deleteNode(TreeNode* root, int key) {
        if(root == nullptr){
            return root;
        }
        // we handle the multiple cases in the subtree directly. 
        if(key > root->val){
            root->right = deleteNode(root->right, key);
        } else {
          if(key < root->val){
             root->left = deleteNode(root->left, key);
        } else {
            if(root->left == nullptr){
                TreeNode* temp = root->right;
                delete root;
                root = temp; // directlt delete the root, and replace with the right one
            } else {
                if(root->right == nullptr){
                    TreeNode* temp = root->left;
                    delete root;
                    root = temp; // directlt delete the root, and replace with the left one 
                } else {
                    TreeNode* temp = findMax(root->left);
                    root->val = temp->val;
                    root->left = deleteNode(root->left, temp->val); // directlt delete the root, and replace with the max one in left
                }
            }   
              
          }  
        }
        return root;
    }
};