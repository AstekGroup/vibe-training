# Plan de Mise en Conformité - Présentation vs Cours Build (3 jours)

**Version** : 1.0
**Date** : 2025-10-25
**Auteur** : Claude Code
**Statut** : 🔴 En attente de validation

---

## 📋 Légende des Cases à Cocher

- `[ ]` Tâche non commencée
- `[~]` Tâche en cours
- `[x]` Tâche terminée
- `[?]` Tâche nécessitant clarification

---

## 🎯 Objectif de la Mise en Conformité

Harmoniser le fichier de présentation HTML (`presentation-vibe-coding-complete.html`) avec les contenus de formation markdown du dossier `COURS/` pour garantir :
- ✅ Cohérence pédagogique entre supports visuels et contenus détaillés
- ✅ Exhaustivité des modules dans la présentation
- ✅ Alignement des plannings et durées
- ✅ Clarté terminologique et conceptuelle

---

## 📊 Analyse des Écarts Identifiés

### ✅ Points Conformes

| Aspect | Statut | Commentaire |
|--------|--------|-------------|
| Structure 3 jours | ✅ Conforme | Architecture générale respectée |
| Objectifs pédagogiques | ✅ Conforme | Alignement global satisfaisant |
| Ordre logique modules | ✅ Conforme | Progression pédagogique cohérente |
| Frameworks cités | ✅ Conforme | BMAD, SuperClaude, Spec-Kit, OpenSpec présents |
| Outils vibe coding | ✅ Conforme | Claude Code, Cursor, Gemini CLI, Continue |

### ❌ Écarts Critiques

| # | Module | Type Écart | Impact | Priorité |
|---|--------|------------|--------|----------|
| 1 | JOUR 1 - Premier TP Live | ❌ Absent des cours | Moyen | 🟡 Moyenne |
| 2 | JOUR 2 - Titre Module MCP | ⚠️ Incohérence | Faible | 🟢 Basse |
| 3 | JOUR 3 - Google ADK | ❌ Absent présentation | **CRITIQUE** | 🔴 Haute |
| 4 | JOUR 3 - Planning horaires | ⚠️ Décalage | Élevé | 🔴 Haute |
| 5 | Acronyme P.O.P.M. | ❓ Non défini | Moyen | 🟡 Moyenne |
| 6 | Rules Engineering | ⚠️ Positionnement flou | Faible | 🟢 Basse |

### 📈 Détail des Écarts

#### Écart #1 : Premier TP Live de Vibe Coding (JOUR 1) ✅ RÉSOLU
**Localisation** : Après "Framework 5 Compétences"
**Présent dans** : ✅ Slides (9h30-10h15) + Présentation complétée
**Solution** : Slide "Premier TP Live de Vibe Coding Instinctif" ajoutée
**Contenu ajouté** :
- Exercice 1 : Snake game avec interface graphique
- Exercice 2 : Todo App CRUD basique
- Exercice 3 : Calcul de Pi (méthode Monte-Carlo)
- Consignes détaillées et débriefing

#### Écart #2 : Incohérence Titre Module MCP (JOUR 2) ✅ RÉSOLU
**Slide** : "TP Configuration Serveurs MCP" (13h30-15h00)
**Fichier cours** : `13h30-15h00-TP-Configuration-Serveurs-MCP.md` (renommé)
**Solution** : Fichier cours renommé pour correspondre au titre des slides

#### Écart #3 : Google ADK Manquant (JOUR 3) ⚠️ CRITIQUE
**Planning cours** : 10h00-12h30 (150 minutes)
**Planning slides** : ❌ Absent, remplacé par extension "Contrat de Contexte"
**Impact** : **2h30 de contenu formation non représenté dans présentation**
**Fichier source** : `JOUR 3/10h00-12h30-Google-ADK.md` (554 lignes)

#### Écart #4 : Planning Horaires JOUR 3
**Slides** :
- 9h00-11h00 : Le Contrat de Contexte (120min)
- 11h00-17h00 : TP Final

**Cours** :
- 9h00-10h00 : Contrat de Contexte (60min)
- 10h00-12h30 : Google ADK (150min)
- 13h30-17h00 : TP Final

**Décalage total** : -90 minutes de contenu théorique

