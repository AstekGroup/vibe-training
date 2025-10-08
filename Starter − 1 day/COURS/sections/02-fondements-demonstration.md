# 2. Fondements et Démonstration Live (9h30 - 10h15)

## 🎯 Objectifs de cette tranche
- Démontrer la puissance du vibe coding par l'exemple
- Présenter le framework des 5 compétences essentielles
- Expliquer le fonctionnement de l'IA générative pour le développement
- Créer l'effet "wow" qui motive pour la suite

## 📝 Contenu

### Démonstration "frimer" en direct (20 minutes)

**Scénario :** Développer une application complète en temps réel devant les participants

#### Exemple de projet démonstration : "Générateur de CV dynamique"

**Prompt de démarrage :**
```
Contexte : Je veux créer un générateur de CV moderne et responsive
Rôle : Tu es un développeur full-stack expert en HTML/CSS/JavaScript
Tâche : Crée une application web complète qui génère un CV professionnel
Contraintes :
- HTML5, CSS3, JavaScript vanilla (pas de framework)
- Design moderne et responsive
- Export PDF possible
- Formulaire intuitif pour saisie des données
Format : Code complet avec fichiers séparés
Exemples : Interface similaire à Canva mais pour les CV
```

**Déroulé de la démo (chronométré) :**
1. **2 min** : Explication du prompt initial
2. **5 min** : Génération et explication du code HTML/CSS
3. **5 min** : Ajout de l'interactivité JavaScript
4. **3 min** : Tests et amélioration en temps réel
5. **5 min** : Questions/réactions des participants

### Framework des 5 compétences essentielles (15 minutes)

#### 1. **THINKING** - La décomposition stratégique
- **Principe** : Réfléchir avant de prompter
- **Exemple** : "Je veux une app de gestion de tâches" → Décomposer en : authentification, CRUD, interface, persistance
- **Piège à éviter** : Prompts trop génériques

#### 2. **FRAMEWORKS** - Les structures éprouvées
- **Principe** : Utiliser des patterns reconnus
- **Exemples** :
  - MVC pour architecture
  - REST pour API
  - Atomic Design pour UI
- **Avantage** : L'IA connaît ces patterns parfaitement

#### 3. **CHECKPOINTS** - La validation continue
- **Principe** : Tester à chaque étape
- **Workflow** : Génération → Test → Validation → Prochaine étape
- **Outils** : Git commits, tests unitaires, revue de code

#### 4. **DEBUGGING** - Le dialogue collaboratif
- **Principe** : L'IA comme partenaire de debugging
- **Approche** : Expliquer le problème, partager l'erreur, demander des solutions alternatives
- **Exemple** : "Mon API retourne une erreur 500, voici le code et le log d'erreur..."

#### 5. **CONTEXT** - L'art du bon niveau de détail
- **Principe** : Ni trop, ni trop peu d'informations
- **Template** : Contexte + Rôle + Tâche + Contraintes + Format + Exemples
- **Évolution** : Adapter le contexte selon l'avancement du projet

### Comprendre le fonctionnement de l'IA (10 minutes)

#### Comment l'IA génère du code

**Métaphore du développeur expert :**
- L'IA a "lu" des millions de lignes de code
- Elle prédit le code le plus probable selon le contexte
- Comme un développeur senior qui a vu tous les patterns possibles

#### Modèles de langage et code

**Points clés :**
- **Training** : Formée sur GitHub, Stack Overflow, documentation officielle
- **Patterns** : Reconnaît les structures et conventions
- **Limitations** : Pas de vraie "compréhension", peut halluciner
- **Force** : Génère du code idiomatique et structuré

#### Pourquoi ça fonctionne si bien ?

1. **Répétition de patterns** : Le code suit des structures prévisibles
2. **Documentation riche** : Beaucoup d'exemples dans les données d'entraînement
3. **Conventions** : Standards de l'industrie largement adoptés
4. **Feedback loop** : L'humain guide et corrige

### Introduction aux serveurs MCP (5 minutes)

#### Qu'est-ce que MCP (Model Context Protocol) ?

**Définition :**
- **MCP** = Protocole standardisé pour connecter l'IA à des outils externes
- **Principe** : L'IA peut utiliser des APIs, bases de données, services cloud via des "serveurs"
- **Avantage** : Élargir les capacités de l'IA au-delà du simple texte

#### Focus sur Context7 - Documentation intelligente

**Context7 en action :**
- **Fonction** : Accès en temps réel à la documentation des frameworks
- **Exemple concret** : "Comment utiliser React Hooks ?" → Documentation officielle à jour
- **Avantage** : Plus besoin de chercher sur Google, l'IA a accès direct aux docs

**Démonstration rapide (2 minutes) :**
```
Prompt : "Montre-moi comment utiliser useState en React avec des exemples"
→ L'IA accède à la doc React via Context7
→ Génère du code avec les bonnes pratiques officielles
```

#### Autres serveurs MCP utiles

**GitHub et Gitlab MCP :**
- Accès direct aux repositories
- Création de PR, issues, gestion de projets
- Intégration native avec le workflow de développement

**Docker MCP :**
- Gestion des conteneurs Docker directement depuis l'IA
- Création et configuration d'environnements de développement
- Déploiement et orchestration de services

#### Pourquoi c'est révolutionnaire ?

1. **Données à jour** : Plus de code obsolète
2. **Intégration native** : L'IA devient un vrai assistant de développement
3. **Workflow unifié** : Tout dans un seul environnement
4. **Productivité** : Moins de context switching

## 🎓 Notes formateur

### Préparation de la démo
- **Test préalable** : Répéter la démo 2-3 fois avant la formation
- **Plan B** : Avoir un code de backup en cas de problème réseau
- **Timing** : Chronomètre chaque étape pour respecter les 20 minutes

### Points d'attention
- **Transparence** : Montrer les échecs et erreurs, c'est normal !
- **Interaction** : Demander des suggestions aux participants
- **Réalisme** : Expliquer que tous les projets ne sont pas si fluides

### Messages clés à faire passer
1. "L'IA ne remplace pas votre expertise, elle l'amplifie"
2. "Le vibe coding demande de nouvelles compétences"
3. "La qualité du prompt détermine la qualité du résultat"

### Transition vers le module suivant
"Maintenant que vous avez vu ce qui est possible, apprenons ensemble à formuler des prompts efficaces. C'est là que tout commence !"

## ✅ Critères de réussite
- [ ] La démonstration fonctionne et impressionne
- [ ] Les 5 compétences sont comprises
- [ ] Les participants posent des questions
- [ ] L'enthousiasme est palpable dans le groupe

## 🔧 Ressources pour la démo

### Outils requis
- Cursor ouvert avec un dossier vide
- Navigateur web pour tester
- Terminal pour les commandes git

### Prompts de secours (si la démo échoue)
```
Prompt simple : Crée un calculateur de pourboire en HTML/CSS/JS
Prompt intermédiaire : Génère un quiz interactif sur un thème au choix
Prompt avancé : Application de gestion de budget personnel
```