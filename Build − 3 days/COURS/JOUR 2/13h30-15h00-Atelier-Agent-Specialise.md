# TP Configuration Serveurs MCP

## Context 7 et intégration GitLab

### Objectifs pédagogiques

À l'issue de ce TP, vous serez capable de :

- Configurer un serveur MCP Context 7
- Intégrer un serveur MCP GitLab
- Utiliser les serveurs MCP dans un environnement de développement
- Déboguer et optimiser la configuration MCP

---

## Partie 1 : Configuration du serveur MCP Context 7

### Étape 1 : Installation

```bash
# Créer le répertoire de travail
mkdir mcp-workshop && cd mcp-workshop

# Initialiser le projet
npm init -y

# Installer les dépendances MCP
npm install @modelcontextprotocol/sdk-server
npm install @modelcontextprotocol/context7-server
```

### Étape 2 : Configuration Context 7

Créez le fichier `mcp-config.json` :

```json
{
  "mcpServers": {
    "context7": {
      "command": "node",
      "args": [
        "./node_modules/@modelcontextprotocol/context7-server/dist/index.js"
      ],
      "env": {
        "CONTEXT7_ROOT_PATH": "./workspace",
        "CONTEXT7_MAX_DEPTH": "5",
        "CONTEXT7_INCLUDE_PATTERNS": "*.js,*.ts,*.json,*.md,*.py",
        "CONTEXT7_EXCLUDE_PATTERNS": "node_modules,*.log,.git"
      }
    }
  }
}
```

### Étape 3 : Création de l'espace de travail

```bash
mkdir workspace
cd workspace

# Créer une structure de projet exemple
mkdir -p src/{components,utils,services}
mkdir -p docs tests

# Créer des fichiers exemples
echo "# Mon Projet MCP" > README.md
echo "console.log('Hello MCP');" > src/index.js
echo '{"name": "mcp-demo", "version": "1.0.0"}' > package.json
```

### Exercice guidé 1 : Test Context 7

1. **Démarrer le serveur Context 7**

   ```bash
   # Dans un terminal
   npx @modelcontextprotocol/context7-server
   ```
2. **Vérifier la connexion**

   - Le serveur doit afficher les ressources détectées
   - Vérifiez que les fichiers de votre workspace sont indexés
3. **Questions de contrôle :**

   - Combien de fichiers ont été indexés ?
   - Quels types de fichiers sont exclus par défaut ?
   - Comment modifier la profondeur de scan ?

---

## Partie 2 : Configuration du serveur MCP GitLab

### Étape 1 : Installation du serveur GitLab

```bash
npm install @modelcontextprotocol/gitlab-server
```

### Étape 2 : Génération du token GitLab

1. Connectez-vous à GitLab
2. Allez dans **Settings > Access Tokens**
3. Créez un token avec les scopes :
   - `read_api`
   - `read_repository`
   - `read_user`

### Étape 3 : Configuration du serveur GitLab

Ajoutez dans `mcp-config.json` :

```json
{
  "mcpServers": {
    "context7": {
      // ... configuration précédente
    },
    "gitlab": {
      "command": "node",
      "args": [
        "./node_modules/@modelcontextprotocol/gitlab-server/dist/index.js"
      ],
      "env": {
        "GITLAB_TOKEN": "votre-token-ici",
        "GITLAB_URL": "https://gitlab.com",
        "GITLAB_DEFAULT_PROJECT": "votre-username/votre-projet"
      }
    }
  }
}
```

### Étape 4 : Sécurisation des credentials

Créez un fichier `.env` :

```bash
GITLAB_TOKEN=glpat-xxxxxxxxxxxxxxxxxxxx
GITLAB_URL=https://gitlab.com
GITLAB_DEFAULT_PROJECT=username/project-name
```

Modifiez la configuration pour utiliser les variables d'environnement :

```json
"env": {
  "GITLAB_TOKEN": "${GITLAB_TOKEN}",
  "GITLAB_URL": "${GITLAB_URL}",
  "GITLAB_DEFAULT_PROJECT": "${GITLAB_DEFAULT_PROJECT}"
}
```

### Exercice guidé 2 : Intégration GitLab

1. **Créer un projet GitLab de test**

   ```bash
   # Cloner ou créer un nouveau repository
   git clone https://gitlab.com/votre-username/votre-projet.git
   cd votre-projet

   # Créer quelques fichiers si nécessaire
   echo "# Projet MCP GitLab" > README.md
   mkdir src && echo "console.log('GitLab MCP');" > src/app.js
   git add . && git commit -m "Initial commit" && git push
   ```
