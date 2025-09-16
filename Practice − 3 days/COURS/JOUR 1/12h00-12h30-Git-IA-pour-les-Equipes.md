# 12h00 - 12h30 : Git + IA pour les Équipes

## 📚 **Sources et références récentes**

### Git Collaboration + AI (2024-2025)
- [The AI-powered DevOps revolution: Redefining developer collaboration - GitHub Blog](https://github.blog/ai-and-ml/github-copilot/the-ai-powered-devops-revolution-redefining-developer-collaboration/) - Vision GitHub officielle
- [State of Git Collaboration Report 2024 | JetBrains](https://blog.jetbrains.com/team/2024/03/05/are-dev-teams-surviving-or-thriving-in-2024-insights-from-jetbrains-and-gitkraken-s-state-of-git-collaboration-report/) - Étude sur 150k+ développeurs
- [AI Copilot Code Quality: 2025 Data Suggests 4x Growth in Code Clones](https://www.gitclear.com/ai_assistant_code_quality_2025_research) - Impact qualité code

*Sources vérifiées : rapport 2024 et données 2025 sur l'impact de l'IA en équipe*

## **Contenu formation**

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

## 📝 **Notes formateur**

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
