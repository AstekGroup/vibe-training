# 4. Exercice Guidé Collectif (11h00 - 12h00)

## 🎯 Objectifs de cette tranche
- Développer collectivement un projet complet en temps réel
- Démontrer le workflow itératif du vibe coding
- Appliquer concrètement les techniques de prompt engineering
- Créer un effet d'apprentissage social et de confiance

## 📝 Contenu

### Projet : Analyseur de Performance Web (60 minutes)

#### Choix du projet
**Pourquoi cet exemple :**
- **Utile** : Outil pratique pour tous les développeurs
- **Complet** : Frontend + logique métier + API calls
- **Progressif** : Évolution naturelle par étapes
- **Démonstratif** : Résultats visuels immédiatement perceptibles

#### Prompt de démarrage (préparé et optimisé)

```markdown
**CONTEXTE :**
Je développe un outil d'analyse de performance web pour aider les développeurs
à auditer rapidement leurs sites. L'outil doit être simple d'usage et fournir
des métriques claires avec des recommandations d'amélioration.

**RÔLE :**
Tu es un développeur front-end expert en performance web et APIs,
spécialisé en HTML5, CSS3, JavaScript vanilla et intégrations d'APIs tierces.

**TÂCHE :**
Crée un analyseur de performance web qui teste une URL fournie par l'utilisateur
et affiche les métriques principales (temps de chargement, taille, scores)
avec des recommandations d'optimisation.

**CONTRAINTES :**
- HTML5, CSS3, JavaScript vanilla (pas de framework)
- Design responsive et moderne
- Utilisation d'APIs publiques de performance (PageSpeed, GTmetrix)
- Interface claire et professionnelle
- Gestion des erreurs et états de chargement

**FORMAT :**
- Code structuré en fichiers séparés (HTML/CSS/JS)
- Interface utilisateur intuitive avec formulaire et résultats
- Commentaires explicatifs dans le code
- Gestion d'erreurs robuste

**EXEMPLES :**
Interface similaire à PageSpeed Insights mais plus simple,
avec des métriques comme WebPageTest et recommandations comme Lighthouse.
```

### Déroulé de développement (50 minutes chronométrées)

#### Phase 1 : Structure de base (10 minutes)
**Actions :**
1. **Prompt initial** : Génération de la structure HTML/CSS de base
2. **Test immédiat** : Ouverture dans le navigateur
3. **Première validation** : Interface responsive et formulaire fonctionnel

**Points d'apprentissage :**
- Importance du test immédiat
- Validation de la structure avant la logique
- Gestion des retours de l'IA

#### Phase 2 : Logique de base (15 minutes)
**Prompt d'amélioration :**
```markdown
Ajoute la logique JavaScript pour :
1. Capturer la soumission du formulaire
2. Valider l'URL entrée par l'utilisateur
3. Afficher un loader pendant l'analyse
4. Simuler temporairement l'appel API (setTimeout)
5. Afficher des résultats de test factices

Conserve le design existant et ajoute les interactions.
```

**Points d'apprentissage :**
- Développement incrémental
- Validation progressive
- Séparation des préoccupations

#### Phase 3 : Intégration API réelle (15 minutes)
**Prompt d'intégration :**
```markdown
Remplace la simulation par une vraie intégration avec l'API PageSpeed Insights.
Utilise cette clé API publique et gère :
1. Les appels AJAX vers l'API Google PageSpeed
2. Le parsing des réponses JSON
3. L'affichage des métriques réelles (score, FCP, LCP)
4. La gestion des erreurs d'API

Fournis le code complet avec gestion d'erreurs robuste.
```

**Points d'apprentissage :**
- Intégration d'APIs tierces
- Gestion des erreurs réseau
- Parsing de données JSON complexes

#### Phase 4 : Améliorations et finitions (10 minutes)
**Prompt de finalisation :**
```markdown
Améliore l'outil avec :
1. Affichage des recommandations d'optimisation
2. Graphiques visuels pour les métriques (barres de progression)
3. Export des résultats en PDF ou partage d'URL
4. Historique des analyses dans localStorage

Optimise également le CSS pour un rendu professionnel.
```

**Points d'apprentissage :**
- Cycle d'amélioration continue
- Fonctionnalités utilisateur avancées
- Persistance de données

### Workflow et observations (tout au long)

#### Git et versioning
```bash
# À chaque étape majeure
git add . && git commit -m "feat: add basic HTML structure"
git add . && git commit -m "feat: implement form validation and loader"
git add . && git commit -m "feat: integrate PageSpeed API"
git add . && git commit -m "feat: add advanced features and styling"
```

#### Débriefing en temps réel
**Questions à poser aux participants :**
- "Que remarquez-vous dans la qualité du code généré ?"
- "Comment l'IA a-t-elle interprété nos contraintes ?"
- "Quelles améliorations proposeriez-vous ?"
- "Qu'est-ce qui vous surprend ?"

## 🎓 Notes formateur

### Préparation technique
- **Test complet** : Reproduire l'exercice intégralement avant la formation
- **API Keys** : Préparer les clés d'API nécessaires (PageSpeed Insights)
- **Backup** : Avoir une version fonctionnelle de secours
- **Environnement** : Cursor/VSCode ouvert, terminal Git prêt

### Gestion de l'imprévu
- **Échec d'API** : Prévoir un fallback avec données mockées
- **Erreur de génération** : Avoir des prompts de correction préparés
- **Timing serré** : Identifier les parties optionnelles à couper

### Animation pédagogique
- **Transparence totale** : Montrer tous les échecs et corrections
- **Participation active** : Demander des suggestions d'amélioration
- **Explication continue** : Commenter chaque action en temps réel

### Messages clés à transmettre
1. **"Le développement devient conversationnel"**
2. **"L'erreur fait partie du processus"**
3. **"L'IA propose, l'humain valide et guide"**
4. **"La qualité dépend de la qualité du prompt"**

### Évaluation en continu
**Signaux positifs à repérer :**
- Questions techniques pertinentes
- Suggestions d'amélioration spontanées
- Expressions d'étonnement positif
- Demandes de précisions sur les techniques

**Signaux d'ajustement :**
- Silence prolongé du groupe
- Questions de compréhension de base
- Expressions de doute ou scepticisme

### Transition vers le module suivant
"Maintenant c'est votre tour ! Vous allez choisir un projet personnel et l'implémenter en appliquant exactement les mêmes techniques. Je serai là pour vous accompagner individuellement."

## ✅ Critères de réussite
- [ ] Le projet fonctionne complètement à la fin
- [ ] Tous les participants ont suivi et compris
- [ ] Le workflow itératif est assimilé
- [ ] La confiance dans l'outil est établie
- [ ] Les questions montrent l'engagement du groupe

## 🔧 Ressources techniques

### APIs recommandées
- **PageSpeed Insights** : API Google gratuite
- **WebPageTest** : Alternative avec plus de détails
- **Lighthouse CI** : Pour l'intégration continue

### Prompts de secours
```markdown
# Si l'API ne fonctionne pas
"Crée une version avec données mockées réalistes"

# Si le design pose problème
"Simplifie l'interface en gardant seulement l'essentiel"

# Si JavaScript complexe
"Divise la logique en fonctions plus petites et commentées"
```

### Structure finale attendue
```
performance-analyzer/
├── index.html          # Interface principale
├── styles.css          # Design responsive
├── script.js           # Logique métier
├── README.md           # Documentation
└── .gitignore          # Fichiers Git
```