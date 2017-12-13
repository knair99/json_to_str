jd = {
	"name": "Cake",
	"ppu": 5,
	"cpu": 5.55,

	"batters":
		{
			"batter":
				[
					{ "id": "1001", "type": "Regular" },
					{ "id": "1002", "type": "Chocolate" },
				]
		},
	"topping":
		[
			{ "id": "5001", "type": "None" },
			{ "id": "5002", "type": "Glazed" },
		],
}


print "The input:"
print str(jd)

q = "'"


def gf(x):
	#print type(x)
	if 'float' in str(type(x)):
		var = ('{0:.2f}'.format(x))
		return var
	elif 'int' in str(type(x)):
		var =   ('{:d}'.format(x))
		return var
	elif 'str' in str(type(x)):
		var = q + x + q
		return var	
	elif 'dict' in str(type(x)):
		st = "{"
		for key, value in x.items():
			st += gf(key) + ": " + gf(value)
			if key != x.keys()[-1]:
				 st += ", "
		return st+ "}"
	elif 'list' in str(type(x)):
		var = str(x)
		st = "["
		for el in x:
			st += gf(el) 
			if el != x[-1]:
				st += ", "
		return st + "]" 
	else:
		return x

sj = "{"
for key, value in jd.items():
	sj +=   gf(key) + ": " + gf(value) 
	if key != jd.keys()[-1]:
		sj += ", "

sj += "}"

print "The output:"
print str(sj)


