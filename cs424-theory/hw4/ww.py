#!/usr/bin/env python3

# Simon Marty
# ww.py


import heapq


def reduce(a, b):
    # Return prefix-reduced form of strings a and b, or None.
    n = min(len(a), len(b))
    return None if a[:n] != b[:n] else (a[n:], b[n:])


def seq2list(seq):
    # Convert (3, (2, (1, None))) to [1, 2, 3]
    ret = []
    while seq != None:
        ret.append(seq[0])
        seq = seq[1]
    return ret[::-1]


def pqpair(r):
    # Order our pq to prefer exploring partial matches
    # with a minimal amount of unmatched text.
    return (len(r[0])+len(r[1]), r)


def mpcp_quiet(dominos, B=10000):
    """
    Given a list of dominos, try to find an MPCP match.
    That is, a match starting with a copy of dominos[0].
    If found, the match is returned as a list of indices.
    The integer B bounds the number of steps searched.
    If there is definitely no match, returns None.
    If we ran out of steps, returns B.
    """
    pq, seq = [], {}
    start = reduce(dominos[0][0], dominos[0][1])
    if start:
        heapq.heappush(pq, pqpair(start))
        seq[start] = (0, None)
    goal = ('', '')
    for step in range(B):
        if len(pq) == 0:  # no solution!
            return None
        thispair = heapq.heappop(pq)[1]
        thisseq = seq[thispair]
        if thispair == goal:  # found it! return match
            return seq2list(thisseq)
        # Try extending thispair with each domino
        for i in range(len(dominos)):
            dom = dominos[i]
            r = reduce(thispair[0]+dom[0], thispair[1]+dom[1])
            if r and (r not in seq):  # new reduced pair
                seq[r] = (i, thisseq)
                if r == goal:  # found it!
                    return seq2list(seq[r])
                # save r for later
                heapq.heappush(pq, pqpair(r))
    # ran out of steps
    return B


def mpcp(dominos, B=10000):
    """
    Run mpcp_quiet(dominos, B), and print the result.
    This function returns nothing.
    """
    print('Solving MPCP:',
          ' '.join("%s/%s" % d for d in dominos))
    sol = mpcp_quiet(dominos, B)
    if sol == None:
        print("NO MATCH (no solution exists)")
    elif sol == B:
        print("NO MATCH FOUND (gave up after %d steps)" % B)
    else:
        print("FOUND MATCH:", ' '.join(str(i) for i in sol))
        print(' '.join(dominos[i][0] for i in sol))
        print(' '.join(dominos[i][1] for i in sol))
    print()  # return nothing


# page227 = [('b', 'ca'), ('a', 'ab'), ('ca', 'a'), ('abc', 'c')]
# # mpcp(page227) # no solution

# # Rearranged, moved the second domino to the front
# page227b = [('a', 'ab'), ('b', 'ca'), ('ca', 'a'), ('abc', 'c')]
# # mpcp(page227b) # finds the match in the book

# # Exercise 5.3, Sipser page 239
# page239 = [('ab', 'abab'), ('b', 'a'), ('aba', 'b'), ('aa', 'a')]
# # mpcp(page239)  # finds the match in the book

# TODO: edit L_dominos, w, and (maybe) B.

L_dominos = [
    ('a', 'a'), ('b', 'b'), ('#', '#'), ('#S#', '#'), ('S', 'S'),

    ('Sa', 'aS'), ('Sb', 'bS'),
    ('bS', 'BS'), ('BS', 'SB'),
    ('Ba', 'aB'), ('Bb', 'bB'),
    ('bB#', '#'),

    ('aS', 'AS'), ('AS', 'SA'),
    ('Aa', 'aA'), ('Ab', 'bA'),
    ('aA#', '#')
]


def dominos(w):
    return [('#', '#S'+w+'#')] + L_dominos


if __name__ == "__main__":
    # This program tests itself, feel free to add more test cases
    test_cases = ['abaaba', 'abab', 'bbbbbb', 'abaa', 'bbaaaabaab', 'aaaaaa']
    B = 10000

    for w in test_cases:

        if type(mpcp_quiet(dominos(w), B)) is list:
            print(f'YES for {w}')

        else:
            print(f'NO  for {w}')
