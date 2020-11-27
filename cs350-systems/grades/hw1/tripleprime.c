/* THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
 * A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - Simon Marty
 */

#include <stdio.h>
#include <stdlib.h>

typedef struct _seg
{
    int bits[256];
    struct _seg *next;
} seg;

typedef struct
{
    seg *segpt;
    int intnum;
    int bitnum;
} coordinate;

void marknonprime(int j);

int testprime(int j);

void sieve(int n);

void computeTriplePrime(int n, int k, int m);

seg *whichseg(int j);

int whichint(int j);

int whichbit(int j);

coordinate getcoord(int j);

void markcoord(coordinate c);

int testcoord(coordinate c);

coordinate incrcoord(coordinate c, int inc);

int whichnum(coordinate c);

void initializeList();

int countPrimes(int n);

void printPrimes(int n);

int checkTriplePrime(int i, int n, int k, int m);

int segmentCount;
seg *head;

int main(int argc, char *argv[])
{
    seg *p;
    if (argc != 2)
        exit(EXIT_FAILURE);
    int N = atoi(argv[1]);

    segmentCount = N / (2 * 8192) + 2;
    head = NULL;

    for (int i = 0; i < segmentCount; i++)
    {
        p = (seg *) malloc(sizeof(seg));
        p->next = head;
        head = p;
    }

    initializeList();
    printf("Calculating odd primes up to %u\n", N);
    sieve(N);

    printf("Found %d odd primes\n", countPrimes(N) - 1);

    printf("Enter two even numbers for triple prime differential\n");


    for (int k, m; scanf("%d %d", &k, &m) == 2;)
    {
        computeTriplePrime(N, k, m);
    }
    exit(EXIT_SUCCESS);
}

void printPrimes(int n){
    if(n < 2) return;

    printf("2 ");

    for(int i = 1; i <= n; i = i + 2) {
        if( testprime(i))
            printf("%d ", i);
    }
}

int countPrimes(int n)
{
    if (n < 2)
    {
        return 0;
    }
    int primeCount = 1;

    for (int i = 3; i <= n; i += 2)
    {
        if (testprime(i)) primeCount++;
    }

    return primeCount;
}

void sieve(int n)
{
    marknonprime(1);
    int i, j;

    for(int k = 3; k*k <= n; k = i + 2)
    {
        for (i = k; i <= n; i++)
        {
            if (testprime(i) == 1) { break; }
        }

        for (j = 2 * i; j <= n; j = j + i)
        {
            if (j % 2 != 0)
                marknonprime(j);
        }
    }
}

void initializeList()
{
    for (int i = 0; i < segmentCount; i++)
    {
        seg *p = head;

        while (p != NULL)
        {
            for (int j = 0; j < 256; j++)
            {
                p->bits[j] = 0;
            }
            p = p->next;
        }
    }
}

void computeTriplePrime(int n, int k, int m)
{
    unsigned int numSolutions = 0;
    unsigned int largestTriplePrime = -1;

    for (int i = 3; i < n; i += 2)
    {
        if(checkTriplePrime(i, n, k, m)) {
            numSolutions++;
            largestTriplePrime = i;
        }
    }
    if (numSolutions > 0)
    {
        printf("%d solutions, largest: (%d, %d, %d)\n", numSolutions, largestTriplePrime,
               largestTriplePrime + k, largestTriplePrime + m);
    } else
    {
        printf("0 solutions.");
    }
}

int checkTriplePrime(int i, int n, int k, int m)
{
    if((i + k) <= n && (i + m) <= n) 
    {
            if (testprime(i) && testprime(i + k) && testprime(i + m))
            {
                return 1;
            }
    }

    return 0;
}

seg *lastSeg = NULL;
int lastSegIndex = 0;

seg *whichseg(int j)
{
    j = ((j - 1) / 2) / 8192;
    int i = 0;
    seg *p = head;
    if (j > lastSegIndex && lastSeg != NULL)
    {
        i = lastSegIndex;
        p = lastSeg;
    }


    for (; i < j; i++)
    {
        p = p->next;
    }

    lastSeg = p;
    lastSegIndex = i;
    return p;

}

int whichint(int j)
{
    return (((j - 1) / 2) / 32) % 256;
}

int whichbit(int j)
{
    return (((j - 1) / 2) % 32);
}

coordinate getcoord(int j)
{
    coordinate c;
    c.segpt = whichseg(j);
    c.intnum = whichint(j);
    c.bitnum = whichbit(j);

    return c;
}

void markcoord(coordinate c)
{
    unsigned int flipper = 1;
    flipper = flipper << c.bitnum;
    c.segpt->bits[c.intnum] = c.segpt->bits[c.intnum] | flipper;
}

int testcoord(coordinate c) {
    unsigned int testBit = 1;
    testBit = testBit << c.bitnum;
    return (c.segpt -> bits[c.intnum] & testBit) == 0;
}

void marknonprime(int j)
{
    if(j % 2 == 0) return;
    markcoord(getcoord(j));
}

int testprime(int j)
{
    if(j % 2 == 0) return 0;
    testcoord(getcoord(j));
}

coordinate incrcoord(coordinate c, int inc)
{
    return getcoord(whichnum(c) + (inc) / 2);
}

int whichnum(coordinate c)
{
    int segmentIndex = 0;
    seg *p = head;
    for (; segmentIndex < segmentCount; segmentIndex++)
    {
        if (p == c.segpt)
        {
            break;
        }
        p = p->next;
    }
    return (int) ((8192 * segmentIndex) + (32 * c.intnum) + c.bitnum);
}
