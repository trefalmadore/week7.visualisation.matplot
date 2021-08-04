from matplotlib import pyplot as plt

label = [ 'mici', 'tochitura', 'cozonac', 'ciorba de burta']
sizes = [ 10 , 20, 50 ,20]
color =[ 'blue' , 'red' , 'purple', 'pink']
explodes =(0,0.2,0,0.1)
plt.pie( sizes, labels=label ,explode = explodes, colors = color)
plt.title('Foods I cooked')
plt.show()