#### Écart #5 : Acronyme P.O.P.M. Non Défini ✅ RÉSOLU
**Utilisation** : Agent P.O.P.M. dans TP Final JOUR 3
**Définition** : ✅ **Product Owner & Project Manager**
**Solution** : Slide de définition des 5 agents ajoutée avant "Processus à suivre"

#### Écart #6 : Rules Engineering
**Slides** : Module "Rules Engineering" (9h30-10h45)
**Cours** : Contenu intégré dans "Contrat de Contexte" mais pas module autonome

---

## 🚀 Plan d'Action Hiérarchisé

### 🔴 PHASE 1 : Modifications Critiques (Priorité HAUTE)

#### Tâche 1.1 : Ajouter Section Google ADK (JOUR 3)
- [x] **Slide 1** : Introduction Google ADK (titre + objectifs)
  - Titre : "Google ADK - Agent Development Kit"
  - Horaire : 10h00-12h30 (150min)
  - Objectifs : Comprendre architecture, créer agent, intégrer outils

- [x] **Slide 2** : Qu'est-ce que Google ADK ?
  - Définition : Framework développement agents IA avec Gemini
  - Analogie : "Assistant personnel → Assistant spécialisé personnalisé"

- [x] **Slide 3** : Architecture ADK (Diagramme)
  ```
  Application/Interface
         ↓
    Agent ADK
    ├─ Gemini Model (Core)
    ├─ Tools & Functions
    └─ Memory & Context
         ↓
  External Services & APIs
  ```

- [x] **Slide 4** : Concepts Clés ADK
  - Agents ADK : Instructions + Outils + Mémoire
  - Tools : Function Calling, API Integration, Custom Tools
  - Memory : Session, Persistent, Context Management

- [x] **Slide 5** : Pourquoi ADK pour Vibe Coding ?
  - Avantages : Personnalisation totale, Intégration facile, Rapidité, Contrôle coûts, Sécurité
  - Cas d'usage : Code review, Génération specs, Analyse conformité, Refactoring, Documentation auto

- [x] **Slide 6** : Installation et Configuration (10h20-10h45)
  - Prérequis : Python 3.10+, GCP account, Gemini API key
  - Installation : `pip install google-adk`
  - Configuration environnement (.env, config Python)

- [x] **Slide 7** : Création Agent Simple (10h45-11h15)
  - Structure projet recommandée
  - Exemple code : Agent Vibe Coding Basique
  - Fichiers : prompts.py, config.py, main.py

- [x] **Slide 8** : Ajout d'Outils (Tools) (11h15-11h45)
  - Exemple : Agent Code Review
  - Fonctions : analyze_code_complexity, check_code_style
  - Intégration dans agent

- [x] **Slide 9** : Exercice Pratique (11h45-12h30)
  - Objectif : Créer Agent Spec Writer
  - Cahier des charges : Description → Questions → Spécification structurée
  - Livrables attendus

- [x] **Slide 10** : Points Clés ADK
  - Google ADK = agents personnalisés Gemini
  - Architecture 3 couches : Instructions + Tools + Memory
  - Function Calling pour intégration outils
  - Vibe Coding bénéficie d'agents spécialisés
  - Configuration flexible + Tests essentiels

**Instructions IA** :
```
TÂCHE : Créer 10 slides Google ADK après slide "Introduction Contrat Contexte"
POSITION : Insérer après ligne ~1783 (section JOUR 3)
STYLE : Respecter classes CSS existantes (.tools-grid, .tool-card, .code-example)
FRAGMENTS : Utiliser class="fragment" pour révélation progressive
COHÉRENCE : Aligner durées avec planning cours (10h00-12h30)
```

#### Tâche 1.2 : Corriger Planning JOUR 3
- [x] **Modifier slide "Programme du Jour 3"** (ligne ~1517)
  - Remplacer : "9h00 - 11h00 : Le Contrat de Contexte"
  - Par : "9h00 - 10h00 : Le Contrat de Contexte (60min)"
  - Ajouter : "10h00 - 12h30 : Google ADK (150min)"

- [x] **Modifier slide en-tête JOUR 3**
  - Confirmer durées : 9h00-10h00 Contexte + 10h00-12h30 ADK + 13h30-17h00 TP

