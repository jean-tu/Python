import md5

m = md5.new()
m.update("Nobody inspects")
m.update(" the spammish repetition")
m.digest()
