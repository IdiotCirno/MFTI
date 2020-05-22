def euclid(x, y):
	if x%y:
		return euclid(y, x%y)
	return y

print(euclid(60, 140))