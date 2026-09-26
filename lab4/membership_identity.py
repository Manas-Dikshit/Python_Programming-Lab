# Membership and identity operators: in, not in, is, is not
text = "python"
nums = [10, 20, 30]
a = 17
b = a

print("'th' in 'python'          :", "th" in text)
print("'z' not in 'python'       :", "z" not in text)
print("20 in [10, 20, 30]        :", 20 in nums)
print("5 not in [10, 20, 30]     :", 5 not in nums)
print("a is b (same object)      :", a is b)
print("a is not b                :", a is not b)
print("[10] is [10] (new object) :", [10] is [10])
