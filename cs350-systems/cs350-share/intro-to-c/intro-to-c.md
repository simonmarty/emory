# Intro to C

## Strings

C has no strings. C has characters

``` 
char x;
x = 'a';
int y;
y = 5;
```

'a' and 5 are both literals here. Similarly, "Hello" is a string
literal.
A C string is an array of characters with a pointer starting at arr[0].
C string have a NULL character at the end. This is how the pointer finds where to stop.

#### System stack

|**Stack**|
|-----|
|Heap|
|<br/>X<br/><br/><br/>|
|BSS - Array is stored here|
|Data - Pointer is stored here|
|Text|

``` 
*name = 'H';
name[i]='e';
*(name + 1) = 'e';
name = 'Hello';
```

Another example

``` 
char *alpha;
char beta[6];
char gamma[];

beta[3];
*(beta + 3);
alpha[3];
```

## Booleans

C has no boolean variables. Numeric 0 is interpreted as false, anything else is interpreted as true. Example:

``` 
int a = 0;
if (a)
{
    return 1;
} else return 0;
```

will return 0.

There are **logical operators**:

| logical operators| Meaning|
|-------|---|
| `&&` | logical AND |
| <code>&#124; &#124; </code> |logical OR|
| `!` | logical NOT|

and **bitwise operators**

|bitwise operator|meaning| example|
|----|-----|---|
| `&` | AND |
|<code>&#124; </code> | OR |
| `^` | XOR |
| `~` | NOT |
| `<<` | bitshift left|
| `>>` | bitshift right|

### More bit operations

```
x |= (1 << 2)
if(x & (1 << C))

# include "types.h"
# define LARGE 1000
# define setbit(x, c) x |= (1 << c)

#ifdef

z = LARGE;
setbit(alpha, 5);
```
That last line gets translated to `alpha |= (1 << 5)` by the C precompiler

## GDB
- run
- print
- list
- break
- display
- up and down
- where