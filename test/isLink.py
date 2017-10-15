def is_link(kind):
  kind.strip() #remove any whitespace that may be in the string
  if kind == "Link":
    return 1
  return 0 #else return false b/c it's something else

print(is_link("Link"))
print(is_link("hello"))
