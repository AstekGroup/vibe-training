# Notes de Formateur - Formation Vibe Coding Starter (1 jour)

## Vue d'ensemble pour le formateur

Cette formation d'une journée introduit les développeurs au concept du Vibe Coding. Le public cible a déjà des compétences en programmation mais découvre l'IA générative pour le développement.

**Objectifs pédagogiques principaux :**
- Comprendre les fondements du vibe coding vs programmation traditionnelle
- Maîtriser le prompt engineering pour le développement
- Acquérir un workflow de développement assisté par IA
- Identifier les risques et bonnes pratiques

---

## 9h00 - 9h30 : Introduction et présentation

### Préparation formateur
- **Matériel :** Présentation Digistorm prête, accès CodeLab/AWS vérifié
- **Vérifications techniques :** Cursor installé sur toutes les machines
- **Ambiance :** Créer un climat de curiosité et d'apprentissage

### Guide d'animation du tour de table
**Questions clés à poser :**
- "As-tu déjà vibe codé ?" → Permet d'identifier le niveau réel vs déclaré
- "Comment vois-tu le vibe coding ?" → Révèle les préjugés/craintes à adresser
- "Quelles sont tes attentes ?" → Ajuster le contenu si nécessaire

**Points d'attention :**
- Notez les profils résistants (souvent les seniors) pour les accompagner spécifiquement
- Repérez les early adopters pour les utiliser comme relais
- Identifiez les projets métier évoqués pour les utiliser en exemples

### Conseils présentation plan
- Soyez transparent sur l'approche "learning by doing"
- Précisez que les erreurs sont normales et formatives
- Mettez l'accent sur l'aspect collaboratif

---

## 9h30 - 10h15 : Fondements et Démonstration Live (45min)

### 9h30-9h45 : Démonstration "Frimer" (15min)

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
   - Préparez 2-3 exemples concrets de projets réalisés
   - Mettez l'accent sur la diversité des projets possibles
   - Montrez le code généré et soulignez la qualité

3. **Débrief interactif** (5min)
   - "Qu'est-ce qui vous surprend ?"
   - "Quelles questions cela soulève ?"

**Points d'attention formateur :**
- Si la démo échoue, transformez l'échec en apprentissage ("Voilà pourquoi nous avons besoin de maîtriser les prompts")
- Gardez un ton enthousiaste mais réaliste
- Préparez des captures d'écran de backup au cas où

### 9h45-10h00 : Framework des 5 Compétences Clés (15min)

**Méthode pédagogique :** Utilisez des exemples concrets pour chaque compétence

**1. Thinking - Décomposer avant de prompter**
```
Exemple pratique à donner :
❌ "Fais-moi une app de todo"
✅ "Je veux une app de todo web qui :
   - Permet d'ajouter/supprimer des tâches
   - Persiste les données localement
   - A une interface responsive"
```

**Points d'insistance :**
- "L'IA n'est pas magique, elle a besoin de clarté"
- "Plus vous êtes précis, moins vous aurez d'aller-retours"

**2. Frameworks - Utiliser des structures éprouvées**
- Montrez le template de prompt (slide suivante)
- Expliquez que c'est comme les design patterns en programmation

**3. Checkpoints - Valider à chaque étape**
```
Workflow type :
git commit → test → prompt suivant → test → commit
```

**4. Debugging - Dialoguer avec l'IA**
- Montrez un exemple de copier-coller d'erreur dans le prompt
- Insistez : "L'IA est votre binôme de debugging"

**5. Context - Le bon niveau de détail**
- Trop vague → résultats imprévisibles
- Trop prescriptif → perte de l'optimisation IA

**Note pour formateur :** Ces 5 compétences sont le cœur de la formation. Y revenir régulièrement.

### 10h00-10h15 : Comment fonctionne l'IA pour le code (15min)

**Objectif :** Démystifier l'IA sans rentrer dans les détails techniques complexes

**Structure suggérée :**

**Introduction historique** (3min)
- Karpathy 2025 comme référence
- Différence fondamentale avec l'autocomplétion classique

**Les LLM expliqués simplement** (7min)
- "Imaginez un développeur qui a lu tout GitHub et Stack Overflow"
- Analogie avec l'expérience humaine : patterns reconnus vs créativité
- Les 3 phases d'entraînement expliquées simplement

**Processus de génération** (3min)
- Token par token : "Comme vous qui réfléchissez mot après mot"
- L'importance de la probabilité et de la température
- Pourquoi ça peut "halluciner"

**Messages clés à faire passer :**
- L'IA propose, le développeur décide
- Elle mémorise des patterns, elle ne comprend pas vraiment
- D'où l'importance de la validation humaine

**Transitions vers la pratique** (2min)
- "Maintenant qu'on sait comment ça marche, apprenons à bien l'utiliser"

