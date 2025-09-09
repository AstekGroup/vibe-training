# 13h30 - 15h30 : "Projet Guidé : Smart Code Assistant" (120min)

### Contenu formation

**Projet unique pour tous mais personnalisable**

**Objectif :** Agent qui améliore la productivité quotidienne

**Architecture imposée :**
- Agent principal + 3 agents spécialisés
- Context engineering avec rules
- Au moins 1 tool externe (API, DB, file system)

**Timeline structurée :**
- **13h30-14h00** : Définition de l'architecture (30min)
- **14h00-15h00** : Implémentation core (60min)
- **15h00-15h30** : Tests et démo préparation (30min)

**Exemples d'agents :**
- **Code Quality** : Linting + suggestions d'amélioration
- **Documentation** : Auto-génération doc à partir du code
- **Testing** : Génération de tests + détection de edge cases

### 📝 Notes formateur

**13h30-14h00 : Définition architecture (30min)**

**Architecture imposée mais flexible :**
```
Smart Code Assistant
├── Agent Principal (Orchestrateur)
│   ├── Analyse des demandes utilisateur
│   ├── Routing vers agents spécialisés
│   └── Coordination des réponses
├── Agent Spécialisé 1 (au choix)
├── Agent Spécialisé 2 (au choix)  
├── Agent Spécialisé 3 (au choix)
├── Context Engineering Layer
│   ├── Rules management
│   ├── Memory persistence
│   └── RAG integration
└── Tools Layer
    ├── Git integration
    ├── File system access
    └── External API (au choix)
```

**13h30-13h45 : Choix des agents spécialisés (15min)**

**Options suggérées :**
- **Code Quality :** Linting, security scan, suggestions
- **Documentation :** Auto-génération, maintenance, API docs
- **Testing :** Test generation, coverage, mocks
- **Performance :** Profiling, optimization suggestions
- **Security :** Vulnerability detection, compliance
- **Deployment :** CI/CD, env management, rollback
- **Monitoring :** Metrics, alerts, health checks

**Requirements obligatoires :**
```yaml
context_requirements:
  rules:
    - general_rules.md (qualité, sécurité)
    - specialized_rules.md (selon agents choisis)
  memory:
    - project_memory.json (decisions, preferences)  
    - user_memory.json (interactions history)
  tools:
    - git_tools (au minimum)
    - file_system_tools
    - 1_external_api (libre choix)
  output_format:
    - structured_responses (JSON/YAML)
    - consistent_styling
```

**14h00-15h00 : Implémentation core (60min)**

**Timeline structurée :**
- **14h00-14h15 :** Setup infrastructure (15min)
- **14h15-14h45 :** Implémentation agents (30min)
- **14h45-15h00 :** Integration et orchestration (15min)

**Points d'attention :**
- Circuler activement, beaucoup de questions techniques
- Aider à la priorisation : "Commencez par l'agent principal"
- Pousser vers solutions simples mais fonctionnelles
