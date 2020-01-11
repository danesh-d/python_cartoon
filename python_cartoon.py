#! /usr/bin/env python

# Written by: Danesh Daroui

# Note: Python supports no tail call eliminaton, so here using tail recursion
# is just for presentation purposes and nothing serious! Or it is just for fun!

import collections;

# Unit test function.
def test(got, expected):
  if (got == expected) : prefix = ' OK '
  else: prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))




#################### Dynamic Programming ####################

# Kadane's algorithm to find the subarray in an array which has the maximum sum
# (dynamic programming).
def max_sub(a):
  max_sofar = max_end = 0;
  for x in a:
    max_end = max(0, max_end + x);
    max_sofar = max(max_sofar, max_end);
  return max_sofar;

# Having a coin of value s return the minimum number of coins in list l to
# change s (dynamic programming).
def min_coins(s, l):
  # Memoization space.
  m = [s] * (s + 1);

  # Cover the case when there is an exact coin for a change.
  m[0] = 0;

  for i in range(1, s + 1):
    for j in l:
      if (j <= i and m[i - j] + 1 < m[i]):
        m[i] = m[i - j] + 1;
  return m[s];

# Fibonacci series using dynamic programming approach with optimzed space.
def fib_dyn(n):
  if (n <= 1):
    return n;

  # Memoization space.
  a = 1;
  b = 1;
  c = 0;

  for i in range(1, n - 1):
    c = a + b;
    a = b;
    b = c;

  return c;




#################### Numbers ####################

# Return factorial of a number.
def fact(n):
  return n * fact(n - 1) if (n > 0) else 1;

# Return factorial of a number (tail recursion).
def fact_tr(n, r):
  return fact_tr(n - 1, r * n) if (n > 0) else r;

# Return fibonacci series result of a number.
def fib(n):
  if (n <= 1):
    return n;
  return fib(n - 1) + fib(n - 2);

# Return fibonacci series result of a number (tail recursion).
def fib_tr(n):
  def fib_help(a, b, n):
    return fib_help(b, a + b, n - 1) if (n > 0) else a;
  return fib_help(0, 1, n)

# Test if a list of numbers is in ascending order.
def ascend(l):
  if (not l): return True;
  for x in range(llen(l) - 1):
    if (l[x] >= l[x + 1]): return False;
  return True;

