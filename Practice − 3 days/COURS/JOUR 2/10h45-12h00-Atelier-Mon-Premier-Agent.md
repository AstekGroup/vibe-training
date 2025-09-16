# 10h45 - 12h00 : Atelier "Mon Premier Agent" (75min)

### Contenu formation

**Objectif pédagogique :** Comprendre concrètement ce qu'est un agent

## 🔧 **Avec Gemini CLI**

### Setup Gemini CLI pour Code Review (10min)

**Installation et initialisation :**

```bash
# Installation rapide
npm install -g @google/gemini-cli

# Authentification
gemini
# Suivre le processus d'authentification dans le navigateur
```

### Agent "Code Reviewer" avec Gemini CLI (25min)

**Configuration de l'agent :**

```bash
cd votre-projet/
gemini
```

**Prompt système optimisé :**

```
Tu es un agent Code Reviewer expert avec 10 ans d'expérience.

MISSION : Analyser les modifications git et fournir un review détaillé

PROCESSUS :
1. Examine tous les fichiers modifiés avec git diff
2. Applique les critères de qualité suivants :
   - Sécurité : Recherche vulnérabilités OWASP Top 10
   - Performance : Identifie bottlenecks potentiels
   - Maintenabilité : Structure, nommage, complexité
   - Tests : Couverture et pertinence

OUTPUT FORMAT :
## 🔍 Code Review Report
### ✅ Points positifs
### ⚠️  Problèmes identifiés
### 🚀 Recommandations d'amélioration
### 📊 Score global : X/10
### 🎯 Actions prioritaires
```

**Exemples d'utilisation pratiques :**

**Test sur bug fix :**

```bash
gemini
> Analyse cette correction de bug et vérifie qu'elle couvre tous les edge cases.
> Regarde particulièrement la gestion des erreurs et les tests associés.
```

**Test sur nouvelle feature :**

```bash
gemini --include-directories ../tests,../docs
> Review cette nouvelle feature d'authentification.
> Vérifie la sécurité, les tests, et l'impact sur l'architecture existante.
```

**Test sur refactoring :**

```bash
gemini
> Analyse ce refactoring. Assure-toi qu'il n'y a pas de régression
> et que le code reste cohérent avec le reste du projet.
```

### Documentation et ressources

- **Guide complet :** [Gemini CLI Documentation](https://developers.google.com/gemini-code-assist/docs/gemini-cli)
- **Exemples d'agents :** [GitHub Repository](https://github.com/google-gemini/gemini-cli)
- **Intégration VS Code :** [Gemini Code Assist](https://cloud.google.com/gemini/docs/codeassist/gemini-cli)

**Débrief collectif** (30min) :

- Qu'est-ce qui a bien marché ?
- Quelles limites avez-vous observées ?
- Comment améliorer cet agent ?

### 📝 Notes formateur

**10h45-11h00 : Setup simple (15min)**

**Configuration Cursor pour agents :**

```
# .cursor/rules
Tu es un agent spécialisé en code review.

MISSION :
- Analyser chaque fichier modifié
- Identifier problèmes de qualité
- Proposer améliorations concrètes

PROCESSUS :
1. Lire modifications git diff
2. Appliquer critères qualité
3. Générer rapport structuré

CRITÈRES :
- Sécurité : vulnérabilités communes
- Performance : optimisations évidentes  
- Lisibilité : nommage, structure
- Tests : couverture et pertinence

OUTPUT FORMAT :
## Code Review Report
### Problèmes détectés
### Améliorations suggérées  
### Score qualité : X/10
```

**11h00-11h30 : Agent "Code Reviewer" (30min)**

**Phase 1 : Configuration (10min)**

- Adaptation rules selon projets participants
- Test de base sur fichier simple

**Phase 2 : Test sur 3 PRs (15min)**

- **PR Bug fix :** Vérifier edge cases
- **PR Feature :** Vérifier architecture
- **PR Refactor :** Vérifier non-régression

**Points d'attention :** Circuler activement, préparer PRs d'exemple

**11h30-12h00 : Débrief collectif (30min)**

**Patterns attendus dans les réponses :**

- ✅ Succès : Configuration simple, résultats immédiats
- ❌ Difficultés : Calibrage critères, verbosité excessive

**Limites typiques :**

- Contexte métier manquant
- Pas de compréhension historique
- Difficultés conventions spécifiques
