# 13h30 - 15h00 : Atelier "Agent Spécialisé" (90min)

### Contenu formation

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
- Tools : linters, analyzer

**Structure :**
- Choix de l'option (5min)
- Setup et paramétrage (20min)
- Développement (50min)
- Demo croisée (15min)

### 📝 Notes formateur

**Templates détaillés par option :**

**Template Option A - Documentation Generator :**
```yaml
# .cursor/rules pour Documentation Generator
Tu es un expert en documentation technique.

MISSION :
Générer documentation complète et professionnelle.

PROCESSUS :
1. Analyser structure projet (packages, modules)
2. Examiner code pour comprendre logique métier
3. Consulter historique git pour contexte évolutif
4. Générer documentation structurée

TOOLS DISPONIBLES :
- File system : lecture code source
- Git commands : historique et commits
- AST parser : structure syntaxique

OUTPUT STANDARD :
- README.md principal avec getting started
- Documentation API (si applicable)  
- Docstrings inline pour fonctions/classes
- Architecture overview avec diagrammes ASCII

STYLE :
- Clair et concis
- Exemples concrets d'usage
- Audience développeur
- Format Markdown standard
```

**Stratégie d'accompagnement :**
- **Documentation Generator :** Focus structuration information
- **Test Writer :** Accent couverture et pertinence
- **Refactor Assistant :** Focus préservation comportement