**Instructions IA** :
```
TÂCHE : Mettre à jour planning JOUR 3 (2 slides concernées)
LIGNES : ~1517-1545 (slide Programme) et header JOUR 3
MODIFICATION : Ajout créneau 10h00-12h30 Google ADK
VALIDATION : Vérifier cohérence avec durées cours (Formation-Complete-Build.md ligne 69-77)
```

#### Tâche 1.3 : Harmoniser Titre Module MCP JOUR 2
- [x] **Option A** : Renommer fichier cours ✅ CHOISI
  - Ancien : `13h30-15h00-Atelier-Agent-Specialise.md`
  - Nouveau : `13h30-15h00-TP-Configuration-Serveurs-MCP.md`

- [ ] **Option B** : Modifier titre slide (NON RETENUE)
  - Ancien : "TP Configuration Serveurs MCP"
  - Nouveau : "Atelier Agent Spécialisé"

- [x] **DÉCISION** : Option A appliquée - Fichier cours renommé

**Instructions IA** :
```
TÂCHE : Harmoniser nomenclature module MCP JOUR 2 ✅ TERMINÉ
CHOIX : Option A appliquée
FICHIER SLIDE : ligne ~1305 (inchangé, titre déjà correct)
FICHIER COURS : JOUR 2/13h30-15h00-TP-Configuration-Serveurs-MCP.md (renommé)
ACTION RÉALISÉE : Renommage fichier markdown pour correspondre aux slides
RÉFÉRENCES MISES À JOUR : PLAN-MISE-EN-CONFORMITE.md
```

---

### 🟡 PHASE 2 : Clarifications et Harmonisations (Priorité MOYENNE)

#### Tâche 2.1 : Définir Acronyme P.O.P.M.
- [x] **Ajouter slide définition** avant TP Final
  - Titre : "Les 5 Agents Spécialisés du TP Final"
  - Agent 1 : P.O.P.M. = **Product Owner & Project Manager** ✅
  - Définition complète des 5 agents avec rôles et livrables
  - Tool-cards avec fragments pour révélation progressive

- [x] **DÉCISION** : P.O.P.M. = Product Owner & Project Manager

**Instructions IA** :
```
TÂCHE : Créer slide définition agents TP Final ✅ TERMINÉ
POSITION : Avant slide "Processus à suivre - Les 5 Agents" (ligne ~2150)
CONTENU : 5 agents définis avec P.O.P.M. = Product Owner & Project Manager
FORMAT : Tool-cards avec fragments + objective-box
LIVRABLE : Slide complète avec rôles, responsabilités et livrables de chaque agent
```

#### Tâche 2.2 : Ajouter Premier TP Live JOUR 1
- [x] **Créer slide après "Framework 5 Compétences"** ✅
  - Titre : "Premier TP Live de Vibe Coding Instinctif"
  - 3 exercices : Snake, Todo App, Calcul Pi Monte-Carlo
  - Objectif : Expérimenter génération code sans prompt structuré
  - Horaire : 9h30 - 10h15 (45min)
  - Contenu : Objective-box + 3 tool-cards + Consignes + Débriefing

**Instructions IA** :
```
TÂCHE : Insérer slide "Premier TP Live" JOUR 1 ✅ TERMINÉ
POSITION : Après slide "Les 5 compétences - Partie 2" (ligne ~757)
CONTENU : 3 exercices détaillés + Consignes + Débriefing
DURÉE : Module 9h30-10h15 (45min)
STYLE : Objective-box + tools-grid (3 tool-cards) + exercise-box
LIVRABLE : Slide complète avec 3 exercices pratiques de vibe coding instinctif
```

#### Tâche 2.3 : Clarifier Positionnement "Rules Engineering"
- [ ] **Option A** : Créer module autonome Rules Engineering
  - Séparer du Contrat de Contexte
  - Créer slides dédiées 9h30-10h45

- [x] **Option B** : Maintenir intégration dans Contrat Contexte ✅
  - Ajouter sous-section clairement identifiée
  - Garder horaire 9h00-10h00 global
  - Slide modifiée : "Module 1e: Rules Engineering (sous-section)"
  - Ajout contexte : "Persistance pratique du contrat de contexte"

- [x] **DÉCISION APPLIQUÉE** : Option B - Intégration maintenue