2. **Tester la connexion GitLab MCP**

   ```bash
   # Démarrer le serveur GitLab
   npx @modelcontextprotocol/gitlab-server
   ```
3. **Vérifications :**

   - Le serveur accède-t-il à votre projet GitLab ?
   - Peut-il lister les branches et commits ?
   - Les issues sont-elles accessibles ?

---

## Partie 3 : Utilisation pratique des serveurs MCP

### Exercice guidé 3 : Workflow complet

Vous allez créer un workflow qui utilise les deux serveurs MCP pour analyser et améliorer un projet.

#### Scenario : Analyse de projet avec Context 7 et GitLab

1. **Préparation du projet**

   ```bash
   # Dans votre workspace
   mkdir mon-app && cd mon-app

   # Créer une structure complexe
   mkdir -p src/{api,frontend,shared} tests docs

   # Fichiers avec différents niveaux de qualité
   cat > src/api/users.js << 'EOF'
   // TODO: Améliorer la gestion d'erreurs
   function getUser(id) {
     return fetch(`/api/users/${id}`)
       .then(response => response.json())
       .catch(err => console.log(err))
   }
   EOF

   cat > src/frontend/app.js << 'EOF'
   // Composant principal - manque documentation
   class App {
     constructor() {
       this.users = []
     }

     async loadUsers() {
       // Code à optimiser
       for(let i = 0; i < 100; i++) {
         const user = await getUser(i)
         this.users.push(user)
       }
     }
   }
   EOF
   ```
2. **Analyse avec Context 7**

   - Lancez Context 7 sur ce workspace
   - Identifiez les patterns de code
   - Analysez la structure du projet
3. **Synchronisation avec GitLab**

   ```bash
   # Pousser le projet vers GitLab
   git init
   git add .
   git commit -m "Projet initial pour analyse MCP"
   git remote add origin https://gitlab.com/votre-username/mon-app.git
   git push -u origin main
   ```
4. **Utilisation combinée des serveurs**

   - Context 7 : Analyse locale du code et suggestions
   - GitLab MCP : Récupération de l'historique et des issues
   - Création de rapports d'amélioration

#### Questions d'analyse :

1. Quels problèmes Context 7 identifie-t-il dans le code ?
2. Comment GitLab MCP peut-il compléter cette analyse ?
3. Quelles améliorations proposeriez-vous ?

---

## Partie 4 : Configuration avancée et optimisation

### Configuration multi-environnement

Créez des configurations pour différents environnements :

```json
{
  "development": {
    "mcpServers": {
      "context7": {
        "env": {
          "CONTEXT7_MAX_DEPTH": "10",
          "CONTEXT7_INCLUDE_PATTERNS": "*"
        }
      }
    }
  },
  "production": {
    "mcpServers": {
      "context7": {
        "env": {
          "CONTEXT7_MAX_DEPTH": "3",
          "CONTEXT7_EXCLUDE_PATTERNS": "*.test.*,*.spec.*"
        }
      }
    }
  }
}
```

### Monitoring et logs

Ajoutez la configuration de monitoring :

```json
{
  "logging": {
    "level": "info",
    "file": "./logs/mcp.log"
  },
  "monitoring": {
    "enabled": true,
    "metrics_port": 9090
  }
}
```

### Exercice guidé 4 : Optimisation des performances

1. **Mesurer les performances**

   - Temps de démarrage des serveurs
   - Temps de réponse aux requêtes
   - Utilisation mémoire
2. **Optimiser la configuration**

   - Ajuster les patterns d'inclusion/exclusion
   - Configurer le cache
   - Limiter la profondeur de scan
3. **Tests de charge**

   - Simuler de multiples requêtes
   - Monitorer les ressources système

---

## Exercice final

### Mini-projet : Tableau de bord MCP

Créez un petit dashboard qui :

1. Affiche le statut des serveurs MCP
2. Montre les statistiques d'utilisation
3. Permet de configurer les paramètres de base

### Critères d'évaluation :

- [ ] Context 7 configuré et fonctionnel
- [ ] GitLab MCP connecté avec authentification
- [ ] Workflow de développement intégrant les deux serveurs
- [ ] Configuration optimisée pour votre cas d'usage
- [ ] Documentation des choix techniques

### Livrables :

1. Configuration MCP complète
2. Script de déploiement automatisé
3. Documentation utilisateur
4. Rapport d'analyse de performance

---

## Ressources complémentaires

### Documentation officielle

- [MCP Specification](https://modelcontextprotocol.io/specification/)
- [Context 7 Server](https://github.com/modelcontextprotocol/context7-server)
- [GitLab MCP Server](https://github.com/modelcontextprotocol/gitlab-mcp-server)
