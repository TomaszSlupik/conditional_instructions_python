# Instrukcje warunkowe w języku Python
# pozwalają na wykonywanie określonych bloków kodu w zależności od spełnienia określonych warunków.

# Sprawdź, czy pliku o podanej nazwie jest z rozszerzeniem '.xlsx'
filename = '01012020_sales.xlsx'
checkFilename = ['YES' if filename.endswith('.xlsx') else 'NO']

print("".join(checkFilename))

print('---')

# Sprawdź czy zmienna code składa się tylko z dużych liter - upper
code = 'DSVNDOICSN'

if code == code.upper():
    print('YES')
else:
    print('NO')

print('---')
# Sprawdź czy zmienna jest obiektem typu int
number = 1.0

if number is int:
    print('YES')
else:
    print('NO')

print('---')

# Sprawdź, czy podane hasło ma wymaganą długość minimum 11 znaków.
password = 'cskdnjcasa#!'

if len(password) > 11:
    print('Password is valid')
else:
    print('Password is too short')

print('---')
# Sprawdź, czy podane hasło ma wymaganą długość 11 znaków oraz zwiera znak specjalny '!'
password = 'cskdnjcasa#!'

if (len(password) > 11) and (password.find('!')):
    print('Password is valid')
else:
    print('Password is invalid')

print('---')

# Sprawdź czy projekt o wartości id istnieje, jeśli nie dodaj id tego projektu do listy.
project_ids = ['02134', '24253']
project_id = '02135'

if project_id not in project_ids:
    project_ids.append(project_id)

print(project_ids)

print('---')

# Wykorzystując instrukcję warunkową sprawdź,
# czy status projektu z id = '02' jest ustawiony na 'new'.
# Jeśli tak, zmień ten status na 'open'.

project_ids = {
    '01': 'open',
    '02': 'new',
    '03': 'in progress',
    '04': 'completed'
}

if project_ids['02'] == 'new':
    project_ids['02'] = 'open'

print(project_ids)

print('---')

# Sprawdź czy item występuje w liście,
# Jeżeli tak, to usuń ten element z listy. W odpowiedzi wydrukuj otrzymaną listę do konsoli.
item = '001'
items = ['001', '000', '003', '005', '006']

if item in items:
    items.remove('001')

print(items)

print('---')

#
"""
sprawdzić, czy pasażer kwalifikuje się do wejścia na pokład zgodnie z następującymi zasadami:
    jeśli pasażer ma mniej niż 18 lat, nie może wejść na pokład samolotu, 
    w tym przypadku wydrukuj do konsoli informację:
    'Sorry, passengers under 18 years old.'

    jeśli pasażer ma ukończone 18 lat i posiada bilet typu 'business',
    jest uprawniony do wejścia na pokład samolotu, w tym przypadku wydrukuj do konsoli informację:
    'Passenger is eligible to board with a business ticket.'

    jeśli pasażer ma ukończone 18 lat i posiada bilet 'economy', 
    jest uprawniony do wejścia na pokład tylko wtedy, gdy ma ukończone 65 lat, 
    w tym przypadku wydrukuj do konsoli informację:
    'Passenger is eligible to board with an economy ticket.'

    jeśli pasażer nie spełnia podanych warunków to wydrukuj do konsoli poniższą informację:
    'Sorry, passenger is not eligible to board the flight.'
"""
age = 22
ticket_type = 'economy'


def ticketCheck(age, ticket_type):
    if age < 18:
        print('Sorry, passengers under 18 years old.')
    elif age > 18 and ticket_type == 'business':
        print('Passenger is eligible to board with a business ticket.')
    elif age > 65 and ticket_type == 'economy':
        print('Passenger is eligible to board with an economy ticket.')
    else:
        print('Sorry, passenger is not eligible to board the flight.')


ticketCheck(age, ticket_type)

"""
Użyj instrukcji warunkowej do obliczenia całkowitej ceny zamówienia zgodnie z następującymi zasadami:
    jeśli kod rabatowy to 'DISCOUNT10', zastosuj rabat 10% do ceny całkowitej
    jeśli kod rabatowy to 'DISCOUNT20', zastosuj rabat 20% do ceny całkowitej
    jeśli kod rabatowy jest nieważny, wydrukuj poniższy komunikat i nie stosuj rabatu:
    'Info: Invalid discount code. No discount will be applied.'
"""

