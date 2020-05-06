#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:45:14 2020

@author: vinny
"""

## This is the module for collecting the Bill of materials for the product
from tabulate import tabulate

def artifact():
    
     # A system Artifact is considered a component 
        artifact_info = []
        name = input('Name of component: ')
        describe = input('describe the component: ')
        
        comp_basis_list = [[1,'unclassified',2,	'brancher',3,	'channeler',4,'connector',5,'magnitude controller'],
             [6,'converter',7,'provisioner',8,'signaler',9,'supporter',10,'separator'],
             [11,'distributor',12,'importer-exporter',13,'transferor',14,'guiders',15,'coupler'],
             [16,'mixer',17,'actuator',18,'regulator',19,'changer',20,'stopper'],
             [21,'output gas material', 22,'output liquid material',23,'output acoustic energy',24,'output electrical energy',25,'output electromagnetic energy'],
             [26,'output hydraulic energy',27,'output magnetic energy',28,'output mechanical energy',29,'output pneumatic energy',30,'output thermal energy'],
             [31,	'output control signal',32,'material supplier',33,'energy supplier',34,'sensor',35,'indicator'],
             [36,'processor',37,'stabilizer',38,'securer',39,'positioner',40,'divider'],
             [41,'abrasive',42,'blade',43,'vibrator',44,'centrifuge',45,'material filter'],
             [46,'brush',47,'diverger',48,'nozzle',49,'electric distributor',50,'housing'],
             [51,'electric cord',52,'carousel',53,'conveyer',54,'electric conductor',55,'electric socket'],
             [56,'electric plug',57,'projectile',58,'belt',59,'clutch',60,'extension'],
             [61,'rotational coupler',62,'shaft',63,'heat exchanger',64,'thermal conductor',65,'em transmitter'],
             [66,'hinge',67,'tube',68,'diode',69,'bearing',70,'link'],
             [71,'sled',72,'clamp',73,'fastener',74,'agitator',75,'door'],
             [76,'electric switch',77,'latch release',78,'valve',79,'potentiometer',80,'thermostat'],
             [81,'transistor',82,'mold',83,'punch',84,'stuffing',85,'choke'],
             [86,'electric resistor',87,'mechanical transformer',88,'inclined plane',89,'lever',90,'needle'],
             [91,'lens',92,'capacitor',93,'inductor',94,'signal filter',95,'cap'],
             [96,'cover',97,'seal',98,'acoustic insulator',99,'electric insulator',100,'fuse'],
             [101,'cushion',102,'friction enhancer',103,'stop',104,'thermal insulator',105,'catalytic converter'],
             [106,'evaporator',107,'condenser',108,'speaker',109,'generator',110,'light source'],
             [111,'hydraulic pump',112,'screw propeller',113,'electromagnet',114,'ic motor',115,'electric motor'],
             [116,'hydraulic piston',117,'armature',118,'cam',119,'crank',120,'wheel'],
             [121,'airfoil',122,'pneumatic piston',123,'fan',124,'pneumatic pump',125,'burner'], 
             [126,'heating element',127,'knob',128,'reservoir',129,'container',130,'bladder'],
             [131,'pressure vessel',132,'battery',133,'magnet',134,'flywheel',135,'spring'],
             [136,'level gauge',137,'voltmeter',138,'ammeter',139,'pressure gauge',140,'displacement gauge'],
             [141,'speed gauge',142,'em sensor' ,143,'visual indicator',144,'auditory indicator',145,'circuit board'],
             [146,'insert',147,'support'  ,148,'bracket',149,'washer',150,'handle'],
             [151,'permeable membrane',152,'rake',153,'screen' ,154,'electric wire' ,155,'electric plate'],
             [156,'thermal wire',157,'thermal plate',158,'glue',159,'key',160,'nut-bolt'],
             [161,'retaining clip',162,'rivet',163,'screw',164,'solder',165,'gear'],
             [166,'pulley',167,'sprocket',168,'analog display',169,'digital display',170,'flag'],
             [171,'indicator light',172,'bell',173,'buzzer',174,'recording' ,175,'assembly'],
             [176,'biological' ,177,'internal' ,178,'external' ,179,'system','','']]
        
        ## Printing tabulated table
        p = comp_basis_list #reassigning varible because I am lazy
        print(tabulate([p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],
                        p[10],p[11],p[12],p[13],p[14],p[15],p[16],p[17],p[18],p[19],
                        p[20],p[21],p[22],p[23],p[24],p[25],p[26],p[27],p[28],p[29],
                        p[30],p[31],p[32],p[33],p[34],p[35]], 
                       headers=['#','Basis Name','#','Basis Name','#','Basis Name','#','Basis Name','#','Basis Name'], tablefmt='orgtbl'))
                                
                                
        success = False
        while success == False:
            try:
               component_basis = int(input('Which basis term best describes the component? (use the corresponding number): '))
               if component_basis > 179 or component_basis < 1:
                   success = False
                   print('Number inputed not found on supplied list. Try again...')
               else:
                   success = True
            except ValueError:
                print( 'That was not a valid number.  Try again...')                       
          
        material_basis_list = [[1,'abs'],[2,'aluminum'],[3,'brass'],[4,'cardboard'],
                                [5,'composite'],[6,'concrete'],[7,'copper'],[8,'foam'],
                                [9,'glass'],[10,'iron'],[11,'metal'],[12,'metal alloy'],
                                [13,'nylon'],[14,'paper'],[15,'plastic'],[16,'rubber'],[17,'steel'],[18,'wood']]
        
        print(tabulate([material_basis_list[0],material_basis_list[1],material_basis_list[2],material_basis_list[3],
                        material_basis_list[4],material_basis_list[5],material_basis_list[6],material_basis_list[7],
                        material_basis_list[8],material_basis_list[9],material_basis_list[10],material_basis_list[11],
                        material_basis_list[12],material_basis_list[13],material_basis_list[14],material_basis_list[15],
                        material_basis_list[16],material_basis_list[17]], 
                        headers=['#','Material Name'], tablefmt='orgtbl')) 
                                 
        success = False
        while success == False:
            try:
               material = int(input('Which basis material best describes the component? (use the corresponding number): '))
               if material > 18 or material < 1:
                   success = False
                   print('Number inputed not found on supplied list. Try again...')
               else:
                   success = True
            except ValueError:
                print( 'That was not a valid number.  Try again...')                              
    
        artifact_info.append(name)
        artifact_info.append(describe)
        artifact_info.append(component_basis)
        artifact_info.append(material)
        
        
        finished_prompt = False
        while finished_prompt != 'yes' or finished_prompt != 'no':
            
            finished_prompt = input('Are there more components to add to the BOM?: ')
            
            if finished_prompt == 'yes':
                return artifact_info, True
            
            elif finished_prompt == 'no':
                return artifact_info, False
            
            else:
                print('')
                print('Please enter yes or no.')



        
def child_data(system_BOM):
    
    child_prompt = False
    success = False
    print('')   
    print('Please use the follow prompt to describe the parent-child component relationship')
    print('(A child is a component connected to another component from a top down perspective)')
    print('Example: A housing could be a child if the system(product), a motor could be a child of a housing')
    print('If unsure default to naming the system (product) the parent')
    
    
    print('')
    system_BOM_first = [x[0] for x in system_BOM]
    print('\n'.join('{}: {}'.format(*k) for k in enumerate(system_BOM_first)))

    while success == False:
        try:
            print('')
            child_prompt = int(input('Enter the number that corresponds to the component parent: '))
            if child_prompt > len(system_BOM)-1 or child_prompt < 0:
                print('Number inputed not found on supplied BOM list. Try again...')
               
            else:
                success = True
        except ValueError:
            print( 'That was not a valid number.  Try again...')
    
    return child_prompt
    
    
      
    

def BOM(system_BOM):
    
    print('')
    print('Please enter the Bill of Material infromation for your product')
    print('It is important to fill this out to the best of your ability')
    print('try to enter the BOM in order of logical product disassembly')
    print('Enter the data for the first component. Then you will prompted to add more components or finish data entry')   
    

    more_components = True
    comp_count = 1
    
    while more_components == True:
        
        print('')
        print('Please enter information for component ',comp_count,'.' )
        
        component = artifact()
        
        component[0].append(child_data(system_BOM))
        
        print('')
        print('')
        
        
        system_BOM.append(component[0])
        
        more_components = component[1]
        
        comp_count = comp_count + 1
        
        
        
    return system_BOM   
        

        
        
        

#p = artifact()
#sys = [['System_name']]  
#bom = BOM(sys)
#p = child_data(sys)