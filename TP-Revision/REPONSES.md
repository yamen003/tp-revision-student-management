
## Partie 7 – Questions de synthèse

**48. Test manuel vs automatisé :** un test manuel est exécuté par une personne, il est lent, difficile à répéter à l'identique et sujet aux oublis. Un test automatisé est un script, rapide, reproductible, exécutable à chaque modification (CI).

**49. Rôle de unittest :** framework de la bibliothèque standard Python pour écrire, organiser (classes `TestCase`, `setUp`/`tearDown`) et exécuter des tests, avec rapport des succès et échecs.

**50. Assertions :** `assertEqual(a, b)` vérifie que `a == b`. `assertTrue(x)` vérifie que `x` est vrai. `assertRaises(Exc)` (souvent avec `with`) vérifie qu'une exception précise est levée.

**51. Cas limites :** les erreurs se concentrent aux bornes (liste vide, 0, 10, 20, division par zéro). Ce sont les cas que les développeurs oublient et où les conditions (`<` vs `<=`) sont les plus fragiles.

**52. Git vs GitHub :** Git est l'outil de versionnement décentralisé (local). GitHub est un service d'hébergement de dépôts Git avec collaboration (pull requests, Actions, issues).

**53. Rôle d'un commit :** enregistrer un instantané cohérent du projet avec un message, qui permet de suivre l'historique, de comparer et de revenir en arrière.

**54. Workflow GitHub Actions :** processus automatisé défini dans le dépôt, déclenché par des événements (push, pull request, planning), composé de jobs et d'étapes exécutés sur des runners.

**55. Rôle du fichier YAML :** décrire de façon déclarative le workflow (déclencheurs, environnement, étapes) ; il est versionné avec le code.

**56. GitHub Actions vs Jenkins :** GitHub Actions est un service CI/CD intégré à GitHub, hébergé (runners fournis), configuré en YAML. Jenkins est un serveur d'automatisation open source, auto-hébergé, très extensible par plugins, avec des pipelines décrits dans un `Jenkinsfile`, et demande plus de maintenance.

**57. Test en échec dans un pipeline :** l'étape échoue, le pipeline s'arrête (les étapes suivantes sont ignorées), le build est marqué en échec et l'équipe est notifiée ; le code défectueux n'est pas déployé.

**58. Tests unitaires vs fonctionnels :** un test unitaire vérifie une petite unité isolée (une fonction), rapidement. Un test fonctionnel vérifie un comportement complet du point de vue de l'utilisateur (interface + logique), plus lent et plus fragile.

**59. Rôle de Selenium WebDriver :** fournir l'API et le pilote qui commandent le navigateur (navigation, saisie, clics, lecture du DOM).

**60. Pourquoi un navigateur :** parce que l'on teste le rendu et le comportement réels (HTML, CSS, JavaScript, formulaires) tels que l'utilisateur les voit, ce qu'un simple appel de fonction ne vérifie pas.

**61. Test Selenium vs manuel dans un navigateur :** les actions sont les mêmes, mais Selenium est scripté, répétable, rapide, exécutable en CI et sans intervention humaine, alors que le test manuel dépend de l'opérateur.

**62. Couverture élevée = absence de bugs ?** Non. La couverture mesure les lignes ou branches exécutées, pas la qualité des vérifications. Un test sans assertion pertinente couvre du code sans rien prouver ; des cas limites, des interactions ou des exigences manquantes peuvent rester non testés. Une bonne couverture est nécessaire mais pas suffisante.
