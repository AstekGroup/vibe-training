# Vibe Coding: Formation Starter (1j)

v1 Philippe Pary - Thomas Foutrein
2025-05-27

Première approche d'une formation Vibe Coding en une journée
Formation "Vibe Coding" pour Développeurs Débutants


Une journée pour apprendre à coder avec l'assistance de l'IA

##  Pré-requis
* Connaissance d'au moins un langage de programmation ou scripting
* Matériel de travail adapté à la programmation
* VScode installé
* Cursor installé
* Licence Copilot./ Cursor (fournies pour la durée de la formation)

## Objectifs de la formation
* Utiliser Cursor et d'autres IDE optimisés pour l'IA
* Formuler des prompts efficaces pour l'IA dans un contexte de développement
* Développer un projet complet en utilisant les techniques de "Vibe Coding"

## Cours

### 9h00 - 9h30 : Introduction et présentation

Tour de table:
    * Nom, fonction
    * As-tu déjà vibe codé ?
    * Comment vois-tu le vibe coding ?
    * Ta machine est prête ? (Cursor installé)
    * Quelles sont tes attentes vis à vis de la journée ? 

➡️ Présentation du plan de la journée

### 9h30 - 10h15 : Information : Les outils du "Vibe Coding" (Théorie)

#### Vibe coding

