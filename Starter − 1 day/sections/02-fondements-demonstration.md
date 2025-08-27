# 9h30 - 10h15 : Fondements et Démonstration Live (45min)

## Contenu formation

### 9h30-9h45 : Démonstration "Frimer" (15min)

Démonstration en direct d'une création rapide d'application en utilisant le vibe coding. Nous allons générer un environnement containerisé pour notre codelab directement avec l'IA. Nous examinerons également des exemples concrets de projets développés lors des sessions précédentes pour illustrer l'efficacité de cette approche.

- vibe-coder le codelab de la journée (générer un container)
- présenter les sites des sessions précédentes

### 9h45-10h00 : Framework des 5 Compétences Clés (15min)

1. **Thinking** : Décomposer le problème avant de prompter
   - "Que veux-je exactement ?"
   - "Quelles sont les contraintes ?"

2. **Frameworks** : Utiliser des structures éprouvées
   - Templates de prompt
   - Patterns architecturaux connus

3. **Checkpoints** : Valider à chaque étape
   - Tests à chaque fonctionnalité
   - Commits réguliers

4. **Debugging** : Dialoguer avec l'IA pour corriger
   - Copier-coller les erreurs dans le prompt
   - Demander des explications étape par étape

5. **Context** : Fournir le bon niveau de détail
   - Ni trop vague, ni trop prescriptif
   - Exemples concrets et contre-exemples

> Inspiré des meilleures pratiques industrielles 2025

### 10h00-10h15 : Comment fonctionne l'IA pour le code et le vibe coding (15min)

Concept popularisé début 2025 par Andrej Karpathy (co-fondateur d'OpenAI)

Technique de programmation assisté par des LLMs et basé sur du prompt. Il se différencie d'un outil de complétion basé sur les LLMs comme Copilot par l'importance cruciale du prompt dans le processus de développement.

Le vibe-coding peut être utilisé comme un outil low/no-code. Ceci dit, la pratique des derniers mois démontre que comme tous les outils low/no-code, un non-informaticien va produire des logiciels de mauvaise qualité de cette façon (failles de sécurités, bugs…). Cette pratique est à réserver pour les POC ou le prototypage.

Entre les mains d'un développeur compétent, les outils de vibe-coding entraînent une hausse de la productivité et de l'efficacité. Mais également une transformation du métier.

#### Les LLM : comprendre les fondements

Les Large Language Models (LLM) sont des modèles d'intelligence artificielle entraînés sur d'immenses corpus de textes et de code pour prédire la suite la plus probable d'une séquence donnée.

**L'apprentissage d'un LLM :**
1. **Pré-entraînement**: le modèle est exposé à d'énormes quantités de texte et code
2. **Fine-tuning**: le modèle est affiné sur des tâches spécifiques
3. **RLHF**: les réponses sont évaluées par des humains

**Le processus de génération de code :**
1. **Tokenisation**: votre prompt est découpé en tokens
2. **Contextualisation**: le modèle analyse le prompt dans son contexte
3. **Prédiction auto-régressive**: le modèle génère un token après l'autre
4. **Échantillonnage**: introduction d'une randomisation contrôlée

**Les limites :**
- **"hallucination"** de fonctionnalités inexistantes
- Incapacité à exécuter le code généré
- Connaissance limitée aux données d'entraînement
- Difficultés avec des problèmes très spécifiques

## 📝 Notes formateur

### 9h30-9h45 : Démonstration "Frimer" (15min)

**Objectif pédagogique :** Créer l'envie et lever les appréhensions initiales

**Script de démo suggéré :**
1. **"Je vais créer notre environnement de TP en live"** (5min)
   ```
   Prompt suggéré : "Crée un environnement Docker containerisé pour un CodeLab de formation Vibe Coding avec :
   - Un serveur web simple
   - Un éditeur de code accessible via navigateur
   - Des exemples de projets pré-configurés
   - Script de déploiement automatique"
   ```

2. **Montrer les sites des sessions précédentes** (5min)
   - Préparez 2-3 exemples concrets de projets réalisés
   - Mettez l'accent sur la diversité des projets possibles
   - Montrez le code généré et soulignez la qualité

3. **Débrief interactif** (5min)
   - "Qu'est-ce qui vous surprend ?"
   - "Quelles questions cela soulève ?"

**Points d'attention formateur :**
- Si la démo échoue, transformez l'échec en apprentissage ("Voilà pourquoi nous avons besoin de maîtriser les prompts")
- Gardez un ton enthousiaste mais réaliste
- Préparez des captures d'écran de backup au cas où

### 9h45-10h00 : Framework des 5 Compétences Clés (15min)

**Méthode pédagogique :** Utilisez des exemples concrets pour chaque compétence

**1. Thinking - Décomposer avant de prompter**
```
Exemple pratique à donner :
❌ "Fais-moi une app de todo"
✅ "Je veux une app de todo web qui :
   - Permet d'ajouter/supprimer des tâches
   - Persiste les données localement
   - A une interface responsive"
```

**Points d'insistance :**
- "L'IA n'est pas magique, elle a besoin de clarté"
- "Plus vous êtes précis, moins vous aurez d'aller-retours"

**2. Frameworks - Utiliser des structures éprouvées**
- Montrez le template de prompt (slide suivante)
- Expliquez que c'est comme les design patterns en programmation

**3. Checkpoints - Valider à chaque étape**
```
Workflow type :
git commit → test → prompt suivant → test → commit
```

**4. Debugging - Dialoguer avec l'IA**
- Montrez un exemple de copier-coller d'erreur dans le prompt
- Insistez : "L'IA est votre binôme de debugging"

**5. Context - Le bon niveau de détail**
- Trop vague → résultats imprévisibles
- Trop prescriptif → perte de l'optimisation IA

**Note pour formateur :** Ces 5 compétences sont le cœur de la formation. Y revenir régulièrement.

### 10h00-10h15 : Comment fonctionne l'IA pour le code (15min)

**Objectif :** Démystifier l'IA sans rentrer dans les détails techniques complexes

**Structure suggérée :**

**Introduction historique** (3min)
- Karpathy 2025 comme référence
- Différence fondamentale avec l'autocomplétion classique

**Les LLM expliqués simplement** (7min)
- "Imaginez un développeur qui a lu tout GitHub et Stack Overflow"
- Analogie avec l'expérience humaine : patterns reconnus vs créativité
- Les 3 phases d'entraînement expliquées simplement

**Processus de génération** (3min)
- Token par token : "Comme vous qui réfléchissez mot après mot"
- L'importance de la probabilité et de la température
- Pourquoi ça peut "halluciner"

**Messages clés à faire passer :**
- L'IA propose, le développeur décide
- Elle mémorise des patterns, elle ne comprend pas vraiment
- D'où l'importance de la validation humaine

**Transitions vers la pratique** (2min)
- "Maintenant qu'on sait comment ça marche, apprenons à bien l'utiliser"