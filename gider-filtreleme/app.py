
giderler = [
    {"tarih": "28.11.2025", "etiket":"yemek"},
    {"tarih": "02.12.2025", "etiket":"market"},
    {"tarih": "25.05.2026", "etiket":"eglence"}
]
sonuc = []
sonuc2= []
beklenilen_tarih = input("Hangi tarih için işlem yapmak istiyorsunuz: (gün, ay, yıl şeklinde giriniz.)")
assert beklenilen_tarih != "", "Tarih alanı boş kalamaz."
etiket_kategorisi = input("Hangi etiket için işlem yapmak istiyorsunuz: (yemek, market, eglence)")
assert etiket_kategorisi in ["yemek", "market", "eglence"], "Kategori hatası."



def filtre():
    for i in giderler:
        kayit_tarihi = i["tarih"]
        if kayit_tarihi == beklenilen_tarih:
            assert kayit_tarihi == beklenilen_tarih, "tarihler eşleşmiyor."
            sonuc.append(i)

def etiket():
    for i in giderler:
        kayit_etiket = i["etiket"]
        if kayit_etiket == etiket_kategorisi:
            sonuc2.append(i) 

filtre()
etiket()

print(f"Tarih: {sonuc} ")
print(f"Etiket: {sonuc2} ")            


