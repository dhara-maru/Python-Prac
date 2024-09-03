from matplotlib import pyplot as plt
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],
label="Hasee toh Phasee",width=.5)
plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],
label="Meri Pyaari Bindu", color='r',width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Collection (crores)')
plt.title('Movie Collection Information')
plt.show()