item1_price = 100.0
item2_price = 50.0
discount_code = 'DISCOUNT20'


def allPrice(item1, item2, code):
    if code == 'DISCOUNT10':
        yourCash = item1 + item2 - ((item1 + item2) * 0.1)
        print(f'Total price of the order is $ {yourCash}')
    elif code == 'DISCOUNT20':
        yourCash = item1 + item2 - ((item1 + item2) * 0.2)
        print(f'Total price of the order is $ {yourCash}')
    else:
        print('Info: Invalid discount code. No discount will be applied.')


allPrice(item1_price, item2_price, discount_code)

print('---')

"""
Następnie użyj instrukcji warunkowej do obliczenia całkowitego wyniku zespołu zgodnie z następującymi zasadami:
    każda zdobyta bramka to 10 punktów
    jeśli drużyna zdobędzie więcej niż 5 bramek, zdobywa dodatkowe 5 punktów bonusowych
    jeśli drużyna zdobędzie więcej niż 10 bramek, zdobywa dodatkowe 10 punktów bonusowych
Punkty bonusowe po przekroczeniu 5 i 10 punktów są sumowane, 
tzn. po przekroczeniu więcej niż 10 bramek drużyna zdobywa obydwa bonusy. 
Oblicz całkowity wynik drużyny, dodając punkty zdobyte ze zdobytych bramek 
i wszelkie stosowne punkty bonusowe. 
"""
goals_scored = 8
bonus_points = 0


def numberOfGoals(goals_scored):
    new_point = goals_scored * 10
    if goals_scored > 5:
        new_point += 5
    if goals_scored > 10:
        new_point += 10

    return new_point


print(f"Total score of the team is {numberOfGoals(goals_scored)}.")

print('---')

"""
do obliczenia mocy wyjściowej panelu słonecznego zgodnie z następującymi zasadami:
    jeśli intensywność światła słonecznego jest mniejsza lub równa 200, moc wyjściowa wynosi 0 watów
    jeśli intensywność światła słonecznego jest większa niż 200, ale mniejsza lub równa 400, 
    moc wyjściowa wynosi 100 watów
    jeśli intensywność światła słonecznego jest większa niż 400, ale mniejsza lub równa 600, 
    moc wyjściowa wynosi 200 watów
    jeśli intensywność światła słonecznego jest większa niż 600, moc wyjściowa wynosi 300 watów
"""

sunlight_intensity = 500.0


def solarPanel(power):
    if power < 200:
        return 0
    elif 400 >= power > 200:
        return 100
    elif 600 >= power > 400:
        return 200
    else:
        return 300


print(
    f"Power output of the solar panel is {solarPanel(sunlight_intensity)} watts.")

print('---')

"""
użyj instrukcji warunkowej do określenia oceny ucznia zgodnie z następującymi zasadami:
    jeśli wynik quizu jest mniejszy niż 60, ocena to F
    jeśli wynik quizu wynosi od 60 do 69 włącznie, ocena to D
    jeśli wynik quizu mieści się w przedziale od 70 do 79 włącznie, ocena to C
    jeśli wynik quizu mieści się w przedziale od 80 do 89 włącznie, ocena to B
    jeśli wynik quizu wynosi 90 lub więcej, ocena to A
"""

quiz_score = 87


def quiz(score):
    if score < 60:
        return "F"
    elif 69 >= score > 60:
        return "D"
    elif 79 >= score > 70:
        return "C"
    elif 89 >= score > 80:
        return "B"
    elif 90 >= score:
        return "A"


print(f"""The student's grade is "{quiz(quiz_score)}".""")

print('---')

"""
Następnie użyj instrukcji warunkowej do określenia kosztu pokoju hotelowego zgodnie z następującymi zasadami:
    podstawowy koszt pokoju hotelowego to 100 USD za noc
    jeśli podróżny zostaje dłużej niż 7 nocy, otrzymuje 10% zniżki
    jeśli podróżny posiada kod rabatowy 'SUMMER20', otrzymuje 20% zniżki
    jeśli podróżny posiada kod rabatowy 'WINTER10', otrzymuje 10% zniżki
    jeśli podróżny nie ma kodu rabatowego lub ma nieważny kod rabatowy,
      wydrukuj poniższy komunikat i nie stosuj rabatu:
    'No discount will be applied.'
"""
num_nights = 10
discount_code = 'SUMMER20'


