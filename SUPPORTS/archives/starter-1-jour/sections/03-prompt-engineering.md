# 10h15 - 11h00 : Prompt Engineering Pratique (45min)

## Contenu formation

### Principes fondamentaux pour communiquer avec l'IA

Chaque modèle d'IA possède des instructions par défaut qui définissent son comportement général. Les outils comme Cursor permettent de personnaliser ces instructions à différents niveaux :

- **Rules générales**: Users rules dans la configuration
- **Rules locales**: dans un dossier `.cursor/rules`
- **Utiliser `context7`** pour de meilleurs résultats
- **Le prompt** en tant que tel

### Template de Prompt Efficace

```
## Contexte
[Décris le projet et l'objectif]

## Rôle  
Tu es un [expertise] expert en [technologie]...

## Tâche
[Action précise à réaliser]

## Contraintes
- Technologies : [liste précise]
- Standards : [conventions de code] 
- Tests : [requis/optionnel]

## Format attendu
- Code commenté
- Gestion d'erreurs
- [Autres spécifications]

## Exemples
Input: [exemple d'entrée]
Output: [exemple de sortie attendue]
```

### Exercice Collectif : Amélioration de Prompts (15 minutes)

**Prompt à améliorer :**
❌ "Fais une calculatrice web"

**Version améliorée attendue :**

✅ **Contexte :** Calculatrice web professionnelle pour comptables
**Rôle :** Tu es un développeur front-end expert en JavaScript vanilla
**Tâche :** Développe une calculatrice avec :
- Opérations de base (+, -, *, /)
- Historique des 10 derniers calculs
- Gestion des décimales (2 chiffres après virgule)
- Raccourcis clavier
- Design responsive

**Contraintes :**
- HTML5/CSS3/JS vanilla (pas de framework)
- Compatible IE11+
- Accessible (ARIA labels)
- Stockage local pour l'historique

**Format :** Code modulaire, commenté, avec tests unitaires simples

## 📝 Notes formateur

### 10h15-10h30 : Les niveaux de prompt (15min)

**Concept à expliquer clairement :**
L'IA a plusieurs "couches" d'instructions :
1. **Instructions système** (invisibles)
2. **Rules globales** (votre configuration)
3. **Rules locales** (.cursor/rules)
4. **Le prompt** (votre demande)

**Démonstration pratique :**
- Ouvrir Cursor et montrer les User Rules
- Créer un `.cursor/rules` avec des règles simples
- Montrer la différence avec/sans rules

**Points d'attention formateur :**
- Insistez sur la hiérarchie : système > global > local > prompt
- Expliquez que les rules économisent du temps sur le long terme

### 10h30-10h45 : Template de Prompt Efficace (15min)

**Méthode pédagogique :**
- Montrez d'abord un prompt "mauvais"
- Appliquez le template étape par étape
- Montrez le résultat amélioré

### 10h45-11h00 : Exercice Collectif d'amélioration (15min)

**Animation suggérée :**

**Prompt de base :** "Fais une calculatrice web"

**Étapes de l'exercice :**
1. **Collecte des problèmes** (3min) : "Que manque-t-il ?"
2. **Amélioration collaborative** (7min) : Construire le prompt ensemble au tableau
3. **Version finale** (3min) : Montrer le résultat attendu
4. **Débrief** (2min) : "Combien de temps ça vous aurait pris avant/après ?"

**Résultat attendu (à préparer) :**
```
## Contexte
Calculatrice web professionnelle pour comptables

## Rôle  
Tu es un développeur front-end expert en JavaScript vanilla

## Tâche
Développe une calculatrice avec :
- Opérations de base (+, -, *, /)
- Historique des 10 derniers calculs
- Gestion des décimales (2 chiffres après virgule)
- Raccourcis clavier
- Design responsive

## Contraintes
- HTML5/CSS3/JS vanilla (pas de framework)
- Compatible IE11+
- Accessible (ARIA labels)
- Stockage local pour l'historique

## Format
Code modulaire, commenté, avec tests unitaires simples
```

**Note formateur :** Cet exercice est crucial. Prenez le temps, même si ça déborde légèrement.