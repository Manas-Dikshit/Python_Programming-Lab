# 24. Compare aliases and copies (shallow vs nested)
marks = [60, 75]
alias = marks                   # same object
copy = marks.copy()             # separate object
alias[0] = 90
print("marks:", marks)
print("alias:", alias)
print("copy :", copy)            # unchanged: separate list

nested = [[60], [75]]
alias2 = nested
shallow = nested.copy()         # outer list copied, inner lists shared
alias2[0][0] = 90
print("nested :", nested)
print("shallow:", shallow)      # inner list changed too
