# Vibe Coding: Formation Master (3j)

v2 Philippe Pary - Thomas Foutrein
2025-08-26

## Pré-requis
* Connaissance d'au moins un langage de programmation ou scripting
* Matériel de travail adapté à la programmation
* VScode installé
* Un ou plusieurs agents de Vibe Coding installés (Cursor, Gemini CLI, etc.)
* Licence Copilot / Cursor (fournies pour la durée de la formation)
* Un projet personnel à développer

## Objectifs de la formation
- Maîtriser les concepts avancés du Vibe Coding et du développement agentique.
- Comprendre et implémenter des stratégies de Context Engineering robustes.
- Utiliser des frameworks avancés (BMAD, SuperClaude, CCPM) pour structurer le développement IA.
- Développer un projet complet en appliquant les meilleures pratiques du Context Engineering.
- Sécuriser les interactions avec les agents IA.

## Cours

### Première journée : Fondements Accélérés + Préparation Concepts Avancés

**Adaptation du contenu starter pour niveau Master :**
- **Rythme accéléré** : Public expérimenté
- **Exemples d'entreprise** : Projets complexes vs personnels
- **Transition J2-J3** : Introduction concepts avancés en fin de journée

#### 9h00 - 9h30 : Introduction et présentation

**Tour de table spécifique Master :**
- Nom, fonction, niveau d'expérience IA
- Projets d'entreprise envisagés avec les agents
- Attentes sur les concepts avancés (Context Engineering, sécurité)

#### 9h30 - 10h15 : Framework des 5 Compétences + Preview Agents

**Les 5 compétences avec perspective avancée :**
1. **Thinking** → *Vers la planification multi-agents*
2. **Frameworks** → *Vers BMAD, CCPM (aperçu)*  
3. **Checkpoints** → *Vers les feedback loops automatisés*
4. **Debugging** → *Vers l'auto-correction d'agents*
5. **Context** → *Vers le Context Engineering (J3)*

**Teaser :** "Demain nous verrons comment ces 5 compétences deviennent autonomes dans les agents"

#### 10h15 - 11h00 : Prompt Engineering Niveau Entreprise

**Template de prompt Master :**

```
## Contexte Entreprise
[Système/Plateforme, utilisateurs, contraintes business]

## Rôle Expert
Tu es un [architecte/senior] expert en [domaine technique]

## Tâche Complexe
[Objectif technique avec contraintes performance/sécurité]

## Contraintes Entreprise
- Architecture : [microservices, cloud, etc.]
- Conformité : [GDPR, SOX, etc.]
- Performance : [SLA, charge, disponibilité]
- Sécurité : [authentification, audit, encryption]

## Livrable Professionnel
[Code + tests + docs + monitoring]
```

**Exemple concret :**
✅ **Contexte :** Plateforme SaaS de facturation (1M+ utilisateurs)
**Rôle :** Architecte logiciel senior expert en systèmes distribués
**Tâche :** Service de calcul de prix dynamique avec :
- API REST haute performance (>1000 req/s)
- Cache Redis distribué
- Pricing rules configurables
- Monitoring OpenTelemetry

#### 11h00 - 12h00 : Exercice Guidé "Niveau Master"

**Projet : API de Recommandation Intelligente**
- Backend Python/FastAPI avec ML basique
- Frontend React avec visualisations
- Tests automatisés + CI/CD
- Documentation auto-générée

*But :* Montrer la complexité que nous gérerons avec les agents J2-J3

#### 12h00 - 12h30 : Git + IA pour les Équipes

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

#### 13h30 - 16h00 : Exercices Individuels Niveau Master

**Projets au choix :**
1. **Microservice de Gestion d'Événements** (Event Sourcing + CQRS)
2. **API Gateway avec Rate Limiting** (Performance + Sécurité)
3. **Système de Cache Distribué** (Redis + Consistency)
4. **Pipeline ML en Production** (MLOps + Monitoring)

#### 16h15 - 17h00 : Finalisation et Bonnes Pratiques Entreprise

**Code Review assisté par IA niveau entreprise :**
- Sécurité : OWASP Top 10
- Performance : Profiling et optimisation
- Maintenabilité : Clean Architecture
- Conformité : Audit trails

