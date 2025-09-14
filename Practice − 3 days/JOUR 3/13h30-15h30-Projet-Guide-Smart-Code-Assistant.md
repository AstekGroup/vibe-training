# 13h30 - 15h30 : "Projet Guidé : Context Rules Builder" (120min)

### Contenu formation

**Projet unique pour tous mais personnalisable**

**Objectif :** Maîtriser le **Context Engineering** avec un système de rules dynamiques

**Architecture simplifiée :**
- 1 agent principal avec context adaptatif
- Système de rules YAML dynamiques
- Focus sur patterns context, pas sur orchestration complexe

**Timeline focus Context Engineering :**
- **13h30-14h00** : Conception du système de rules (30min)
- **14h00-15h00** : Implémentation context adaptatif (60min)
- **15h00-15h30** : Tests et validation patterns (30min)

**Exemples de contexts adaptatifs :**
- **Code Review Context** : Rules différentes selon type de fichier
- **Documentation Context** : Templates variables selon projet
- **Debug Context** : Approche adaptée selon langage/framework

### 📝 Notes formateur

**13h30-14h00 : Définition architecture (30min)**

**Architecture Context Engineering focus :**
```
Context Rules Builder
├── Agent Principal
│   ├── Détection de contexte
│   ├── Sélection rules appropriées
│   └── Application context dynamique
├── Rules Engine
│   ├── Rules YAML par contexte
│   ├── Validation et fallback
│   └── Templates réutilisables
└── Context Detection
    ├── File type detection
    ├── Project structure analysis
    └── User preferences
```

**13h30-13h45 : Choix des agents spécialisés (15min)**

**Contexts à implémenter :**
- **JavaScript Context :** Rules spécifiques ES6, React, Node
- **Python Context :** Rules adaptées PEP8, Django, Flask
- **Markdown Context :** Templates documentation, blog
- **Git Context :** Messages commits, branch naming
- **Debug Context :** Approche par langage et framework
- **Review Context :** Critères selon type de changement

**Requirements obligatoires :**
```yaml
context_requirements:
  rules_structure:
    - base_rules.yaml (comportement général)
    - context_rules.yaml (par langage/situation)
    - fallback_rules.yaml (cas non prévus)
  detection_logic:
    - file_extension_mapping
    - project_structure_patterns  
    - user_preferences
  output_format:
    - consistent_templating
    - context_aware_responses
    - adaptive_verbosity
```

**14h00-15h00 : Implémentation core (60min)**

**Timeline Context Engineering :**
- **14h00-14h15 :** Setup rules YAML et structure (15min)
- **14h15-14h45 :** Implémentation detection et application (30min)
- **14h45-15h00 :** Tests patterns et validation (15min)

**Points d'attention - Focus Context Engineering :**
- Circuler pour aider sur patterns context, pas sur tech
- Aider à la conception : "Commencez par détection simple"
- Pousser vers rules claires et testables, éviter sur-ingénierie
