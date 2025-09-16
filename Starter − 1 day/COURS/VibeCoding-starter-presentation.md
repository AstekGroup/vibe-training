---
marp: true
theme: default
header: '![height:50px](https://astekgroup.fr/wp-content/uploads/2021/04/Astek-3.png)'
footer: 'C2 - Diffusion limitée'
paginate: true
---

<!-- _class: lead -->
# **Vibe Coding: Formation Starter**
### Une journée pour apprendre à coder avec l'assistance de l'IA

**Philippe Pary & Thomas Foutrein**
*v2 - 2025-08-26*

---

# Objectifs de la formation

- **Coder** avec une assistance IA (Cursor)
- **Améliorer** du code existant
- **Intégrer** l'IA dans votre workflow
- **Personnaliser** l'outil à vos besoins
- **Formuler** des prompts efficaces
- **Développer** un projet complet en "Vibe Coding"

---

# Tour de table

- **Qui êtes-vous ?** (Nom, fonction)
- **Votre expérience avec l'IA ?** (Déjà vibe codé ?)
- **Votre vision du vibe coding ?**
- **Vos attentes** pour aujourd'hui ?

---

# Le Vibe Coding, c'est quoi ?

Une technique de programmation assistée par LLM où le **prompt** est au cœur du développement.

- **Plus qu'une simple auto-complétion**.
- Le développeur devient un **architecte** et un **guide** pour l'IA.
- **Transformation du métier** : plus de relecture, de conception et de tests.

> Concept popularisé par Andrej Karpathy (co-fondateur d'OpenAI) début 2025.

---

# Comment ça marche ? (Les LLMs)

1.  **Pré-entraînement** sur des milliards de lignes de code et de texte.
2.  **Fine-tuning** sur des tâches spécifiques (génération de code, etc.).
3.  **RLHF** (Reinforcement Learning from Human Feedback) pour affiner la qualité.

**Processus de génération :**
- **Tokenisation** du prompt.
- **Analyse du contexte** (code, fichiers ouverts).
- **Génération auto-régressive** (token par token).

⚠️ **Limites :** Hallucinations, connaissance limitée, pas de test direct du code. Le développeur reste indispensable !

---

# Les Outils du Vibe Coding

| Outil | Type | Avantages | Inconvénients |
|:---|:---|:---|:---|
| **Claude Code** | CLI | ✅ Puissance Claude 4 | ⚠️ Pas d'IDE |
| **Cursor** | Éditeur dédié | ✅ Optimisé, personnalisable | ⚠️ App séparée |
| **gemini-cli** | Outil CLI | ✅ Scriptable, gratuit | ⚠️ Pas de GUI |
| **Continue** | Extension VSCode | ✅ Open source, intégré | ⚠️ Moins stable |
| **Copilot** | Extension multi-IDE | ✅ Mature, très répandu | ⚠️ Moins orienté "vibe" |

**Modèles 2025 :** Claude 4 Sonnet • ChatGPT-5 • Gemini-2.5-pro

---

# Workflow : Deux approches

### 1. Itératif
On part d'un prompt initial, puis on ajoute les fonctionnalités une par une.
- ✅ **Meilleure maîtrise** de l'évolution.
- ❌ **Risque de "partir en vrille"**. Pensez à commiter souvent !

### 2. One Big Happy Prompt
On prépare un cahier des charges très détaillé en amont.
- ✅ **Projet structuré**, moins de régressions.
- ❌ **Relecture fastidieuse**, temps de développement potentiellement plus long.

---

# Framework des 5 Compétences Clés

1. **🧠 Thinking** : Décomposer le problème avant de prompter
2. **🏗️ Frameworks** : Utiliser des structures éprouvées  
3. **✅ Checkpoints** : Valider à chaque étape
4. **🐛 Debugging** : Dialoguer avec l'IA pour corriger
5. **📝 Context** : Fournir le bon niveau de détail

> Inspiré des meilleures pratiques industrielles 2025

---

# Template de Prompt Efficace

```
## Contexte
[Décris le projet et l'objectif]

## Rôle  
Tu es un [expertise] expert en [technologie]...

## Tâche
[Action précise à réaliser]

## Contraintes
- Technologies : [liste précise]
- Standards : [conventions de code]
- Tests : [requis/optionnel]

## Format attendu
- Code commenté + gestion d'erreurs
```

---

# Exemples : Do's & Don'ts

### ❌ Prompt Inefficace
*"Fais une calculatrice web"*

**Problèmes :** Trop vague, pas de contraintes

### ✅ Prompt Efficace  
**Contexte :** Calculatrice professionnelle pour comptables  
**Rôle :** Développeur front-end expert JavaScript vanilla  
**Tâche :** Calculatrice avec historique, raccourcis clavier, responsive  
**Contraintes :** HTML5/CSS3/JS vanilla, accessible, stockage local

---

# Pièges à éviter

- **Git est votre ami** : `git commit -m "checkpoint"` à chaque fonctionnalité
- **Relecture critique** : L'IA peut halluciner des APIs inexistantes
- **Sécurité** : Vérifiez les vulnérabilités potentielles  
- **Prompts précis** : Plus de détails = meilleurs résultats

---

# À vous de jouer ! (Exercices)

## Phase 1 : Exercice Guidé (ensemble)
**Analyseur de Performance Web** - développement collectif

## Phase 2 : Exercices Individuels
1.  **Snake en Vanilla JS** - aspect ludique + `localStorage`
2.  **Calcul de Pi en Python** - méthode Monte-Carlo
3.  **Gestionnaire de tâches** - application pratique
4.  **Mini-défi debugging** - corriger code buggy

---

# Git + IA : Workflow Recommandé

```bash
# Workflow avec checkpoints
git checkout -b feature/user-auth
git commit -m "init: setup project structure"

# Après chaque prompt réussi
git add . && git commit -m "feat: implement login form"

# L'IA aide pour les commits
git diff --cached
# Prompt : "Génère un message de commit pour ces modifications"
```

**Astuce** : Branches d'expérimentation pour tester différents prompts

---

# Risques & Considérations

- **Green IT** : Chaque prompt a un coût énergétique
- **Sécurité** : Context poisoning, vulnérabilités générées  
- **Éthique** : Biais dans le code (i18n, accessibilité)
- **Juridique** : Licences, RGPD, droits d'auteur

---

<!-- _class: lead -->
# Bilan & Perspectives

- **Tour de table**
- **Le Vibe Coding est en constante évolution.**
- **Questions ?**

