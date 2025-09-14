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