def priceHotel(nights, code):
    price = 100
    allPriceHotel = price * nights

    if nights > 7:
        allPriceHotel *= 0.9

    if code == 'SUMMER20':
        allPriceHotel *= 0.8
    elif code == 'WINTER10':
        allPriceHotel *= 0.9
    else:
        print('No discount will be applied.')

    return allPriceHotel


print(
    f"Total cost of the hotel room is $ {priceHotel(num_nights, discount_code)}.")

print('---')

"""
poziom gracza zgodnie z następującymi zasadami:
    jeśli gracz ma mniej niż 100 XP, jest na poziomie 1
    jeśli gracz ma od 100 do 499 XP, jest na poziomie 2
    jeśli gracz ma od 500 do 999 XP, jest na poziomie 3
    jeśli gracz ma 1000 XP lub więcej, jest na poziomie 4
"""

xp = 750


def yourLevel(xp):
    if xp >= 1000:
        level = 4
        return level
    elif 999 >= xp > 500:
        level = 3
        return level
    elif 499 >= xp > 100:
        level = 2
        return level
    else:
        level = 1
        return level


print(f"The player is at level {yourLevel(xp)}.")

print('---')

"""
jeśli gracz używa miecza - 'sword', a wróg nosi skórzaną zbroję - 'leather', 
zadawane obrażenia wynoszą 10 punktów
jeśli gracz używa miecza - 'sword', a wróg nosi zbroję kolczugi - 'chainmail', 
zadawane obrażenia wynoszą 5 punktów
jeśli gracz używa topora - 'axe', a wróg nosi skórzaną zbroję - 'leather', 
zadawane obrażenia wynoszą 5 punktów
jeśli gracz używa topora - 'axe', a wróg nosi zbroję kolczugi - 'chainmail', 
zadawane obrażenia wynoszą 10 punktów
jeśli gracz używa łuku - 'bow', zadawane obrażenia wynoszą zawsze 3 punkty
"""
weapon_type = 'sword'
armor_type = 'leather'


def userPlayer(weapon, armor):
    if weapon == 'sword' and armor == 'leather':
        return 10
    elif weapon == 'sword' and armor == 'chainmail':
        return 5
    elif weapon == 'axe' and armor == 'leather':
        return 5
    elif weapon == 'axe' and armor == 'chainmail':
        return 10
    elif weapon == 'bow':
        return 3


print(
    f"The player can inflict {userPlayer(weapon_type, armor_type)} points of damage.")

print('---')

"""
--jeśli żołnierz ma mniej niż 1 rok służby, jest szeregowcem - 'Private'
--jeśli żołnierz ma od 1 do 3 lat służby, a jego ocena wydajności wynosi co najmniej 7,0, 
jest kapralem - 'Corporal'
--jeśli żołnierz ma od 1 do 3 lat służby, a jego ocena wydajności jest niższa niż 7,0, 
jest szeregowcem pierwszej klasy - 'Private First Class'
--jeśli żołnierz ma od 4 do 6 lat służby, a jego ocena wydajności wynosi co najmniej 7,0, 
jest sierżantem - 'Sergeant'
--jeśli żołnierz ma od 4 do 6 lat służby, a jego ocena wydajności jest niższa niż 7,0, 
jest kapralem - 'Corporal'
--jeśli żołnierz ma 7 lub więcej lat służby, a jego ocena wydajności wynosi co najmniej 7,0, 
jest sierżantem sztabowym - 'Staff Sergeant'
--jeśli żołnierz ma 7 lub więcej lat służby, a jego ocena wydajności jest niższa niż 7,0, 
jest sierżantem - 'Sergeant'
"""
years_of_service = 5
performance_rating = 8.5


def solider(year, performance):
    if 1 > year:
        return 'Private'
    elif 3 >= year > 1 and performance >= 7.0:
        return 'Corporal'
    elif 3 >= year > 1 and 7 > performance:
        return 'Private First Class'
    elif 6 >= year > 4 and performance >= 7.0:
        return 'Sergeant'
    elif 6 >= year > 4 and 7 > performance:
        return 'Corporal'
    elif year >= 7 and performance >= 7.0:
        return 'Staff Sergeant'
    elif year >= 7 and 7 > performance:
        return 'Sergeant'


print(
    f"The soldier's rank is {solider(years_of_service, performance_rating)}.")

