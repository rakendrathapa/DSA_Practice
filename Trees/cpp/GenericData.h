#ifndef _GENERIC_DATA_H
#define _GENERIC_DATA_H

#include <iostream>

namespace _GenericData{

template <class Type> class Ref;        // forward reference

template <class Type> class GenericData
{
private:
    typedef unsigned long ULONG;
    GenericData(Type* p=nullptr)
    {
        if(p == nullptr){
            p = new Type;
        }
        pData=p;
        dwRefs=1;
    }
    ULONG AddRef() {
        return ++dwRefs;
    }

    ULONG Release(){
        dwRefs--;
        if(dwRefs == 0){
            delete this;
            return 0;
        }
        return dwRefs;
    }

    // Accessors
    Type* operator->() { return pData;}
    operator Type&(){ return *pData;}
    Type& getData(){return *pData;}
    ~GenericData() {
        if(pData){ delete pData;}
    }

    Type* pData;
    ULONG dwRefs;
    friend class Ref<Type>;
};

template <class Type> class Ref
{
    typedef GenericData<Type> GDataT;

public:
    typedef unsigned long ULONG;
    typedef unsigned long KEY;

    // ctors
    Ref(const Type &t) { pData = new GDataT(new Type(t));}
    Ref(Type *p){
        if(p){
            pData = new GDataT(p);
        }else{
            pData = nullptr;
        }
    }
    Ref() { pData = new GDataT();}
    Ref(const Ref<Type> &rhs){
        pData = rhs.pData;
        if(pData){
            pData->AddRef();
        }
    }

    // dtor
    virtual ~Ref() {if(pData) pData->Release();}

    // operator =
    Ref& operator=(const Ref<Type> &rhs){
        Release();
        pData = rhs.pData;
        if(pData){ pData->AddRef();}
        return *this;
    }

    Ref& operator=(const Type &t){
        Release();
        pData = new GDataT(new Type(t));
        return *this;
    }

    Ref& operator=(Type *p){
        Release();
        if(p){ pData = new GDataT(p);}
        else{ pData = nullptr;}
        return *this;
    }

    // operator ==
    bool operator==(const Ref<Type> &rhs){
        return pData == rhs.pData;
    }

    Ref Clone(){
        if(pData == nullptr){
            return Ref();
        }
        return Ref(pData->getData());
    }

    void Release(){
        if(pData){
            pData->Release();
        }
        pData = nullptr;
    }

    bool IsNull(){
        return pData==nullptr;
    }

    // Accessors
    Type* operator->(){
        return pData->operator->();
    }

    Type& GetData(){
        return pData->getData();
    }

    operator Type&(){
        return pData->getData();
    }

    KEY Key(){
        return ((KEY)pData) + 1;
    }

protected:
    ULONG GetRefCount(){
        if(pData == nullptr){return 0;}
        return pData->dwRefs;
    }

    // ctor
    Ref(KEY key){
        try
        {
            pData = (GDataT*)(key - 1);
            if(pData){
                pData->AddRef();
            }
        }
        catch(const std::exception& e)
        {
            std::cerr << e.what() << std::endl;
            pData = nullptr;
        }

    }

private:
    GenericData<Type> *pData;
};

} //namespace _GenericData

using _GenericData::Ref;

#endif
