def is_photo(kind):
  kind.strip()
  if kind == "Photo":
    return 1
  return 0

print(is_photo("Link"))
print(is_photo("Photo"))
print(is_photo("Video"))