#### 17h00 - 17h15 : Transition vers les Concepts Avancés

**Préparation mentale J2-J3 :**
- **Récap des acquis** : 5 compétences maîtrisées
- **Limitations du prompt manuel** : Pourquoi passer aux agents ?
- **Preview Jour 2** : "Imaginez ces 5 compétences automatisées..."

**Glossaire pour demain :**
- **Agent** : IA autonome avec outils et planification
- **MCP** : Model Context Protocol (connexion IA ↔ outils)
- **Context Engineering** : Art d'optimiser l'information pour l'IA
- **BMAD** : Framework de planification collaborative
- **RAG** : Retrieval Augmented Generation

#### 17h15 - 17h30 : Challenge Overnight

**"Agent Simulator" :**
"Réfléchissez : pour automatiser votre workflow d'aujourd'hui, quels seraient les 3 agents spécialisés nécessaires ?"

**Format attendu :**
- Agent 1 : [Nom] - [Fonction] - [Outils nécessaires]
- Agent 2 : [Nom] - [Fonction] - [Outils nécessaires]  
- Agent 3 : [Nom] - [Fonction] - [Outils nécessaires]

*Nous commencerons J2 en partageant vos idées*

### Deuxième journée : Plongée dans le Vibe Coding Agentique

#### 9h00 - 9h30 : Retour Challenge + Introduction Agents

**Partage du challenge overnight :**
- Tour de table : vos 3 agents imaginés
- Analyse collective : patterns récurrents
- Transition : "Voyons comment créer ces agents"

#### 9h30 - 10h30 : Agents IA : Théorie et Pratique Avancées

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

#### 10h30 - 10h45 : Pause

#### 10h45 - 12h00 : Atelier "Mon Premier Agent" (75min)

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

#### 12h00 - 12h30 : Introduction MCP Simplifiée (30min)

**MCP = Model Context Protocol** (pas Model-Controller-Prompter)

**Démonstration live du formateur :**
- Exemple : Agent qui lit des APIs externes
- Exemple : Agent qui accède à une base de données
- Q&R : "Quels tools aimeriez-vous pour vos agents ?"

#### 12h30 - 13h30 : Pause déjeuner

#### 13h30 - 15h00 : Atelier "Agent Spécialisé" (90min)

**Choix entre 3 agents prêts :**

**Option A : "Documentation Generator"**
- Input : Codebase Python/JS
- Output : README.md structuré
- Tools : file system, git log

**Option B : "Test Writer"**  
- Input : Fonction sans tests
- Output : Suite de tests unitaires
- Tools : framework de tests, coverage

**Option C : "Refactor Assistant"**
- Input : Code legacy
- Output : Version refactorisée + rapport
- Tools : linter, analyzer

**Structure :**
- Choix de l'option (5min)
- Setup et paramétrage (20min)
- Développement (50min)
- Demo croisée (15min)

#### 15h00 - 15h15 : Pause

#### 15h15 - 16h45 : Sécurité Avancée des Agents IA (90min)

**Nouvelles menaces 2025 :**
- **Agent hijacking** : Détournement d'agents autonomes
- **Context poisoning** : Injection de contexte malveillant  
- **Tool abuse** : Utilisation malveillante des outils d'agents
- **Data exfiltration** : Fuite via les logs d'agents

**Défenses pratiques (démonstrations) :**
- **Sandbox des agents** : containers, permissions limitées
- **Audit trails** : Logs détaillés des actions d'agents
- **Input validation** : Sanitisation des prompts users
- **Rate limiting** : Protection contre l'abuse d'APIs

**Atelier sécurité (30min) :**
- Analyse d'un cas de "prompt injection" 
- Création de règles de sécurité pour agents
- Test de résistance aux attaques

#### 16h45 - 17h30 : Frameworks Avancés + Bilan J2

**BMAD-METHOD Détaillée :**

**B**rainstorm → **M**odel → **A**nalyze → **D**evelop

