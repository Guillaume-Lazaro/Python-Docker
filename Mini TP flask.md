# Mini TP - Flask API

1. Flask est un (mini) framework Python pour faire des applications web très simplement et rapidement,
en effet pas besoin de html/CSS et js, Flask crée dynamiquement des pages web via le moteur Jinja.

2. Le code http est le code renvoyé par une requête web, les plus connus sont 404 le code d'erreur le
plus courant, ou tout simplement 200 pour informer que tout va bien. Les codes allant de 100 à 527
ont été définis et sont "réservés" certains codes sont inutilisés et la plage 600 est souvent utilisé
pour les messages d'erreurs personnalisés.

3. En python la variable __name__ renvoie le nom du module actuel, si il est différent de __main__
cela signifie que le code est importé et lancé depuis un autre fichier .py, par contre si il renvoie
bien __main__ alors cela signifie simplement que nous sommes dans le module principal, le point d'entrée
de l'application. (Désolé pour cette explication brouillone, j'ai essayé avec mes propres mots...)

4. Une route est une association entre une adresse IP de destination (type 127.0.0.0/100) et une 
passerelle qui servira de route (d'où le nom) pour acheminer les données via cette passerelle.

5. Un fichier statique est simplement un fichier qui permet de définir des régles CSS ou des 
pages html qui ne sont pas dynamiques ou alors une liste de variables à récupérer lors de 
l'exécution du code. Les templates à l'opposé, sont eux plutôt des textes à trous préconçus (des 
pages webs, pas des vrais textes) que le développeur peut aggrémenter comme il le souhaite. 
Flask permet d'utiliser et de créer ses propres templates (de la même maniére que beaucoup 
de framework js).

6. Jinja2 est un moteur de template utilisable en python et qui génére des pages html, justement en
utilisant des templates (fonction render_template() )