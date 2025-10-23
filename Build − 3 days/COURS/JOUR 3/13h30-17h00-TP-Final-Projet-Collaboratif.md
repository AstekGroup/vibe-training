# 14h00 - 17h00 : TP FINAL - Projet Collaboratif Multi-Agents (6h)

*Formation Vibe Coding - Durée estimée : 6 heures*

---

## 🎯 CONTEXTE & OBJECTIFS

**Mise en situation :** Vous êtes une équipe de développement qui vient de recevoir une demande client. Vous devez orchestrer différents agents spécialisés pour livrer un projet complet avec son MCP (Minimum Viable Product).

**Objectifs pédagogiques :**

- Maîtriser l'orchestration d'agents spécialisés
- Appliquer une méthodologie projet structurée
- Produire un livrable fonctionnel et sa documentation
- Développer un regard critique sur les processus IA

---

## 📋 CAHIER DES CHARGES

**Sujet :** *Application de gestion de bibliothèque personnelle*

**Description du besoin :**

> "Je souhaite une application web simple pour gérer ma collection de livres. Je veux pouvoir ajouter des livres (titre, auteur, année, genre), les marquer comme lus/non-lus, les rechercher et filtrer par genre. J'aimerais aussi voir des statistiques basiques sur ma collection (nombre total, pourcentage de livres lus, genre favori). L'interface doit être intuitive et responsive. Budget modéré, délai : 2 semaines."

---

## 🔄 PROCESSUS À SUIVRE

### ÉTAPE 1 : Agent P.O.P.M. (Product Owner Project Manager)

**Mission :** Définir le projet dans sa globalité

**Prompt suggéré :**

```
Tu es un Product Owner expérimenté. À partir du besoin client suivant : [insérer cahier des charges], je veux que tu :

1. Reformules les besoins en user stories détaillées
2. Priorises les fonctionnalités (MoSCoW)
3. Estimes la complexité et les risques
4. Proposes un planning de développement
5. Définis les critères d'acceptance pour chaque story
6. Identifies les contraintes techniques potentielles

Format ta réponse de manière structurée avec des sections claires.
```

**Livrables attendus :**

- Backlog produit priorisé
- User stories avec critères d'acceptance
- Planning macro du projet
- Analyse des risques

---

### ÉTAPE 2 : Agent Architecte

**Mission :** Établir l'architecture et les choix technologiques

**Prompt suggéré :**

```
Tu es un architecte logiciel senior. En te basant sur les spécifications du P.O. : [insérer résultats étape 1], je veux que tu :

1. Proposes une architecture technique adaptée
2. Justifies tes choix technologiques (stack, base de données, etc.)
3. Définis la structure des données
4. Crées un diagramme d'architecture
5. Identifies les patterns de conception à utiliser
6. Proposes une stratégie de déploiement
7. Évalues la scalabilité de la solution

Contraintes : Application web, budget modéré, maintenance simple.
```

**Livrables attendus :**

- Schéma d'architecture
- Choix technologiques justifiés
- Modèle de données
- Guide d'installation et déploiement

---

### ÉTAPE 3 : Agent(s) Développeur(s)

**Mission :** Développer les fonctionnalités de base

**Approche recommandée :** Créer 2-3 agents développeurs spécialisés

- Agent Frontend (UI/UX)
- Agent Backend (API/Base de données)
- Agent DevOps (Configuration/Déploiement)

**Prompt type pour chaque agent :**

```
Tu es un développeur [Frontend/Backend/DevOps] expert. En suivant l'architecture définie : [insérer résultats étape 2], développe :

[Pour Frontend]
- Interface utilisateur responsive
- Gestion des états et interactions
- Intégration avec l'API backend

[Pour Backend]
- API REST complète
- Gestion de la base de données
- Logique métier

[Pour DevOps]
- Configuration de l'environnement
- Scripts de déploiement
- Documentation technique

Code propre, commenté, avec gestion d'erreurs.
```

**Livrables attendus :**

- Code source complet et fonctionnel
- Documentation technique
- Guide d'installation

---

### ÉTAPE 4 : Agent QA (Quality Assurance)

**Mission :** Tester et valider la qualité du code

**Prompt suggéré :**