print('---')
"""
jeśli dochód danej osoby jest mniejszy lub równy 10 000 USD i jest singlem, stawka podatku wynosi 10%
jeśli dochód danej osoby jest mniejszy lub równy 10 000 USD i jest ona w związku małżeńskim, 
stawka podatku wynosi 8%
jeśli dochód danej osoby wynosi od 10 001 do 50 000 USD i jest singlem, stawka podatku wynosi 15%
jeśli dochód danej osoby wynosi od 10 001 do 50 000 USD i jest ona w związku małżeńskim, stawka podatku wynosi 13%
jeśli dochód osoby jest większy niż 50 000 USD i jest singlem, stawka podatku wynosi 20%
jeśli dochód danej osoby jest większy niż 50 000 USD i są małżeństwem, stawka podatku wynosi 18%
"""
income = 45000.0
marital_status = 'married'

def merried(income, marital_status):
    if 10000 >= income and marital_status == 'single':
        rate = '10.0%'
    elif 10000 >= income and marital_status == 'married':
        rate = '8.0%'
    elif 50000 > income >= 10001 and marital_status == 'single':
        rate = '15.0%'
    elif 50000 > income >= 10001 and marital_status == 'married':
        rate = '13.0%'
    elif income > 50000 and marital_status == 'single':
        rate = '20.0%'
    elif income > 50000 and marital_status == 'married':
        rate = '18.0%'
    return rate


print(f"The tax rate is {merried(income, marital_status)}.")

print('---')

"""
określ, czy kupić, trzymać, czy sprzedać akcje zgodnie z następującymi zasadami:
jeśli trend cenowy akcji jest wzrostowy, a bieżąca cena jest niższa lub 
równa średniej cenie z ostatnich 30 dni, trzymaj akcje
jeśli trend cen akcji jest wzrostowy, a bieżąca cena jest wyższa
 niż średnia cena z ostatnich 30 dni, kup akcje
jeśli trend cen akcji jest spadkowy, a bieżąca cena jest wyższa lub równa 
średniej cenie z ostatnich 30 dni, trzymaj akcje
jeśli trend cenowy akcji jest spadkowy, a bieżąca cena jest niższa 
niż średnia cena z ostatnich 30 dni, sprzedaj akcje
jeśli trend cenowy akcji jest stabilny, a bieżąca cena jest niższa lub 
równa średniej cenie z ostatnich 30 dni, kup akcje
jeśli trend cenowy akcji jest stabilny, a bieżąca cena jest wyższa 
niż średnia cena z ostatnich 30 dni, sprzedaj akcje
"""
current_price = 75.0
price_trend = 'up'
average_price = 70.0

def calculate(price_trend, current_price, average_price):
    if price_trend == 'up' and average_price >= current_price:
        return 'hold'
    elif price_trend == 'up' and current_price > average_price:
        return 'buy'
    elif price_trend == 'down' and average_price > current_price:
        return 'sell'
    elif price_trend == 'stable' and average_price >= current_price:
        return 'buy'
    elif price_trend == 'stable' and current_price > average_price:
        return 'sell'
    
print(f"The recommended action is to {calculate(price_trend, current_price, average_price)} the stock.")

print('---')

""""
jeśli wynik gracza jest mniejszy niż 1000, znajduje się on na poziomie 1
jeśli wynik gracza mieści się w przedziale od 1000 do 4999, jest na poziomie 2
jeśli wynik gracza mieści się w przedziale od 5000 do 9999 i pozostało mu co najmniej 1 życie, jest na poziomie 3
jeśli wynik gracza mieści się w przedziale od 5000 do 9999 i nie ma już życia, jest na poziomie 2
jeśli wynik gracza wynosi 10 000 lub więcej i pozostały mu co najmniej 2 życia, jest na poziomie 4
jeśli wynik gracza wynosi 10 000 lub więcej i pozostało mu 1 życie, jest na poziomie 3
jeśli wynik gracza wynosi 10 000 lub więcej i nie ma już życia, jest na poziomie 2
"""
score = 7000
lives = 2

def playerGames (score, lives):
    if 1000 >= score:
        level = 1
    elif 4999 > score > 1000:
        level = 2
    elif 9999 > score > 5000 and lives > 1:
        level = 3
    elif 9999 > score > 5000 and lives == 0:
        level = 2
    elif level >= 10000 and lives >= 2:
        level = 4
    elif level >= 10000 and lives == 1:
        level = 3
    elif level >= 10000 and lives == 0:
        level = 2
    return level 

print(f"The player is at level {playerGames(score, lives)}.")