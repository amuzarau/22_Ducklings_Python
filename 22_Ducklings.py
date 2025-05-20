"""Duckling Screensaver.
A screensaver of many many ducklings.

>" )   =^^)    (``=   ("=  >")    ("=
(  >)  (  ^)  (v  )  (^ )  ( >)  (v )
 ^ ^    ^ ^    ^ ^    ^^    ^^    ^^
"""

import random, shutil, sys, time

PAUSE = 0.2
DENSITY = 0.10

DUCKLING_WIDTH = 5
LEFT = 'left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
ALOOF = 'aloof'
CHUBBY = 'chubby'
VERY_CHUBBY = 'very_chubby'
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'


WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1

def main():
    print('Duckling Screensaver')
    print('Press ctrl-C to quit...')
    time.sleep(2)

    duckling_lanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:
        for lane_num, duckling_obj in enumerate(duckling_lanes):
            if (duckling_obj == None and random.random() <= DENSITY):
                duckling_obj = Duckling()
                duckling_lanes[lane_num] = duckling_obj

            if duckling_obj != None:
                print(duckling_obj.get_next_body_part(), end='')

                if duckling_obj.part_to_display_next == None:
                    ducling_lanes[lane_num] = None

            else:
                print(' ' * DUCKLING_WIDTH, end='')

        print()
        sys.stdout.flush()
        time.sleep(PAUSE)

                


