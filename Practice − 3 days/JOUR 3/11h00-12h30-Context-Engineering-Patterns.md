# 11h00 - 12h30 : "Context Engineering Patterns" (90min)

### Contenu formation

**6 mini-ateliers de 15min chacun :**

1. **Prompt Chaining** : Séquence de 3 prompts interdépendants
2. **Conditional Loading** : Rules qui s'activent selon le contexte
3. **Memory Patterns** : Garder l'historique des décisions
4. **RAG Simple** : Agent qui interroge de la documentation
5. **Multi-Modal** : Agent qui traite code + images/diagrammes
6. **Error Recovery** : Agent qui corrige ses propres erreurs

**Format :** Rotation par binômes (groupes × 6 stations)

### 📝 Notes formateur

**Structure organisationnelle :**
- 6 stations de 15min chacune
- Rotation par binômes 
- Chaque station = 1 pattern spécifique
- Animation formateur + supports auto-porteurs

**Station 1 : Prompt Chaining (11h00-11h15)**

**Pattern expliqué :**
```
Prompt 1 (Architecture) : "Conçois l'architecture de cette API"
↓
Prompt 2 (Implémentation) : "Implémente selon cette architecture"  
↓
Prompt 3 (Tests) : "Génère les tests pour cette implémentation"
```

**Exercice pratique :**
```
Tâche : "Système de notification push"
Prompt 1 : Définir l'architecture
Prompt 2 : Implémenter les composants
Prompt 3 : Ajouter monitoring et alerting
Règle : Chaque prompt utilise l'output du précédent
```

**Station 2 : Conditional Loading (11h15-11h30)**

**Pattern expliqué :**
```yaml
context_rules:
  language_detected:
    python: load python_standards.md
    javascript: load js_standards.md
    typescript: load ts_standards.md
  
  project_phase:
    prototype: load rapid_dev.md
    production: load production_ready.md
    maintenance: load refactor_rules.md
```

**Station 3 : Memory Patterns (11h30-11h45)**

**Template memory :**
```markdown
## Project: [nom]
## Date: [date]

### Decisions Made:
- **Architecture choice:** Microservices vs Monolith
- **Rationale:** [pourquoi cette décision]
- **Trade-offs:** [avantages/inconvénients]

### Lessons Learned:
- **What worked well:** [patterns efficaces]
- **What to avoid:** [erreurs à ne pas répéter]

### For Next Time:
- **Improvements:** [améliorations identifiées]
- **Tools to try:** [outils à explorer]
```

**Station 4 : RAG Simple (11h45-12h00)**

**Pattern expliqué :**
```
User Query → Semantic Search → Retrieve Docs → 
Augment Prompt → Generate Answer
```

**Pseudo-code RAG :**
```python
def rag_agent(user_query):
    # 1. Search relevant docs
    docs = semantic_search(user_query, knowledge_base)
    
    # 2. Augment prompt with context
    augmented_prompt = f"""
    Context from documentation: {docs}
    User question: {user_query}
    Answer using the provided context.
    """
    
    # 3. Generate informed response  
    return ai_model.generate(augmented_prompt)
```

**Station 5 : Multi-Modal (12h00-12h15)**

**Pattern expliqué :**
```
Inputs multiples : Code + Diagramme UML + Spécs texte
↓
Agent analyse tous les formats
↓  
Output cohérent qui réconcilie toutes les sources
```

**Station 6 : Error Recovery (12h15-12h30)**

**Pattern expliqué :**
```python
def self_correcting_agent(task):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            result = generate_solution(task)
            if validate_solution(result):
                return result
            else:
                task = refine_task_with_errors(task, result)
        except Exception as e:
            task = add_error_context(task, e)
    
    # Escalate to human after max retries
    return escalate_to_human(task, failed_attempts)
```