# Return all digits in a number as elements in a list.
def all_digits(n):
  if n < 10: return [n];
  else: return all_digits(n // 10) + [n % 10];

# Find all pairs in an array where their sum is exatly k.
def kpair_ht(l, k):
  ps = [];
  d = collections.defaultdict(bool);
  for x in l:
    if d[x]: ps += [(x, k - x)];
    d[k - x] = True;
  return ps;

# Having a list of numbers, we shuffle it and remove an item, the goal is
# to find the missed number from the original list.
def missed_num(l1, l2):
  mn = 0;
  for n in l1 + l2: mn ^= n;
  return mn;




#################### List Processing ####################

# Returns intersection between two lists.
def inter(l1, l2):
  if (l1 and l2):
    return [head(l1)] + inter(tail(l1), l2) if (head(l1) in l2) else\
                                                            inter(tail(l1), l2);
  else: return [];

# Returns difference between two lists.
def diff(l1, l2):
  return [i for i in l1 + l2 if i not in l1 or i not in l2];

# Remove all duplicated elements in a list and return the unique list.
def unique(l):
  if (l):
    if (head(l) in tail(l)): return unique(tail(l));
    else: return [head(l)] + unique(tail(l));
  else: return l;

# Return length of a list.
def llen(l):
  return llen(l[1:]) + 1 if l else 0;

# Returns tail of a list.
def tail(l):
  return l[1:];

# Returns head of a list.
def head(l):
  return l[0] if l else None;

# Returns last element of a list.
def last(l):
  return l[llen(l) - 1] if l else None;

# Returns foot of the list (the list without its last element).
def foot(l):
  return l[:llen(l) - 1];

# Returns sum of all elements in a list of numbers.
def ssum(l):
  return head(l) + ssum(tail(l)) if l else 0;

# Returns minimum value in a list.
def mmin(l):
  if (not l): return None;
  if (llen(l) == 1) : return head(l);
  else:
    return head(l) if (head(l) < mmin(tail(l))) else mmin(tail(l));

# Returns the maximum value in a list.
def mmax(l):
  if (not l): return None;
  if (llen(l)==1): return l[0];
  else:
    if (head(l) > mmax(tail(l))): return head(l);
    else: return mmax(tail(l));

# Returns reverse of a list.
def rev(l):
  return rev(tail(l)) + [head(l)] if l else l;

# Returns all elements in a list which are lesser than an element.
def lesser(l, e):
  return list(filter(lambda x: x < e, l));

# Returns all elements in a list which are greater than or equal to an element.
def greater(l, e):
  return list(filter(lambda x: x >= e, l));

# Return sorted list from an unsorted list using quick sort algorithm.
def qsort(l):
  return qsort(lesser(tail(l), head(l))) + [head(l)] +\
         qsort(greater(tail(l), head(l))) if l else l;

# Binary search over a sorted list.
def bsearch(l, e):
  if (not l): return False;
  elif (llen(l) == 1): return (l[0] == e);
  else:
    p = llen(l) // 2;
    mid = l[p];
    if (mid==e): return True;
    elif (mid > e): return bsearch(l[0 : p], e);
    else: return bsearch(l[p : llen(l)], e);




#################### String Processing ####################

# Compare two strings and return true, false or none according to the string
# lengths.
def strcmp(s1, s2):
  if (not s1 and s2): return True;
  elif (s1 and not s2): return False;
  elif (not s1 and not s2): return None;
  else: return strcmp(tail(s1), tail(s2));

# Find how many times a string pattern is repeated in a string.
def strpat(s, p):
  if (s and p):
    f = s.find(head(p));
    if (f == -1): return 0;
    else:
      ff = True;
      for i in range(f + 1, f + llen(p)):
        if (s[i] != p[i - f]):
          ff = False;
          break;
      if (ff): return strpat(s[f + 1:], p) + 1;
      else: return strpat(s[f + 1 : ], p);
  else: return 0;

# Returns true if the given string is a palindrome, otherwise returns false.
def pal(s):
  if (s):
    if ((head(s) == last(s)) and pal(s[1 : llen(s) - 1])): return True
    else: return False;
  else: return True;

# Returns all permutations of a string.
def perm(s):
  ps = [];
  if (llen(s) <= 1): ps = [s];
  else:
    for i in range(llen(s)):
      for p in perm(s[:i] + s[i + 1:]):
        ps += [s[i] + p];
  return ps;

# Returns all permutations of a string using generator.
def perm_gen(s):
  ps = [];
  if (llen(s) <= 1): ps = [s];
  else:
    for i in range(llen(s)):
      for p in perm(s[:i] + s[i + 1:]):
         yield [s[i] + p];

# O(n) algorithm to find if two strings are anagrams or not.
def anagrams(s1, s2):
  if (llen(s1) != llen(s2)): return False;
  d = collections.defaultdict(int);
  for x in s2: d[x] += 1;
  for x in s2:
    if (not d[x]): return False;
  return True;

# Two strings are shuffled and merged to create a new string, this function
# makes sure that the new string has the same order in the old strings or not.
def shuff(s1, s2, s3):
  if not (s1 and s2):
    if (s1 + s2 == s3):	return True;
    else: return False;
  if (head(s1) == head(s3) and shuff(tail(s1), s2, tail(s3))): return True;
  elif (head(s2) == head(s3) and shuff(s1, tail(s2), tail(s3))): return True;
  else: return False;

# Two strings are shuffled and merged to create a new string, this function
# makes sure that the new string has the same order in the old strings or not
# this implementation non-recursive and based on indices.
def shuff2(s1, s2, s3):
  if not(s1 and s2):
    if (s1 + s2 == s3):	return True;
    else: return False;
  i=collections.defaultdict(int);
  l1 = [];
  l2 = [];
  for x in s3:
    i[x] = s3.index(x);
  for x in s1:
    l1 += [i[x]];
  for x in s2:
    l2 += [i[x]];
  if (ascend(l1) and ascend(l2)): return True;
  else: return False;

# Remove duplicate characters in a string and keep only the first occurence.
def remove_dups(s):
  if (not s): return s;
  res = "";
  i = collections.defaultdict(int);
  for x in s:
    if (i[x] == 0):
      i[x] = 1;
      res += x;
  return res;

# Find the longest common suffix between two strings.
def lcs(s1, s2):
  return lcs(foot(s1), foot(s2)) + last(s1) if (last(s1) == last(s2) and
                                                llen(s1 + s2) > 0) else "";

# Find the longest common suffix between two strings (tail recursion).
def lcs_tr(s1, s2, common):
  return lcs_tr(foot(s1), foot(s2), last(s1) + common) if (last(s1) == last(s2)
                                                         and llen(s1 + s2) > 0)\
                                                       else common;

# Find the longest common prefix between two strings.
def lcp(s1, s2):
  return head(s1) + lcp(tail(s1), tail(s2)) if (head(s1) == head(s2) and
                                                llen(s1 + s2) > 0) else "";

# Find the longest common prefix between two strings (tail recursion).
def lcp_tr(s1, s2, common):
  return lcp_tr(tail(s1), tail(s2), common + head(s1)) if (head(s1) == head(s2)
                                                         and llen(s1 + s2) > 0)\
                                                       else common;

# Find longest common substring between two strings.
# The complexity is O(nm) where n and m are length of s1 and s2.
def l_com_s(s1, s2):
  s = "";  # Longest common string so far.
  common = "";
  for i in range(llen(s1)):
    for j in range(llen(s2)):
      # Common suffix at this stage using tail recursion.
      cs = lcs_tr(s1[:i], s2[:j], common);
      if (llen(cs) > llen(s)): s = cs;
  return s;

# Number of all occurences of a substring in a string.
def all_occs(s, ss):
  if (not s or not ss): return 0;
  if (s == ss): return 1;
  if (s[0] == ss[0]):
    n = 0;
    for i in range(llen(s) - 1):
      if (s[i] != ss[i]):
        break;
      n += 1;
    if (n == llen(s) - 1): return  1 + all_occs(s, ss[ n + 1:]);
    else: return all_occs(s, ss[n + 1:]);
  return all_occs(s, ss[1:]);




#################### Main Entry and Testing ####################
if __name__ == "__main__":
  l = [1, 2, 3, 7, 3, 3, 9, 45, 23, 32, 11, 45, 22];
  print("under test list: ", l);
  print("unit test results:");
  test(llen(l), 13);
  test(head(l), 1);
  test(head([]), None);
  test(last(l), 22);
  test(last([]), None);
  test(tail(l), [2, 3, 7, 3, 3, 9, 45, 23, 32, 11, 45, 22]);
  test(tail([]), []);
  test(foot(l), [1, 2, 3, 7, 3, 3, 9, 45, 23, 32, 11, 45]);
  test(foot([]), []);
  test(rev(l), [22, 45, 11, 32, 23, 45, 9, 3, 3, 7, 3, 2, 1]);
  test(ssum(l), 206);
  test(qsort(lesser(l, 3)), [1, 2]);
  test(qsort(greater(l, 9)), [9, 11, 22, 23, 32, 45, 45]);
  test(qsort(l), [1, 2, 3, 3, 3, 7, 9, 11, 22, 23, 32, 45, 45]);
  test(bsearch(qsort(l), 7), True);
  test(bsearch(qsort(l), 17), False);
  test(strpat("xxxxabcxxxabcxxxx", "abc"), 2);
  test(strpat("xxxxabcxxxabc", "abc"), 2);
  test(strpat("xxxxaabcxxxabcxxxx", "abc"), 2);
  test(strpat("aaaaaaaaaa", "a"), 10);
  test(strpat("aaaaaaaaaa:", "aa"), 9);
  test(strpat("xxxxabababzzzzzzz:", "abab"), 2);
  test(strpat("aaa:", "aa"), 2);
  test(pal("this"), False);
  test(pal("afa"), True);
  test(pal("abcddcba"), True);
  test(qsort(unique(l)), [1, 2, 3, 7, 9, 11, 22, 23, 32, 45]);
  test(mmin(l), 1);
  test(mmax(l), 45);
  test(perm("abc"), ["abc", "acb", "bac", "bca", "cab", "cba"]);
  test(fib(0), 0);
  test(fib(1), 1);
  test(fib(10), 55);
  test(fib_tr(0), 0);
  test(fib_tr(1), 1);
  test(fib_tr(10), 55);
  test(fib_dyn(0), 0);
  test(fib_dyn(1), 1);
  test(fib_dyn(10), 55);
  test(fact(0), 1);
  test(fact(1), 1);
  test(fact(5), 120);
  test(fact_tr(0, 1), 1);
  test(fact_tr(1, 1), 1);
  test(fact_tr(5, 1), 120);
  test(inter([1, 2, 3], [33, 3, 5, 2, 1, 55, 32, 16]), [1, 2, 3]);
  test(diff([1, 2, 3], [33, 3, 5, 2, 1, 55, 32, 16]), [33, 5, 55, 32, 16]);
  test(max_sub([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6);
  test(min_coins(11, [1, 3, 5]), 3);
  test(anagrams("danesh", "danehs"), True);
  test(anagrams("danesh", "sepideh"), False);
  test(kpair_ht([11, 34, 23, 42, 22, 0, 4, 21, 18, 1, -1], 22), [(0, 22),
                                                                 (18, 4),
                                                                 (1, 21),
                                                                 (-1, 23)]);
  test(missed_num([1, 2, 3, 4, 5, 6], [6, 2, 1, 3, 5]), 4);
  test(shuff("abc", "def", "adbecf"), True);
  test(shuff2("abc", "def", "adbecf"), True);
  test(ascend([34, 33, 25, 54, 73, 23, 5, 2]), False);
  test(ascend([33, 54, 73, 92, 542, 842]), True);
  test(remove_dups("tree traversal"), "tre avsl");
  test(all_digits(1234567890), [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]);
  test(all_occs('test', 'onetesttwotestthreetest'), 3);
  test(lcs('abcdefg', 'xxxyyyefg'), 'efg');
  test(lcs('abcdefg', []), '');
  test(lcs([], []), '');
  test(lcs_tr('abcdefg', 'xxxyyyefg', ""), 'efg');
  test(lcs_tr('abcdefg', [], ""), '');
  test(lcs_tr([], [], ""), '');
  test(lcp('efgabcd', 'efgxxxyyy'), 'efg');
  test(lcp('abcdefg', []), '');
  test(lcp([], []), '');
  test(lcp_tr('efgabcd', 'efgxxxyyy', ""), 'efg');
  test(lcp_tr('abcdefg', [], ""), '');
  test(lcp_tr([], [], ""), '');
  test(l_com_s('abcdefg', 'axxbcdyyy'), 'bcd');

  # Testing generator implementation of all permutations in a list using next().
  print("\nNow testing the generator of all permutations with __next__() command");
  pp = perm_gen("abc");
  print(pp.__next__());
  print(pp.__next__());
  print(pp.__next__());
  print(pp.__next__());
  print(pp.__next__());
  print(pp.__next__());

  # Testing generator implementation of all permutations in a list using an
  # iterator.
  print("\nNow testing the generator of all permutations with an iterator");
  gg = perm_gen("abc");
  for g in gg:
    print(g);

