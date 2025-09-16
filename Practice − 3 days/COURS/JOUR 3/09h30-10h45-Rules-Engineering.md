# 9h30 - 10h45 : "Rules Engineering" (75min)

### Contenu formation

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

### 📝 Notes formateur

**9h30-9h50 : Audit de règles existantes (20min)**

**3 fichiers à analyser :**

**Fichier 1 - Règles basiques (bonnes pratiques) :**
```
Tu es un développeur Python expert.
Utilise toujours des type hints.
Écris des docstrings pour toutes les fonctions.
Privilégie la lisibilité à la performance.
```

**Fichier 2 - Règles problématiques :**
```
Fais du bon code.
Sois efficace.
N'oublie pas les tests.
Attention à la sécurité.
```

**Fichier 3 - Règles avancées (exemple à suivre) :**
```
# Contexte : API fintech haute performance
Tu es un senior backend engineer spécialisé en systèmes financiers.

STACK TECHNOLOGIQUE :
- Python 3.11+ avec FastAPI
- PostgreSQL avec SQLAlchemy async
- Redis pour caching
- Pytest pour tests

CONTRAINTES RÉGLEMENTAIRES :
- PCI DSS Level 1 compliance
- SOX audit requirements  
- GDPR pour données EU

STANDARDS QUALITÉ :
- Type hints obligatoires (mypy strict)
- Couverture tests > 95%
- Logging structuré (JSON)
- Métriques OpenTelemetry

SÉCURITÉ :
- Jamais de secrets en dur
- Validation inputs avec Pydantic
- Audit trail pour toutes mutations
- Rate limiting sur tous endpoints
```

**Questions d'analyse :**
- "Lesquelles donnent des instructions actionables ?"
- "Comment mesurer l'efficacité de ces règles ?"

**9h50-10h20 : Création de règles modulaires (30min)**

**Exercice pratique (binômes) :**

**Étape 1 : Règles générales (10min)**
```
Créez `rules-general.md` avec :
- Principes qualité universels
- Standards sécurité de base
- Patterns communication préférés
```

**Étape 2 : Règles spécifiques (15min)**
```
Créez 3 fichiers spécialisés :
- `rules-backend.md` : API, databases, performance
- `rules-frontend.md` : UI, UX, responsiveness  
- `rules-mobile.md` : Cross-platform, performance
```

**10h20-10h45 : Test en conditions réelles (25min)**
- Application sur mini-projet
- Comparaison avant/après des réponses IA
- Mesure qualitative de l'amélioration

**Points d'attention :**
- Insister sur l'itération : "Rules parfaites n'existent pas"
- Montrer importance du test : "Rules non testées = inutiles"
