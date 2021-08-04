from matplotlib import pyplot as plt

label = [ 'mici', 'tochitura', 'cozonac', 'ciorba de burta', 'salrmale', 'dulciuri']
sizes = [ 10 , 20, 50 ,20,15,35]
color =[ 'blue' , 'red' , 'purple', 'pink','orange','grey']
explodes =(0,0,0,0,0,0.1)
plt.pie( sizes, labels=label ,explode = explodes, colors = color)
plt.title('Food wich I like to eat')
plt.show()