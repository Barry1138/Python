from Man import *
from Hombre import *

guy_1 = Man('Richard')
guy_2 = Hombre('Retardo')

guy_1.speak('LEARN TO SPEAK ENGLISH.\n')
guy_2.speak('No entiendo inglés.\n')

Person.speak(guy_1)
Person.speak(guy_2)
