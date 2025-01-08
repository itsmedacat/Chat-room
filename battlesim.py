import random
skh = 5
huh = 5
skdl = 2
skdh = 5
hudl = 2
hudh = 5
skal = 1
skah = 4
hual = 1 
huah = 4
quit = 1
skc = 0
huc = 0
skv = 0
huv = 0
draws = 0
sbt = 'none'
hbt = 'none'
global skeletonf
global humanf
skeletonf = input('skeletons').replace(" " , "")
if skeletonf.isdigit():
    skeletonf = int(skeletonf)
else:
    quit += 1
    print('NOOOOOOOOOOOO')
if quit != 2:
    humanf = input('human').replace(" " , "")
    if humanf.isdigit():
        humanf = int(humanf)
    else:
        print('bad')
        quit += 1

# function for skeleton battle tactic

def skesbt():
    global sbt
    global quit
    sbt = input('Select a battle tactic for skeletons.').lower().replace(" " , "")
    if sbt in ['massedattack' , 'boxformation' , 'none']:
        choose = input(f'you have selected {sbt} are you satisified? Yes/No').lower().replace(" " , "")
        if choose == 'no':
            skesbt()
        elif choose not in ['yes' , 'no']:
            print('what?')
            quit += 1
    else:
        print('put in an actual tactic!')
        quit += 1

# calling function
if quit != 2:
    skesbt()

# the actual battle
# debug print(quit)
while quit != 2 and humanf > 0 and skeletonf > 0:
    
    # massed attack
    
    if sbt == 'massedattack':
        difference = skeletonf - humanf
        if difference >= (humanf * 1.2):
            skah += (difference * 0.2)
            skal += (difference * 0.2)
        elif difference < 0:
            skah += (difference * 0.1)
            skal += (difference * 0.1)
        else:
            skal -= (difference * 0.1)
    
    # box formation

    elif sbt == 'boxformation':
        # debug print(skeletonf)
        boxes = skeletonf / 10
        reamainder = skeletonf % 10
        if reamainder > 0:
            skah -= 0.03
            skal -= 0.03
        elif hbt != 'boxformation' :
            huah -= 0.01
        elif reamainder == 0:
            skah += 0.1
            skal += 0.1

    hua = random.uniform(hual, huah)
    ska = random.uniform(skal,skah) 
    if hua > ska:
        skeletonf -= 1
        skc += 1
        huv += 1
        print('Humans win the battle.')
    elif hua < ska:
        humanf -= 1
        huc += 1
        skv += 1
        print('Skeletons win the battle.')
    else:
        humanf -= 1
        huc += 1
        skeletonf -= 1
        skc += 1
        draws += 1
        print('The battle is a draw.')
    
if quit != 2 and skeletonf != 0:
    
    print('The Skeletons win the war.')
    print('Human Casualties:' , huc)
    print('Skeleton Victories:' , skv)
    print('Skeleton Casualties:' , skc)
    print('Human Victories:' , huv)
    print('Draws:' , draws)
elif quit != 2 and humanf != 0:
    print('The Humans win the war.')
    print('Human Casualties:' , huc)
    print('Skeleton Victories:' , skv)
    print('Skeleton Casualties:' , skc)
    print('Human Victories:' , huv)
    print('Draws:' , draws)
elif quit != 2 and humanf ==0 and skeletonf == 0: 
    print('The war is a stalemate.')
    print('Human Casualties:' , huc)
    print('Skeleton Victories:' , skv)
    print('Skeleton Casualties:' , skc)
    print('Human Victories:' , huv)
    print('Draws:' , draws)
