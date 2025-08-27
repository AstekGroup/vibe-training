# JOUR 2 - 9h30-10h30 : Agents IA : Théorie et Pratique Avancées

## Contenu formation

**Types d'agents par fonction :**
- **Reasoning agents** : Claude Code, Cursor Composer
- **Code agents** : GitHub Copilot, Continue  
- **Multi-modal agents** : GPT-4V, Claude avec vision
- **Specialized agents** : Devin (coding), WindSurf Cascade

**Anatomie technique d'un agent :**
- **Planning loop** : Décomposition de tâches complexes
- **Tool use** : APIs, file system, git, web
- **Memory management** : Context window, RAG, vectorstore
- **Self-correction** : Error handling et retry logic

**Démonstration live** : Agent custom avec tools (15min)

## 📝 Notes formateur

### 9h30-9h45 : Types d'agents par fonction (15min)

**Taxonomie pratique pour l'entreprise :**

**Reasoning agents :**
- **Exemples :** Claude Code, Cursor Composer
- **Usage :** Planification complexe, architecture decisions
- **Cas d'usage :** "Conçois l'architecture microservices pour ce système"

**Code agents :**
- **Exemples :** GitHub Copilot, Continue
- **Usage :** Génération de code, refactoring
- **Cas d'usage :** "Implémente cette API selon les specs OpenAPI"

**Multi-modal agents :**
- **Exemples :** GPT-4V, Claude avec vision
- **Usage :** Analyse de diagrammes, UI mockups
- **Cas d'usage :** "Génère le code à partir de ce mockup Figma"

**Specialized agents :**
- **Exemples :** Devin (full coding), WindSurf Cascade
- **Usage :** Tâches spécifiques bout-en-bout
- **Cas d'usage :** "Développe complètement cette feature avec tests"

**Points d'insistance :**
- Pas de hiérarchie, mais de la spécialisation
- Choisir l'agent selon la tâche, pas par habitude
- Combinaison possible pour des workflows complexes

### 9h45-10h15 : Anatomie technique d'un agent (30min)

**Les 4 composants essentiels :**

**1. Planning loop (7min)**
```
Cycle agent typique :
1. Receive task
2. Break down into steps  
3. Execute step
4. Evaluate result
5. Adjust plan if needed
6. Continue or complete
```

**Démonstration :** Montrez un agent décomposant "créer une API" en sous-tâches

**2. Tool use (8min)**
**Catégories de tools :**
- **File system :** Read, write, search files
- **Version control :** Git operations, branch management
- **Web :** API calls, web scraping, documentation lookup
- **Execution :** Run code, tests, build processes

**Exemple pratique :** Agent qui utilise git + file system + test runner

**3. Memory management (8min)**
**Types de mémoire :**
- **Context window :** Conversation immédiate (limité)
- **Session memory :** État du projet en cours
- **Long-term memory :** Connaissances accumulées (RAG)
- **Shared memory :** Information partagée entre agents

**4. Self-correction (7min)**
**Patterns d'auto-correction :**
- **Error detection :** Parsing des erreurs de compilation/execution
- **Retry strategies :** Tentatives avec ajustements
- **Fallback mechanisms :** Solutions alternatives
- **Learning loops :** Amélioration des prompts selon les résultats

### 10h15-10h30 : Démonstration live (15min)

**Agent custom avec tools - Construction en direct**

**Objectif :** Montrer la faisabilité technique sans magie

**Agent suggéré : "Documentation Updater"**
1. **Setup** (3min) : Configuration de base dans Cursor
2. **Tools integration** (5min) : File system + Git tools
3. **Logic implementation** (4min) : Rules et prompts système
4. **Test live** (3min) : Utilisation sur un vrai projet

**Points d'animation :**
- Transparent sur les limites et échecs
- Montrez le code/configuration, pas seulement le résultat
- Préparez un backup si l'IA ne coopère pas