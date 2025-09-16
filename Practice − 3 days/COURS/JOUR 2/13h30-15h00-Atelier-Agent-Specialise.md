# 13h30 - 15h00 : Atelier "Agent Spécialisé" (90min)

### Contenu formation

**Choix entre 3 agents simples - Focus apprentissage agent :**

**Option A : "Assistant Veille Tech"**
- Input : Liste de sources RSS/blogs
- Output : Résumé quotidien personnalisé
- Tools : RSS reader, markdown

**Option B : "Organiseur Fichiers"**  
- Input : Dossier désordonné
- Output : Structure organisée + rapport
- Tools : file system, patterns

**Option C : "Générateur Commits"**
- Input : Git diff
- Output : Message commit structuré
- Tools : git commands, templates

**Structure - Focus compétences agent :**
- Choix de l'option (5min)
- Conception agent (15min) 
- Implémentation simple (50min)
- Test et amélioration (20min)

### 📝 Notes formateur

**Templates détaillés par option :**

**Template Option A - Assistant Veille Tech :**
```yaml
# .cursor/rules pour Assistant Veille Tech
Tu es un assistant de veille technologique.

MISSION :
Créer un résumé quotidien personnalisé depuis des sources tech.

PROCESSUS :
1. Lire les flux RSS/blog fournis
2. Identifier les articles pertinents
3. Extraire les points clés
4. Générer un résumé structuré

TOOLS SIMPLES :
- RSS reader basique
- Template markdown
- Filtrage par mots-clés

OUTPUT :
- Résumé quotidien markdown
- Catégorisation par thèmes
- Liens vers articles complets
- Score de pertinence

STYLE :
- Format digest lisible
- Focus sur l'actionnable
- Maximum 5 articles/jour
```

**Stratégie d'accompagnement - Focus compétences agent :**
- **Assistant Veille :** Focus automatisation et filtrage intelligent
- **Organiseur Fichiers :** Focus patterns reconnaissance et logique
- **Générateur Commits :** Focus templates et consistance

## 🤖 **Implémentations avec Gemini CLI**

### Option A : Assistant Veille Tech avec Gemini CLI

**Setup et configuration :**
```bash
# Installation et authentification
npm install -g @google/gemini-cli
gemini

# Création du dossier projet
mkdir tech-watch-agent && cd tech-watch-agent
```

**Prompt système complet pour Gemini CLI :**
```bash
gemini
> Tu es un Assistant Veille Technologique expert.

MISSION : Créer un résumé quotidien personnalisé de veille tech

WORKFLOW :
1. Analyse des sources tech (Medium, Dev.to, GitHub Trending)
2. Extraction des points clés par article
3. Classification par catégories (AI/ML, Web Dev, DevOps, Security)
4. Génération d'un digest markdown structuré

CRITÈRES DE PERTINENCE :
- Nouveautés technologiques significatives
- Retours d'expérience pratiques
- Outils et frameworks émergents
- Tendances d'adoption en entreprise

OUTPUT FORMAT :
# 📰 Veille Tech - [DATE]

## 🤖 Intelligence Artificielle
- [Titre] - [Source] - [Score: X/10]
  Résumé en 2 phrases max + lien

## 🌐 Développement Web
## ⚙️ DevOps & Infrastructure  
## 🔒 Sécurité
## 🎯 Points d'Action
```

**Exemple d'utilisation :**
```bash
gemini
> Analyse ces 10 articles tech que j'ai bookmarkés cette semaine.
> Génère un résumé structuré avec les 5 articles les plus pertinents
> pour une équipe de développement full-stack.
```

### Option B : Organiseur Fichiers avec Gemini CLI

**Configuration de l'agent :**
```bash
cd dossier-desordonne/
gemini --include-directories ./*
```

**Prompt spécialisé :**
```bash
> Tu es un Agent Organiseur de Fichiers expert en architecture de projets.

MISSION : Analyser et réorganiser une structure de fichiers chaotique

PROCESSUS :
1. Scanner tous les fichiers et dossiers
2. Identifier les patterns et types de contenu
3. Proposer une architecture logique
4. Générer les commandes de reorganisation
5. Créer un rapport de migration

RÈGLES D'ORGANISATION :
- Séparer code source, assets, docs, tests
- Grouper par fonctionnalités métier
- Respecter les conventions du langage/framework
- Maintenir la traçabilité des déplacements

OUTPUT :
## 📁 Plan de Reorganisation
### Structure actuelle (analyse)
### Structure proposée
### Commandes de migration
### Fichiers à supprimer/consolider
```

**Exemple pratique :**
```bash
gemini
> Ce dossier contient 200 fichiers mélangés : JS, CSS, images, docs.
> Analyse le contenu et propose une structure propre pour un projet React.
> Génère les commandes bash pour la migration.
```

### Option C : Générateur Commits avec Gemini CLI

**Setup dans un projet git :**
```bash
cd mon-projet-git/
# Faire quelques modifications
git add .
gemini
```

**Agent Commit Generator :**
```bash
> Tu es un Expert Git Commit Generator suivant les conventions professionnelles.

MISSION : Analyser git diff et générer des messages de commit parfaits

ANALYSE REQUISE :
1. Type de changement (feat/fix/refactor/docs/test)
2. Scope affecté (module/composant)
3. Impact sur l'API (breaking change?)
4. Description concise et précise

FORMAT CONVENTIONAL COMMITS :
type(scope): description concise

Description détaillée si nécessaire
- Point 1
- Point 2

BREAKING CHANGE: description si applicable
Fixes #123

EXEMPLES :
feat(auth): add JWT token validation middleware
fix(api): handle null response in user service  
refactor(components): extract Button to shared library
```

**Utilisation avec différents types de commits :**
```bash
# Pour un bug fix
gemini
> Analyse ce git diff et génère un message de commit pour cette correction de bug

# Pour une nouvelle feature  
gemini
> Ces changements ajoutent l'authentification OAuth. Génère le commit message.

# Pour un refactoring
gemini  
> J'ai extrait 3 composants dans des fichiers séparés. Crée le commit approprié.
```

### Resources et documentation

- **Documentation officielle :** [Gemini CLI - Google Developers](https://developers.google.com/gemini-code-assist/docs/gemini-cli)
- **Guide d'installation :** [GitHub - google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- **Exemples avancés :** [Gemini CLI Complete Guide](https://collabnix.com/gemini-cli-the-complete-guide-to-googles-revolutionary-ai-command-line-interface-2025/)
- **Intégration CI/CD :** [Gemini CLI GitHub Actions](https://blog.google/technology/developers/introducing-gemini-cli-github-actions/)
