import matplotlib.pyplot as plt
Genres = [1,2,3,4,5]
Indian_Classical =[7,8,6,11,7]
Bollywood = [2,3,4,3,2]
Dance =[7,8,7,2,2]
Desi_HipHop = [8,5,7,8,13] 
plt.plot([],[],color='m', label='Indian Classical', linewidth=5)
plt.plot([],[],color='c', label='Bollywood', linewidth=5)
plt.plot([],[],color='r', label='Dance', linewidth=5)
plt.plot([],[],color='k', label='Desi HipHop', linewidth=5)
plt.stackplot(Genres, Indian_Classical,Bollywood,Dance,Desi_HipHop, colors=['r','m','k','c'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Music Genre Popularity Area Plot ')
plt.legend()
plt.show()