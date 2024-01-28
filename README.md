# Wolle

Dies ist ein Beispiel für eine mögliche Implementierung eines Wolle-Vergleichs-portals. 

Der Such-Button auf Wollplatz.de funktioniert leider nicht mehr, daher habe ich stattdessen händisch selbst nach dem Queryparameter für den Searchcall gesucht. Der Parameter ist "s", wenn man manuell https://www.wollplatz.de/wolle?s=Drops eingibt funktioniert die Suche zumindest noch. 

Leider ist die Seite mittlerweile Cloudflare geschützt, weswegen auch das per http-request nicht funktioniert. Deswegen habe ich zumindest die html-responses genommen und die scraper per unittest getestet, siehe ./Wollplatz/scraper/test. 
Mehr lässt sich aufgrund von Cloudflare allerdings leider nicht machen. 

Zum Aufbau des Repos: 

Die einzelnen integrierten Onlineshops, werden als Klasse in der index.py des jeweiligen OnlineShop-Ordners definiert. Die Methoden für ein Preisvergleichsportal wären in dem Fall: 

        login, getProducts, addToCart, validateShoppingCart und order 

Die Suchergebnisse werden auf einer Datenbank gespeichert, hier für den Zweck der Codingchallenge hätte ich die Ergebnisse in einer einfachen CSV Datei gespeichert, da das Portal mit Cloudflare geblockt ist, konnte ich die Übung hier aber leider nicht zu ende führen. 
