# Formation Vibe Coding Starter (1 jour) - Guide Complet

v2 Philippe Pary - Thomas Foutrein  
2025-08-26

**Guide intégré : Contenu formation + Notes formateur**

---

## Vue d'ensemble

### Objectifs de la formation
* Coder avec Cursor
* Améliorer du code existant avec Cursor
* Intégrer Cursor dans un environnement de développement existant
* Personnaliser Cursor à vos besoins métier
* Formuler des prompts efficaces pour l'IA dans un contexte de développement
* Développer un projet complet en utilisant les techniques de "Vibe Coding"

### Pré-requis
* Connaissance d'au moins un langage de programmation ou scripting
* Connaissance des processus de développement informatique
* Connaissance du contrôle de version (git)
* Connaissance des IDE (VSCode, IntelliJ)
* Matériel de travail adapté à la programmation
* VScode installé
* Cursor installé
* Licence Copilot / Cursor (fournies pour la durée de la formation)

### Public cible
Cette formation d'une journée introduit les développeurs au concept du Vibe Coding. Le public cible a déjà des compétences en programmation mais découvre l'IA générative pour le développement.

### Planning de la journée

| Horaire | Module | Durée | Contenu |
|---------|--------|--------|---------|
| **9h00 - 9h30** | **Introduction** | 30min | Tour de table, présentation du programme |
| **9h30 - 10h15** | **Fondements** | 45min | Démo "frimer", 5 compétences, fonctionnement IA |
| **10h15 - 11h00** | **Prompt Engineering** | 45min | Template de prompt, exercice collectif |
| **11h00 - 12h00** | **Exercice Guidé** | 60min | Analyseur Performance Web (développement collectif) |
| **12h00 - 12h30** | **Exercices Individuels** | 30min | Choix projets, démarrage (Snake, Pi, Todo, Debug) |
| **12h30 - 13h30** | **🍽️ PAUSE DÉJEUNER** | 60min | |
| **13h30 - 14h00** | **Retour d'expérience** | 30min | Tour de table sur apprentissages matinaux |
| **14h00 - 16h00** | **Développement** | 120min | Projets individuels + accompagnement formateur |
| **16h00 - 16h15** | **☕ PAUSE** | 15min | |
| **16h15 - 17h15** | **Finalisation** | 60min | Review code IA, tests, optimisation, documentation |
| **17h15 - 17h30** | **Risques** *(optionnel)* | 15min | Green IT, sécurité, éthique, aspects juridiques |
| **17h30 - 18h00** | **Bilan** | 30min | Présentation projets, évaluation, perspectives |

**🎯 Objectif central :** Maîtriser le workflow complet du vibe coding en une journée intensive et pratique.

---

## 9h00 - 9h30 : Introduction et présentation

### Contenu formation

**Tour de table :**
* Nom, fonction
* As-tu déjà vibe codé ?
* Comment vois-tu le vibe coding ?
* Ta machine est prête ? (client vibe coding installé) / accès au CodeLab
* Quelles sont tes attentes vis à vis de la journée ?

➡️ Présentation du plan de la journée
➡️ Questionnaire début de formation : https://forms.office.com/e/yRmPCTs2Ln

### 📝 Notes formateur

**Préparation :**
- **Matériel :** Présentation Digistorm prête, accès CodeLab/AWS vérifié
- **Vérifications techniques :** Cursor installé sur toutes les machines
- **Ambiance :** Créer un climat de curiosité et d'apprentissage

**Guide d'animation du tour de table :**
- "As-tu déjà vibe codé ?" → Permet d'identifier le niveau réel vs déclaré
- "Comment vois-tu le vibe coding ?" → Révèle les préjugés/craintes à adresser
- "Quelles sont tes attentes ?" → Ajuster le contenu si nécessaire

**Points d'attention :**
- Notez les profils résistants (souvent les seniors) pour les accompagner spécifiquement
- Repérez les early adopters pour les utiliser comme relais
- Identifiez les projets métier évoqués pour les utiliser en exemples

---

## 9h30 - 10h15 : Fondements et Démonstration Live (45min)

### Contenu formation

#### 9h30-9h45 : Démonstration "Frimer" (15min)

Démonstration en direct d'une création rapide d'application en utilisant le vibe coding. Nous allons générer un environnement containerisé pour notre codelab directement avec l'IA. Nous examinerons également des exemples concrets de projets développés lors des sessions précédentes pour illustrer l'efficacité de cette approche.

