# 9h00 - 11h00 : Le Contrat de Contexte (120min)

## 📚 **Sources et références récentes**

### Context Engineering (2024-2025)

- [A Survey of Context Engineering for Large Language Models](https://arxiv.org/abs/2507.13334) - Étude scientifique complète (juillet 2025)
- [Context Engineering: Elevating AI Strategy from Prompt Crafting to Enterprise Competence](https://medium.com/@adnanmasood/context-engineering-elevating-ai-strategy-from-prompt-crafting-to-enterprise-competence-b036d3f7f76f) - Vision entreprise
- [The rise of "context engineering" | LangChain Blog](https://blog.langchain.com/the-rise-of-context-engineering/) - Perspective technique
- [Context Engineering - What it is, and techniques to consider | LlamaIndex](https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider) - Guide pratique

*Sources vérifiées : publications de juillet 2025 et plus récentes*

---

## **Objectifs de la session**

À l'issue de cette session, vous serez capables de :
- Comprendre les enjeux du Context Engineering
- Maîtriser les 6 piliers du contexte
- Rédiger et utiliser un Contrat de Contexte
- Identifier les champs essentiels pour chaque type d'agent

---

## **9h00-9h15 : Introduction au Context Engineering (15min)**

### Qu'est-ce que le Context Engineering ?

**Définition :** L'art d'orchestrer l'information pour maximiser l'efficacité des agents IA.

**Analogie pédagogique :**
"Si l'agent est un expert consultant, le Context Engineering c'est lui fournir exactement le dossier dont il a besoin pour exceller."

### Enjeux business

- **Harmonisation** : Règles de travail communes entre toutes les parties prenantes
- **Productivité :** Agents 3-5x plus efficaces avec contexte optimisé
- **Qualité :** Réduction significative des erreurs et itérations
- **ROI :** Moins de temps humain pour superviser
- **Scalabilité :** Agents qui s'adaptent automatiquement
- **Transmissibilité** : Passage de projet d'une équipe à une autre facilité

---

## **9h15-10h00 : Les 6 Piliers du Contexte (45min)**

### 1. System Instructions (10min)
- **Fonction :** Personnalité et comportement de base
- **Exemple :** "Tu es un architecte senior avec 10 ans d'expérience..."
- **Champs clés :**
  - Rôle et expertise
  - Style de communication
  - Contraintes comportementales
  - Format de réponse

### 2. Memory (10min)
- **Short-term :** Conversation en cours
- **Long-term :** Connaissances accumulées
- **Exemple :** "Tu te souviens que ce client préfère React à Vue"
- **Champs clés :**
  - Mémoire de session
  - Mémoire persistante
  - Règles de rétention
  - Structure des données

### 3. RAG (Retrieval) (10min)
- **Mécanisme :** Recherche sémantique + injection contexte
- **Exemple :** Query "authentification" → Récupère docs sécurité
- **Champs clés :**
  - Sources de données
  - Stratégies de recherche
  - Critères de pertinence
  - Gestion des erreurs

### 4. Tools (5min)
- **Puissance :** Agents qui agissent, pas seulement qui parlent
- **Champs clés :**
  - Outils disponibles
  - Paramètres d'entrée
  - Conditions d'usage
  - Gestion des erreurs

### 5. Output Format (5min)
- **Cohérence :** Réponses prévisibles et exploitables
- **Champs clés :**
  - Structure attendue
  - Contraintes de format
  - Niveau de détail
  - Langue et style

### 6. Feedback Loops (5min)
- **Adaptation :** Personnalisation progressive aux besoins
- **Champs clés :**
  - Métriques de qualité
  - Processus d'amélioration
  - Validation croisée
  - Évolution du contexte

---

## **10h00-10h15 : Pause (15min)**

---

## **10h15-11h00 : Structure du Contrat de Contexte (45min)**

### Présentation du Contrat de Contexte

Le **Contrat de Contexte** est un document fonctionnel qui définit précisément les exigences contextuelles pour un agent IA. Il sert d'interface de communication entre le Product Owner, le client et l'équipe de développement.

### Les 5 sections principales

#### 📋 **1. Informations Générales (5min)**

| Champ | Description | Exemple |
|-------|-------------|---------|
| **ID Contrat** | Identifiant unique | `CC-[PROJET]-[AGENT]-[VERSION]` |
| **Nom de l'Agent** | Nom fonctionnel | `Assistant Réclamations Voyageurs` |
| **Version** | Numéro de version | `1.2.3` |
| **Date de Création** | Date initiale | `2025-01-15` |
| **Statut** | État du contrat | `Brouillon/Validé/Approuvé/Production` |

#### 🎯 **2. Définition Fonctionnelle (10min)**

**Mission de l'Agent :**
- Description claire et concise de ce que fait l'agent
- Objectif métier et impact attendu
- Périmètre et limites fonctionnelles

**Cas d'Usage Principaux :**
Pour chaque cas d'usage :
- Nom du cas d'usage
- Déclencheur (événement)
- Acteurs impliqués
- Résultat attendu
- Critères de succès

#### 🧠 **3. Spécification du Contexte (15min)**

**Instructions Système :**
```markdown
Tu es [description du rôle].

Tes caractéristiques :
- [Expertise spécialisée]
- [Style de communication]
- [Approche méthodologique]

Règles obligatoires :
1. [Règle de validation]
2. [Règle de confidentialité]
3. [Règle d'escalade]

Format de réponse :
1. Résumé de situation
2. Analyse effectuée
3. Recommandation/Action
4. Prochaines étapes
```

**Sources de Connaissance :**

| Source | Type | Description | Criticité |
|--------|------|-------------|-----------|
| `[Système 1]` | `API/Base/Fichier` | `[Type de données]` | `Critique/Important/Optionnel` |

**Outils Disponibles :**

| Outil | Description | Paramètres | Conditions d'Usage |
|-------|-------------|------------|------------------|
| `[nom_outil]` | `[Fonction métier]` | `[Entrées requises]` | `[Quand utiliser]` |

#### ⚙️ **4. Configuration Technique (10min)**

**Contraintes de Performance :**

| Métrique | Valeur Cible | Valeur Limite |
|----------|--------------|---------------|
| **Temps de Réponse** | `< 2 secondes` | `< 5 secondes` |
| **Utilisation Tokens** | `< 3000 tokens` | `< 4000 tokens` |
| **Précision** | `≥ 95%` | `≥ 90%` |

**Gestion des Erreurs :**

| Type d'Erreur | Comportement | Escalade |
|---------------|--------------|----------|
| **Données Manquantes** | `Demander confirmation` | `Automatique` |
| **Données Incohérentes** | `Prioriser source fiable` | `Validation humaine` |
| **Erreur Système** | `Mode dégradé` | `Support technique` |

#### 📊 **5. Validation et Métriques (5min)**

**Critères de Validation :**
- Compréhension correcte : ≥ 95%
- Pertinence des réponses : ≥ 90%
- Conformité aux règles : 100%
- Temps de traitement : < objectif défini

**Tests d'Acceptation :**
```gherkin
Étant donné [situation]
Quand [action]
Alors [résultat attendu]
Et [vérifications]
```

---

## **Exercice pratique : Exemple de Contrat**

**Cas d'étude :** Agent de Classification Royal Air Maroc

### Contrat de Contexte - Agent de Classification

#### Informations Générales
- **ID** : CC-RAM-CLASSIFICATION-1.0
- **Agent** : Classification et Dispatch des Réclamations
- **Mission** : Analyser automatiquement les réclamations clients et les router vers les équipes appropriées

#### Sources de Données
1. **HubSpot CRM** : Nouveaux tickets, messages clients
2. **Altea** : Données de réservation et vol
3. **Base Règles** : Critères de classification RAM
4. **Système RH** : Charge des équipes

#### Outils Disponibles
- `classify_claim_type(message, attachments)`
- `determine_priority(client_tier, claim_type, urgency)`
- `route_to_team(claim_data, team_availability)`

#### Exemple de Contexte Assemblé
```markdown
## Instructions
Tu es l'agent de classification Royal Air Maroc.
Analyse chaque réclamation et détermine le routage optimal.

## Réclamation
- ID: TICK-2025-001
- Client: Jean Dupont (Gold Safar Flyer)
- Message: "Mon vol AT123 du 15/01 a été annulé..."

## Données Vol
- Vol: AT123, Date: 15/01/2025
- Statut: Annulé (météo)
- Passagers affectés: 156

## Équipes Disponibles
- Irrégularités: 3 agents (70% charge)
- VIP: 1 agent (30% charge)

## Classification Attendue
Type: Irrégularité vol
Priorité: Élevée (client Gold)
Équipe: VIP (disponible)
```

---

## **Points clés à retenir**

1. **Le Contrat de Contexte est un outil de communication** entre toutes les parties prenantes
2. **Chaque champ a un impact direct** sur la performance de l'agent
3. **La validation croisée** (métier + technique) est essentielle
4. **L'itération** permet d'améliorer progressivement le contexte
5. **La documentation des exemples** facilite la validation et les tests

---

## **Préparation pour l'après-midi**

Cette session théorique prépare le TP final de l'après-midi où vous mettrez en pratique tous ces concepts dans un projet collaboratif multi-agents complet.

---

## **Annexe : Template Complet du Contrat de Contexte**

### Vue d'Ensemble

Ce document constitue un **Contrat de Contexte** fonctionnel qui définit précisément les exigences contextuelles pour un agent IA. Il sert d'interface de communication entre le Product Owner, le client et l'équipe de développement.

### 📋 Informations Générales

#### Identification du Contrat

| Champ | Valeur |
|-------|--------|
| **ID Contrat** | `CC-[PROJET]-[AGENT]-[VERSION]` |
| **Nom de l'Agent** | `[Nom fonctionnel de l'agent]` |
| **Version** | `[X.Y.Z]` |
| **Date de Création** | `[YYYY-MM-DD]` |
| **Dernière Mise à Jour** | `[YYYY-MM-DD]` |
| **Statut** | `[Brouillon/Validé/Approuvé/En Production]` |

#### Parties Prenantes

| Rôle | Nom | Email | Responsabilité |
|------|-----|-------|----------------|
| **Product Owner** | `[Nom]` | `[email]` | Définition fonctionnelle et validation |
| **Client/Métier** | `[Nom]` | `[email]` | Expression du besoin et acceptation |
| **Lead Développeur** | `[Nom]` | `[email]` | Implémentation technique |
| **Architecte IA** | `[Nom]` | `[email]` | Conception du contexte |

### 🎯 Définition Fonctionnelle de l'Agent

#### Mission de l'Agent

**Description** : `[Description claire et concise de ce que fait l'agent]`

**Objectif Métier** : `[Impact attendu sur le processus métier]`

**Périmètre** : `[Limites fonctionnelles de l'agent]`

#### Cas d'Usage Principaux

**Cas d'Usage #1**
- **Nom** : `[Nom du cas d'usage]`
- **Déclencheur** : `[Événement qui déclenche ce cas]`
- **Acteurs** : `[Qui est impliqué]`
- **Résultat Attendu** : `[Ce qui doit être produit]`
- **Critères de Succès** : `[Comment mesurer le succès]`

### 🧠 Spécification du Contexte

#### 1. Instructions Système

**Rôle et Personnalité**
```
Tu es [description du rôle de l'agent].

Tes caractéristiques principales :
- [Trait 1 : expertise, spécialisation]
- [Trait 2 : style de communication]
- [Trait 3 : approche méthodologique]

Ton objectif est de [objectif principal en une phrase].
```

**Règles de Comportement**
```
Règles obligatoires :
1. [Règle 1 - ex: Toujours vérifier les données avant de répondre]
2. [Règle 2 - ex: Respecter la confidentialité des données client]
3. [Règle 3 - ex: Escalader en cas d'ambiguïté]

Règles interdites :
1. [Interdiction 1 - ex: Ne jamais divulguer d'informations sensibles]
2. [Interdiction 2 - ex: Ne pas prendre de décisions sans validation]
3. [Interdiction 3 - ex: Ne pas modifier les données sans autorisation]
```

**Format de Réponse Attendu**
```
Structure de réponse :
1. [Section 1 : Résumé de la situation]
2. [Section 2 : Analyse effectuée]
3. [Section 3 : Recommandation/Action]
4. [Section 4 : Prochaines étapes]

Contraintes de format :
- Langue : [Français/Multilingue selon détection]
- Longueur : [Minimum X mots, Maximum Y mots]
- Style : [Professionnel/Empathique/Technique]
- Niveau : [Grand public/Expert/Technique]
```

#### 2. Sources de Connaissance

**Sources de Données Obligatoires**

| Source | Type | Description | Fréquence de Mise à Jour | Criticité |
|--------|------|-------------|-------------------------|-----------|
| `[Nom Système 1]` | `[API/Base/Fichier]` | `[Description des données]` | `[Temps réel/Quotidien/Hebdomadaire]` | `[Critique/Important/Optionnel]` |
| `[Nom Système 2]` | `[API/Base/Fichier]` | `[Description des données]` | `[Temps réel/Quotidien/Hebdomadaire]` | `[Critique/Important/Optionnel]` |

#### 3. Outils Disponibles

**Outils Système**

| Nom de l'Outil | Description Fonctionnelle | Paramètres d'Entrée | Sortie Attendue | Conditions d'Usage |
|-----------------|--------------------------|---------------------|-----------------|-------------------|
| `[nom_outil_1]` | `[Ce que fait l'outil]` | `[Liste des paramètres]` | `[Format de sortie]` | `[Quand l'utiliser]` |
| `[nom_outil_2]` | `[Ce que fait l'outil]` | `[Liste des paramètres]` | `[Format de sortie]` | `[Quand l'utiliser]` |

#### 4. Gestion de la Mémoire

**Mémoire de Session**
- **Durée de Vie** : `[Durée de la session utilisateur]`
- **Informations Conservées** : `[Liste des éléments à retenir]`
- **Limite de Capacité** : `[Nombre max d'éléments ou tokens]`

**Mémoire Persistante**
- **Données Client** : `[Informations client à conserver entre sessions]`
- **Apprentissages** : `[Patterns et règles apprises]`
- **Historique** : `[Interactions significatives à conserver]`

### 🔧 Spécifications Techniques

#### Contraintes de Performance

| Métrique | Valeur Cible | Valeur Limite | Mesure |
|----------|--------------|---------------|---------|
| **Temps de Réponse** | `[X secondes]` | `[Y secondes max]` | `[Temps total traitement]` |
| **Utilisation Tokens** | `[X tokens moyens]` | `[Y tokens max]` | `[Contexte + réponse]` |
| **Précision** | `[X% minimum]` | `[Y% acceptable]` | `[Validation métier]` |
| **Disponibilité** | `[X% uptime]` | `[Y% minimum]` | `[Temps de service]` |

#### Gestion des Erreurs

| Type d'Erreur | Cause | Comportement Attendu | Escalade |
|---------------|-------|---------------------|----------|
| **Données Manquantes** | `[Source indisponible]` | `[Demander confirmation/Utiliser défaut]` | `[Automatique/Manuelle]` |
| **Données Incohérentes** | `[Conflit entre sources]` | `[Prioriser source fiable/Demander clarification]` | `[Validation humaine]` |
| **Limite de Contexte** | `[Trop d'informations]` | `[Compression intelligente/Priorisation]` | `[Log pour optimisation]` |
| **Erreur Système** | `[Panne technique]` | `[Mode dégradé/Message d'erreur]` | `[Support technique]` |

### 📊 Métriques et Validation

#### Critères de Validation Fonctionnelle

| Critère | Description | Méthode de Test | Seuil d'Acceptation |
|---------|-------------|-----------------|-------------------|
| **Compréhension** | L'agent comprend correctement la demande | Test avec cas réels | `≥ 95%` |
| **Pertinence** | Les réponses sont adaptées au contexte | Évaluation expert métier | `≥ 90%` |
| **Completude** | Toutes les informations nécessaires sont fournies | Check-list validation | `≥ 95%` |
| **Conformité** | Respect des règles métier et réglementaires | Audit conformité | `100%` |

### ✅ Checklist de Validation

#### Validation Fonctionnelle
- [ ] **Mission de l'agent clairement définie**
- [ ] **Cas d'usage documentés avec exemples**
- [ ] **Sources de données identifiées et validées**
- [ ] **Règles métier formalisées**
- [ ] **Comportements d'exception définis**
- [ ] **Critères de succès mesurables**
- [ ] **Tests d'acceptation rédigés**
- [ ] **Validation client obtenue**

#### Validation Technique
- [ ] **Faisabilité technique confirmée**
- [ ] **Architecture du contexte validée**
- [ ] **Intégrations système spécifiées**
- [ ] **Contraintes de performance définies**
- [ ] **Stratégies d'optimisation planifiées**
- [ ] **Gestion des erreurs implémentée**
- [ ] **Sécurité et conformité assurées**
- [ ] **Plan de monitoring défini**

---

*Template créé pour faciliter la communication et assurer la qualité du Context Engineering dans les projets d'agents IA.*