**Instructions IA** :
```
TÂCHE : Structurer contenu Rules Engineering
CHOIX : Attendre validation utilisateur (Option A ou B)
CONTENU SOURCE : Slides existantes lignes ~1619-1753
SI OPTION A : Créer section autonome avec header "Rules Engineering"
SI OPTION B : Renforcer titre sous-section dans "Contrat de Contexte"
```

---

### 🟢 PHASE 3 : Améliorations Pédagogiques (Priorité BASSE)

#### Tâche 3.1 : Enrichir "Les 5 Compétences"
- [ ] Détailler progression Starter → Build pour chaque compétence
- [ ] Ajouter exemples concrets d'évolution
- [ ] Illustrer avec cas d'usage entreprise

**Instructions IA** :
```
TÂCHE : Approfondir slides "Les 5 Compétences"
LIGNES : ~713-757
AJOUT : Exemples concrets transition Starter → Build
FORMAT : Tableaux comparatifs ou tool-cards avec évolution
VALIDATION : Optionnel, amélioration qualitative
```

#### Tâche 3.2 : Ajouter Exemples Code Google ADK
- [x] Intégrer snippets code dans slides ADK ✅
- [x] Exemples : analyze_code_complexity, check_code_style ✅
- [x] Code d'intégration des outils dans l'agent ✅
- [x] Ajout 3 nouvelles slides avec code complet ✅

**Instructions IA** :
```
TÂCHE : Enrichir slides ADK avec code samples ✅ TERMINÉ
SLIDES AJOUTÉES : 3 slides avec exemples de code complets
- Slide 1 : Code analyze_code_complexity (fonction complète)
- Slide 2 : Code check_code_style (fonction complète)
- Slide 3 : Intégration outils dans Agent (create_code_review_agent)
SOURCE : Fichier JOUR 3/10h00-12h30-Google-ADK.md lignes 298-414
FORMAT : Balises <div class="code-example"> avec font-size optimisé
POINTS CLÉS : Objective-box explicatif sur fonctionnement outils
```

#### Tâche 3.3 : Uniformiser Format Horaires
- [ ] Standardiser affichage horaires : "HHhMM - HHhMM"
- [ ] Vérifier cohérence durées slides vs cours
- [ ] Corriger variations typographiques

**Instructions IA** :
```
TÂCHE : Normaliser affichage horaires dans toute la présentation
FORMAT CIBLE : "HHhMM - HHhMM" (ex: "9h00 - 10h30")
RECHERCHE : Identifier tous formats d'horaires
CORRECTION : Appliquer format uniforme
VALIDATION : Vérifier cohérence durées calculées
```

---

## ✅ Checklist de Validation Finale

### Conformité Structurelle
- [ ] Planning JOUR 1 : Horaires slides = Horaires cours
- [ ] Planning JOUR 2 : Horaires slides = Horaires cours
- [ ] Planning JOUR 3 : Horaires slides = Horaires cours (incluant ADK)
- [ ] Tous modules cours ont slides correspondantes
- [ ] Toutes slides ont contenu cours associé

### Conformité Contenu
- [ ] Google ADK : Section complète avec 10 slides
- [ ] Acronymes définis : P.O.P.M., BMAD, CCPM, SuperClaude, Spec-Kit, OpenSpec
- [ ] Outils MCP : Context7 + GitLab documentés
- [ ] Frameworks : BMAD, OpenSpec, Spec-Kit expliqués
- [ ] Exemples pratiques présents pour chaque concept clé

### Conformité Terminologique
- [ ] Titres modules identiques slides/cours
- [ ] Noms outils cohérents (Claude Code, Cursor, Gemini CLI, etc.)
- [ ] Définitions concepts uniformes (agents, MCP, ADK, etc.)

### Conformité Pédagogique
- [ ] Progression logique Starter → Build respectée
- [ ] Exercices pratiques annoncés = exercices cours
- [ ] Objectifs pédagogiques alignés
- [ ] Durées modules réalistes et cohérentes

---

## ❓ Décisions en Attente de Validation

### Décision #1 : Signification P.O.P.M.
**Question** : Que signifie l'acronyme P.O.P.M. pour l'agent du TP Final ?
**Options** :
- A) Product Owner & Project Manager
- B) Product & Planning Manager
- C) Autre (à spécifier)

**Choix** : `[ ]` A  `[ ]` B  `[ ]` C : _______________

