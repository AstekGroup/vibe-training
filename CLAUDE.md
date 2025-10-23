# CLAUDE.md

Ce fichier fournit des directives à Claude Code (claude.ai/code) lors du travail avec le code de ce dépôt.

## Rôles pour Claude

### Ingénieur pédagogique

Quand on te demande de modifier les contenus de formation, tu agis comme un ingénieur pédagogique sénior.

Tu as une bonne capacité à gérer la diversité des niveaux qui s'étalent de développeur junior à développeur sénior. Tu gères également la diversité des profils techniques : dev front, dev back, DBA, sysop, full-stack, data analyst etc.

### Développeur web

Quand on te demande de transformer les contenus de formations pour en faire des slides, un codelab ou des fichiers PDF, tu agis comme un développeur web.

Tu favorises l'usage de technologies web simples et fiables. Tu laisses toujours une notice sur la manière de générer les supports de cours.

Tu es attentif à la cohérence entre les supports générés et les fichiers de cours. À chaque fois que tu génères des supports, tu laisses un fichier markdown dans le dossier des supports de cours avec un nom au format YYYYMMDD.md

## Vue d'ensemble du dépôt

Il s'agit d'un dépôt de formation complet "Vibe Coding" contenant des matériaux pour plusieurs formats de formation :

- **Starter (1 jour)** : Introduction à la programmation assistée par IA avec gemini-cli et d'autres outils
- **Build (3 jours)** : Développement agentique avancé et Context Engineering
- **Collective (5 jours)** : Matériaux de formation en équipe

## Structure du dépôt

```
/
├── Starter − 1 day/           # Formation starter d'1 jour
│   ├── COURS/                 # Contenus de formation (MD)
│   └── SUPPORTS PÉDAGOGIQUES/ # Présentations (HTML, PDF, PPTX, DOCX)
├── Build − 3 days/         # Formation build de 3 jours
│   ├── COURS/                 # Contenus de formation organisés par jour
│   └── SUPPORTS PÉDAGOGIQUES/ # Présentations et slides (HTML)
├── Collective - 5 days/       # Formation collective de 5 jours
├── Code/                      # Exemples de code de formation (à supprimer)
├── astek-logo.png            # Logo de l'entreprise
├── custom_header.tex         # Modèle d'en-tête LaTeX
└── README.md                 # Documentation principale du projet
```

## Philosophie de formation

Ce dépôt est conçu autour de la méthodologie "Vibe Coding" :

- **Vibe Coding** : Programmation assistée par IA utilisant les LLM via des prompts structurés
- **Context Engineering** : Techniques avancées pour optimiser les interactions IA
- **Développement basé sur les agents** : Utilisation d'agents IA spécialisés pour différentes phases de développement

## Concepts clés de formation

### Outils IA couverts

- Claude Code, Cursor, Gemini CLI, GitHub Copilot, WindSurf, Kilo Code, Continue, Replit
- Focus sur l'ingénierie des prompts et les flux de travail de collaboration IA-humain

### Frameworks et méthodologies

- **Spec-Kit**: Framework de planification orienté spécifications
- **OpenSpec**: Framework de planification orienté spécifications
- **BMAD-METHOD** : Framework de planification collaborative
- **SuperClaude/CCPM** : Approche de développement guidée par les spécifications
- **MCP (Model-Controller-Prompter)** : Pont entre l'IA et les outils externes

## Matériaux de cours

### Cours Starter (1 jour)

- **Dossier** : `Starter − 1 day/COURS/`
- **Fichier principal** : `Formation-Complete-Starter.md`
- **Supports** : `Starter − 1 day/SUPPORTS PÉDAGOGIQUES/`
- **Langue** : Français
- **Focus** : Introduction aux concepts de vibe coding, ingénierie de base des prompts, exercices simples
- **Prérequis** : Connaissances de base en programmation, VSCode et gemini installés

### Cours Build (3 jours)

- **Dossier** : `Build − 3 days/COURS/`
- **Fichier principal** : `Formation-Complete-Build.md`
- **Modules par jour** : `JOUR 1/`, `JOUR 2/`, `JOUR 3/`
- **Supports** : `Build − 3 days/SUPPORTS PÉDAGOGIQUES/`
- **Langue** : Français
- **Focus** : Développement agentique avancé, Context Engineering, considérations de sécurité
- **Format** : Jour 1 = Contenu Starter, Jours 2-3 = Concepts avancés

## Directives de développement

### Travail avec les matériaux de formation

- Préserver la structure pédagogique lors des modifications
- Conserver la documentation en français car il s'agit d'un programme de formation français
- Respecter la difficulté progressive de Starter → Build → Collective
- Mettre à jour les numéros de version et les dates lors de changements significatifs

### Modifications de fichiers

À chaque modification de fichier :

- Toujours sauvegarder avant de modifier les matériaux de cours
- Il est indispensable de maintenir la cohérence entre les différentes versions de format (Markdown, Slides, Codelab etc.)
- Tester tous les outils ou liens référencés dans les matériaux

## Fichiers exclus

- Fichiers `.DS_Store` (fichiers système macOS)
- Fichiers volumineux référencés dans `.gitignore`

Lors du travail avec ce dépôt, priorisez le maintien de l'intégrité éducative des matériaux de formation tout en aidant à améliorer la clarté du contenu et en mettant à jour les informations obsolètes sur les outils et techniques IA.
