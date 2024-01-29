## Überblick

Dies ist ein Beispiel für eine mögliche Implementierung eines Wolle-Vergleichs-portals. 

Der Such-Button auf Wollplatz.de funktioniert leider nicht mehr, daher habe ich stattdessen händisch selbst nach dem Queryparameter für den Searchcall gesucht. Der Parameter ist "s", wenn man manuell https://www.wollplatz.de/wolle?s=Drops eingibt funktioniert die Suche zumindest noch. 
Die Seite ist Cloudflare geschützt, weswegen die Library cloudscraper verwendet werden muss. 

## Aufbau des Repos: 

Die einzelnen integrierten Onlineshops, werden als Klasse in der index.py des jeweiligen OnlineShop-Ordners definiert (Hier wurde nur zur Verdeutlichung ein zweiter Ordner hinzugefügt). Die Methoden für ein Preisvergleichsportal wären in dem Fall: 

        login, getProducts, addToCart, validateShoppingCart und order 

Die Klassen sollten von einer übergreifenden, abstrakten Klasse erben welche diese Methoden enthält. 

Die Suchergebnisse werden in einer Datenbank gespeichert, hier für den Zweck der Codingchallenge habe ich die Ergebnisse in einer einfachen CSV Datei gespeichert. 

## Testen

Da hier nur 1 Portal, und nur die Such-Methode implementiert ist, gibt es nur 1 Funktionalität zu testen. 

   1. cd Wollplatz
   2. `QUERY=DMC python3 getProductsTest.py`
   3. `QUERY=Stylecraft python3 getProductsTest.py`
   4. `QUERY=Drops python3 getProductsTest.py`
   5. `QUERY=Natura python3 getProductsTest.py`

   Für `Hahn`gibt es leider keine Suchergebnisse.





