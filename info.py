'''
 * File: info.py
 * Project: Engipy
 * Author: kvant666ubl (GitHub)
 * -----
 * Last Modified: ***
 * Modified By: kvant666ubl
 * -----
 * Summary:
 * Contains basics theoretical information about reliability: 
 * formulas, methods, and examples. 
 '''

from colorama import init 
from termcolor import colored

def theory():

     print(colored('''


      :::::::::         :::        ::::::::    :::::::::::     ::::::::      :::::::: 
     :+:    :+:      :+: :+:     :+:    :+:       :+:        :+:    :+:    :+:    :+: 
    +:+    +:+     +:+   +:+    +:+              +:+        +:+           +:+         
   +#++:++#+  .  +#++:++#++: . +#++:++#++   .   +#+   .    +#+        .  +#++:++#++   
  +#+    +#+    +#+     +#+          +#+       +#+        +#+                  +#+    
 #+#    #+#    #+#     #+#   #+#    #+#       #+#        #+#    #+#    #+#    #+#     
#########     ###     ###    ########     ##########     ########      ########       
                                                                                                            
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
''', 'yellow'));
     
     print(colored('''
    1. Failure Rate λ (lambda)''', 'yellow'));

     print(colored(
'''         Is the frequency with which a system or component fails, expressed in failures per unit of time.
         All electronic components has this parameter. It determines the reliability of an element of the system. 
         λ is usually a tabular value and it is specified in the dimension failures per million operating hours (10^-6).
     ''', 'white'));


     print(colored('''
    2. Mean Time Between Failures (MTBF)''', 'yellow'));
     print(colored(
'''         Is the predicted time between failures of system, during normal system operation. 
         It can be calculated as the arithmetic mean (average) time between failures of a system as:
      
       MTBF  =  1 / λ,         [hours]  
                                where: λ (lambda) - is a failure rate;
     ''', 'white'));

     print(colored('''
    3. Mean Time To Failure (MTTF)''', 'yellow'));
     print(colored(
'''         Is a basic measure of reliability for non-repairable systems. 
         It is the mean time expected until the first failure of a piece of equipment. 
         MTTF is a statistical value and is meant to be the mean over a long period of time and a large number of units. 
         MTBF should be used only in reference to a repairable item, while MTTF should be used for non-repairable items. 
         However, MTBF is commonly used for both repairable and non-repairable items. 
    
        MTTF  =  total-hours-of-operation / total-number-of-items-being-tracked     [hours]
     ''', 'white'));

     print(colored('''
    4. Mean Time To Repair (MTTR)''', 'yellow'));
     print(colored(
'''         It is a time required to repair a system and restore it to full functionality. 
         The MTTR time starts when the repairs start and it goes on until operations are restored. 
         This includes repair time, testing period, and return to the normal operating condition.

         MTTR  =  total-maintenance-time  / total-number-of-repairs    [hours]
     ''', 'white'));

     print(colored('''
    5. Availability Ai (inherent)''', 'yellow'));
     print(colored(
'''         Probability that an item will operate satisfactorily at a given point in time 
         when used under stated conditions in an ideal support environment.
         It excludes logistics time, waiting or administrative downtime, and preventive maintenance downtime.
         It includes corrective maintenance downtime.
         Availability is calculated using the following formula:

         - if element is repairable:
            
                Ai   =   MTBF  /  (MTBF + MTTR);   ( * 100% optional)
         
         - if element is one-off/non-repairable:

                Ai   =   MTTF  /  (MTTF + MTTR);   ( * 100% optional)
     ''', 'white'));

     print(colored('''
    6. Reliability R(t)''', 'yellow'));
     print(colored(
'''         The probability that a system operating under specified conditions shall perform satisfactorily for a given period of time.
         It is the one of the most important part.
         The following formula for reliability:
''', 'white'));
     print(colored('''
        R(t)
         |
    100% |.
         | .        R(t)  =  exp(-λ * t)
         |  .        
         |    .       
         |      .
         |         .  
         |            .
     37% |________________.
         |                |   .
         |                |        .
         |________________|_____________ t
                         MTBF
         
         In practice, MTBF is approximately in range of 37-63 %.
     
     
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++      
     
     
     
     
     ''', 'green'))



def howto():
     print('Will be soon..')