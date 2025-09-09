# 12h00 - 12h30 : Introduction MCP Simplifiée (30min)

### Contenu formation

**MCP = Model Context Protocol** (pas Model-Controller-Prompter)

**Démonstration live du formateur :**
- Exemple : Agent qui lit des APIs externes
- Exemple : Agent qui accède à une base de données
- Q&R : "Quels tools aimeriez-vous pour vos agents ?"

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