Concept récent, de février 2025. Par Andrej Karpathy (co-fondateur d'OpenAI)

Technique de programmation assisté par des LLMs et basé sur du prompt. Il se différencie d'un outil de complétion basé sur les LLMs comme Copilot par l'importance crucciale du prompt dans le processus de développement.

Le vibe-coding peut être utilisé comme un outil low/no-code. Ceci dit, la pratique des derniers mois démontre que comme tous les outils low/no-code, un non-informaticien va produire des logiciels de mauvaise qualité de cette façon (failles de sécurités, bugs…). Cette pratique est à réserver pour les POC ou le prototypage.

Entre les mains d'un développeur compétent, les outils de vibe-coding entraînent une hausse de la productivité et de l'efficacité. Mais également une transformation du métier.

#### Workflow du développeur avec de l'IA

Dans tous les cas, l'écrasante majorité du code sera rédigée par LLM. Quelques bugs ou fonctionnalité peuvent être traîtées à la main, soit que le LLM s'y casse les dents, soit qu'il soit plus rapide, plus fun ou instructif de faire ainsi.

Le métier de développeur consiste surtout à s'assurer de la qualité du code produit. La partie relecture de code, comme pour une PR/MR, devient centrale.

##### 1. Itératif

Étape par étape. On commence par un gros prompt qui défini le projet (on verra plus tard comment en faire des règles)
On ajoute les fonctionnalités (ou les refacto) un à un à partir de prompts successif. 

✅ Meilleure maîtrise de l'évolution du logiciel
❌ Pensez à commiter chaque étape fonctionnelle, le vibe-coding peut vite partir en vrille

Exemple de session: URL

##### 2. One big happy prompt

On prépare un prompt très détaillé, générallement sous la forme d'un fichier markdown et on accompagne l'IA dans la réalisation du projet

✅ Peu de risques de régressions entre les prompts: le LLM sait où il va. Le projet a été pensé et structuré
❌ La relecture et bonne compréhension de ce qui a été généré est longue et fastidieuse. Le temps de développement est généralement augmenté

Exemple de prompt complet:
`

`

#### Les outils disponibles

* Replit: https://replit.com/ Éditeur en ligne
* WindSurf: https://windsurf.com/ 
* Kilo code : https://marketplace.visualstudio.com/items?itemName=kilocode.Kilo-Code Plugin VSCode 
* Continue : https://marketplace.visualstudio.com/items?itemName=Continue.continue Plugin VSCode
* Cursor: https://www.cursor.com/ logiciel retenu au sein d'Astek

#### Comment fonctionne l'IA pour le code

Notions : 
- LLM (modèles fondations, modèles entraînés)
- data source
- vectorisation
- prompt engineering
- MCP
- Agent IA
- Agent2Agent

Comme pour tout sujet, les LLM fonctionnent en perroquets stochastiques : ils analysent un texte donné, réduit en tokens, et tentent de déduire l'intention entre le prompt et la codebase.

Le LLM tente alors de générer la réponse la plus probable, sur base de son entraînement et de son nombre de paramètres possibles._

<Schemas issus du net ici>

| Aspect                      | Vibe Coding                                        | Traditional Coding                                       |
|:----------------------------|:---------------------------------------------------|:---------------------------------------------------------|
| **Approach**                | Describe desired outcomes in plain language        | Write code line-by-line using programming languages      |
| **Tool Used**               | Large Language Models (LLMs)                       | IDEs, compilers, debuggers, and coding frameworks        |
| **User Skill Level**        | Suitable for beginners and non-programmers         | Requires strong technical knowledge                      |
| **Coding Knowledge**        | Minimal – focuses on intent, not syntax            | High – user must understand logic, syntax, and structure |
| **Speed**                   | Fast – good for quick builds and iteration         | Slower – more precision and planning involved            |
| **Control and Precision**   | Lower – depends on the AI's interpretation         | High – every line is written and reviewed by developer   |
| **Best For**                | Rapid prototyping, small tools, idea exploration   | Scalable, secure, and production-grade systems           |
| **Review Process**          | Output reviewed post-generation; often iterative   | Code is reviewed during and after development            |
| **Security & Maintenance**  | Higher risk due to unknowns in generated code      | Easier to secure and maintain with full understanding    |
| **Learning Curve**          | Low – users can start building with basic guidance | High – requires learning languages, logic, and debugging |

#### Modèles à favoriser 

**Claude 4** Opus (plus cher, limité) ou Sonnet

Gemini-2.5-pro donne de bons résultats

ChatGPT-4.1 sur le front

C'est aussi très subjectif, d'un dev à l'autre on apprécie des choses différentes. Un LLM plus ou moins verbeux, réflexif… 

➡️ Faire un essai en one try des différents modèles avec le prompt `Développe un système de gestion de site web statique à partir de fichiers markdown en utilisant Python3, HTML, Javascript (sans framework) et TailWind`

#### Principales Limites et pièges à éviter

- Comitez ! L'IA peut ruiner en quelques minutes plusieurs semaines de travail
- Faites des branches locales en grande quantité pour tester plusieurs prompts pour régler un même point
- Soyez attentif à la couverture des tests
- Soyez attentif à la relecture de code

### 10h30 - 11h00 : Information : L'art du prompt engineering pour le code (Théorie)

##### Principes fondamentaux pour communiquer avec l'IA

On tourne autour du prompt. Le prompt a plusieurs niveaux 

- Rules générales: Users rules dans la configuration. S'appliqueront à tous les projets. Vous pouvez par exemple lui demander d'être didactique ou à l'inverse laconique
- Rules locales: dans un dossier `.cursor/rules` s'applique au dossier et aux sous-dossiers. Utile en cas de mono-repo pour appliquer un comportement différent suivant le dossier (language de programmation, règles de développement dont convention de nommage des variables, contexte général du projet)
- Utiliser `context7` pour avoir de meilleurs résultats https://github.com/upstash/context7
- Le prompt en tant que tel

Pour les rules consultez: https://docs.cursor.com/context/rules 

#### Structure d'un prompt efficace pour le développement

Rappeler 
- contexte général du projet
- exemples de données (et contre-exemples)
- exemples de règles métier (et contre-exemples)
- dans quel dossier travailler (et préciser si l'IA doit s'y contraindre, elle a tendance à aller un peu partout sinon)

#### Exemples de prompts qui fonctionnent vs ceux qui échouent

???

#### Adapter ses prompts selon le contexte et l'objectif

???

### 11h00 - 12h30 : Compréhension : Premiers pas pratiques (Pratique)

#### Exercices simples de génération de code

- Générer un snake en HTML/CSS/JS (sans Framework) avec sauvegarde des meilleurs score en `localStorage`
- Calculer en python une approximation de Pi en utilisant la méthode de Monte-Carlo
- Création d'une application client/serveur de gestion des tâches
- Bot Discord/Telegram/… qui indique la météo à partir d'une commande

#### Mini-défis pour tester différentes approches de prompts

avoir des repos buggy en PHP, Java et React

avoir une suite de Fibonacci en boucle infinie

### 13H30-14H00 : Compréhension : retour expérience (Théorie)

Tour de table:
    * Qu'as-tu appris ce matin ? 
    * Quelles difficultés as-tu rencontrées ?
    * Qu'est-ce qui t'a le plus marqué ? 

### 14h00 - 14h30 : Compréhension: Planification de projet (Théorie)

- Tour de table:
    * Choisir un projet
    * Consulter l'IA en mode Ask pour rédiger un plan de développement
    * Décomposer le projet en étapes 

### 14h30 - 16h00 : Utilisation : Développement assisté par IA (Pratique)

- Développer le projet
- Affiner son guidage l'IA
- Débugguer avec l'IA (cmd+L ou ctrl+L pour envoyer les logs au prompt)
- Générer la documentation

### 16h15 - 17h15 : Maîtrise : Finalisation et optimisation (Pratique)

- Revue de code assistée par IA: Passez en mode Ask, rédiger un prompt `Tu es un développeur expert, tu es mon binôme et tu relis mon code. Liste ici toutes les améliorations fonctionnelles, dans l'usage de librairies, dans le code que tu pourras trouver. Pointe les bonnes pratiques à adopter. Souligne les problèmes de sécurité que tu as repérés`
- Optimisation des performances: consulter l'IA (mode Ask) et appliquer les recommandations
- Tests automatisés générés par l'IA: consulter l'IA (mode Ask) et faites lui rédiger les tests. Passer en revue, compléter (ou faire compléter)
- Finalisation du projet: faire rédiger, ou relire, la documentation. Demander de préparer une image Docker.

### 17h15 - 18h00 : Bilan et perspectives (Théorie et discussion)

* Présentation des projets réalisés (tour de table)
    * Quelles difficultées as-tu rencontrées ?
    * Quelles bonnes pratiques as-tu retenues ?
    * As-tu des ressources à partager ? 
    * As-tu des questions ? 
</initial_code>
