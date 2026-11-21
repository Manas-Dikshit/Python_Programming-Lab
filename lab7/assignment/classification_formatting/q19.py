# 19. Expand tabs and encode/decode UTF-8 text
print("expandtabs(4):", repr("ID\tName".expandtabs(4)))

data = "café".encode("utf-8")
print("bytes        :", data)
print("decoded      :", data.decode("utf-8"))
