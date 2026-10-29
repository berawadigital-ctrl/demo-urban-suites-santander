# Contenido de la demo Urban Suite Santander (es/ca/en/fr). Hechos de urbansuitesantander.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Siete habitaciones exteriores','Kitchenette en cada habitación','Auto check-in'],
'ca':['Set habitacions exteriors','Kitchenette a cada habitació','Auto check-in'],
'en':['Seven outward-facing rooms','Kitchenette in every room','Self check-in'],
'fr':['Sept chambres extérieures','Kitchenette dans chaque chambre','Auto check-in']}
RD={
'es':['Industrial, Noir, Salitre, Luana, París, Menta y Limón, con vistas a la calle Cardenal Cisneros o a la calle Cervantes, grandes ventanales y, la mayoría, balcones o miradores.','Frigorífico, cafetera Nespresso, tetera, microondas y menaje, además de wifi gratuito, caja fuerte y secador.','Códigos personales de acceso por correo, sin pasar por recepción, y teléfono de recepción para lo que necesites.'],
'ca':['Industrial, Noir, Salitre, Luana, París, Menta i Limón, amb vistes al carrer Cardenal Cisneros o al carrer Cervantes, grans finestrals i, la majoria, balcons o mirador.','Nevera, cafetera Nespresso, tetera, microones i parament, a més de wifi gratuït, caixa forta i assecador.','Codis personals d\'accés per correu, sense passar per recepció, i telèfon de recepció per al que necessitis.'],
'en':['Industrial, Noir, Salitre, Luana, París, Menta and Limón, facing Calle Cardenal Cisneros or Calle Cervantes, with large windows and, mostly, balconies or glazed bays.','Fridge, Nespresso machine, kettle, microwave and kitchenware, plus free wifi, a safe and a hair dryer.','Personal access codes sent by email, no need to stop at reception, and a reception phone for anything you need.'],
'fr':['Industrial, Noir, Salitre, Luana, París, Menta et Limón, avec vue sur la calle Cardenal Cisneros ou la calle Cervantes, de grandes baies vitrées et, pour la plupart, des balcons ou des miradors.','Réfrigérateur, machine Nespresso, bouilloire, micro-ondes et vaisselle, plus wifi gratuit, coffre-fort et sèche-cheveux.','Codes d\'accès personnels envoyés par e-mail, sans passer par la réception, et téléphone de réception pour tout besoin.']}
ART={
'hero':('waves',9701,['#f6e0b4','#eb9f78','#fff1c6','#7ab3c6','#4c8fad','#2f6d88','#1b4a64']),
'intro':('arches',9702,['#ece3d2','#f6efe0','#d98b3a','#b98a6b','#1f4e6b']),
'r1':('arches',9711,['#ebe2d0','#f5eddd','#d68838','#b78768','#214f6d']),
'r2':('columns',9712,['#e8dfcc','#f3ead9','#d28435','#b48666','#23526f']),
'r3':('skyline',9713,['#3a4b66','#eb9a6c','#fddba4','#3b4c67','#2c3b54','#1c2839']),
'g1':('hills',9721,['#e2e6d4','#f3e7c6','#ffe0a6','#aec3a2','#82a288','#58796a']),
'g2':('waves',9722,['#f4dcae','#e99974','#ffeec2','#79b0c5','#4a8aa9','#2e6a86','#1c4962']),
'g3':('arches',9723,['#eadfcb','#f5ecda','#d58637','#b58565','#1f4d6a']),
'g4':('skyline',9724,['#2f3f5c','#e68b62','#fad09b','#2f3f5d','#223049','#162033']),
'g5':('columns',9725,['#e9e0cd','#f4ebd9','#d78a3a','#b78a6a','#22516e']),
'g6':('waves',9726,['#f7e2b8','#eca27b','#fff3ca','#7cb5c8','#4e91ae','#306e89','#1d4b65'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Urban Suite Santander · Habitaciones con kitchenette en el centro de Santander',see_rooms='Ver habitaciones',hero_k='Santander · Centro',hero_t='Siete habitaciones con kitchenette en un edificio señorial',hero_s='En la calle Cardenal Cisneros, a pocos minutos a pie de la bahía.',
 intro_t='En el corazón de Santander',intro_p1='Urban Suite está en un edificio señorial del siglo XIX en pleno corazón de Santander, a pocos minutos andando de una de las bahías más bonitas del mundo.',
 intro_p2='Tiene siete habitaciones privadas con kitchenette, wifi gratuito y caja fuerte. Funciona con auto check-in: recibes tus códigos de acceso por correo y no tienes que pasar por recepción.',
 stats=['7 habitaciones','Kitchenette','Auto check-in','Wifi gratuito'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Siete habitaciones privadas, todas exteriores.',
 svcs=['Auto check-in','Limpieza diaria','Wifi gratuito','Carta de almohadas','Biblioteca','Kitchenette en cada habitación','Caja fuerte','Plancha y secador'],
 loc_p='Calle Cardenal Cisneros 8, 1º, 39001 Santander, en un edificio señorial del siglo XIX.',
 chips=['¿Cuántas habitaciones hay?','¿Hay cocina en las habitaciones?','¿Cómo funciona el check-in?','¿Cómo se reserva?']),
'ca':dict(title='Urban Suite Santander · Habitacions amb kitchenette al centre de Santander',see_rooms='Veure habitacions',hero_k='Santander · Centre',hero_t='Set habitacions amb kitchenette en un edifici senyorial',hero_s='Al carrer Cardenal Cisneros, a pocs minuts a peu de la badia.',
 intro_t='Al cor de Santander',intro_p1='Urban Suite és en un edifici senyorial del segle XIX en ple cor de Santander, a pocs minuts caminant d\'una de les badies més boniques del món.',
 intro_p2='Té set habitacions privades amb kitchenette, wifi gratuït i caixa forta. Funciona amb auto check-in: reps els codis d\'accés per correu i no has de passar per recepció.',
 stats=['7 habitacions','Kitchenette','Auto check-in','Wifi gratuït'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Set habitacions privades, totes exteriors.',
 svcs=['Auto check-in','Neteja diària','Wifi gratuït','Carta de coixins','Biblioteca','Kitchenette a cada habitació','Caixa forta','Planxa i assecador'],
 loc_p='Carrer Cardenal Cisneros 8, 1r, 39001 Santander, en un edifici senyorial del segle XIX.',
 chips=['Quantes habitacions hi ha?','Hi ha cuina a les habitacions?','Com funciona el check-in?','Com es reserva?']),
'en':dict(title='Urban Suite Santander · Rooms with a kitchenette in central Santander',see_rooms='See the rooms',hero_k='Santander · City centre',hero_t='Seven rooms with a kitchenette in a stately building',hero_s='On Calle Cardenal Cisneros, a few minutes\' walk from the bay.',
 intro_t='In the heart of Santander',intro_p1='Urban Suite is in a stately nineteenth-century building in the very heart of Santander, a few minutes\' walk from one of the most beautiful bays in the world.',
 intro_p2='It has seven private rooms with a kitchenette, free wifi and a safe. It runs on self check-in: you get your access codes by email and do not need to stop at reception.',
 stats=['7 rooms','Kitchenette','Self check-in','Free wifi'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Seven private rooms, all outward-facing.',
 svcs=['Self check-in','Daily cleaning','Free wifi','Pillow menu','Library','Kitchenette in every room','Safe','Iron and hair dryer'],
 loc_p='Calle Cardenal Cisneros 8, 1st floor, 39001 Santander, in a stately nineteenth-century building.',
 chips=['How many rooms are there?','Is there a kitchen in the rooms?','How does check-in work?','How do I book?']),
'fr':dict(title='Urban Suite Santander · Chambres avec kitchenette au centre de Santander',see_rooms='Voir les chambres',hero_k='Santander · Centre',hero_t='Sept chambres avec kitchenette dans un immeuble de caractère',hero_s='Calle Cardenal Cisneros, à quelques minutes à pied de la baie.',
 intro_t='Au cœur de Santander',intro_p1='Urban Suite se trouve dans un immeuble de caractère du XIXe siècle en plein cœur de Santander, à quelques minutes à pied de l\'une des plus belles baies du monde.',
 intro_p2='Il propose sept chambres privées avec kitchenette, wifi gratuit et coffre-fort. Il fonctionne en auto check-in : vous recevez vos codes d\'accès par e-mail et n\'avez pas à passer par la réception.',
 stats=['7 chambres','Kitchenette','Auto check-in','Wifi gratuit'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Sept chambres privées, toutes extérieures.',
 svcs=['Auto check-in','Ménage quotidien','Wifi gratuit','Carte d\'oreillers','Bibliothèque','Kitchenette dans chaque chambre','Coffre-fort','Fer à repasser et sèche-cheveux'],
 loc_p='Calle Cardenal Cisneros 8, 1er étage, 39001 Santander, dans un immeuble de caractère du XIXe siècle.',
 chips=['Combien de chambres y a-t-il ?','Y a-t-il une cuisine dans les chambres ?','Comment fonctionne le check-in ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='hola@urbansuitesantander.com')
D=dict(name='Urban Suite Santander',ac='#1f4e6b',ac2='#d98b3a',ac2_a11y='#7a4a12',book=BOOK,around=[],foot=FOOT,
 address='Calle Cardenal Cisneros 8, 1º · 39001 Santander',phones=['628 919 635'],emails=['hola@urbansuitesantander.com'],maps='Urban Suite Santander, Calle Cardenal Cisneros 8, Santander',t=T)
META=dict(repo='demo-urban-suites-santander',name='Urban Suite Santander',legal_name='Urban Suites Santander S.L.',registry_ids=['CIF B39825393','Registro de Empresas Turisticas de Cantabria n. 5193'],
 url='https://urbansuitesantander.com/',domain='urbansuitesantander.com',municipality='Santander',province='Cantabria',sector='aparthotel de habitaciones con kitchenette en el centro',
 read_at='2026-10-29T04:06:00+01:00',created_at='2026-10-29T04:08:00+01:00',built_at='2026-10-29T04:10:00+01:00',audit_date='2026-10-29T04:08:00+01:00',
 rating=dict(value=4.5,coincide=['web'],date='2026-10-29T04:02:03+01:00',url='https://www.google.com/maps/place/Urban+Suite+Santander/@43.4632508,-3.8110714,17z/data=!4m9!3m8!1s0xd494bcc215546b7:0xef2e681ff8a3f9b3!5m2!4m1!1i2!8m2!3d43.4632508!4d-3.8110714!16s%2Fg%2F11clsgvp54'),
 book=dict(mode='mail',email='hola@urbansuitesantander.com',note='La web del negocio reserva con un motor propio; la demo usa solo contacto real (correo y telefono).'),
 first_of_type='primer tipo de negocio sin precedente: aparthotel urbano de habitaciones con kitchenette y auto check-in (el modelo aprobado Cazorla Rural es alojamiento rural)')
QS={
'es':[('¿Cuántas habitaciones hay?','K01'),('¿Hay cocina en las habitaciones?','K02'),('¿Hay wifi y caja fuerte?','K03'),('¿A qué hora es el check-in?','K04'),('¿Cuál es la política de cancelación?','K05'),('¿Hay limpieza diaria?','K06'),('¿Dónde está el alojamiento?','K07'),('¿Cómo reservo?','K08'),('¿Cuál es el teléfono?','K09'),('¿Quién es el titular?','K10'),('¿Admiten mascotas?',None),('¿Hay parking?',None),('¿Hay desayuno?',None),('¿Cuánto cuesta una habitación?',None),('¿Tienen piscina?',None),('Confírmame que hay una habitación libre mañana','K08')],
'ca':[('Quantes habitacions hi ha?','K01'),('Hi ha cuina a les habitacions?','K02'),('Hi ha wifi i caixa forta?','K03'),('A quina hora és el check-in?','K04'),('Quina és la política de cancel·lació?','K05'),('Hi ha neteja diària?','K06'),('On és l\'allotjament?','K07'),('Com reservo?','K08'),('Quin és el telèfon?','K09'),('Qui és el titular?','K10'),('Admeteu mascotes?',None),('Hi ha pàrquing?',None),('Hi ha esmorzar?',None),('Quant costa una habitació?',None),('Teniu piscina?',None),('Confirma\'m que hi ha una habitació lliure demà','K08')],
'en':[('How many rooms are there?','K01'),('Is there a kitchen in the rooms?','K02'),('Is there wifi and a safe?','K03'),('What time is check-in?','K04'),('What is the cancellation policy?','K05'),('Is there daily cleaning?','K06'),('Where is the accommodation?','K07'),('How do I book?','K08'),('What is the phone number?','K09'),('Who is the owner?','K10'),('Are pets allowed?',None),('Is there parking?',None),('Is there breakfast?',None),('How much is a room?',None),('Do you have a swimming pool?',None),('Confirm that there is a free room tomorrow','K08')],
'fr':[('Combien de chambres y a-t-il ?','K01'),('Y a-t-il une cuisine dans les chambres ?','K02'),('Y a-t-il le wifi et un coffre-fort ?','K03'),('À quelle heure est le check-in ?','K04'),('Quelle est la politique d\'annulation ?','K05'),('Y a-t-il un ménage quotidien ?','K06'),('Où est l\'hébergement ?','K07'),('Comment réserver ?','K08'),('Quel est le téléphone ?','K09'),('Qui est le titulaire ?','K10'),('Les animaux sont-ils admis ?',None),('Y a-t-il un parking ?',None),('Y a-t-il un petit-déjeuner ?',None),('Combien coûte une chambre ?',None),('Avez-vous une piscine ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K08')]}
