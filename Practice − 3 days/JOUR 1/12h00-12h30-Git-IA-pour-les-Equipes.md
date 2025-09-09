# 12h00 - 12h30 : Git + IA pour les Équipes

### Contenu formation

**Workflows d'équipe avec IA :**
```bash
# L'IA aide pour les reviews
git request-pull main | pbcopy
# Prompt IA : "Analyse cette PR et suggère des améliorations"

# L'IA aide pour les conflits
git status | pbcopy  
# Prompt IA : "Résous ces conflits en gardant la cohérence"
```

**Preview Jour 2 :** "Demain : agents qui font les reviews automatiquement"

### 📝 Notes formateur

**12h00-12h10 : Problématiques équipes (10min)**

**Challenges collectés :**
- Revues de code chronophages
- Conflits de merge complexes
- Messages de commit peu informatifs
- Documentation obsolète

**12h10-12h25 : Solutions IA démontrées (15min)**

**1. Reviews automatisées (5min) :**
```bash
git request-pull main
# Prompt : "Analyse cette PR pour :
# - Problèmes de sécurité
# - Impact performance  
# - Respect conventions
# - Tests manquants"
```

**2. Résolution conflits (5min) :**
```bash
git status
# Prompt : "Résous ces conflits en gardant cohérence"
```

**3. Messages de commit (5min) :**
```bash
git diff --cached
# Prompt : "Génère message commit conventionnel"
```
