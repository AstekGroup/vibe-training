# 12h00 - 12h30 : Introduction MCP Simplifiée (30min)

### Contenu formation

**MCP = Model Context Protocol** (pas Model-Controller-Prompter)

**Démonstration live du formateur :**
- Exemple : Agent qui lit des APIs externes
- Exemple : Agent qui accède à une base de données
- Q&R : "Quels tools aimeriez-vous pour vos agents ?"

### Serveurs MCP recommandés

**Context7** - Documentation et exemples de code
- URL : https://context7.com/
- Usage : Recherche dans la documentation officielle des frameworks
- Configuration : Automatique via Claude Desktop

**GitHub MCP Server** - Intégration GitHub
- Repository : https://github.com/github/github-mcp-server
- Guide d'installation : [Installation pour Gemini CLI](https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-gemini-cli.md)
- Usage : Gestion des issues, PR, repositories

**Autres serveurs populaires :**
- **SQLite** - Accès bases de données locales
- **File System** - Manipulation avancée de fichiers
- **Web Search** - Recherche web intégrée
- **Docker** - Gestion conteneurs
- **AWS** - Services cloud Amazon

### Référence complète
Liste exhaustive des serveurs MCP disponibles :
📚 **[Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers)**

### 📝 Notes formateur

**12h00-12h05 : Clarification terminologique (5min)**

**Définition simple :**
- **Problème :** Les IA sont isolées, pas d'accès outils externes
- **Solution MCP :** Protocole standard connexion IA ↔ outils
- **Bénéfice :** Agents qui agissent sur le monde réel

**12h05-12h25 : Démonstrations live (20min)**

**Demo 1 : Agent API météo (10min)**
```
Agent prompt :
"Tu es un assistant météo utilisant OpenWeatherMap.
Quand on demande la météo :
1. Appelles l'API avec la ville
2. Interprètes les données JSON
3. Donnes réponse lisible avec recommandations"
```

**Demo 2 : Agent base de données (10min)**
```
Agent prompt :
"Tu es un assistant commercial avec accès base produits.
Tu peux :
1. Rechercher produits par critères
2. Vérifier les stocks
3. Recommander alternatives
4. Calculer prix avec remises"
```
