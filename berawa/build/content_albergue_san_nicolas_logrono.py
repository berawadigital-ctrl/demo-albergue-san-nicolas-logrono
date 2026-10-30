# Contenido de la demo Albergue San Nicolás (Logroño) (es/en/fr/de). Hechos de alberguesannicolas.es leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin valoraciones ni opiniones de clientes.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Zimmer.'}
H={'es':['Habitación San Mateo','San Bernabé y Santiago (privadas)'],'en':['San Mateo room','San Bernabé and Santiago (private)'],'fr':['Chambre San Mateo','San Bernabé et Santiago (privées)'],'de':['Zimmer San Mateo','San Bernabé und Santiago (privat)']}
RD={
'es':['La habitación principal, con espacio para 14 personas: camas cerradas con cortina, toma eléctrica, luz individual, bolsa portaobjetos y cajón de equipaje individual.','San Bernabé: privada con 2 literas, máximo 4 personas. Santiago: privada con 1 litera y guardaobjetos con candado, máximo 2 personas.'],
'en':['The main room, with space for 14 people: enclosed beds with curtain, power socket, individual light, pocket for belongings and individual luggage drawer.','San Bernabé: private with 2 bunk beds, up to 4 people. Santiago: private with 1 bunk bed and lockable storage, up to 2 people.'],
'fr':['La chambre principale, pour 14 personnes : lits fermés avec rideau, prise électrique, lumière individuelle, pochette et tiroir à bagages individuel.','San Bernabé : privée avec 2 lits superposés, 4 personnes maximum. Santiago : privée avec 1 lit superposé et rangement à cadenas, 2 personnes maximum.'],
'de':['Das Hauptzimmer mit Platz für 14 Personen: geschlossene Betten mit Vorhang, Steckdose, eigenes Licht, Ablagetasche und eigene Gepäckschublade.','San Bernabé: privat mit 2 Etagenbetten, höchstens 4 Personen. Santiago: privat mit 1 Etagenbett und abschließbarem Fach, höchstens 2 Personen.']}
ART={
'hero':('arches',9981,['#3a1f24','#d49a5c','#efcb93','#6b2f37','#52232a','#2e1317']),
'intro':('skyline',9982,['#efe9e0','#d39b62','#efcb98','#6b2f37','#52232a','#2e1317']),
'r1':('columns',9991,['#efece6','#f8f5f0','#6b2f37','#52232a','#2e1317']),
'r2':('arches',9992,['#ece5da','#c98f58','#3d4a2f','#2a3420','#161c10']),
'g1':('hills',9993,['#ecece2','#efe2c6','#d49b62','#a9a77c','#7d7c55','#55543a']),
'g2':('skyline',9994,['#2e2026','#d89c5f','#f2cf9a','#5a3a44','#472e36','#2a1b20']),
'g3':('arches',9995,['#e9dfd0','#cf935a','#6b2f37','#3a1f24','#1f1013']),
'g4':('waves',9996,['#3a1f24','#e0a66a','#f3d4a4','#5a2f37','#46242b','#261316'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Albergue San Nicolás · Albergue de peregrinos en el centro de Logroño',see_rooms='Ver las habitaciones',hero_k='Logroño · Calle Mayor',hero_t='Albergue de peregrinos en el casco histórico de Logroño',hero_s='En la calle Marqués de San Nicolás, la Calle Mayor, un punto clave del Camino de Santiago. Capacidad máxima de 20 huéspedes.',
 intro_t='Funcional, cómodo y bien situado',intro_p1='Literas amplias con cortina de intimidad, luz de cortesía, enchufe individual y bolsillo para el móvil. Habitaciones sencillas, limpias y bien ventiladas, con aire acondicionado.',
 intro_p2='Rodeado de monumentos, bares de tapas y lugares de interés: todo a pie, sin desplazamientos. Bienvenidos peregrinos con credencial y viajeros.',
 stats=['20 plazas','3 habitaciones','Wifi gratis','Cocina comedor'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Una habitación compartida y dos privadas.',
 svcs=['Wifi gratis','Cocina equipada','Lavadora-secadora','Taquillas individuales','Baños adaptados','Aire acondicionado'],
 around_s='A pocos metros de Santiago el Real y de la Concatedral de Santa María de la Redonda; muy cerca de las calles Laurel y San Juan.',
 loc_p='Calle San Nicolás 102 · 26003 Logroño (La Rioja). El albergue abre a las 13:00 y cierra a las 22:00.',
 chips=['¿Qué habitaciones tenéis?','¿Cuánto cuesta la noche?','¿A qué hora abrís?','¿Cómo reservo?']),
'en':dict(title='Albergue San Nicolás · Pilgrim hostel in central Logroño',see_rooms='See the rooms',hero_k='Logroño · Calle Mayor',hero_t='Pilgrim hostel in the old town of Logroño',hero_s='On Marqués de San Nicolás street, the Calle Mayor, a key point of the Camino de Santiago. Maximum capacity of 20 guests.',
 intro_t='Practical, comfortable and well located',intro_p1='Roomy bunks with privacy curtain, courtesy light, individual socket and phone pocket. Simple, clean, well-ventilated rooms with air conditioning.',
 intro_p2='Surrounded by monuments, tapas bars and sights: everything on foot. Pilgrims with a credential and other travellers are welcome.',
 stats=['20 beds','3 rooms','Free wifi','Kitchen-dining room'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='One shared room and two private ones.',
 svcs=['Free wifi','Equipped kitchen','Washer-dryer','Individual lockers','Adapted bathrooms','Air conditioning'],
 around_s='A few metres from Santiago el Real and the Co-cathedral of Santa María de la Redonda; very close to Laurel and San Juan streets.',
 loc_p='Calle San Nicolás 102 · 26003 Logroño (La Rioja). The hostel opens at 13:00 and closes at 22:00.',
 chips=['Which rooms do you have?','How much is a night?','What time do you open?','How do I book?']),
'fr':dict(title='Albergue San Nicolás · Gîte de pèlerins au centre de Logroño',see_rooms='Voir les chambres',hero_k='Logroño · Calle Mayor',hero_t='Gîte de pèlerins dans le centre historique de Logroño',hero_s='Rue Marqués de San Nicolás, la Calle Mayor, étape clé du Chemin de Saint-Jacques. Capacité maximale de 20 personnes.',
 intro_t='Pratique, confortable et bien situé',intro_p1='Lits superposés spacieux avec rideau, veilleuse, prise individuelle et pochette pour le téléphone. Chambres simples, propres et bien aérées, climatisées.',
 intro_p2='Entouré de monuments, de bars à tapas et de lieux d’intérêt : tout à pied. Pèlerins avec credencial et voyageurs bienvenus.',
 stats=['20 places','3 chambres','Wifi gratuit','Cuisine-salle à manger'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Une chambre partagée et deux privées.',
 svcs=['Wifi gratuit','Cuisine équipée','Lave-linge séchant','Casiers individuels','Salles de bain adaptées','Climatisation'],
 around_s='À quelques mètres de Santiago el Real et de la cocathédrale Santa María de la Redonda ; tout près des rues Laurel et San Juan.',
 loc_p='Calle San Nicolás 102 · 26003 Logroño (La Rioja). Le gîte ouvre à 13:00 et ferme à 22:00.',
 chips=['Quelles chambres avez-vous ?','Combien coûte une nuit ?','À quelle heure ouvrez-vous ?','Comment réserver ?']),
'de':dict(title='Albergue San Nicolás · Pilgerherberge im Zentrum von Logroño',see_rooms='Zimmer ansehen',hero_k='Logroño · Calle Mayor',hero_t='Pilgerherberge in der Altstadt von Logroño',hero_s='In der Straße Marqués de San Nicolás, der Calle Mayor, einem wichtigen Punkt des Jakobswegs. Höchstens 20 Gäste.',
 intro_t='Praktisch, bequem und gut gelegen',intro_p1='Geräumige Etagenbetten mit Sichtschutzvorhang, Leselicht, eigener Steckdose und Handytasche. Einfache, saubere, gut belüftete Zimmer mit Klimaanlage.',
 intro_p2='Umgeben von Denkmälern, Tapas-Bars und Sehenswürdigkeiten: alles zu Fuß. Pilger mit Credencial und andere Reisende sind willkommen.',
 stats=['20 Plätze','3 Zimmer','Kostenloses WLAN','Küche mit Essbereich'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Ein Mehrbettzimmer und zwei Privatzimmer.',
 svcs=['Kostenloses WLAN','Ausgestattete Küche','Waschtrockner','Einzelne Schließfächer','Barrierefreie Bäder','Klimaanlage'],
 around_s='Wenige Meter von Santiago el Real und der Konkathedrale Santa María de la Redonda; ganz nah an den Straßen Laurel und San Juan.',
 loc_p='Calle San Nicolás 102 · 26003 Logroño (La Rioja). Die Herberge öffnet um 13:00 und schließt um 22:00 Uhr.',
 chips=['Welche Zimmer gibt es?','Was kostet eine Nacht?','Wann öffnen Sie?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB='https://reservas.alberguesannicolas.es/'
BOOK=dict(mode='engine',url={l:RB+'?locale='+l for l in ('es','en','fr','de')})
D=dict(name='Albergue San Nicolás',ac='#3a1f24',ac2='#6b2f37',ac2_a11y='#52232a',book=BOOK,around=['Iglesia de Santiago el Real','Concatedral de Santa María de la Redonda'],foot=FOOT,
 address='Calle San Nicolás 102 · 26003 Logroño',phones=['+34 608 184 728','+34 941 056 631'],emails=['reservas@alberguesannicolas.es'],maps='Albergue San Nicolás, Calle Marqués de San Nicolás 102, 26003 Logroño',t=T)
META=dict(repo='demo-albergue-san-nicolas-logrono',name='Albergue San Nicolás',legal_name='Estudio Urya SL',registry_ids=['B26068882'],
 url='https://alberguesannicolas.es/',domain='alberguesannicolas.es',municipality='Logroño',province='La Rioja',sector='albergue de peregrinos de 20 plazas en la Calle Mayor de Logroño',
 read_at='2026-10-30T09:08:00+01:00',created_at='2026-10-30T09:07:00+01:00',built_at='2026-10-30T09:20:00+01:00',audit_date='2026-10-30T09:03:22+01:00',
 rating=dict(value=4.5,coincide=['web'],date='2026-10-29T12:56:31+01:00',url='https://www.google.com/maps/place/Albergue+San+Nicol%C3%A1s/@42.4671482,-2.4476297,17z/data=!4m9!3m8!1s0xd5aab5ff3ce6105:0x608f9b04357ad870!5m2!4m1!1i2!8m2!3d42.4671482!4d-2.4476297!16s%2Fg%2F11yb6jnkr3'),
 book=dict(mode='engine',url=RB,note='motor de reservas real de su web (reservas.alberguesannicolas.es, enlace «Reserva ya»), HTTP 200 comprobado el 30/10/2026 con locale es/en/fr/de.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Cuánto cuesta la noche?','K02'),('¿A qué hora abrís?','K03'),('¿Hay wifi?','K04'),('¿Necesito credencial?','K05'),('¿Se puede fumar?','K06'),('¿Dónde está el albergue?','K07'),('¿Admitís mascotas?','K08'),('¿Cómo reservo?','K09'),('¿Podéis confirmarme disponibilidad para mañana?','K09'),('¿Hay bares de tapas cerca?','K10'),('¿Tenéis piscina?',None),('¿Hay gimnasio?',None)],
'en':[('Which rooms do you have?','K01'),('How much is a night?','K02'),('What time do you open?','K03'),('Is there wifi?','K04'),('Do I need a credential?','K05'),('Can I smoke?','K06'),('Where is the hostel?','K07'),('Do you accept pets?','K08'),('How do I book?','K09'),('Can you confirm availability for tomorrow?','K09'),('Are there tapas bars nearby?','K10'),('Do you have a swimming pool?',None),('Is there a gym?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Combien coûte une nuit ?','K02'),('À quelle heure ouvrez-vous ?','K03'),('Y a-t-il le wifi ?','K04'),('Faut-il la credencial ?','K05'),('Peut-on fumer ?','K06'),('Où se trouve le gîte ?','K07'),('Acceptez-vous les animaux ?','K08'),('Comment réserver ?','K09'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K09'),('Y a-t-il des bars à tapas ?','K10'),('Avez-vous une piscine ?',None),('Y a-t-il une salle de sport ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Was kostet eine Nacht?','K02'),('Wann öffnen Sie?','K03'),('Gibt es WLAN?','K04'),('Brauche ich eine Credencial?','K05'),('Darf man rauchen?','K06'),('Wo liegt die Herberge?','K07'),('Sind Haustiere erlaubt?','K08'),('Wie kann ich buchen?','K09'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K09'),('Gibt es Tapas-Bars in der Nähe?','K10'),('Haben Sie ein Schwimmbad?',None),('Gibt es ein Fitnessstudio?',None)]}