**Template BMAD :**
```yaml
brainstorm:
  - user_stories: []
  - constraints: []
  - success_criteria: []

model:
  - architecture: []
  - data_flow: []
  - technologies: []

analyze:
  - risks: []
  - trade_offs: []
  - validation_strategy: []

develop:
  - milestones: []
  - agent_prompts: []
  - validation_tests: []
```

**Bilan de la journée :**
- Retours d'expérience sur les agents créés
- Discussion sur l'impact sur le métier de développeur
- Préparation J3 : "Demain, Context Engineering pour agents encore plus intelligents"

### Troisième journée : Le "Context Engineering" en Pratique

#### 9h00 - 9h30 : Introduction au Context Engineering

**Qu'est-ce que le Context Engineering ?** 
L'art d'orchestrer l'information pour maximiser l'efficacité des agents IA.

**Les 6 Piliers du Contexte détaillés :**
1. **System Instructions** : Rules, personas, constraints
2. **Memory** : Short-term (conversation) vs Long-term (files)
3. **RAG (Retrieval)** : Documentation, codebase indexing
4. **Tools** : Functions, APIs, external systems
5. **Output format** : Structured responses, templates
6. **Feedback loops** : Learning from interactions

#### 9h30 - 10h45 : "Rules Engineering" (75min)

**Objectif :** Maîtriser les fichiers de contexte persistant

**Exercice progressif :**

**Étape 1 (20min) : Audit de règles existantes**
- Analyser 3 fichiers `.cursor/rules` fournis
- Identifier bonnes vs mauvaises pratiques

**Étape 2 (30min) : Création de règles modulaires**
- Règles générales : style, sécurité, performance
- Règles spécifiques : backend vs frontend vs mobile
- Template de règles par stack technologique

**Étape 3 (25min) : Test en conditions réelles**
- Appliquer les règles sur un mini-projet
- Mesurer l'amélioration de la qualité des réponses

#### 10h45 - 11h00 : Pause

#### 11h00 - 12h30 : "Context Engineering Patterns" (90min)

**6 mini-ateliers de 15min chacun :**

1. **Prompt Chaining** : Séquence de 3 prompts interdépendants
2. **Conditional Loading** : Rules qui s'activent selon le contexte
3. **Memory Patterns** : Garder l'historique des décisions
4. **RAG Simple** : Agent qui interroge de la documentation
5. **Multi-Modal** : Agent qui traite code + images/diagrammes
6. **Error Recovery** : Agent qui corrige ses propres erreurs

**Format :** Rotation par binômes (groupes × 6 stations)

#### 12h30 - 13h30 : Pause déjeuner

#### 13h30 - 15h30 : "Projet Guidé : Smart Code Assistant" (120min)

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

#### 15h30 - 15h45 : Préparation Demos (15min)

**Template de présentation imposé :**
1. Problème résolu (2min)
2. Architecture choisie (1min) 
3. Démo live (2min)
4. Leçons apprises (1min)

#### 15h45 - 16h45 : Présentation des Projets et Feedback (60min)

**Format optimisé :**
- 4 groupes présentent (24min)
- Discussion collective sur les patterns observés (20min)
- Partage des découvertes techniques (16min)

#### 16h45 - 17h00 : Pause

#### 17h00 - 18h00 : Métriques, Maintenance et Perspectives (60min)

**Mesurer l'Efficacité de vos Agents :**

**KPIs techniques :**
- Temps de résolution de tâches
- Taux de succès première tentative
- Qualité du code généré (linting, tests)

**KPIs business :**
- Productivité développeur
- Réduction du time-to-market
- Satisfaction équipe

**Lifecycle Management des Agents :**
- **Versioning** : Comment faire évoluer vos prompts/rules
- **A/B Testing** : Tester différentes approches d'agents
- **Monitoring** : Observer le comportement en production
- **Rollback** : Stratégies de retour en arrière

**Techniques avancées (preview) :**
- **Multi-agent orchestration** : Agents spécialisés qui collaborent
- **Dynamic context loading** : Conditional includes
- **Agent-to-agent communication** : Pour formations futures

**Ressources pour continuer :**
- Communautés et forums spécialisés
- Documentation officielle des outils
- Veille technologique recommandée

**Évaluation de la formation** (10min)

**Questions/réponses finales**