- vibe-coder le codelab de la journée (générer un container)
- présenter les sites des sessions précédentes

#### 9h45-10h00 : Framework des 5 Compétences Clés (15min)

1. **Thinking** : Décomposer le problème avant de prompter
   - "Que veux-je exactement ?"
   - "Quelles sont les contraintes ?"

2. **Frameworks** : Utiliser des structures éprouvées
   - Templates de prompt
   - Patterns architecturaux connus

3. **Checkpoints** : Valider à chaque étape
   - Tests à chaque fonctionnalité
   - Commits réguliers

4. **Debugging** : Dialoguer avec l'IA pour corriger
   - Copier-coller les erreurs dans le prompt
   - Demander des explications étape par étape

5. **Context** : Fournir le bon niveau de détail
   - Ni trop vague, ni trop prescriptif
   - Exemples concrets et contre-exemples

> Inspiré des meilleures pratiques industrielles 2025

#### 10h00-10h15 : Comment fonctionne l'IA pour le code et le vibe coding (15min)

Concept popularisé début 2025 par Andrej Karpathy (co-fondateur d'OpenAI)

Technique de programmation assisté par des LLMs et basé sur du prompt. Il se différencie d'un outil de complétion basé sur les LLMs comme Copilot par l'importance cruciale du prompt dans le processus de développement.

Le vibe-coding peut être utilisé comme un outil low/no-code. Ceci dit, la pratique des derniers mois démontre que comme tous les outils low/no-code, un non-informaticien va produire des logiciels de mauvaise qualité de cette façon (failles de sécurités, bugs…). Cette pratique est à réserver pour les POC ou le prototypage.

Entre les mains d'un développeur compétent, les outils de vibe-coding entraînent une hausse de la productivité et de l'efficacité. Mais également une transformation du métier.

##### Les LLM : comprendre les fondements

Les Large Language Models (LLM) sont des modèles d'intelligence artificielle entraînés sur d'immenses corpus de textes et de code pour prédire la suite la plus probable d'une séquence donnée.

**L'apprentissage d'un LLM :**
1. **Pré-entraînement**: le modèle est exposé à d'énormes quantités de texte et code
2. **Fine-tuning**: le modèle est affiné sur des tâches spécifiques
3. **RLHF**: les réponses sont évaluées par des humains

**Le processus de génération de code :**
1. **Tokenisation**: votre prompt est découpé en tokens
2. **Contextualisation**: le modèle analyse le prompt dans son contexte
3. **Prédiction auto-régressive**: le modèle génère un token après l'autre
4. **Échantillonnage**: introduction d'une randomisation contrôlée

**Les limites :**
- **"hallucination"** de fonctionnalités inexistantes
- Incapacité à exécuter le code généré
- Connaissance limitée aux données d'entraînement
- Difficultés avec des problèmes très spécifiques

### 📝 Notes formateur

**9h30-9h45 : Démonstration "Frimer" (15min)**

**Objectif pédagogique :** Créer l'envie et lever les appréhensions initiales

**Script de démo suggéré :**
1. **"Je vais créer notre environnement de TP en live"** (5min)
   ```
   Prompt suggéré : "Crée un environnement Docker containerisé pour un CodeLab de formation Vibe Coding avec :
   - Un serveur web simple
   - Un éditeur de code accessible via navigateur
   - Des exemples de projets pré-configurés
   - Script de déploiement automatique"
   ```

2. **Montrer les sites des sessions précédentes** (5min)
3. **Débrief interactif** (5min) : "Qu'est-ce qui vous surprend ?"

**Points d'attention :** Si la démo échoue, transformez l'échec en apprentissage

**9h45-10h00 : Framework des 5 Compétences (15min)**

**Exemples concrets pour chaque compétence :**

**1. Thinking :**
```
❌ "Fais-moi une app de todo"
✅ "Je veux une app de todo web qui :
   - Permet d'ajouter/supprimer des tâches
   - Persiste les données localement
   - A une interface responsive"
```

**Points d'insistance :**
- "L'IA n'est pas magique, elle a besoin de clarté"
- "Plus vous êtes précis, moins vous aurez d'aller-retours"

**Note formateur :** Ces 5 compétences sont le cœur de la formation. Y revenir régulièrement.

**10h00-10h15 : Comment fonctionne l'IA (15min)**

**Objectif :** Démystifier l'IA sans rentrer dans les détails techniques complexes

**Messages clés à faire passer :**
- L'IA propose, le développeur décide
- Elle mémorise des patterns, elle ne comprend pas vraiment
- D'où l'importance de la validation humaine

---

## 10h15 - 11h00 : Prompt Engineering Pratique (45min)

### Contenu formation

#### Principes fondamentaux pour communiquer avec l'IA

Chaque modèle d'IA possède des instructions par défaut qui définissent son comportement général. Les outils comme Cursor permettent de personnaliser ces instructions à différents niveaux :

- **Rules générales**: Users rules dans la configuration
- **Rules locales**: dans un dossier `.cursor/rules`
- **Utiliser `context7`** pour de meilleurs résultats
- **Le prompt** en tant que tel

#### Template de Prompt Efficace

```
## Contexte
[Décris le projet et l'objectif]

## Rôle  
Tu es un [expertise] expert en [technologie]...

## Tâche
[Action précise à réaliser]

## Contraintes
- Technologies : [liste précise]
- Standards : [conventions de code] 
- Tests : [requis/optionnel]

## Format attendu
- Code commenté
- Gestion d'erreurs
- [Autres spécifications]

## Exemples
Input: [exemple d'entrée]
Output: [exemple de sortie attendue]
```

#### Exercice Collectif : Amélioration de Prompts (15 minutes)

**Prompt à améliorer :**
❌ "Fais une calculatrice web"

**Version améliorée attendue :**

✅ **Contexte :** Calculatrice web professionnelle pour comptables
**Rôle :** Tu es un développeur front-end expert en JavaScript vanilla
**Tâche :** Développe une calculatrice avec :
- Opérations de base (+, -, *, /)
- Historique des 10 derniers calculs
- Gestion des décimales (2 chiffres après virgule)
- Raccourcis clavier
- Design responsive

**Contraintes :**
- HTML5/CSS3/JS vanilla (pas de framework)
- Compatible IE11+
- Accessible (ARIA labels)
- Stockage local pour l'historique

**Format :** Code modulaire, commenté, avec tests unitaires simples

### 📝 Notes formateur

**10h15-10h30 : Les niveaux de prompt (15min)**

**Concept à expliquer clairement :**
L'IA a plusieurs "couches" d'instructions :
1. **Instructions système** (invisibles)
2. **Rules globales** (votre configuration)
3. **Rules locales** (.cursor/rules)
4. **Le prompt** (votre demande)

**Démonstration pratique :**
- Ouvrir Cursor et montrer les User Rules
- Créer un `.cursor/rules` avec des règles simples
- Montrer la différence avec/sans rules

**10h30-10h45 : Template de Prompt Efficace (15min)**

**Méthode pédagogique :**
- Montrez d'abord un prompt "mauvais"
- Appliquez le template étape par étape
- Montrez le résultat amélioré

**10h45-11h00 : Exercice Collectif (15min)**

**Animation suggérée :**
1. **Collecte des problèmes** (3min) : "Que manque-t-il ?"
2. **Amélioration collaborative** (7min) : Construire au tableau
3. **Version finale** (3min) : Montrer le résultat
4. **Débrief** (2min) : "Temps avant/après ?"

**Note formateur :** Cet exercice est crucial. Prenez le temps, même si ça déborde.

---

## 11h00 - 12h00 : Exercice Guidé Collectif (60min)

### Contenu formation

**Analyseur de Performance Web** (développement ensemble)
- Interface HTML avec champ URL
- Analyse temps de chargement avec JavaScript
- Affichage des métriques et recommandations
- Démonstration du workflow itératif en temps réel

### 📝 Notes formateur

**Objectifs pédagogiques :**
- Montrer le workflow itératif en conditions réelles
- Démontrer les 5 compétences en action
- Gérer les erreurs et ajustements en live

**11h00-11h15 : Préparation et plan (15min)**

**Prompt initial suggéré :**
```
"Je veux créer un analyseur de performance web simple avec :
- Interface HTML avec un champ pour saisir une URL
- JavaScript qui mesure le temps de chargement
- Affichage des métriques (temps de réponse, taille, recommandations)
- Design simple mais professionnel

Technologies : HTML5, CSS3, JavaScript vanilla
Format : fichiers séparés, code commenté"
```

**Animation :**
- Écrivez le prompt en direct avec l'aide de l'audience
- Appliquez le template vu précédemment
- Montrez votre réflexion ("Thinking" en action)

**11h15-11h45 : Développement en live (30min)**

**Techniques d'animation :**
- Commentez vos actions : "Je vais d'abord tester le HTML de base"
- Si erreur : "Parfait ! Voilà une occasion de voir le debugging"
- Montrez les checkpoints : "Commit après chaque fonctionnalité"

**11h45-12h00 : Débrief et optimisation (15min)**

**Questions à poser :**
- "Qu'avez-vous observé dans ma manière de procéder ?"
- "Quelles erreurs ai-je faites ?"
- "Comment améliorer le processus ?"

---

## 12h00 - 12h30 : Début Exercices Individuels (30min)

### Contenu formation

#### Phase 1 : Exercice Guidé (fait ensemble)
**Analyseur Web** - développement collectif en live

#### Phase 2 : Exercices Individuels (suite après pause)
1. **Snake HTML/JS** - aspect ludique pour l'apprentissage JavaScript
2. **Pi Monte-Carlo Python** - bon pour comprendre les algorithmes  
3. **Gestionnaire tâches simple** - application pratique quotidienne
4. **Mini-défi debugging** - corriger du code buggy généré volontairement

##### Exemple de prompt optimisé pour le Snake :

❌ **Version basique :** "Crée un jeu de snake en JavaScript"

✅ **Version optimisée :**
**Contexte :** Jeu éducatif pour apprendre JavaScript
**Rôle :** Tu es un expert en développement de jeux web vanilla JS
**Tâche :** Développe un Snake avec :
- Canvas HTML5 pour le rendu
- Contrôles flèches + WASD
- Score et meilleur score (localStorage)
- Game over avec restart
- Vitesse progressive

**Contraintes :**
- HTML5/CSS3/JS pur (pas de bibliothèques)
- Code modulaire et commenté
- 60 FPS fluides
- Responsive sur mobile

**Bonus :** Effets sonores et animations CSS simples

### 📝 Notes formateur

**12h00-12h10 : Présentation des exercices (10min)**

**Conseils de choix :**
- "Choisissez selon votre appétence, pas votre niveau"
- "L'objectif est d'apprendre le processus, pas de finir"
- "N'hésitez pas à changer si vous vous ennuyez"

**12h20-12h30 : Démarrage supervisé (10min)**
- Circulez pour aider aux premiers prompts
- Vérifiez que chacun utilise le template
- Rassurez sur la normalité des premiers échecs

**Note formateur :** Cette demi-heure donne le ton de l'après-midi. Soyez très présent.

---

## 13H30-14H00 : Retour d'expérience (30min)

### Contenu formation

Tour de table:
* Qu'as-tu appris ce matin ? 
* Quelles difficultés as-tu rencontrées ?
* Qu'est-ce qui t'a le plus marqué ?

### 📝 Notes formateur

**Structure suggérée :**
- 3 minutes par personne maximum
- Questions rotatives pour éviter la répétition

**Questions clés par tour :**
1. **Premier tour :** "Qu'as-tu appris qui t'a le plus marqué ?"
2. **Deuxième tour :** "Quelles difficultés as-tu rencontrées ?"
3. **Troisième tour :** "Une chose que tu vas changer ?"

**Points à faire ressortir :**
- Les erreurs sont normales et formatrices
- La patience dans le dialogue avec l'IA
- L'importance de la précision dans les prompts

---

## 14h00 - 16h00 : Exercices Individuels + Accompagnement (120min)

### Contenu formation

#### 14h00 - 14h15 : Choix de projet (15min)
- Tour de table: choisir un projet personnel
- Application du template de prompt à votre projet

#### 14h15 - 16h00 : Développement assisté par IA (105min)

- Consulter l'IA en mode Ask pour rédiger un plan de développement
- Développer le projet
- Affiner son guidage l'IA
- Débugguer avec l'IA (cmd+L ou ctrl+L pour envoyer les logs au prompt)
- Générer la documentation

### 📝 Notes formateur

**14h00-14h15 : Choix de projet (15min)**

**Projets suggérés si manque d'inspiration :**
- Application de gestion de budget personnel
- Outil de génération de mots de passe sécurisés  
- Mini-CRM pour freelances
- Dashboard de suivi d'habitudes
- Convertisseur de devises avec API

**14h15-16h00 : Développement assisté (105min)**

**Rôle du formateur :**
- **Tour de table toutes les 20 minutes**
- **Intervention types :**
  - Si blocage technique : "Montre-moi ton prompt"
  - Si résultat insatisfaisant : "Comment reformuler ?"
  - Si découragé : "C'est normal, tu apprends"

**Conseils par type de difficultés :**
- **Prompt trop vague :** Retour au template + exemples concrets
- **Code qui ne fonctionne pas :** Copier l'erreur dans un nouveau prompt
- **Résultats incohérents :** Vérifier les contraintes du prompt
- **Perfectionnisme :** "L'objectif est d'apprendre, pas de finir"

---

## 16h15 - 17h15 : Finalisation et Bonnes Pratiques (60min)

### Contenu formation

- **Revue de code assistée par IA**: Prompt `Tu es un développeur expert, tu es mon binôme et tu relis mon code. Liste toutes les améliorations fonctionnelles, dans l'usage de librairies, dans le code. Pointe les bonnes pratiques à adopter. Souligne les problèmes de sécurité.`

- **Optimisation des performances**: consulter l'IA (mode Ask) et appliquer les recommandations

- **Tests automatisés générés par l'IA**: faire rédiger les tests, passer en revue, compléter

- **Finalisation du projet**: faire rédiger ou relire la documentation

- **Analyse critique du processus**: demandez à l'IA d'analyser le processus de développement et de proposer des améliorations

- **Documentation des apprentissages**: créez un document résumant les techniques qui ont fonctionné

### 📝 Notes formateur

**16h15-16h35 : Revue de code assistée par IA (20min)**

**Prompt type à faire utiliser :**
```
"Tu es un développeur expert, tu es mon binôme et tu relis mon code. 
Liste ici toutes les améliorations fonctionnelles, dans l'usage de librairies, 
dans le code que tu pourras trouver. Pointe les bonnes pratiques à adopter. 
Souligne les problèmes de sécurité que tu as repérés."
```

**Animation :**
- Demandez à 2-3 volontaires de partager leurs résultats
- Montrez la différence de qualité avant/après review IA
- Insistez : "L'IA est votre relecteur permanent gratuit"

**16h35-16h55 : Tests et optimisation (20min)**

**Tests automatisés (10min) :**
- Prompt : "Génère des tests unitaires complets pour ce code"

**Optimisation performances (10min) :**
- Prompt : "Analyse ce code et propose 3 optimisations de performance"

**16h55-17h15 : Documentation et analyse (20min)**

**Documentation automatisée :**
```
"Génère une documentation complète pour ce projet avec :
- README.md avec installation et usage
- Commentaires dans le code
- Documentation API si applicable"
```

**Analyse critique :**
```
"Analyse le processus de développement que j'ai suivi.
Propose 3 améliorations pour un projet futur similaire.
Identifie les étapes où j'ai perdu du temps."
```

---

## 17h15 - 17h30 : Risques à connaître (15min) - Section optionnelle

### Contenu formation

#### Développement durable et Green IT

Le vibe coding a des implications sur l'empreinte carbone. Pour un vibe coding respectueux :
- Optimisez vos prompts pour réduire les interactions
- Privilégiez les modèles plus légers quand possible
- Demandez du code efficient en ressources
- Validez la performance énergétique

#### Sécurité : les défis du code généré par IA

Les LLM peuvent générer du code vulnérable. Pour vous protéger :
- Vérifiez systématiquement le code avant exécution
- Utilisez des outils d'analyse statique
- Ne partagez jamais de secrets dans vos prompts
- Restez vigilant face aux comportements inhabituels
- Appliquez le principe de moindre privilège

#### Considérations éthiques

L'IA reflète les biais de ses données d'entraînement. Pour un vibe coding éthique :
- Examinez le code pour identifier les biais
- Diversifiez vos exemples dans les prompts
- Spécifiez l'inclusivité et l'accessibilité
- Testez avec des perspectives diverses
- Documentez l'usage de l'IA dans votre code

#### Aspects juridiques

- Documentez votre processus de vibe coding
- Vérifiez les licences des modèles utilisés
- Soyez attentif aux licences dans le code généré
- Consultez un expert juridique pour les gros projets

### 📝 Notes formateur

**Approche recommandée :**
- Ton informatif, pas alarmiste
- Focus sur les solutions, pas la peur
- Lier aux bonnes pratiques enseignées

**17h15-17h20 : Green IT (5min)**
- "Chaque prompt a un coût énergétique"
- "Prompts précis = moins de consommation"

**17h20-17h25 : Sécurité (5min)**
- "L'IA peut générer des vulnérabilités"
- "Toujours relire avant d'exécuter"
- Bonnes pratiques sans faire peur

**17h25-17h30 : Éthique et juridique (5min)**
- "L'IA a des biais, soyez vigilants"
- "Documentation = protection"

**Note :** Cette section peut créer de l'anxiété. Restez positif et pratique.

---

## 17h30 - 18h00 : Bilan et perspectives (30min)

### Contenu formation

* **Présentation des projets réalisés** (tour de table)
  * Quelles difficultés as-tu rencontrées ?
  * Quelles bonnes pratiques as-tu retenues ?
  * As-tu des ressources à partager ? 
  * As-tu des questions ? 

* **Évaluation de la formation** (10 minutes): https://forms.office.com/e/5FU2ftKCs9?origin=lprLink 

* **Rappel**: le vibe est une méthode récente en constante évolution : maintenez une veille technologique sur le sujet

### 📝 Notes formateur

**17h30-17h45 : Présentation des projets (15min)**

**Format efficace :**
- 2 minutes par personne maximum
- Structure imposée :
  1. "Mon projet en 30 secondes"
  2. "Ma plus grande difficulté"
  3. "Ma plus belle réussite"
  4. "Ce que j'aurais fait différemment"

**17h45-17h55 : Consolidation des apprentissages (10min)**

**Questions pour solidifier :**
- "Quelles sont les 3 règles d'or du vibe coding ?"
- "Qu'allez-vous changer dès demain ?"
- "Quel sera votre premier projet vibe coding au boulot ?"

**17h55-18h00 : Évaluation et ressources (5min)**
- Ressources pour continuer
- Encouragement à la pratique

---

## Ressources et outils

### Les IDE disponibles

| Outil           | Type             | Avantages                                        | Inconvénients                                |
|:----------------|:-----------------|:-------------------------------------------------|:---------------------------------------------|
| **Claude Code** | Outil CLI        | ✅ Puissance du modèle Claude                    | ⚠️ Pas d'intégration IDE                     |
| **Cursor**      | Éditeur dédié    | ✅ Interface optimisée pour le vibe coding       | ⚠️ Application séparée à installer           |
| **gemini-cli**  | Outil CLI        | ✅ Scriptable, gratuit                          | ⚠️ Pas d'interface graphique                 |
| **Copilot**     | Extension multi-IDE | ✅ Largement adopté, mature                   | ⚠️ Moins orienté vibe coding                 |
| **WindSurf**    | Éditeur dédié    | ✅ Interface moderne                             | ⚠️ Relativement récent                       |
| **Continue**    | Extension VSCode | ✅ Open source                                   | ⚠️ Moins stable                              |
| **Replit**      | Éditeur en ligne | ✅ Environnement complet                         | ⚠️ Nécessite connexion internet              |

### Workflow Git recommandé

```bash
# Workflow type pour une fonctionnalité
git checkout -b feature/user-auth
git commit -m "init: setup project structure"

# Après chaque prompt réussi
git add . && git commit -m "feat: implement login form"
git add . && git commit -m "feat: add validation logic"
```

### Modèles à favoriser 

- **Claude 4 Sonnet** (excellent, rapport qualité/prix)
- **Gemini-2.5-pro** (bons résultats)
- **ChatGPT-5** (dernière version, lent, trop aléatoire)

---

## Points clés à retenir

### Les 5 Compétences du Vibe Coding
1. **Thinking** : Décomposer avant de prompter
2. **Frameworks** : Utiliser des structures éprouvées
3. **Checkpoints** : Valider à chaque étape
4. **Debugging** : Dialoguer avec l'IA pour corriger
5. **Context** : Fournir le bon niveau de détail

### Template de Prompt Universel
- **Contexte** : Décrivez le projet
- **Rôle** : Définissez l'expertise attendue
- **Tâche** : Action précise à réaliser
- **Contraintes** : Technologies et standards
- **Format** : Structure de sortie attendue
- **Exemples** : Cas concrets d'usage

### Bonnes Pratiques Essentielles
- **Commits fréquents** : Sauvegarde après chaque étape
- **Validation humaine** : L'IA propose, vous décidez
- **Itération courte** : Amélioration progressive
- **Documentation** : Code commenté et expliqué
- **Tests** : Validation systématique du code généré

Cette formation doit être énergique, pratique et rassurante. L'objectif est de créer des ambassadeurs du vibe coding qui repartiront avec l'envie d'expérimenter dans leur environnement professionnel.