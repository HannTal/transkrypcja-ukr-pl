print("Wklej tekst, dwie puste linie z rzedu koncza, można enterowac")
stopword = ""
tekst = ""
stopy=0
while True: #czy byłoby lepiej while stopy<2 i mniej ifów? Byc może! TODO sprawdzić kiedy python sprawdza warunek while, sprawdzić best practices w takim wypadku. Kontrargument - edytowalność po ilu pustych liniach stopujemy.
    line = input() #bo input() pobiera po 1 linii, a chcemy ich wiecej, będzie sumowanie
    if line.strip() == stopword: #sprawdza czy linia ma 0 tekstu
        if stopy==1: #rozpoznanie 2 pustych linii
            break
        else:
            stopy=1 #rozpoznaje pierwsza pusta linie
    tekst += "%s\n" % line #dodaj linie inputu do pelnego tekstu od nowej linii
    if line.strip() != stopword:
        stopy=0 #zeruje licznik pustych linii na rozpoznaniu kolejnej z tekstem

#lista zamian znaków, kolejność ze znaczeniem przy digrafach, nie tu
#Jeśli wybieram transkrybować Ть na ć, to wrzucać na początku
tekst=tekst.replace("Б","B")
tekst=tekst.replace("б","b")
tekst=tekst.replace("В","W")
tekst=tekst.replace("в","w")
tekst=tekst.replace("Г","H")
tekst=tekst.replace("г","h")
tekst=tekst.replace("Ґ","G")
tekst=tekst.replace("ґ","g")
tekst=tekst.replace("Д","D")
tekst=tekst.replace("д","d")
tekst=tekst.replace("Є","Je")
tekst=tekst.replace("є","je")
tekst=tekst.replace("Ж","Ż")
tekst=tekst.replace("ж","ż")
tekst=tekst.replace("З","Z")
tekst=tekst.replace("з","z")
tekst=tekst.replace("И","Y")
tekst=tekst.replace("и","y")
tekst=tekst.replace("Ї","Ji")
tekst=tekst.replace("ї","ji")
tekst=tekst.replace("Й","J")
tekst=tekst.replace("й","j")
tekst=tekst.replace("Л","L")
tekst=tekst.replace("л","l")
tekst=tekst.replace("Н","N")
tekst=tekst.replace("н","n")
tekst=tekst.replace("П","P")
tekst=tekst.replace("п","p")
tekst=tekst.replace("Р","R")
tekst=tekst.replace("р","r")
tekst=tekst.replace("С","S")
tekst=tekst.replace("с","s")
tekst=tekst.replace("У","U")
tekst=tekst.replace("у","u")
tekst=tekst.replace("Ф","F")
tekst=tekst.replace("ф","f")
tekst=tekst.replace("Х","Ch")
tekst=tekst.replace("х","h")
tekst=tekst.replace("Ц","C")
tekst=tekst.replace("ц","c")
tekst=tekst.replace("Ч","Cz")
tekst=tekst.replace("ч","cz")
tekst=tekst.replace("Ш","Sz")
tekst=tekst.replace("ш","sz")
tekst=tekst.replace("Щ","Szcz")
tekst=tekst.replace("щ","szcz")
tekst=tekst.replace("Ь","`")
tekst=tekst.replace("ь","`")
tekst=tekst.replace("Ю","Ju")
tekst=tekst.replace("ю","ju")
tekst=tekst.replace("Я","Ja")
tekst=tekst.replace("я","ja")
tekst=tekst.replace("К","K")
tekst=tekst.replace("к","k")
tekst=tekst.replace("М","M")
tekst=tekst.replace("м","m")
tekst=tekst.replace("Т","T")
tekst=tekst.replace("т","t")

#zwraca wynik
print(tekst)