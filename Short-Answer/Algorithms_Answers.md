#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n)

    The while loop would be O(n^3). But inside the loop, we are getting closer to the base case by O(n^2) with each iteration. This can be expressed as n^3 / n^2 = n. As a result, the time complexity is O(n).

b) O(n log n) ( it might be O(n^2)... )

    This section of code has a "for" loop going through n elements, and inside this loop there is a "while" loop that goes through half as many elements. The inner "while" loop doubles j every time, so j will approach n much more quickly than j will increase. The inner "while" loop therefore has a O(log n) runtime, and the outer loop must do this n times. As a result, the total runtime is O(n log n).

c) O(n)

    The number of recursive calls made is approximately n. Increasing n increases the number linearly. So, O(n)

## Exercise II

Start at floor 1 because 0 is ground and go up until we are at a floor where the egg breaks. This linear strategy minimizes broken eggs but not dropped eggs.

A binary strategy minimizes dropped eggs. Start at the middle floor. If the egg breaks, eliminate the top half of the building from consideration and go to the midpoint of the remaining half. Or, if the egg does not break, eliminate the lower half and go up to the middle of the remaining top half. When the egg breaks, eliminate all above floors. In the remaining space, binary search for a floor where the egg does not break and eliminate all below floors. Do this until one floor remains.

With this strategy, the specific floor can be determined in O(log n) time complexity.
