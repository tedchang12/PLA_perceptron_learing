from bokeh.plotting import figure, output_file, show
def main():
	filek = open("TD.csv",mode='r')
	global filer
	filer = filek.readlines()
	x1=[]
	x2=[]
	y1=[]
	y2=[]
	for i in range(0,len(filer)):
		filer[i] = filer[i].split(",")
		filer[i][0] = int(filer[i][0])
		filer[i][1] = int(filer[i][1])
		filer[i][2] = int(filer[i][2])
		if(filer[i][2]==1):
			x1.append(filer[i][0])
			y1.append(filer[i][1])
		elif(filer[i][2]==-1):
			x2.append(filer[i][0])
			y2.append(filer[i][1])

	output_file("line.html")
	p = figure(x_range=(-10,10),y_range=(-10,10))
	p.circle(x1,y1,size=20, color="navy", alpha=0.5)
	p.square(x2,y2,size=20, color="red", alpha=0.5)
	w = [float(0),float(0)]
	Fa = [float(0),float(0)]
	global err
	err = True
	while(err):
		w[0],w[1],err = find_err(w[0],w[1])
		Fa[0]=1.0
		if(w[1]!=0):
			Fa[1]=(float(w[0])/float(w[1]))*-1
		else:
			Fa[1]=0
		#print(str(w[0])+"	"+str(w[1]))
		if(not err):
			p.line([Fa[0]*-10,Fa[0]*10], [Fa[1]*-10,Fa[1]*10], legend="Fa.", line_width=2)
			p.line([0,w[0]], [0,w[1]], legend="Fa.", line_width=2)
	show(p)
def find_err(xarc,yarc):
	if(xarc==0 and yarc==0):
		return filer[0][0],filer[0][1],True
	else:
		boltemp=False
		for i in range(0,len(filer)):
			if(filer[i][2]==1):
				if((filer[i][0]*xarc)+(filer[i][1]*yarc)<=0):
					boltemp=True
					#print(str(filer[i][0])+"	"+str(filer[i][1]))
					return filer[i][0]+xarc,filer[i][1]+yarc,boltemp
					break;
			elif(filer[i][2]==-1):
				if((filer[i][0]*xarc)+(filer[i][1]*yarc)>=0):
					boltemp=True
					#print(str(filer[i][0])+"	"+str(filer[i][1]))
					return filer[i][0]-xarc,filer[i][1]-yarc,boltemp
					break;
		if(boltemp==False):
			return xarc,yarc,boltemp
		

main()