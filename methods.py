from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np

def ask1():
    print('''For computing λ load factor, temperature coefficient and coefficient of severity of conditions are required.  
                ''')
    quesKn = str(input("1. Is the load factor (Kn) is defined for each element? (Y/n) "))

    quesKt = str(input('''
2. Is your PCB operating under normal conditions?
   Means that your device will not be operated outside the earth's atmosphere, or under high pressure or temperature etc. 
   Normal temperature defined in the range of 20-25 °C  (Y/n) '''))
    return quesKn, quesKt


def MTBF(failure_rate):
    if isinstance(failure_rate, float) == False:
        raise Exception("Incorrect value of Failure Rate! It must be float.")
    else:
        mtbf = 1 / failure_rate
        new_mtbf = float("{0:.1f}".format(mtbf))
        print("         MTBF of system is: ", new_mtbf, " ~ ", round(new_mtbf), " [hours]")
        return new_mtbf


def MTTF(total_operations, total_items):
    if (isinstance(total_operations, int) == False) and (isinstance(total_items, int) == False):
        raise Exception("Incorrect! Both values must be non-negative int!")
    else:
        mttf = total_operations / total_items
        new_mttf = float("{0:.1f}".format(mttf))
        print("         MTTF of system is: ", new_mttf, " ~ ", round(new_mttf), " [hours]")
        return new_mttf


def MTTR(total_use, total_repairs):
    if (isinstance(total_repairs, int) == False) and (isinstance(total_use, int) == False):
        raise Exception("Incorrect! Both values must be non-negative int!")
    else:
        mttr = total_use / total_repairs
        new_mttr = float("{0:.1f}".format(mttr))
        print("         MTTR of system is: ", new_mttr, " ~ ", round(new_mttr), " [hours]")
        return new_mttr


def simple_lambda(_type, N):
    Kt = 1.0
    Ks = 1.0
    _sum = 0.0

    if   _type == 'R' or _type == 'r': Kw = 0.6; lambda_base = 0.50*(10**-6)
    elif _type == 'C' or _type == 'c': Kw = 0.6; lambda_base = 0.02*(10**-6)
    elif _type == 'D' or _type == 'd': Kw = 0.4; lambda_base = 0.02*(10**-6)
    elif _type == 'T' or _type == 't': Kw = 0.6; lambda_base = 0.50*(10**-6)
    else: raise Exception("Incorrect value of inputed type!")

    for i in range(1, N+1): 
        Kn = float(input("      Input the load factor: "))
        _sum = _sum + (lambda_base * Kw)
    lambda_sys = Kn * Kt * Ks * _sum
    print('\nDone! Current lambda of group is: ', lambda_sys, '\n')
    return lambda_sys


def Ai(_type, mtbf_OR_mttf, mttr):
    if _type == 'r':
        print("Calculating for repairable system...")
    elif _type == 'n':
        print("Calculating for one-off/non-repairable...")
    
    ai =  (mtbf_OR_mttf  /  (mtbf_OR_mttf + mttr)) * 100
    ai = round(ai, 1)
    print("     Inherent Availability (Ai) is: ", ai, "%\n")
    return ai

def plotR(clust):
    t = np.arange(1, 1000, 1)
    R = np.exp((-clust[0]*(10**4)) * t)

    print('Attention! The real value of reliability will be R*(10**-4)\n')
    plt.rcParams["figure.figsize"] = (13,9)
    fig, axs = plt.subplots(2,1)

    collabel=('Failure Rate (λ)', 'MTBF', 'MTTF', 'MTTR', 'Ai')
    axs[0].axis('tight')
    axs[0].axis('off')
    new_clust = [str(clust[i]) for i in range(0, len(clust))] 
    the_table = axs[0].table(cellText=[new_clust],
                             colLabels=collabel,
                             loc='center')
    the_table.set_fontsize(12)
    the_table.scale(0.8, 1.5)

    axs[1].grid(color='b', linewidth=1, linestyle=':')
    axs[1].plot(t, R, label='# Test ' + r'$R(t)$', 
             color='r', linestyle='-', linewidth=3)
    plt.show()



def reliability():
    results = PrettyTable()
    
    lambda_system = {'R': 0.0, 'C': 0.0, 'D': 0.0, 'T': 0.0}
    
    q1, q2 = ask1(); print('\n')
    
    if (q1 == 'Y' or q1 == 'y') and (q2 == 'Y' or q2 == 'y'):
        ex = True
        while ex:
            try:
                Type = str(input("Enter type of electronic components group (<R>, <C>, <D>, <T>) or <q> to quit: "))
                print('\n')

                if Type == 'R' or Type == 'r':
                    Nr = int(input("Enter number of resistors in this group: "))
                    lambda_system['R'] = simple_lambda('R', Nr)
                
                elif Type == 'C' or Type == 'c':
                    Nc = int(input("Enter number of capasitors in this group: "))
                    lambda_system['C'] = simple_lambda('C', Nc)
                
                elif Type == 'D' or Type == 'd':
                    Nd = int(input("Enter number of diodes in this group: "))
                    lambda_system['D'] = simple_lambda('D', Nd)
                
                elif Type == 'T' or Type == 't':
                    Nt = int(input("Enter number of transistors in this group: "))
                    lambda_system['D'] = simple_lambda('T', Nt)
                
                elif Type == 'Q' or Type == 'q':
                    ex = False
        
            except ValueError:
                print('Incorrect data types. See <howto>\n')
            except Exception as error:
                print(error)
        
        my_failure_rate = sum(lambda_system.values())
        if (my_failure_rate == 0.0):
            exit()

        print('Failure Rate λ (lambda) of all system (PCB) is:')
        for key, value in lambda_system.items():
            print(" {0}: {1}".format(key,value))
        print('\n')

        print("MTBF calculating...")
        my_mtbf  = MTBF(my_failure_rate)
        
        print("\nMTTF calculating...")
        O = int(input("    1. Total hours of operation of device: "))
        I = int(input("    2. Total number of items that being tracked: "))
        
        my_mttf  = MTTF(O, I)
        print("\nMTTR calculating...")
        M = int(input("    1. Total maintenance time:  "))
        R = int(input("    2. Total number of repairs: "))
        
        my_mttr = MTTR(M, R)
        print("\nInherent Availability calculating...")
        my_Ai = Ai('r', my_mtbf, my_mttr)
        
        results.field_names = ['Failure Rate (λ)', 'MTBF', 'MTTF', 'MTTR', 'Ai']
        results.add_row([str(my_failure_rate), str(my_mtbf)+'[h]', (str(my_mttf)+'[h]'), (str(my_mttr)+'[h]'), (str(my_Ai)+'%')])
        print(results, '\n')

        plot_com = str(input("Make plot of R = exp(-lambda * t)? [Y/n] "))
        if plot_com == 'y' or plot_com == 'R':
            plotR([my_failure_rate, my_mtbf, my_mttf, my_mttr, my_Ai])
            print('\n')
        else:
            print('Ok!\n') 

        return True
    # elif ((q1 == 'N' or q1 == 'n') and (q2 == 'N' or q2 == 'n')):
    else:
        print("Waiting for updating...\nWill be soon!\n")
        return False