//
// Created by Administrator on 2022/10/17.
//

#include "stdio.h"
int islike(bitree* s,bitree* t)
{
    if(s== nullptr&&t= nullptr)
        return 1;
    else if(s== nullptr||t== nullptr)
        return 0;
    else
    {
        return islike(s->left,t->left)&&islike(s->right,t->right);
    }
}
bitree* Create_add(bitree* s,bitree* t,bitree* z)
{
    if(s== nullptr||t== nullptr)
    {
        return nullptr;
    } else
    {
        z=(bitree*)malloc(sizeof(bitree*));
        z->data=s->data+t->data;
        Create_add(bitree* s->left,bitree* t->left,bitree* z->left);
        Create_add(bitree* s->right,bitree* t->right,bitree* z->right);
    }
}