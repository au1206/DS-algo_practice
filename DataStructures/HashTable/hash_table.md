
# Hash Tables
[source: William Fiset Youtube](https://github.com/williamfiset/data-structures/blob/master/slides/hashtable/hashtable.pdf)


##What is a hash table?
A Hash table (HT) is a data structure that provides a mapping from keys to values using a technique called hashing.

A hash function H(x) is a function that maps a key ‘x’ to a whole number in a fixed range.


## PROPERTIES OF A HASH FUNCTION

- If H(x) = H(y) then objects x and y might be equal, but if H(x) ≠ H(y) then x and y are certainly not equal.

    This means that instead of comparing x and y directly a smarter approach is to first compare their hash values, 
    and only if the hash values match do we need to explicitly compare x and y.


- A hash function H(x) must be deterministic. This means that if H(x) = y then H(x) must always produce y and never another value. 

- We try very hard to make uniform hash functions to minimize the number of hash collisions.



## GENERAL INSERTION IN HASH TABLE
```

x = 1
keyHash = H1(k) mod N
index = keyHash
while table[index] != null:
    index = (keyHash + P(k,x)) mod N
    x = x + 1

insert (k,v) at table[index]

----------------------------------------------
P(x) : is the probing function
H1(k): is the hash function 1
```

## Operation Average Worst:

| Operation  | Average Time | Worst Case |
| :----------:|:----------: | :---------:|
| Insertion  |  O(1)*       |  O(n)      |
| Removal    | O(1)*        |  O(n)      |
| Search     | O(1)*        |  O(n)      |

* The constant time behaviour attributed
to hash tables is only true if you have
a good uniform hash function! 

---

## HASH COLLISIONS
A hash collision is when two objects x, y hash to the same value (i.e. H(x) = H(y)).

### DEALING WITH HASH COLLISIONS

- Separate chaining deals with hash collisions by maintaining a data structure (usually a linked list) to hold all the 
  different values which hashed to a particular value.

- Open addressing deals with hash collisions by finding another place within the hash table for the object to go by 
  offsetting it from the position to which it hashed to.



### Open addressing
When using open addressing as a collision resolution technique the key-value pairs are stored in the table itself as 
opposed to a data structure like in separate chaining.


This means we need to care a great deal about the size of our hash table and how many elements are currently in the 
table.

**Load factor = items in table / size of table**

**NOTE:** The O(1) constant time behaviour attributed to hash tables assumes the load factor (α) is kept below a certain 
fixed value. This means once α > threshold we need to grow the table size (ideally exponentially, e.g. double).


### Open addressing main idea
When we want to insert a key-value pair (k,v) into the hash table we hash the key and obtain an original position for 
where this key-value pair belongs, i.e H(k).

If the position our key hashed to is occupied, try another position in the hash table by offsetting the current position 
subject to a probing sequence P(x). Keep doing this until an unoccupied slot is found.

**Linear probing:**
P(x) = ax + b where a, b are constants

**Quadratic probing:**
P(x)= ax² + bx + c, where a,b,c are constants

**Double hashing:**
P(k,x) = x*H2(k), where H2(k) is a secondary hash function

**Pseudo random number generator:**
P(k,x) = x*RNG(H(k),x), where RNG is a random number generator function seeded with H(k).


### Chaos of Cycles
Most randomly selected probing sequences modulo N will produce a cycle shorter than
the table size. This becomes problematic when you are trying to insert a key-value pair and all the buckets on the cycle 
are occupied because you will get stuck in an infinite loop!


#### For Linear Probing
The infinite loop problem is solved when a and N are relatively prime. Two numbers are relatively prime if their 
Greatest Common Denominator (GCD) is equal to one. Hence, when GCD(a,N) = 1 the probing function P(x) be able to 
generate a complete cycle and we will always be able to find an empty bucket!

A common choice for P(x) is P(x) = 1x

Since GCD(N,1) = 1 no matter the choice
of N (table size)


#### For Quadratic Probing
1) Let P(x) = x² keep the table size a prime number > 3 and also keep α ≤ ½
2) Let P(x) = (x² + x)/2 and keep the table size a power of two
3) Let P(x) = (-1x)*x² and keep the table size a prime N where N ≡ 3 mod 4



#### For Double Hashing
DoubleHashing is a probing method which probes according to a constant multiple of another hash function, specifically:

P(k,x) = x*H2(k), where H2(k) is a
second hash function 


To fix the issue of cycles in double hashing pick the table size to be a **prime number** and also compute the value of δ


**δ = H2(k) mod N**

If δ = 0 then we are guaranteed to be stuck in a cycle, so when this happens set δ = 1

**Note:** Notice that 1 ≤ δ < N and GCD(δ,N) = 1 since N is prime. Hence, with these conditions we know that modulo N 
the sequence H1(k), H1(k)+1δ, H1(k)+2δ, H1(k)+3δ, H1(k)+4δ, … is certain to have order N 


**To resize while double hashing one strategy is compute 2N and find the next prime above this value.**