# 10h45 - 12h00 : Atelier "Mon Premier Agent" (75min)

### Contenu formation

**Objectif pédagogique :** Comprendre concrètement ce qu'est un agent

**Exercice guidé (45min) :**
1. **Setup simple** (15min) : Cursor + rules basiques
2. **Agent "Code Reviewer"** (30min) :
   - Prompt système : "Tu es un reviewer senior"
   - Tool : Accès au diff git  
   - Test sur 3 PRs types (bug fix, feature, refactor)

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