---

### Décision #2 : Module MCP - Harmonisation Titre
**Question** : Comment harmoniser le titre du module MCP JOUR 2 ?
**Options** :
- A) Renommer fichier cours : `13h30-15h00-TP-Configuration-Serveurs-MCP.md`
- B) Modifier slide : "Atelier Agent Spécialisé"

**Choix** : `[ ]` A  `[ ]` B

---

### Décision #3 : Rules Engineering - Positionnement
**Question** : Rules Engineering doit-il être un module autonome ?
**Options** :
- A) Module séparé 9h30-10h45 avec slides dédiées
- B) Sous-section intégrée dans "Contrat de Contexte" 9h00-10h00

**Choix** : `[ ]` A  `[ ]` B

---

### Décision #4 : Niveau de Détail Google ADK
**Question** : Quel niveau de détail pour les slides Google ADK ?
**Options** :
- A) Synthétique : Concepts clés + 1 exemple (6-8 slides)
- B) Exhaustif : Architecture + Exemples code + Exercice (10-12 slides)

**Choix** : `[ ]` A  `[ ]` B

---

## 📊 Métriques de Conformité

### Avant Mise en Conformité
- **Modules cours couverts dans slides** : 16/19 (84%)
- **Horaires alignés** : JOUR 1 ✅ | JOUR 2 ✅ | JOUR 3 ❌
- **Contenu critique manquant** : Google ADK (2h30)
- **Incohérences terminologiques** : 3 (P.O.P.M., MCP, Rules)

### Cible Après Mise en Conformité
- **Modules cours couverts dans slides** : 19/19 (100%)
- **Horaires alignés** : JOUR 1 ✅ | JOUR 2 ✅ | JOUR 3 ✅
- **Contenu critique manquant** : 0
- **Incohérences terminologiques** : 0

---

## 📅 Estimation Temporelle

| Phase | Nombre Tâches | Temps Estimé |
|-------|---------------|--------------|
| Phase 1 (Critique) | 3 tâches principales | 2-3 heures |
| Phase 2 (Moyenne) | 3 tâches | 1-2 heures |
| Phase 3 (Basse) | 3 tâches | 1 heure |
| Validation finale | Checklist complète | 30 minutes |
| **TOTAL** | **9 tâches** | **4h30-6h30** |

---

## 🎯 Prochaines Étapes

1. **Validation Plan** : Confirmer priorités et décisions en attente
2. **Phase 1** : Exécuter tâches critiques (Google ADK + Planning)
3. **Revue Intermédiaire** : Vérifier cohérence après Phase 1
4. **Phase 2** : Clarifications et harmonisations
5. **Phase 3** : Améliorations pédagogiques (optionnel)
6. **Validation Finale** : Checklist exhaustive + Tests présentation

---

## 📝 Notes et Commentaires

### Note Formateur
Ce plan garantit l'alignement parfait entre support visuel (présentation HTML) et contenus pédagogiques détaillés (cours markdown). La priorité est donnée à l'ajout du module Google ADK (2h30 de formation) actuellement absent.

### Suivi des Modifications
| Date | Action | Auteur | Statut |
|------|--------|--------|--------|
| 2025-10-25 | Création du plan | Claude Code | ✅ Terminé |
| 2025-10-25 | **Tâche 1.1** : Ajout section Google ADK (10 slides) | Claude Code | ✅ Terminé |
| 2025-10-25 | **Tâche 1.2** : Correction planning JOUR 3 | Claude Code | ✅ Terminé |
| 2025-10-25 | **Tâche 1.3** : Harmonisation titre module MCP (Option A) | Claude Code | ✅ Terminé |
| 2025-10-25 | **Tâche 2.1** : Définition acronyme P.O.P.M. | Claude Code | ✅ Terminé |
| 2025-10-25 | **Tâche 2.2** : Ajout Premier TP Live JOUR 1 | Claude Code | ✅ Terminé |
| 2025-10-25 | **Tâche 2.3** : Clarification Rules Engineering (Option B) | Claude Code | ✅ Terminé |
| 2025-10-25 | **Tâche 3.2** : Ajout exemples code Google ADK (3 slides) | Claude Code | ✅ Terminé |

---

**Fin du Document**
Dernière mise à jour : 2025-10-25
