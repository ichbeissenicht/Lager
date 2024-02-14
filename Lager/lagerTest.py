import lagerLib as lib

lib.productStorageConfigPath = "storage.json"
lib.productLibraryConfigPath = "library.json"
lib.readConfigStorage()
lib.readConfigLibrary()


while 1:

    waitforscan = input("Warte auf Scan...   ")
    if waitforscan == "einlagern":
        produkt = input("Wenn das Produkt bereits einen QR-Code hat Scannen Sie diesen einfach ein, andernfalls drücken Sie einfach Enter")

        if produkt == "":


            wafer = lib.newWafer(
                    lib.newID32(),
                    name="wafer1",
                    charge=1,
                    typ=5,
                    sperrVermerk=True,
                    reserviert=input("Fuer wen ist dieser Wafer reserviert? ")
                )


        else:
            wafer=lib.newWaferFromData(produkt)



        lp = input("Lagerplatz?")
        lib.addEntry(
            lp,
            wafer
        )

        #lib.printConfig()
        lib.writeConfigLibary()
        lib.writeConfigStorage() #Speichert Config in storage.json
        print("Einlagern Abgeschlossen")
        break



    elif waitforscan == "auslagern":
        produkt_loeschen = input("QR Code Scannen: ")





        #print(lib.newWaferFromData(produkt_loeschen))
        #lib.deleteEntry(lib.newWaferFromData(produkt_loeschen))
        #lib.writeConfig()  # Speichert Config

    elif waitforscan == "info":
        pass
    else:
        print("Falsche eingabe Ausgeführt!")
        break