```
Tu es un QA Engineer expérimenté. Analyse le code développé et :

1. Crée un plan de tests complet (unitaires, intégration, E2E)
2. Identifies les cas de test critiques
3. Écris des tests automatisés pour les fonctions principales
4. Effectue une revue de sécurité basique
5. Vérifie la conformité aux user stories
6. Proposes des améliorations de qualité
7. Rédiges un rapport de test

Fournis des scripts de test exécutables.
```

**Livrables attendus :**

- Plan de tests détaillé
- Scripts de tests automatisés
- Rapport de qualité avec recommandations

---

### ÉTAPE 5 : Agent Relecteur de Code

**Mission :** Code review et optimisation

**Prompt suggéré :**

```
Tu es un senior developer spécialisé en code review. Analyse le code produit et fournis :

1. Une évaluation de la qualité du code (lisibilité, maintenabilité)
2. Des suggestions d'optimisation de performance
3. Une vérification des bonnes pratiques
4. Des recommandations d'architecture si nécessaire
5. Un score qualité global avec justification
6. Une checklist des points à améliorer avant mise en production

Sois constructif et pédagogique dans tes retours.
```

**Livrables attendus :**

- Rapport de code review
- Checklist d'améliorations
- Score qualité global

---

## 🎯 LIVRABLE FINAL : MCP (Minimum Complete Product)

**Le MCP doit contenir :**

1. **Code source complet** avec structure claire
2. **Base de données** configurée avec données de test
3. **Interface utilisateur** fonctionnelle et responsive
4. **API** opérationnelle avec endpoints documentés
5. **Tests** automatisés et passants
6. **Documentation** utilisateur et technique
7. **Guide** d'installation et déploiement

---

## 🔍 PHASE DE CRITIQUE ET ANALYSE

**Questions de réflexion :**

### Analyse du Processus

1. Quelles ont été les forces et faiblesses de chaque agent ?
2. Où avez-vous observé des pertes d'information entre agents ?
3. Quels ajustements de prompts ont été nécessaires ?
4. Le processus séquentiel était-il optimal ?

### Analyse du Résultat

5. Le MCP répond-il aux besoins initiaux du client ?
6. Quelles fonctionnalités auraient mérité plus d'attention ?
7. L'architecture proposée est-elle adaptée et scalable ?
8. La qualité du code est-elle satisfaisante ?

### Analyse Critique du Vibe Coding

9. Dans quels contextes cette approche multi-agents est-elle pertinente ?
10. Quels sont les risques et limitations identifiés ?
11. Comment optimiser la collaboration entre agents ?
12. Quand privilégier un agent unique vs multiple agents ?

---

## 📊 CRITÈRES D'ÉVALUATION

### Aspects techniques (60%)

- Fonctionnalité du MCP
- Qualité du code
- Respect de l'architecture
- Couverture de tests

### Processus Vibe Coding (25%)

- Qualité des prompts
- Orchestration des agents
- Traçabilité des décisions
- Cohérence globale

### Analyse critique (15%)

- Profondeur de l'analyse
- Pertinence des observations
- Propositions d'amélioration
- Vision stratégique

---

## 💡 CONSEILS POUR LES FORMATEURS

1. **Encouragez l'itération** : Les apprenants peuvent revenir sur des étapes précédentes
2. **Favorisez les échanges** : Travail en binômes recommandé
3. **Documentez les prompts** : Demandez de sauvegarder tous les prompts utilisés
4. **Variez les sujets** : Proposez 2-3 cahiers des charges différents au choix
5. **Préparez des prompts de déblocage** pour les étapes critiques

---

## 📝 PLANNING DÉTAILLÉ

### 14h00-14h30 : Étape 1 - Agent P.O.P.M.

- Analyse du besoin client
- Création du backlog produit
- Définition des user stories

### 14h30-15h00 : Étape 2 - Agent Architecte

- Conception de l'architecture
- Choix technologiques
- Modélisation des données

### 15h15-15h30 : **PAUSE**

### 15h15-16h00 : Étape 3 - Agents Développeurs

- Développement Frontend
- Développement Backend
- Configuration DevOps

### 16h00-16h30 : Étape 4 - Agent QA et Code Review

- Plan de tests
- Tests automatisés
- Rapport qualité

### 16h30-17h00 : Phase d'analyse critique

- Réflexion sur le processus
- Discussion collective
- Synthèse des apprentissages

---

*Cet exercice permet une mise en pratique complète des concepts Vibe Coding tout en produisant un livrable concret et une analyse critique constructive du processus.*
