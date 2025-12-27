# Solution – Part 1

## Description
This solution processes a sequence of movement instructions and tracks a numeric code
that is updated step by step. Each instruction consists of a direction (`R` or another
character) followed by a number indicating how much the code should change.

The code is always kept within the range **0–99** using modular arithmetic.
Whenever the code becomes exactly **0**, a counter is incremented.

---

## Approach
1. Split the input data into individual instructions.
2. Initialize the code with a starting value of `50`.
3. For each instruction:
   - Extract the numeric value.
   - Increase the code if the instruction starts with `R`, otherwise decrease it.
   - Normalize the code to stay within the range `0–99`.
4. Count how many times the code reaches `0`.
5. Print the final count.

---

## Key Concepts
- String parsing
- Conditional logic
- Loops
- Modular arithmetic
- Counter tracking

---

## Time Complexity
- **O(n)**, where `n` is the number of instructions.

---

## Notes
This implementation focuses on clarity and correctness rather than execution speed,
and it reflects a step-by-step simulation of the problem logic.
