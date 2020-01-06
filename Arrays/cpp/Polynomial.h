#include <iostream>

class Polynomial;       // forward declaration of the class Polynomial.
class Term
{
    friend Polynomial;
private:
    float coef;     // coefficient
    int exp;        // exponent
};

class Polynomial
{
// p(x)=a0 x^e0 + . . . + an x^en; a set of ordered pairs of <ei, ai>
// where ai is a nonzero float coefficient and ei is a non-negative integer exponent.
public:
    Polynomial();
    Polynomial(int cap);
    Polynomial(Term *t);          // Construct the polynomial of p(x) = 0
    ~Polynomial();

    Polynomial Add(Polynomial poly);        // Return the sum of the polynomials *this and poly.
    Polynomial Mult(Polynomial poly);       // Return the product of the polynomials *this and poly.
    float Eval(float f);        // Evaluate the polynomial *this at f and return the result.

private:
    Term* termArray;        // Array of nonzero terms
    int capacity;           // size of termArray.
    int terms;              // number of nonzero terms.

    void NewTerm(float coef, int exp)
    {
        if(terms > capacity){
            throw "Capacity, Terms Mismatch";
        }

        if(terms == capacity){
            capacity = capacity*2;
            Term *temp = new Term[capacity]();
            for(int i=0; i<terms; i++){
                temp[i] = termArray[i];
            }
            delete[] termArray;
            termArray = temp;
        }

        termArray[terms].coef = coef;
        termArray[terms++].exp = exp;
    }
};

Polynomial::Polynomial() : capacity(512), terms(0)
{
    termArray = new Term[capacity]();
}


Polynomial::Polynomial(int cap) : capacity(cap)
{
    termArray = new Term[cap]();
    terms=0;
}

Polynomial::Polynomial(Term* t) :  termArray(t)
{
    while(t){
        if(t->coef){terms++;}
        capacity++;
        t++;
    }
}

Polynomial::~Polynomial()
{
    if(termArray != nullptr){
        delete[] termArray;
        terms = 0;
    }
}

Polynomial Polynomial::Add(Polynomial b)
{
    // Return the sum of the polynomial *this and b
    Polynomial c;
    int aPos=0, bPos=0;

    try{
        while((aPos < terms) && (bPos < b.terms))
        {
            if(termArray[aPos].exp == b.termArray[bPos].exp){
                float t = termArray[aPos].coef + termArray[bPos].coef;
                if(t){
                    c.NewTerm(t, termArray[aPos].exp);
                }
                aPos++;bPos++;
            }
            else if(termArray[aPos].exp < b.termArray[bPos].exp){
                c.NewTerm(b.termArray[bPos].coef, b.termArray[bPos].exp);
                bPos++;
            }
            else{
                c.NewTerm(termArray[aPos].coef, termArray[aPos].exp);
                aPos++;
            }
        }
        // Add in remaining of *this
        for(; aPos < terms; aPos++){
            c.NewTerm(termArray[aPos].coef, termArray[bPos].exp);
        }

        // Add in remaining of b(x)
        for(; bPos < b.terms; bPos++){
            c.NewTerm(termArray[bPos].coef, b.termArray[bPos].exp);
        }
    }
    catch(char *errMsg)
    {
        std::cerr << "Error:" << errMsg << std::endl;
        return nullptr;
    }

    return c;
}