---

## 10h15 - 11h00 : Prompt Engineering Pratique (45min)

### Structure détaillée de cette section cruciale

**10h15-10h30 : Les niveaux de prompt (15min)**

**Concept à expliquer clairement :**
L'IA a plusieurs "couches" d'instructions :
1. **Instructions système** (invisibles, définies par l'outil)
2. **Rules globales** (votre configuration utilisateur)
3. **Rules locales** (spécifiques au projet/.cursor/rules)
4. **Le prompt** (votre demande spécifique)

**Démonstration pratique :**
- Ouvrir Cursor et montrer les User Rules
- Créer un dossier `.cursor/rules` avec des règles simples
- Montrer la différence de réponse avec/sans rules

**Points d'attention formateur :**
- Insistez sur la hiérarchie : système > global > local > prompt
- Expliquez que les rules économisent du temps sur le long terme

**10h30-10h45 : Template de Prompt Efficace (15min)**

**Présentation du template :**
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

**Méthode pédagogique :**
- Montrez d'abord un prompt "mauvais"
- Appliquez le template étape par étape
- Montrez le résultat amélioré

**10h45-11h00 : Exercice Collectif d'amélioration (15min)**

**Animation suggérée :**

**Prompt de base :** "Fais une calculatrice web"

**Étapes de l'exercice :**
1. **Collecte des problèmes** (3min) : "Que manque-t-il ?"
2. **Amélioration collaborative** (7min) : Construire le prompt ensemble au tableau
3. **Version finale** (3min) : Montrer le résultat attendu
4. **Débrief** (2min) : "Combien de temps ça vous aurait pris avant/après ?"

**Résultat attendu (à préparer) :**
```
## Contexte
Calculatrice web professionnelle pour comptables

## Rôle  
Tu es un développeur front-end expert en JavaScript vanilla

## Tâche
Développe une calculatrice avec :
- Opérations de base (+, -, *, /)
- Historique des 10 derniers calculs
- Gestion des décimales (2 chiffres après virgule)
- Raccourcis clavier
- Design responsive

## Contraintes
- HTML5/CSS3/JS vanilla (pas de framework)
- Compatible IE11+
- Accessible (ARIA labels)
- Stockage local pour l'historique

## Format
Code modulaire, commenté, avec tests unitaires simples
```

**Note formateur :** Cet exercice est crucial. Prenez le temps, même si ça déborde légèrement.

---

## 11h00 - 12h00 : Exercice Guidé Collectif (60min)

### **Analyseur de Performance Web**

**Objectifs pédagogiques :**
- Montrer le workflow itératif en conditions réelles
- Démontrer les 5 compétences en action
- Gérer les erreurs et ajustements en live

**Structure détaillée :**

**11h00-11h15 : Préparation et plan (15min)**
```
Prompt initial suggéré :
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
- Si erreur : "Parfait ! Voilà une occasion de voir le debugging en action"
- Montrez les checkpoints : "Commit après chaque fonctionnalité qui marche"

**Points de vigilance :**
- Préparez des solutions de backup si l'IA ne coopère pas
- Impliquez l'audience : "Que proposez-vous pour améliorer ce prompt ?"
- N'hésitez pas à montrer vos hésitations et ratés

**11h45-12h00 : Débrief et optimisation (15min)**

**Questions à poser :**
- "Qu'avez-vous observé dans ma manière de procéder ?"
- "Quelles erreurs ai-je faites ?"
- "Comment améliorer le processus ?"

**Points à faire ressortir :**
- L'importance des iterations courtes
- Le dialogue constant avec l'IA
- La validation à chaque étape

---

## 12h00 - 12h30 : Début Exercices Individuels (30min)

### Animation de cette transition cruciale

**12h00-12h10 : Présentation des exercices individuels (10min)**

**Les 4 exercices proposés :**
1. **Snake HTML/JS** - Apprentissage ludique JavaScript
2. **Pi Monte-Carlo Python** - Compréhension algorithmes
3. **Gestionnaire tâches simple** - Application pratique
4. **Mini-défi debugging** - Correction de code buggy

**Conseils de choix :**
- "Choisissez selon votre appétence, pas votre niveau"
- "L'objectif est d'apprendre le processus, pas de finir"
- "N'hésitez pas à changer si vous vous ennuyez"

**12h10-12h20 : Exemple détaillé Snake (10min)**

**Montrez la différence prompt basique vs optimisé :**

❌ **Version basique :** "Crée un jeu de snake en JavaScript"

✅ **Version optimisée :** (Montrer le prompt complet de la formation)

**12h20-12h30 : Démarrage supervisé (10min)**
- Circulez pour aider aux premiers prompts
- Vérifiez que chacun utilise le template
- Rassurez sur la normalité des premiers échecs

**Note formateur :** Cette demi-heure donne le ton de l'après-midi. Soyez très présent.

---

## Pause déjeuner - Notes pour le formateur

### Préparation de l'après-midi
- Préparez 3-4 projets de debugging (code volontairement buggy)
- Vérifiez les avancées individuelles pour adapter l'accompagnement
- Identifiez qui a besoin d'aide technique vs méthodologique

### Repos pédagogique
- L'après-midi sera intense en accompagnement individuel
- Rechargez-vous, car vous allez passer de table en table

---

## 13h30 - 14h00 : Retour d'expérience (30min)

### Guide d'animation du tour de table

**Structure suggérée :**
- 3 minutes par personne maximum
- Questions rotatives pour éviter la répétition

**Questions clés par tour :**
1. **Premier tour :** "Qu'as-tu appris ce matin qui t'a le plus marqué ?"
2. **Deuxième tour :** "Quelles difficultés as-tu rencontrées ?"
3. **Troisième tour :** "Une chose que tu vas changer dans ta façon de coder ?"

**Techniques d'animation :**
- Reformulez et valorisez chaque réponse
- Rebondissez sur les points communs
- Transformez les difficultés en apprentissages collectifs

**Points à faire ressortir :**
- Les erreurs sont normales et formatrices
- La patience dans le dialogue avec l'IA
- L'importance de la précision dans les prompts

---

## 14h00 - 16h00 : Exercices Individuels + Accompagnement (120min)

### 14h00-14h15 : Choix de projet (15min)

**Méthode de choix de projet :**
- Tour de table rapide : 1 minute par personne
- Chacun annonce son projet et pourquoi
- Validation rapide de la faisabilité

**Projets suggérés si manque d'inspiration :**
- Application de gestion de budget personnel
- Outil de génération de mots de passe sécurisés  
- Mini-CRM pour freelances
- Dashboard de suivi d'habitudes
- Convertisseur de devises avec API

**Application du template :**
- Faites rédiger le prompt initial en binômes
- Validation croisée avant de commencer

### 14h15-16h00 : Développement assisté (105min)

**Rôle du formateur pendant cette phase :**

**Tour de table toutes les 20 minutes :**
- Vérifiez les avancées
- Identifiez les blocages techniques vs méthodologiques
- Proposez des ajustements de prompts

**Intervention types :**
- **Si blocage technique :** "Montre-moi ton prompt, on va l'améliorer ensemble"
- **Si résultat insatisfaisant :** "L'IA t'a donné quoi ? Comment reformuler ?"
- **Si découragé :** "C'est normal, tu es en train d'apprendre. Montre-moi où tu en es"

**Conseils spécifiques par type de difficultés :**

**Prompt trop vague :**
- Retour au template
- "Ajoute 2 exemples concrets"

**Code qui ne fonctionne pas :**
- "Copie l'erreur exacte dans un nouveau prompt"
- "Demande à l'IA d'expliquer l'erreur d'abord"

**Résultats incohérents :**
- "Vérifie les contraintes dans ton prompt"
- "L'IA a-t-elle bien compris le contexte ?"

**Perfectionnisme :**
- "L'objectif est d'apprendre, pas de finir"
- "Tu peux itérer après la formation"

**Conseils d'animation :**
- Gardez un chrono visible pour tous
- Annoncez les étapes restantes régulièrement
- Créez une ambiance de laboratoire d'expérimentation

---

## 16h15 - 17h15 : Finalisation et Bonnes Pratiques (60min)

### Structure de cette section cruciale

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

**16h35-16h55 : Tests automatisés et optimisation (20min)**

**Méthode :**
1. **Tests automatisés** (10min)
   - Montrez comment demander à l'IA de générer des tests
   - Exemple de prompt : "Génère des tests unitaires complets pour ce code"

2. **Optimisation performances** (10min)
   - Prompt type : "Analyse ce code et propose 3 optimisations de performance"
   - Montrez l'application des recommandations

**16h55-17h15 : Documentation et analyse critique (20min)**

**Documentation automatisée :**
```
Prompt suggéré : "Génère une documentation complète pour ce projet avec :
- README.md avec installation et usage
- Commentaires dans le code
- Documentation API si applicable"
```

**Analyse critique du processus :**
```
Prompt suggéré : "Analyse le processus de développement que j'ai suivi pour ce projet.
Propose 3 améliorations pour un projet futur similaire.
Identifie les étapes où j'ai perdu du temps."
```

**Points à faire ressortir :**
- La documentation peut être automatisée mais doit être relue
- L'IA peut analyser votre propre processus de développement
- L'amélioration continue est clé dans le vibe coding

---

## 17h15 - 17h30 : Risques à connaître (15min) - Section optionnelle

### Guidance pour traiter cette section sensible

**Approche recommandée :**
- Ton informatif, pas alarmiste
- Mettre l'accent sur les solutions, pas sur la peur
- Lier aux bonnes pratiques déjà enseignées

**17h15-17h20 : Green IT et éco-responsabilité (5min)**

**Messages clés :**
- "Chaque prompt a un coût énergétique"
- "Optimisez vos prompts = moins de consommation"
- "Code efficient = empreinte réduite"

**Conseils pratiques :**
- Prompts précis pour réduire les iterations
- Demander explicitement du code efficient
- Choisir le bon modèle selon la complexité

**17h20-17h25 : Sécurité du code généré (5min)**

**Points critiques sans faire peur :**
- "L'IA peut générer des vulnérabilités involontaires"
- "Toujours relire avant d'exécuter"
- "Utilisez des outils d'analyse statique"

**Bonnes pratiques :**
- Ne jamais mettre de secrets dans les prompts
- Réviser systématiquement le code de sécurité
- Appliquer le principe de moindre privilège

**17h25-17h30 : Aspects éthiques et juridiques (5min)**

**Approche équilibrée :**
- "L'IA a des biais, soyez vigilants"
- "Documentation de votre processus = protection"
- "Consultez un juriste pour les gros projets"

**Note formateur :** Cette section peut créer de l'anxiété. Restez positif et pratique.

---

## 17h30 - 18h00 : Bilan et perspectives (30min)

### Animation du bilan final

**17h30-17h45 : Présentation des projets (15min)**

**Format efficace :**
- 2 minutes par personne maximum
- Structure imposée :
  1. "Mon projet en 30 secondes"
  2. "Ma plus grande difficulté"
  3. "Ma plus belle réussite"
  4. "Ce que j'aurais fait différemment"

**Rôle du formateur :**
- Valoriser chaque réalisation
- Souligner les apprentissages
- Rebondir sur les difficultés communes

**17h45-17h55 : Consolidation des apprentissages (10min)**

**Questions pour solidifier :**
- "Quelles sont les 3 règles d'or du vibe coding que vous retiendrez ?"
- "Qu'allez-vous changer dès demain dans votre développement ?"
- "Quel sera votre premier projet vibe coding au boulot ?"

**Synthèse formateur :**
Rappeler les 5 compétences et leur progression aujourd'hui

**17h55-18h00 : Évaluation et ressources (5min)**
- Lien évaluation : https://digistorm.app/p/5314548
- Ressources pour continuer
- Encouragement à la pratique

---

## Points d'attention généraux pour le formateur

### Gestion du groupe
- **Hétérogénéité des niveaux :** Utilisez les plus avancés comme ressources pour les autres
- **Résistance au changement :** Montrez les gains concrets, pas la théorie
- **Perfectionnistes :** Rappelez régulièrement que l'objectif est d'apprendre, pas de finir

### Gestion du temps
- **Buffers intégrés :** 5 minutes de marge sur chaque section
- **Priorités :** Si retard, sacrifier la section risques plutôt que la pratique
- **Rythme :** Alternez théorie (max 15min) et pratique

### Gestion technique
- **Backup plans :** Solutions préparées si l'IA ne coopère pas
- **Exemples préparés :** Code et prompts testés au préalable
- **Support individuel :** Gardez du temps pour les difficultés spécifiques

### Messages clés à répéter
1. "L'IA propose, vous décidez"
2. "L'erreur est formatrice en vibe coding"
3. "La précision du prompt détermine la qualité du résultat"
4. "Validation et tests sont non négociables"
5. "Le vibe coding change le métier, ne le supprime pas"

---

## Ressources pour le formateur

### Liens utiles à avoir sous la main
- Documentation Cursor : https://docs.cursor.com
- Templates de règles : (préparer 3-4 exemples types)
- Projets d'exemple : (avoir 5-6 projets aboutis en backup)

### Phrases de transition entre sections
- "Maintenant qu'on a vu la théorie, passons à la pratique"
- "Vous avez expérimenté X, voyons maintenant comment l'industrialiser"
- "Ces difficultés sont normales, voici comment les surmonter"

### Gestion des questions difficiles
- **"L'IA va remplacer les développeurs ?"** → "Elle transforme le métier vers plus de créativité et moins de routine"
- **"C'est de la triche ?"** → "C'est un outil, comme l'IDE ou Stack Overflow"
- **"Comment être sûr que le code est correct ?"** → "Même validation que le code humain : tests, review, outils"

---

Cette formation doit être énergique, pratique et rassurante. L'objectif est de créer des ambassadeurs du vibe coding qui repartiront avec l'envie d'expérimenter dans leur environnement professionnel.