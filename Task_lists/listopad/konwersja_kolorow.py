def RGB2HEX(R,G,B):
	return "#{0:02x}{1:02x}{2:02x}".format(R,G,B)

def HEX2RGB(HEX):
	h = HEX.lstrip('#')
	return tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))