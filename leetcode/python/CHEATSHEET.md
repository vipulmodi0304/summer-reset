# 🧠 Python Cheat Sheet for Arrays & Hashing Problems

---

## 🔤 Strings

| Task                   | Code                                 | Notes                   |
| ---------------------- | ------------------------------------ | ----------------------- |
| Sort a string          | `sorted("eat")` → `['a', 'e', 't']`  | Returns list of chars   |
| Join list to string    | `"".join(['a', 'e', 't'])` → `"aet"` | Needed after sorting    |
| String → list of chars | `list("cat")` → `['c', 'a', 't']`    | Rarely used, but useful |
| Iterate over string    | `for c in s:`                        | Character by character  |
| Check char exists      | `'a' in s`                           | O(n) time               |
| String length          | `len(s)`                             | O(1)                    |

---

## 📦 Lists (Arrays)

| Task                  | Code                             | Notes                 |
| --------------------- | -------------------------------- | --------------------- |
| Create list           | `nums = [1, 2, 3]`               |                       |
| Add to end            | `nums.append(4)`                 |                       |
| Remove from end       | `nums.pop()`                     | Returns last element  |
| Iterate with index    | `for i, num in enumerate(nums):` |                       |
| Iterate by value      | `for num in nums:`               |                       |
| Check if value exists | `if 3 in nums:`                  | O(n)                  |
| Sort list             | `nums.sort()`                    | In-place              |
| Copy and sort         | `sorted(nums)`                   | Returns new list      |
| Reverse list          | `nums.reverse()`                 | In-place              |
| Slice list            | `nums[1:4]`                      | Index 1 to 3          |
| Two pointers          | `left, right = 0, len(nums) - 1` | Used in many patterns |

---

## 🧮 Dictionaries (Hash Maps)

| Task                | Code                      | Notes                 |
| ------------------- | ------------------------- | --------------------- |
| Create empty        | `m = {}`                  |                       |
| Add / update key    | `m['a'] = 1`              |                       |
| Increment key count | `m[c] = m.get(c, 0) + 1`  | Avoids key errors     |
| Check key exists    | `'a' in m`                | O(1)                  |
| Iterate keys/values | `for k, v in m.items():`  |                       |
| Get all keys        | `m.keys()` → `['a', 'b']` |                       |
| Get all values      | `m.values()` → `[1, 2]`   |                       |
| Compare maps        | `m1 == m2`                | Deep value comparison |

---

## 🧩 Sets

| Task               | Code           | Notes                |
| ------------------ | -------------- | -------------------- |
| Create set         | `s = set()`    |                      |
| Add to set         | `s.add(x)`     |                      |
| Check existence    | `if x in s:`   | O(1)                 |
| Remove item        | `s.remove(x)`  | Errors if not exists |
| Discard item       | `s.discard(x)` | No error             |
| Convert list → set | `set(nums)`    | Removes duplicates   |

---

## 🧰 Other Useful Tricks

| Task                              | Code                                                  | Notes                     |
| --------------------------------- | ----------------------------------------------------- | ------------------------- |
| Frequency map from string         | `for c in s: m[c] = m.get(c, 0) + 1`                  | Without Counter           |
| Reverse string                    | `s[::-1]`                                             | Slicing                   |
| Sort list of strings by frequency | `sorted(m.items(), key=lambda x: x[1], reverse=True)` | Used in Top K problems    |
| Remove duplicates                 | `list(set(nums))`                                     | Order not guaranteed      |
| Initialize 26-letter count array  | `[0] * 26`                                            | For lowercase letter freq |

---

## 🧩 Most Common Problem Patterns

| Problem                      | Pattern                  | What to Use              |
| ---------------------------- | ------------------------ | ------------------------ |
| Two Sum                      | Hash map of value: index | O(n) lookup              |
| Valid Anagram                | Frequency map            | Dict or sort             |
| Group Anagrams               | Map with sorted key      | Dict of lists            |
| Contains Duplicate           | Use Set                  | Fast check               |
| Longest Substring w/o Repeat | Sliding Window + Set     | Move left/right pointers |
| Top K Frequent Elements      | Dict + Sort or Heap      | Sort by value            |
| Product Except Self          | Prefix & Suffix arrays   | Avoid division           |
| Longest Consecutive Sequence | Set for fast lookup      | O(n) with set            |
