import numpy as np
import matplotlib.pyplot as plt


with np.load('x.npz') as data:
    x=data['x']
        
with np.load('TD_Reeds.npz') as data:
    sfMBSparse  = data['sfMBSparse']
    sfEulerS    = data['sfEulerSI']
    sfEulerOCI  = data['sfEulerOCI']
    sfSS        = data['sfSS']
    sfMBSiBig   = data['sfMBSiBig']
    sfMBSi      = data['sfMBSi']
    sfMB_trad   = data['sfMB_trad']


def subplots():
    fig, ax = plt.subplots(4,1, sharex=True)
    
    fig.set_size_inches(6,5)
    
    mid1 = int(sfMBSparse.shape[1]/3)
    mid2 =  int(2*sfMBSparse.shape[1]/3)
    trans_lab = 'Transient'
    
    ss_color = 'blue'
    trans_color = 'black'
    
    i=0
    ax[i].plot(x, sfSS, '--', color=ss_color, label='Stead State')
    ax[i].plot(x, sfMBSparse[:,0], '-g', label=trans_lab)
    ax[i].set_xlim(0, 8)
    ax[i].set_ylabel('ϕ')
    ax[i].set_title('Δt=0')
    ax[i].text(6.5,3, 'steady state')
    ax[i].text(3, 0.5, 'transient')
    ax[i].grid()
    #ax[i].legend(loc="upper right")
    
    #ax[i].spines['right'].set_visible(False)
    #ax[i].spines['top'].set_visible(False)
    
    
    i+=1
    ax[i].plot(x, sfSS, '--', color=ss_color)
    ax[i].plot(x, sfMBSparse[:,mid1], '-g')
    ax[i].set_title('    1')
    ax[i].set_xlim(0, 8)
    ax[i].set_ylabel('ϕ')
    ax[i].grid()
    ax[i].text(4,4.5, 'steady state')
    ax[i].text(2,1.5, 'transient')
    #ax[i].spines['right'].set_visible(False)
    #ax[i].spines['top'].set_visible(False)
    
    
    i+=1
    ax[i].plot(x, sfSS, '--', color=ss_color)
    ax[i].plot(x, sfMBSparse[:,mid2], '-g')
    ax[i].set_title('    2')
    ax[i].set_xlim(0, 8)
    ax[i].set_ylabel('ϕ')
    ax[i].grid()
    ax[i].text(4,4.5, 'steady state')
    ax[i].text(2,2.5, 'transient')
    #ax[i].spines['right'].set_visible(False)
    #ax[i].spines['top'].set_visible(False)
    
    
    i+=1
    ax[i].plot(x, sfSS, '--', color=ss_color)
    ax[i].plot(x, sfMBSparse[:,-1], '-g')
    ax[i].set_title('    3')
    ax[i].set_xlim(0, 8)
    ax[i].set_xlabel('Position [cm]')
    ax[i].set_ylabel('ϕ')
    ax[i].grid()
    ax[i].text(4,4.5, 'steady state')
    ax[i].text(2,2.5, 'transient')
    #ax[i].spines['right'].set_visible(False)
    #ax[i].spines['top'].set_visible(False)
    
    
    
    plt.tight_layout()

    #subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=2)
    
    #plt.show()
    plt.savefig('reeds.png', dpi=300)
    

def moive():
    fig,ax = plt.subplots()
        
    ax.grid()
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$\phi$')
    ax.set_title('Scalar Flux (ϕ)')

    import matplotlib.animation as animation

    line1, = ax.plot(x, sfMBSparse[:,0], '-k',label="MB-OCI-Big")
    #line2, = ax.plot(x, sfMB_trad[:,0], '-r',label="MB-OCI-Small")
    line3, = ax.plot(x, sfEuler[:,0], '-g',label="BE-SI")
    line4, = ax.plot(x, sfMBSi[:,0], '-b',label="MB-SI")
    line5, = ax.plot(x, sfMBSiBig[:,0], '-y',label="MB-SI-GPU")
    line6, = ax.plot(x, sfSS, '-p',label="SS")
    text   = ax.text(8.0,0.75,'') 
    ax.legend()
    plt.ylim(-0.2, 8.2)

    def animate(k):
        line1.set_ydata(sfMBSparse[:,k])
        #line2.set_ydata(sfMB_trad[:,k])
        line3.set_ydata(sfEuler[:,k])
        line4.set_ydata(sfMBSi[:,k])
        line5.set_ydata(sfMBSiBig[:,k])
        line6.set_ydata(sfSS)
        text.set_text(r'$t \in [%.1f,%.1f]$ s'%(dt*k,dt*(k+1)))

    simulation = animation.FuncAnimation(fig, animate, frames=N_time)

    writervideo = animation.PillowWriter(fps=250)
    simulation.save('td_reeds.gif') #saveit!
    
    
if __name__ == '__main__':
    subplots()
