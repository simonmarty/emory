## This is a python3 program. Try running it with:
##
##    python3 MPCP.py
##
## You can also use this more interactively, see MPCP-demo.txt
##
## For homework problems you want to edit L_dominos, a list of pairs
## of strings, defined below.
##
## If you don't have python, you may prefer a "live notebook"
## version of this at https://github.com/mgrigni/cs424

# Here we define an MPCP solver, with two versions:
#
#    mpcp_quiet(dominos, B) -- quietly returns something
#    mpcp(dominos, B)       -- prints result, returns nothing
#
# 'dominos' is a list of dominos, where a domino is a pair of strings
# (as described by Sipser, see some examples below).
# These solvers look for a match starting with the first domino.
# 'B' is an integer bounding the length of our search, you may omit
# it to use a default value.

# First, a few helper functions
def reduce(a, b):
  # Return prefix-reduced form of strings a and b, or None.
  n = min(len(a), len(b))
  return None if a[:n]!=b[:n] else (a[n:], b[n:])

def seq2list(seq):
  # Convert (3, (2, (1, None))) to [1, 2, 3]
  ret = []
  while seq != None:
    ret.append(seq[0])
    seq = seq[1]
  return ret[::-1]

import heapq
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
    if len(pq)==0: # no solution!
      return None
    thispair = heapq.heappop(pq)[1]
    thisseq = seq[thispair]
    if thispair == goal: # found it! return match
      return seq2list(thisseq)
    # Try extending thispair with each domino
    for i in range(len(dominos)):
      dom = dominos[i]
      r = reduce(thispair[0]+dom[0], thispair[1]+dom[1])
      if r and (r not in seq): # new reduced pair
        seq[r] = (i, thisseq)
        if r==goal: # found it!
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
  if sol==None:
    print("NO MATCH (no solution exists)")
  elif sol==B:
    print("NO MATCH FOUND (gave up after %d steps)" % B)
  else:
    print("FOUND MATCH:", ' '.join(str(i) for i in sol))
    print(' '.join(dominos[i][0] for i in sol))
    print(' '.join(dominos[i][1] for i in sol))
  print()  # return nothing

## Examples:

# Example from Sipser page 227
page227 = [('b', 'ca'), ('a', 'ab'), ('ca', 'a'), ('abc', 'c')]
# mpcp(page227) # no solution

# Rearranged, moved the second domino to the front
page227b = [('a', 'ab'), ('b', 'ca'), ('ca', 'a'), ('abc', 'c')]
# mpcp(page227b) # finds the match in the book

# Exercise 5.3, Sipser page 239
page239 = [('ab', 'abab'), ('b', 'a'), ('aba', 'b'), ('aa', 'a')]
# mpcp(page239)  # finds the match in the book

# Examples with no solution
# mpcp([('b', 'baaab'), ('aa', '')]) # no solution (solver is definite)
# mpcp([('b', 'baab'), ('aa', '')]) # solver gives up

## Language defined by L_dominos:
#
# This last section defines a language L (see comments below).
#
# As an exercise, you may be asked to modify the list L_dominos (below)
# so that L becomes some other language.
#
# TODO: edit L_dominos, w, and (maybe) B.

L_dominos = [
  # as given, defines L = {w in {a,b}*: w has an odd number of b's}
  ('a', 'a'), ('b', 'b'), ('#', '#'),
  ('Sa', 'S'), ('Sb', 'T'),
  ('Ta', 'T'), ('Tb', 'S'), ('#T#', '#')
]

# You (or a grader!) may pick w, an input string in {a,b}*
w = 'ababab'

# You may also pick B (depending on w), large enough to find a
# match if there is one. This B suffices for our examples:
B = 10000

# You should not need to edit anything below.

# For a given input string w, we define dominos(w) by creating a new
# first domino ('#', '#Sw#'), and adding that to the front of L_dominos.
# This 'S' looks like the start state in Sipser's reduction (from A_TM to MPCP).
# However, for homework problems you are *not* required to use Sipser's method,
# in particular your dominos do not need to simulate a Turing machine.
def dominos(w):
  return [('#', '#S'+w+'#')] + L_dominos

# L_dominos defines this language:
#    L = { w in {a,b}*: dominos(w) has a match }.
#
# If a match exists, and B is large enough, then mpcp(dominos(w), B)
# will find the match.

# If the user runs "python MPCP.py" from the command line, then just
# do the MPCP example determined by L_dominos, w, and B:
if __name__ == "__main__":
  mpcp(dominos(w), B)
