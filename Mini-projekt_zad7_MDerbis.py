class Samochod:

    def __init__(self, marka, model, rok_produkcji, przebieg):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg

    def __str__(self):
        return f'Samochód marki: {self.marka}, model: {self.model}, rok produkcji: {self.rok_produkcji}, przebieg: {self.przebieg}.'

    def __lt__(self, other):
        return self.przebieg < other.przebieg



samochod1 = Samochod('Opel', 'Astra', 2003, 220000)
samochod2 = Samochod('Skoda', 'Fabia', 2018, 90000)
samochod3 = Samochod('Ford', 'Fiesta', 2011, 150000)

print(samochod1)
print(samochod2)
print(samochod3)

print(samochod1<samochod2)
print(samochod2<samochod3)
print(samochod3<samochod1)