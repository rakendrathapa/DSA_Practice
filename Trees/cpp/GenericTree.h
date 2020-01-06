#ifndef _T_GENERIC_TREE_H
#define _T_GENERIC_TREE_H

//#pragma warning(disable:4786)

#include<vector>
using namespace std;

#include "GenericData.h"

template<class Type> class NodeData;

template <class Type,class DataType2=NodeData<Type> > class Tree;
template <class Type> class NodeData
{
private:
    typedef Ref<NodeData> NodeRef;
    NodeData(const Type &Data) : tData(Data){}
    NodeData(Type *pData) : tData(pData) {}
    NodeData() : Parent((NodeData*) nullptr){}
    virtual ~NodeData(){};

private:
    Ref<Type> tData;
    std::vector<NodeRef> vChilds;
    Ref<NodeData> Parent;
    friend class Tree<Type>;
    friend class Ref<NodeData>;
    friend _GenericData::GenericData<NodeData>;
};

template <class Type,class DataType2>
class Tree : private Ref<DataType2>
{
    typedef Ref<DataType2> NodeBase;
public:
    typedef Tree<Type> Node;
    Node Parent()
    {
        if(NodeBase::GetData().IsNull() == false){
            return NodeBase::GetData().Parent;
        }
        return *this;
    }

    operator Type&(){
        return (NodeBase::GetData().tData.GetData());
    }

    Type* operator->(){
        return &(NodeBase::GetData().tData.GetData());
    }

    // __declspec( property( get=GetData) ) Ref<Type> Data;
    Ref<Type> GetData() {
        return NodeBase::GetData().tData;
    }

    bool IsLeaf(){
        return (NodeBase::GetData().vChilds.size() == 0);
    }

    bool IsNode(){
        return (NodeBase::GetData().vChilds.size() > 0);
    }

    bool IsRoot(){
        return NodeBase::GetData().Parent.IsNull();
    }

    bool operator ==(const Node &rhs){
        return (*(NodeBase*)this == (NodeBase&)rhs);
    }

    //__declspec( property( get=GetNodes) ) Node Nodes[];
    Node GetNodes(int nIndex) { return (Node)NodeBase::GetData().vChilds[nIndex];}

    //__declspec( property( get=GetCount) ) int Count;
    int GetCount() { return NodeBase::GetData().vChilds.size(); }

    //__declspec( property( get=GetKey) ) unsigned long Key;
    unsigned long GetKey() { return NodeBase::Key(); }

    Node AddNode(const Type &t){
        Node n(t);
        ((NodeBase &)n).GetData().Parent=(*this);
        NodeBase::GetData().vChilds.push_back(n);
        return n;
    }

    void Delete(){
        if(NodeBase::GetData().Parent->IsNull()==false){
            NodeBase::GetData().Parent->DeleteNode(*this);
        }
    }

    void DeleteNode(int nIndex){
        NodeBase::GetData().vChilds.erase(NodeBase::GetData().vChilds.begin() + nIndex);
    }

    void Delete(Node &node){
        auto it = std::find(NodeBase::GetData().vChilds.begin(), NodeBase::GetData().vChilds.end(), node);
        if(it != NodeBase::GetData().vChilds.end()){
            NodeBase::GetData().vChilds.erase(it);
        }
    }

    Tree(const Type &Data) : NodeBase(Data) {};
    Tree(Type *Data): NodeBase(Data) {};
    Tree() {}
    Tree(const Tree<Type> &rhs) : NodeBase(rhs) {};
    Tree(const NodeBase rhs) : NodeBase(rhs){};
    Tree(unsigned long key) : NodeBase(key){};

    virtual ~Tree()
    {
        ReleaseNode();
    }

private:
    void ReleaseNode(){
        if(NodeBase::IsNull()) return;
        unsigned long nRefs = NodeBase::GetRefCount();
        int nChilds = NodeBase::GetData().vChilds.size();
        if(nRefs == (unsigned long)(nChilds+1)){
            std::vector<NodeBase> &vChilds = NodeBase::GetData().vChilds;
            for (size_t n=0; n<vChilds.size(); n++){
                vChilds[n]->Parent.Release();
                ((Node &)vChilds[n]).ReleaseNode();
            }
        }
    }
};

#endif
