# Formation Vibe Coding Starter (1 jour) - Guide Complet

v2 Philippe Pary - Thomas Foutrein
2025-08-26

**Guide intégré : Contenu formation + Notes formateur**

## Objectifs de la formation

* Coder avec Cursor
* Améliorer du code existant avec Cursor
* Intégrer Cursor dans un environnement de développement existant
* Personnaliser Cursor à vos besoins métier
* Formuler des prompts efficaces pour l'IA dans un contexte de développement
* Développer un projet complet en utilisant les techniques de "Vibe Coding"

## Pré-requis

* Connaissance d’au moins un langage de programmation ou scripting
* Connaissance des processus de développement informatique
* Connaissance du contrôle de version (git)
* Connaissance des IDE (VSCode, IntelliJ…)
* Matériel de travail adapté à la programmation IDE installé avec accès à un outil de vibe coding (cursor, gemini-cli …

## Public cible

Cette formation d'une journée introduit les développeurs au concept du Vibe Coding. Le public cible a déjà des compétences en programmation mais découvre l'IA générative pour le développement.

## Planning de la journée

| Horaire                 | Module                            | Durée | Contenu                                              |
| ----------------------- | --------------------------------- | ------ | ---------------------------------------------------- |
| **9h00 - 9h30**   | **Introduction**            | 30min  | Tour de table, présentation du programme            |
| **9h30 - 10h15**  | **Fondements**              | 45min  | Démo "frimer", 5 compétences, fonctionnement IA    |
| **10h15 - 11h00** | **Prompt Engineering**      | 45min  | Template de prompt, exercice collectif               |
| **11h00 - 12h00** | **Exercice Guidé**         | 60min  | Analyseur Performance Web (développement collectif) |
| **12h00 - 12h30** | **Exercices Individuels**   | 30min  | Choix projets, démarrage (Snake, Pi, Todo, Debug)   |
| **12h30 - 13h30** | **🍽️ PAUSE DÉJEUNER**    | 60min  |                                                      |
| **13h30 - 14h00** | **Retour d'expérience**    | 30min  | Tour de table sur apprentissages matinaux            |
| **14h00 - 16h00** | **Développement**          | 120min | Projets individuels + accompagnement formateur       |
| **16h00 - 16h15** | **☕ PAUSE**                | 15min  |                                                      |
| **16h15 - 17h15** | **Finalisation**            | 60min  | Review code IA, tests, optimisation, documentation   |
| **17h15 - 17h30** | **Risques** *(optionnel)* | 15min  | Green IT, sécurité, éthique, aspects juridiques   |
| **17h30 - 18h00** | **Bilan**                   | 30min  | Présentation projets, évaluation, perspectives     |

**🎯 Objectif central :** Maîtriser le workflow complet du vibe coding en une journée intensive et pratique.

## 📚 Sections détaillées

La formation est maintenant divisée en 10 modules autonomes, chacun dans un fichier séparé :

1. **[9h00 - 9h30 : Introduction et présentation](sections/01-introduction-presentation.md)**

   - Tour de table interactif avec questions guide
   - Présentation détaillée du programme
   - Notes formateur pour l'animation et gestion du groupe
2. **[9h30 - 10h15 : Fondements et Démonstration Live](sections/02-fondements-demonstration.md)**

   - Démonstration "frimer" chronométrée (20 min)
   - Framework des 5 compétences clés (THINKING, FRAMEWORKS, CHECKPOINTS, DEBUGGING, CONTEXT)
   - Explication du fonctionnement de l'IA générative
3. **[10h15 - 11h00 : Prompt Engineering Pratique](sections/03-prompt-engineering.md)**

   - Les 6 piliers d'un prompt efficace
   - Template de prompt universel avec structure CONTEXTE-RÔLE-TÂCHE-CONTRAINTES-FORMAT-EXEMPLES
   - Exercice collectif de transformation d'un prompt inefficace
4. **[11h00 - 12h00 : Exercice Guidé Collectif](sections/04-exercice-guide.md)**

   - Développement d'un Analyseur de Performance Web
   - Workflow itératif en 4 phases chronométrées
   - Démonstration du cycle prompt → test → validation → commit
5. **[12h00 - 12h30 : Début Exercices Individuels](sections/05-exercices-individuels-debut.md)**

   - Présentation détaillée des 4 exercices (Snake, Calculateur Pi, Todo App, Débogage Legacy)
   - Accompagnement personnalisé au choix selon profil
   - Lancement supervisé avec premier commit
6. **[13h30 - 14h00 : Retour d&#39;expérience](sections/06-retour-experience.md)**

   - Tour de table structuré (3 min par participant)
   - Analyse collective des patterns de succès et difficultés
   - Consolidation des apprentissages et ajustement pour l'après-midi
7. **[14h00 - 16h00 : Développement Accompagné](sections/07-developpement-accompagne.md)**

   - Développement intensif en cycles de 30 minutes
   - Accompagnement formateur rotatif (15 min par participant)
   - Support technique, méthodologique et coaching pédagogique
8. **[16h15 - 17h15 : Finalisation et Bonnes Pratiques](sections/08-finalisation-bonnes-pratiques.md)**

   - Revue de code assistée par IA avec audit automatisé
   - Génération de tests automatisés
   - Documentation automatisée et standards professionnels
9. **[17h15 - 17h30 : Risques à connaître](sections/09-risques-connaitre.md)** *(optionnel)*

   - Impact environnemental et éco-responsabilité
   - Sécurité du code généré et vulnérabilités fréquentes
   - Aspects éthiques, propriété intellectuelle et transparence
10. **[17h30 - 18h00 : Bilan et perspectives](sections/10-bilan-perspectives.md)**

    - Présentation des projets (4 min par participant)
    - Évaluation de satisfaction et atteinte des objectifs
    - Ressources pour continuer et mise en réseau

## Les IDE disponibles

| Outil                 | Type                | Avantages                                   | Inconvénients                          | Site officiel                                                                   |
| :-------------------- | :------------------ | :------------------------------------------ | :-------------------------------------- | :------------------------------------------------------------------------------ |
| **Claude Code** | Outil CLI           | ✅ Puissance du modèle Claude              | ⚠️ Pas d'intégration IDE             | [claude.com/product/claude-code](https://claude.com/product/claude-code)         |
| **Cursor**      | Éditeur dédié    | ✅ Interface optimisée pour le vibe coding | ⚠️ Application séparée à installer | [cursor.sh](https://cursor.sh)                                                     |
| **gemini-cli**  | Outil CLI           | ✅ Scriptable, gratuit                      | ⚠️ Pas d'interface graphique          | [github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **Copilot**     | Extension multi-IDE | ✅ Largement adopté, mature                | ⚠️ Moins orienté vibe coding         | [github.com/features/copilot](https://github.com/features/copilot)                 |
| **Kilo Code**   | Éditeur dédié    | ✅ Interface moderne, optimisé pour l'IA   | ⚠️ Relativement récent               | [kilocode.ai](https://kilocode.ai)                                                 |
| **Shai**        | Éditeur dédié    | ✅ Solution souveraine                      | ⚠️ Nouveau sur le marché             | [github.com/ovh/shai](https://github.com/ovh/shai)                               |
| **Continue**    | Extension VSCode    | ✅ Open source                              | ⚠️ Moins stable                       | [continue.dev](https://continue.dev)                                               |
