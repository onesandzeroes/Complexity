# Exercise 5.2
## Order of growth of `MakeCdfFromList`

Making the `Hist` (through `MakeHistFromList()`) is **O(n)**: need to go
through the list of items once, and setting the dictionary
(using `hist.Incr()`) is **O(1)** on average (although **O(n)** in the worst
case?). If setting the dictionary is assumed to be **O(n)**, then making
the `Hist` would be **O(n^2)**.

Making the `Cdf` (which ends up occuring through `MakeCdfFromItems()`) is
**O(nlogn)**, since the items in the `Hist` must be sorted. Then there are
some `append`s (**O(1)**) and another list comprehension **O(n)**.

Therefore overall order of growth of `MakeCdfFromList` is just **O(nlogn)**,
since this is the largest exponent?

### Simulations

Simulations (in `test_cdf.py`) seem to show that the order of growth is just
**O(n)**- maybe it's because of the best case **O(n)** performance of timsort?
