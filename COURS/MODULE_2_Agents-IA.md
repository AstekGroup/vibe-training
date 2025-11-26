# MODULE 2 : Agents IA et Développement Agentique

**Durée** : 1 journée (7h)  
**Objectifs** : Maîtriser la conception et l'implémentation d'agents IA, comprendre le Model Context Protocol (MCP) et sécuriser les interactions

---

## 🎯 Objectifs pédagogiques

- Comprendre les différents types d'agents IA et leur anatomie technique
- Développer son premier agent IA fonctionnel
- Maîtriser le Model Context Protocol (MCP) pour l'intégration API/DB
- Sécuriser les interactions avec les agents IA
- Appliquer la BMAD-METHOD pour structurer le développement

---

## 📅 Planning de la journée

| Horaire | Module | Durée | Contenu |
|:--------|:-------|:------|:--------|
| **9h00 - 9h30** | **Retour Challenge + Intro** | 30min | Partage agents imaginés, patterns récurrents |
| **9h30 - 10h30** | **Agents IA Théorie Avancée** | 60min | Types d'agents, anatomie technique, démo live |
| **10h30 - 10h45** | **☕ PAUSE** | 15min | |
| **10h45 - 12h00** | **Mon Premier Agent** | 75min | Setup + Agent "Code Reviewer" + débrief collectif |
| **12h00 - 12h30** | **Introduction MCP** | 30min | Model Context Protocol, démos API/DB |
| **12h30 - 13h30** | **🍽️ PAUSE DÉJEUNER** | 60min | |
| **13h30 - 15h00** | **TP Configuration Serveurs MCP** | 90min | Context 7 et intégration GitLab, configuration MCP pratique |
| **15h00 - 15h15** | **☕ PAUSE** | 15min | |
| **15h15 - 16h45** | **Sécurité Agents IA** | 90min | Menaces 2025, défenses pratiques, atelier sécurité |
| **16h45 - 17h30** | **Frameworks + Bilan J2** | 45min | BMAD-METHOD détaillée, impact métier développeur |

---

## 📚 Contenu détaillé

### 1. Retour Challenge Overnight (30min)
- Partage des 3 agents imaginés par chaque participant
- Identification des patterns récurrents
- Classification selon les types d'agents

### 2. Agents IA : Théorie Avancée (60min)

#### Types d'agents
- **Agents Réactifs** : Réaction directe aux stimuli (chatbots simples)
- **Agents Délibératifs** : Planification et raisonnement (agents de décision)
- **Agents Apprenants** : Apprentissage continu (systèmes adaptatifs)
- **Agents Collaboratifs** : Orchestration multi-agents

#### Anatomie technique d'un agent
```
Agent IA = LLM + Outils + Mémoire + Logique de contrôle
```

- **LLM** : Moteur de raisonnement (GPT, Claude, Gemini)
- **Outils** : APIs, fonctions, bases de données
- **Mémoire** : Contexte court terme + long terme
- **Contrôle** : Boucle décisionnelle, orchestration

#### Démonstration live
Création d'un agent simple avec LangChain ou CrewAI

### 3. Mon Premier Agent : Code Reviewer (75min)

#### Objectif
Développer un agent capable de reviewer du code selon les standards entreprise

#### Étapes
1. **Setup** (15min)
   - Installation dépendances (LangChain/CrewAI)
   - Configuration API keys
   
2. **Développement** (45min)
   - Définition du rôle et des règles
   - Intégration d'outils (linters, analyseurs)
   - Gestion de la mémoire
   - Boucle de review

3. **Test et débrief** (15min)
   - Tests sur du code réel
   - Partage collectif des résultats

### 4. Introduction au Model Context Protocol (MCP) (30min)

#### Qu'est-ce que MCP ?
Protocole standardisé pour connecter les agents IA aux sources de données et APIs

#### Concepts clés
- **Serveurs MCP** : Exposent données et fonctions
- **Clients MCP** : Agents consommant les serveurs
- **Contexte** : Partage d'état entre agents

#### Démonstrations
- MCP pour APIs REST
- MCP pour bases de données
- MCP pour systèmes de fichiers

### 5. TP : Configuration Serveurs MCP (90min)

#### Partie 1 : Context 7 (45min)
- Installation et configuration
- Connexion à GitLab
- Récupération automatique du contexte projet

#### Partie 2 : MCP Pratique (45min)
- Création d'un serveur MCP custom
- Intégration avec agent Code Reviewer
- Tests d'intégration

### 6. Sécurité des Agents IA (90min)

#### Menaces 2025
- **Prompt Injection** : Manipulation via prompts malveillants
- **Data Leakage** : Fuite de données sensibles
- **Agent Hijacking** : Prise de contrôle de l'agent
- **Hallucination Attacks** : Exploitation des hallucinations

#### Défenses pratiques
- **Input Validation** : Sanitization des entrées
- **Output Filtering** : Validation des sorties
- **Sandboxing** : Isolation des agents
- **Monitoring** : Surveillance continue

#### Atelier sécurité (30min)
- Attaques simulées
- Mise en place de guardrails
- Tests de robustesse

### 7. BMAD-METHOD (45min)

#### Présentation détaillée
**B**rainstorm → **M**odel → **A**rchitect → **D**evelop

- **Brainstorm** : Génération d'idées avec agents IA
- **Model** : Modélisation assistée (UML, diagrammes)
- **Architect** : Architecture technique avec validation IA
- **Develop** : Développement orchestré par agents

#### Impact métier développeur
- Gain de productivité (30-50%)
- Amélioration qualité
- Réduction de la dette technique
- Nouvelles compétences requises

---

## 🛠️ Outils utilisés

- **Frameworks agents** : LangChain, CrewAI, AutoGen
- **MCP** : Context 7, serveurs MCP custom
- **Sécurité** : OWASP LLM Top 10, guardrails-ai
- **Monitoring** : LangSmith, traces d'audit

---

## 📦 Livrables

- ✅ Agent Code Reviewer fonctionnel
- ✅ Serveur MCP configuré et intégré
- ✅ Checklist sécurité agents IA
- ✅ Compréhension BMAD-METHOD

---

## 📖 Ressources

- Documentation LangChain/CrewAI
- Spécification MCP
- OWASP LLM Top 10
- Templates BMAD-METHOD

---

**Prochaine étape** : Jour 3 - Context Engineering et Projet Final
