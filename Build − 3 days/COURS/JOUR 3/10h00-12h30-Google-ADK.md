# 10h00 - 12h00 : Google ADK (Agent Development Kit)

## 📚 **Sources et références**

### Documentation officielle Google ADK (2025)

- [Google ADK Documentation](https://ai.google.dev/adk) - Documentation officielle
- [Getting Started with ADK](https://github.com/google/adk) - Guide de démarrage rapide
- [ADK Examples Repository](https://github.com/google/adk-examples) - Exemples de code

---

## **Objectifs de la session**

À l'issue de cette session, vous serez capables de :

- Comprendre l'architecture Google ADK et ses composants
- Configurer un environnement de développement ADK
- Créer un agent simple avec Google ADK
- Intégrer des outils externes via ADK
- Déployer un agent ADK pour le vibe-coding

---

## **10h00-10h20 : Introduction à Google ADK**

### Qu'est-ce que Google ADK ?

**Définition :** Google Agent Development Kit (ADK) est un framework de développement d'agents IA permettant de créer des agents conversationnels personnalisés avec Gemini.

**Analogie pédagogique :**
"Si Claude Code est comme un assistant personnel polyvalent, Google ADK vous permet de créer votre propre assistant spécialisé exactement comme vous le souhaitez."

### Architecture ADK

```
┌─────────────────────────────────────────┐
│         Application / Interface         │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│           Agent ADK                     │
│  ┌─────────────────────────────────┐   │
│  │  Gemini Model (Core)            │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │  Tools & Functions              │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │  Memory & Context               │   │
│  └─────────────────────────────────┘   │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│     External Services & APIs            │
└─────────────────────────────────────────┘
```

### Concepts clés

#### 1. Agents ADK

- **Définition** : Entité IA autonome avec instructions, outils et mémoire
- **Composants** :
  - Instructions système (personnalité, comportement)
  - Outils disponibles (functions, API calls)
  - Gestion de la mémoire (conversation, contexte)
  - Configuration du modèle Gemini

#### 2. Tools (Outils)

- **Function Calling** : Appel de fonctions Python depuis l'agent
- **API Integration** : Connexion à des services externes
- **Custom Tools** : Création d'outils métier spécifiques

#### 3. Memory & Context

- **Session Memory** : Mémoire de conversation temporaire
- **Persistent Memory** : Stockage long terme (base de données)
- **Context Management** : Gestion optimale du contexte

### Pourquoi ADK pour le Vibe Coding ?

**Avantages :**

- 🎯 **Personnalisation totale** : Agent calibré pour vos besoins spécifiques
- 🔧 **Intégration facile** : Connexion directe avec outils et APIs
- 🚀 **Rapidité** : Déploiement rapide d'agents spécialisés
- 💰 **Contrôle des coûts** : Gestion fine des tokens et appels API
- 🔒 **Sécurité** : Contrôle total des données et accès

**Cas d'usage :**

- Agent de code review spécialisé dans votre stack
- Assistant de génération de specs techniques
- Bot d'analyse de conformité code
- Agent de refactoring intelligent
- Assistant de documentation automatique

---

## **10h20-10h45 : Installation et Configuration**

### Prérequis

```bash
# Python 3.10 ou supérieur
python --version

# Compte Google Cloud Platform
# Clé API Gemini
```

### Installation ADK

```bash
# Installation du package ADK
pip install google-adk

# Installation des dépendances
pip install google-generativeai
pip install python-dotenv

# Vérification de l'installation
python -c "import google.adk; print(google.adk.__version__)"
```

### Configuration de l'environnement

**Fichier `.env` :**

```bash
# Clé API Gemini
GOOGLE_API_KEY=your_gemini_api_key_here

# Configuration optionnelle
GEMINI_MODEL=gemini-2.0-flash-exp
TEMPERATURE=0.7
MAX_TOKENS=8192
```

**Configuration Python :**

```python
import os
from dotenv import load_dotenv
from google.adk import Agent

# Chargement des variables d'environnement
load_dotenv()

# Configuration globale
config = {
    'api_key': os.getenv('GOOGLE_API_KEY'),
    'model': os.getenv('GEMINI_MODEL', 'gemini-2.0-flash-exp'),
    'temperature': float(os.getenv('TEMPERATURE', '0.7')),
    'max_tokens': int(os.getenv('MAX_TOKENS', '8192'))
}
```

### Structure de projet recommandée

```
vibe-coding-agent/
├── .env                    # Variables d'environnement
├── requirements.txt        # Dépendances Python
├── agent/
│   ├── __init__.py
│   ├── config.py          # Configuration de l'agent
│   ├── tools.py           # Définition des outils
│   └── prompts.py         # Instructions système
├── tests/
│   └── test_agent.py      # Tests unitaires
└── main.py                # Point d'entrée
```

---

## **10h45-11h15 : Création d'un Agent Simple**

### Exemple 1 : Agent Vibe Coding Basique

**Fichier `agent/prompts.py` :**

```python
VIBE_CODING_INSTRUCTIONS = """
Tu es un assistant expert en Vibe Coding, spécialisé dans la programmation assistée par IA.

Tes responsabilités :
- Aider à rédiger des prompts efficaces pour la génération de code
- Analyser et critiquer la qualité des prompts
- Suggérer des améliorations pour maximiser les résultats
- Guider sur les meilleures pratiques de collaboration IA-humain

Ton approche :
- Pose des questions de clarification si nécessaire
- Fournis des exemples concrets
- Explique ton raisonnement
- Reste concis mais complet

Format de réponse :
1. Analyse de la demande
2. Recommandations
3. Exemple de prompt amélioré (si applicable)
4. Conseils additionnels
"""
```

**Fichier `agent/config.py` :**

```python
import os
from google.adk import Agent
from agent.prompts import VIBE_CODING_INSTRUCTIONS

def create_vibe_coding_agent():
    """Crée et configure l'agent Vibe Coding"""

    agent = Agent(
        name="VibeCodingAssistant",
        model="gemini-2.0-flash-exp",
        instructions=VIBE_CODING_INSTRUCTIONS,
        temperature=0.7,
        api_key=os.getenv('GOOGLE_API_KEY')
    )

    return agent
```

**Fichier `main.py` :**

```python
from agent.config import create_vibe_coding_agent

def main():
    # Initialisation de l'agent
    agent = create_vibe_coding_agent()

    print("🤖 Agent Vibe Coding prêt !")
    print("Tapez 'quit' pour quitter\n")

    # Boucle de conversation
    while True:
        user_input = input("Vous: ")

        if user_input.lower() == 'quit':
            break

        # Envoi de la requête à l'agent
        response = agent.chat(user_input)

        print(f"\nAgent: {response}\n")

if __name__ == "__main__":
    main()
```

### Test de l'agent

```bash
python main.py
```

**Exemple d'interaction :**

```
Vous: Comment écrire un bon prompt pour générer une fonction de tri ?

Agent:
Analyse de la demande :
Vous souhaitez rédiger un prompt efficace pour générer une fonction de tri.

Recommandations :
1. Spécifiez le langage de programmation
2. Précisez le type de données à trier
3. Indiquez les contraintes (performance, mémoire)
4. Mentionnez les cas limites à gérer

Exemple de prompt amélioré :
"Crée une fonction de tri en Python qui :
- Prend en entrée une liste de dictionnaires
- Trie par le champ 'date' en ordre décroissant
- Gère les cas où 'date' est None (placer en fin)
- Optimise pour des listes de 1000+ éléments
- Inclut les tests unitaires pour les cas limites"

Conseils additionnels :
- Ajoutez des exemples d'entrée/sortie attendus
- Spécifiez le style de code souhaité (PEP8, commentaires)
```

---

## **11h15-11h45 : Ajout d'Outils (Tools)**

### Exemple 2 : Agent avec Fonction de Code Review

**Fichier `agent/tools.py` :**

```python
from typing import Dict, List
import ast

def analyze_code_complexity(code: str, language: str = "python") -> Dict:
    """
    Analyse la complexité d'un code source.

    Args:
        code: Code source à analyser
        language: Langage de programmation

    Returns:
        Dictionnaire avec métriques de complexité
    """
    try:
        if language.lower() == "python":
            tree = ast.parse(code)

            # Comptage des éléments
            functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
            classes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]

            # Calcul de métriques
            lines_of_code = len(code.split('\n'))
            num_functions = len(functions)
            num_classes = len(classes)

            # Score de complexité simple
            complexity_score = (num_functions * 2 + num_classes * 3) / max(lines_of_code / 10, 1)

            return {
                "lines_of_code": lines_of_code,
                "num_functions": num_functions,
                "num_classes": num_classes,
                "complexity_score": round(complexity_score, 2),
                "assessment": _get_complexity_assessment(complexity_score)
            }
    except Exception as e:
        return {"error": f"Erreur d'analyse: {str(e)}"}

def _get_complexity_assessment(score: float) -> str:
    """Évalue le niveau de complexité"""
    if score < 1.0:
        return "Simple - Bonne lisibilité"
    elif score < 2.0:
        return "Modéré - Complexité acceptable"
    elif score < 3.0:
        return "Élevé - Envisager refactoring"
    else:
        return "Très élevé - Refactoring recommandé"

def check_code_style(code: str, language: str = "python") -> Dict:
    """
    Vérifie le respect des conventions de style.

    Args:
        code: Code source à vérifier
        language: Langage de programmation

    Returns:
        Dictionnaire avec résultats de vérification
    """
    issues = []

    if language.lower() == "python":
        lines = code.split('\n')

        for i, line in enumerate(lines, 1):
            # Vérification longueur de ligne
            if len(line) > 79:
                issues.append(f"Ligne {i}: Dépasse 79 caractères")

            # Vérification espaces autour opérateurs
            if '=' in line and not ('==' in line or '!=' in line or '<=' in line or '>=' in line):
                if '= ' not in line and ' =' not in line:
                    issues.append(f"Ligne {i}: Manque d'espaces autour de '='")

        return {
            "total_issues": len(issues),
            "issues": issues[:10],  # Limite aux 10 premiers
            "status": "✅ Conforme" if len(issues) == 0 else f"⚠️ {len(issues)} problèmes détectés"
        }

    return {"error": "Langage non supporté"}
```

**Mise à jour `agent/config.py` :**

```python
from google.adk import Agent
from agent.prompts import VIBE_CODING_INSTRUCTIONS
from agent.tools import analyze_code_complexity, check_code_style

def create_code_review_agent():
    """Crée un agent avec outils de code review"""

    agent = Agent(
        name="CodeReviewAgent",
        model="gemini-2.0-flash-exp",
        instructions=VIBE_CODING_INSTRUCTIONS + """

        Outils disponibles :
        - analyze_code_complexity: Analyse la complexité du code
        - check_code_style: Vérifie les conventions de style

        Utilise ces outils pour fournir des reviews complètes et constructives.
        """,
        tools=[analyze_code_complexity, check_code_style],
        temperature=0.3,  # Plus déterministe pour code review
        api_key=os.getenv('GOOGLE_API_KEY')
    )

    return agent
```

### Test avec outils

```python
from agent.config import create_code_review_agent

agent = create_code_review_agent()

code_sample = """
def calculate_total(items):
    total=0
    for item in items:
        if item['price']>0:
            total=total+item['price']*item['quantity']
    return total
"""

response = agent.chat(f"""
Effectue une review de ce code Python :

{code_sample}

Fournis une analyse complète avec recommandations.
""")

print(response)
```

---

## **11h45-12h00 : Exercice Pratique**

### 🎯 Exercice : Créer un Agent Spec Writer

**Objectif :** Développer un agent ADK qui aide à rédiger des spécifications techniques pour le vibe-coding.

**Cahier des charges :**

Créer un agent qui :
1. Prend en entrée une description de fonctionnalité
2. Pose des questions de clarification si nécessaire
3. Génère une spécification structurée avec :
   - Titre et description
   - Critères d'acceptation
   - Contraintes techniques
   - Exemple de prompt pour génération de code
   - Checklist de validation

**Structure attendue :**

```python
# agent/prompts.py
SPEC_WRITER_INSTRUCTIONS = """
Tu es un expert en rédaction de spécifications techniques pour le vibe-coding.
[Compléter les instructions...]
"""

# agent/tools.py
def validate_spec_completeness(spec: Dict) -> Dict:
    """Valide qu'une spec contient tous les champs requis"""
    # Implémenter la validation
    pass

def generate_acceptance_criteria(description: str) -> List[str]:
    """Génère des critères d'acceptation depuis une description"""
    # Implémenter la génération
    pass

# agent/config.py
def create_spec_writer_agent():
    """Crée l'agent Spec Writer"""
    # Implémenter la création
    pass
```

**Livrables attendus :**

1. Code source complet de l'agent
2. Au moins 2 outils fonctionnels
3. Instructions système claires
4. Exemple d'utilisation avec résultat
5. Documentation rapide (README.md)

**Temps alloué :** 45 minutes

**Critères d'évaluation :**

- ✅ Agent fonctionnel et testable
- ✅ Instructions système pertinentes
- ✅ Outils utiles et bien implémentés
- ✅ Gestion des erreurs
- ✅ Qualité du code produit

---

## **Points clés à retenir**

1. **Google ADK** permet de créer des agents IA personnalisés avec Gemini
2. **Architecture en 3 couches** : Instructions + Tools + Memory
3. **Function Calling** permet l'intégration d'outils externes
4. **Vibe Coding** bénéficie d'agents spécialisés (spec, review, refactoring)
5. **Configuration flexible** pour adapter l'agent à différents contextes
6. **Tests et validation** sont essentiels pour agents de production

---

## **Ressources complémentaires**

### Documentation

- [Google ADK Official Docs](https://ai.google.dev/adk)
- [Gemini Function Calling Guide](https://ai.google.dev/docs/function_calling)
- [ADK Best Practices](https://github.com/google/adk/wiki)

### Exemples de projets

- [ADK Examples Repository](https://github.com/google/adk-examples)
- [Community Agents](https://github.com/topics/google-adk)

### Outils connexes

- [LangChain Integration](https://python.langchain.com/docs/integrations/providers/google)
- [Gemini API Cookbook](https://github.com/google-gemini/cookbook)

---

## **Transition vers l'après-midi**

Lors du TP final (14h00-17h00), vous pourrez utiliser un agent ADK comme l'un des agents spécialisés de votre orchestration multi-agents. Par exemple :

- Agent ADK pour la génération de specs
- Agent ADK pour le code review automatique
- Agent ADK pour l'analyse de conformité

L'intégration d'ADK dans votre workflow multi-agents enrichit considérablement les capacités du système global.

---

*Cette session vous a permis de découvrir Google ADK et de créer vos premiers agents personnalisés pour le vibe-coding. Ces compétences seront directement applicables dans vos projets de développement assisté par IA.*
