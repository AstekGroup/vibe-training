# Vibe Coding: Formation Master (3j)

v2 Philippe Pary - Thomas Foutrein
2025-08-26

## Pré-requis
* Connaissance d'au moins un langage de programmation ou scripting
* Matériel de travail adapté à la programmation
* VScode installé
* Un ou plusieurs agents de Vibe Coding installés (Cursor, Gemini CLI, etc.)
* Licence Copilot / Cursor (fournies pour la durée de la formation)
* Un projet personnel à développer

## Objectifs de la formation
- Maîtriser les concepts avancés du Vibe Coding et du développement agentique.
- Comprendre et implémenter des stratégies de Context Engineering robustes.
- Utiliser des frameworks avancés (BMAD, SuperClaude, CCPM) pour structurer le développement IA.
- Développer un projet complet en appliquant les meilleures pratiques du Context Engineering.
- Sécuriser les interactions avec les agents IA.

## Cours

### Première journée

Identique à la journée *starter*.

### Deuxième journée : Plongée dans le Vibe Coding Agentique

#### 9h00 - 9h30 : Introduction et présentation

* Accueil des participants, tour de table et attentes.
* Présentation des objectifs de la journée : passer du "prompting" au "développement agentique".

#### 9h30 - 10h30 : L'Ère des Agents de Vibe Coding (Théorie)

* **Qu'est-ce qu'un agent ?** : Définition, autonomie, outils, boucle de pensée.
* **Comparatif des agents du marché** : Forces et faiblesses de Claude Code, Cursor, Gemini CLI, Copilot, Kiro, Windsurf.
* **Discussion** : Quel agent pour quel usage ?

#### 10h30 - 10h45 : Pause

#### 10h45 - 12h30 : Frameworks et Serveurs MCP (Théorie et Pratique)

* **Serveurs MCP (Model-Controller-Prompter)** : Le pont entre l'IA et le monde extérieur (APIs, bases de données, web).
* **Frameworks Agent-Agnostiques** : Introduction à la **BMAD-METHOD** pour la planification collaborative.
* **Frameworks Spécifiques** :
    * **SuperClaude / CCPM** : Le développement "spec-driven" pour une traçabilité parfaite.
* **Atelier** : Initialisation d'un environnement de développement agentique.

#### 12h30 - 13h30 : Pause déjeuner

#### 13h30 - 15h00 : Atelier : "Code with Spec" (Pratique)

* **Workshop** : Développement d'une micro-fonctionnalité en utilisant une approche "spec-driven" inspirée de Kiro et CCPM.
    1. Définition des `requirements.md` (besoins).
    2. Élaboration du `design.md` (architecture).
    3. Création des `tasks.md` (plan d'action).
* **Mise en action** : L'agent exécute le plan validé. On observe et on guide.

#### 15h00 - 15h15 : Pause

#### 15h15 - 16h45 : Sécurité des Agents IA (Théorie et Pratique)

* **Les nouvelles menaces** : Prompt Injection, fuite de données, empoisonnement du contexte (MCP Poisoning).
* **Bonnes pratiques** : Comment sécuriser ses `rules`, valider les sources de contexte et utiliser les agents en toute sécurité.
* **Démonstration** : Analyse d'un cas de "prompt injection" et comment le prévenir.

#### 16h45 - 17h30 : Bilan de la journée et Q&A

* Retours d'expérience sur l'atelier "Code with Spec".
* Discussion sur l'impact des agents sur le métier de développeur.

### Troisième journée : Le "Context Engineering" en Pratique

#### 9h00 - 9h30 : Introduction au Context Engineering

* **Qu'est-ce que le Context Engineering ?** : L'art d'orchestrer l'information pour l'IA.
* **Les 6 Piliers du Contexte** : Instructions, Mémoire (court/long terme), RAG, Outils, Format de sortie.

#### 9h30 - 10h45 : Maîtriser le Contexte Persistant (Atelier)

* **Le cœur du réacteur** : Étude approfondie des fichiers de règles des principaux agents.
    * `CLAUDE.md`, `.cursor/rules/`, `GEMINI.md`, `.github/copilot-instructions.md`, `.kiro/steering/`.
* **Atelier** : Création d'un jeu de règles complet et modulaire pour un projet type (Stack, conventions, patterns, etc.).

#### 10h45 - 11h00 : Pause

#### 11h00 - 12h30 : Techniques de Contexte Avancées (Théorie et Pratique)

* **L'inclusion conditionnelle** : Charger le bon contexte au bon moment (ex: `fileMatch` de Kiro, modes de Windsurf).
* **Les références dynamiques** : Lier le contexte à l'état réel du code (ex: `#[[file:path]]` de Kiro).
* **La mémoire automatique** : Laisser l'IA apprendre du projet (ex: Memories de Windsurf).
* **L'automatisation par Agent Hooks** : Déclencher des actions sur des événements (ex: Kiro).
* **Atelier** : Implémentation de règles conditionnelles sur un cas pratique.

#### 12h30 - 13h30 : Pause déjeuner

#### 13h30 - 16h00 : Grand Atelier : Projet Personnel "Context-Engineered"

* Les participants appliquent l'ensemble des techniques apprises à leur projet personnel.
* **Objectif** : Produire un `AGENTS.md` (ou équivalent) robuste, des `steering files`, des règles modulaires et des instructions claires.
* Les formateurs passent en revue les projets pour fournir un support individualisé.

#### 16h00 - 16h15 : Pause

#### 16h15 - 17h15 : Présentation des Projets et Feedback

* Chaque participant (ou groupe) présente son projet et la stratégie de Context Engineering mise en place.
* Discussion de groupe, partage des découvertes et des difficultés.

#### 17h15 - 18h00 : Bilan, Perspectives et Évaluation

* Bonnes pratiques à retenir et pièges à éviter.
* Ressources pour continuer à progresser.
* Questions/réponses finales.
* Évaluation de la formation.
