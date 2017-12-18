# -*- coding: utf-8 -*-
"""
Created on December 2017
@author: Rémi Demol (github.com/remidemol)
"""
#Python imports
import matplotlib.pyplot as plt

#Options
textFontSize=12

zmax = 4.2

#trait bas
r1 = [0.0, 1]
z1 = [.75, .75]

#trait haut
r2 = [0.0, 0.72]
z2 = [0.27, 0.27]

#mur
r3 = [0.0, 0.72]
z3 = [2.0, 2.0]

#mur bas
r4 = [0.72, 0.72]
z4 = [0., 2.0]

#-------SUBPLOT#1
plt.figure(figsize=(5,8))

plt.subplot(1,2,1)

plt.plot(r1,z1,'k--')
plt.plot(r2,z2,'k--')
plt.plot(r3,z3,'k--')
plt.plot(r4,z4,'k--')

#Texte db
#Experimental data
plt.text(0.5, 3.1, 'Exp. : $d_b$ = 5.5', style='italic',bbox={'facecolor':'grey', 'alpha':0.5, 'pad':10}, horizontalalignment='center' , verticalalignment='center')
plt.text(0.5, 1.5, 'Exp. : $d_b$ = 5.0', style='italic',bbox={'facecolor':'grey', 'alpha':0.5, 'pad':10}, horizontalalignment='center' , verticalalignment='center')

#Simulation results
plt.text(r4[1]*0.5*0.5, 0.5*z2[1], '$(I)$',horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)
plt.text(r4[1]*0.5+0.1, 0.5*z2[1], '4.9' , horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)

plt.text(r4[1]*0.5*0.5, 0.5*(z1[1]-z2[1])+z2[1], '$(II)$' , horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)
plt.text(r4[1]*0.5+0.1, 0.5*(z1[1]-z2[1])+z2[1], '6.2' , horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)

plt.text(r4[1]*0.5*0.5, 0.5*(z3[1]-z1[1])+z1[1]-0.2, '$(III)$' , horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)
plt.text(r4[1]*0.5+0.1, 0.5*(z3[1]-z1[1])+z1[1]-0.2, '5.3' , horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)

plt.text(0.5*0.5, 0.5*(4.2-z3[1])+z3[1]-0.3, '$(IV)$' , horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)
plt.text(0.5+0.1, 0.5*(4.2-z3[1])+z3[1]-0.3, '5.6' , horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)

plt.text(0.5*(1-r4[1])+r4[1], 0.5*z1[1]+0.2, '$(V)$' , horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)
plt.text(0.5*(1-r4[1])+r4[1], 0.5*z1[1], '7.0' , horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)

x = [0,  0.5,  1]
my_xticks = ['0','0.5','1']
plt.xticks(x, my_xticks)

y = [0,  0.5,  1,1.5, 2,2.5, 3,3.5, 4]
my_yticks = ['0','0.5','1','1.5','2','2.5','3','3.5','4']
plt.yticks(y, my_yticks)

#Axis
plt.xlabel('$r/R$')
plt.ylabel('$z/D$')
plt.axis([0, 1, 0, zmax])
plt.title('$d_b$ [mm] (50k)')

#-------SUBPLOT#2
plt.subplot(1,2,2)

plt.plot(r1,z1,'k--')
plt.plot(r2,z2,'k--')
plt.plot(r3,z3,'k--')
plt.plot(r4,z4,'k--')

#Texte db
#Experimental data
plt.text(0.5, 3.1, 'Exp. : $d_b$ = 5.5', style='italic',bbox={'facecolor':'grey', 'alpha':0.5, 'pad':10}, horizontalalignment='center' , verticalalignment='center')
plt.text(0.5, 1.5, 'Exp. : $d_b$ = 5.0', style='italic',bbox={'facecolor':'grey', 'alpha':0.5, 'pad':10}, horizontalalignment='center' , verticalalignment='center')

#Simulation results
plt.text(r4[1]*0.5*0.5, 0.5*z2[1], '$(I)$',horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)
plt.text(r4[1]*0.5+0.1, 0.5*z2[1], '4.6' , horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)

plt.text(r4[1]*0.5*0.5, 0.5*(z1[1]-z2[1])+z2[1], '$(II)$' , horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)
plt.text(r4[1]*0.5+0.1, 0.5*(z1[1]-z2[1])+z2[1], '6.0' , horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)

plt.text(r4[1]*0.5*0.5, 0.5*(z3[1]-z1[1])+z1[1]-0.2, '$(III)$' , horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)
plt.text(r4[1]*0.5+0.1, 0.5*(z3[1]-z1[1])+z1[1]-0.2, '5.3' , horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)

plt.text(0.5*0.5, 0.5*(4.2-z3[1])+z3[1]-0.3, '$(IV)$' , horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)
plt.text(0.5+0.1, 0.5*(4.2-z3[1])+z3[1]-0.3, '5.5' , horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)

plt.text(0.5*(1-r4[1])+r4[1], 0.5*z1[1]+0.2, '$(V)$' , horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)
plt.text(0.5*(1-r4[1])+r4[1], 0.5*z1[1], '6.6' , horizontalalignment='center' , verticalalignment='center' , fontsize=textFontSize)

x = [0,  0.5,  1]
my_xticks = ['0','0.5','1']
plt.xticks(x, my_xticks)

cur_axes = plt.gca()
cur_axes.axes.get_yaxis().set_ticklabels([])

#Axis
plt.xlabel('$r/R$')
plt.axis([0, 1, 0, zmax])
plt.title('$d_b$ [mm] (150k)')

#Show graph
plt.show()
