# 9h30 - 10h30 : Agents IA : Théorie et Pratique Avancées

## 📚 **Sources et références récentes**

### Frameworks d'agents IA (2024-2025)

- [The Definitive Guide to AI Agent Frameworks in 2025](https://priyanshis.medium.com/the-definitive-guide-to-ai-agent-frameworks-in-2025-choosing-the-right-tool-for-your-ai-f69e8fa644d5) - Guide complet des frameworks
- [Top 9 AI Agent Frameworks as of September 2025](https://www.shakudo.io/blog/top-9-ai-agent-frameworks) - Comparatif actualisé
- [The Best AI Agents in 2025: Tools, Frameworks, and Platforms Compared | DataCamp](https://www.datacamp.com/blog/best-ai-agents) - Analyse DataCamp

### Systèmes multi-agents

- [I Tried 12 AI Agent Frameworks in 2025 — Here&#39;s the Brutally Honest Guide](https://generativeai.pub/i-tried-12-ai-agent-frameworks-in-2025-heres-the-brutally-honest-guide-you-actually-need-d68dbf6ed2ad) - Retours d'expérience pratiques

*Sources vérifiées : articles de septembre 2025 et plus récents*

## **Contenu formation**

**Types d'agents par fonction :**

- **Agents de raisonnement** : Claude Code, Cursor Composer
- **Agents de code** : GitHub Copilot, Continue
- **Agents multi-modaux** : GPT4-V, Claude avec vision
- **Agents spécialisés** : Devin (codage), WindSurf Cascade

**Anatomie technique d'un agent :**

- **Boucle de planification** : Décomposition de tâches complexes
- **Utilisation d'outils** : APIs, système de fichiers, git, web
- **Gestion de mémoire** : Fenêtre de contexte, RAG, base vectorielle
- **Auto-correction** : Gestion d'erreurs et logique de reprise

**Démonstration live** : Agent custom avec tools (15min)

## 🛠️ **Exemples pratiques avec Gemini CLI**

### Création d'agents spécialisés avec Gemini CLI

**Agent d'analyse de code :**

```bash
cd my-project/
gemini
> Tu es un agent d'analyse de code expert. Analyse ce projet et identifie :
> 1. Les vulnérabilités potentielles
> 2. Les points d'amélioration de performance
> 3. Les problèmes de maintenabilité
> Fournis un rapport structuré avec des recommandations précises.
```

**Agent de création de fonctionnalités :**

```bash
gemini --include-directories ../lib,../docs
> Je veux créer un système d'authentification JWT pour cette API.
> Génère le code complet avec :
> - Middleware d'authentification
> - Routes login/register
> - Tests unitaires
> - Documentation API
```

**Agent de refactorisation :**

```bash
gemini -p "Refactorise ce composant React pour utiliser les crochets modernes et améliorer les performances"
```

**Ajout d'un serveur MCP**

éditer le fichier `.gemini/setting.json`

```json
{
  "mcpServers": {
    "context7": {
      "httpUrl": "https://mcp.context7.com/mcp"
    }
  }
}
```

### Documentation officielle et ressources

- **Documentation principale :** [Gemini CLI - Google for Developers](https://developers.google.com/gemini-code-assist/docs/gemini-cli)
- **Repository GitHub :** [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- **Guide Cloud :** [Gemini CLI - Google Cloud](https://cloud.google.com/gemini/docs/codeassist/gemini-cli)

## 📝 **Notes formateur**

**9h30-9h45 : Types d'agents (15min)**

**Taxonomie pratique pour l'entreprise :**

**Agents de raisonnement :**

- **Usage :** Planification complexe, décisions d'architecture
- **Cas :** "Conçois l'architecture microservices pour ce système"

**Agents de code :**

- **Usage :** Génération de code, refactorisation
- **Cas :** "Implémente cette API selon les spécifications OpenAPI"

**Agents multi-modaux :**

- **Usage :** Analyse de diagrammes, maquettes d'interface
- **Cas :** "Génère le code à partir de cette maquette Figma"

**9h45-10h15 : Anatomie technique (30min)**

**Les 4 composants essentiels :**

**1. Boucle de planification (7min)**

```
Cycle d'agent typique :
1. Recevoir tâche → 2. Décomposer → 3. Exécuter étape
4. Évaluer → 5. Ajuster plan → 6. Continuer/Terminer
```

**2. Utilisation d'outils (8min)**

- **Système de fichiers :** Lecture, écriture, recherche
- **Contrôle de version :** Opérations Git
- **Web :** Appels d'API, consultation de documentation
- **Exécution :** Lancement de code, tests, compilation

**3. Gestion de mémoire (8min)**

- **Fenêtre de contexte :** Conversation immédiate
- **Mémoire de session :** État du projet en cours
- **Mémoire à long terme :** Connaissances accumulées (RAG)
- **Mémoire partagée :** Informations partagées entre agents

**4. Auto-correction (7min)**

- **Détection d'erreurs :** Analyse des erreurs de compilation
- **Stratégies de reprise :** Tentatives avec ajustements
- **Mécanismes de repli :** Solutions alternatives
- **Boucles d'apprentissage :** Amélioration des prompts selon les résultats

**10h15-10h30 : Démonstration live (15min)**

**Agent "Documentation Updater" :**

1. **Configuration** (3min) : Configuration de base Cursor
2. **Intégration d'outils** (5min) : Système de fichiers + Git
3. **Implémentation de logique** (4min) : Règles et prompts
4. **Test en direct** (3min) : Utilisation sur projet réel
