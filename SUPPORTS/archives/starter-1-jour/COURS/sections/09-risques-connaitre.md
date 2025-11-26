# 9. Risques à Connaître (17h15 - 17h30) *(Optionnel)*

## 🎯 Objectifs de cette tranche
- Sensibiliser aux risques du développement assisté par IA
- Présenter les bonnes pratiques de sécurité et éthique
- Aborder les considérations environnementales
- Établir un cadre d'usage responsable
- Préparer les participants à une adoption professionnelle éclairée

## 📝 Contenu

### Green IT et éco-responsabilité (5 minutes)

#### Impact environnemental de l'IA

**Consommation énergétique :**
- Entraînement des modèles : coût carbone important
- Inférence : impact par requête relativement faible
- Comparaison : 1 requête Claude ≈ 1 recherche Google

**Bonnes pratiques éco-responsables :**
```
✅ Optimiser les prompts pour réduire les tokens
✅ Éviter les requêtes répétitives inutiles
✅ Privilégier les modèles locaux quand possible
✅ Regrouper les questions en une seule requête
❌ Éviter les prompts de test sans valeur ajoutée
❌ Ne pas utiliser l'IA pour des tâches triviales
```

#### Principe de proportionnalité
- **Tâche simple** → Solution simple (pas d'IA)
- **Tâche complexe** → IA justifiée
- **Automatisation** → ROI environnemental positif

### Sécurité du code généré (10 minutes)

#### Vulnérabilités fréquentes dans le code IA

**Injection de code :**
```javascript
// ❌ Code vulnérable souvent généré
eval(userInput);
document.innerHTML = userContent;

// ✅ Alternatives sécurisées à demander
JSON.parse(userInput);
element.textContent = userContent;
```

**Gestion des secrets :**
```javascript
// ❌ Exposition fréquente
const apiKey = "sk-12345...";
localStorage.setItem('password', userPassword);

// ✅ Bonnes pratiques
const apiKey = process.env.API_KEY;
// Utilisation de librairies de hachage sécurisées
```

**Validation insuffisante :**
```javascript
// ❌ L'IA oublie souvent la validation
function processData(data) {
    return data.map(item => item.value);
}

// ✅ Toujours demander la validation
function processData(data) {
    if (!Array.isArray(data)) throw new Error('Invalid data');
    return data.filter(item => item && item.value)
               .map(item => item.value);
}
```

#### Checklist de sécurité

**Avant mise en production :**
- [ ] Audit de sécurité du code généré
- [ ] Tests de pénétration basiques
- [ ] Validation de toutes les entrées utilisateur
- [ ] Chiffrement des données sensibles
- [ ] Gestion appropriée des erreurs (pas d'exposition d'infos)

### Aspects éthiques et juridiques (10 minutes)

#### Propriété intellectuelle

**Droits d'auteur du code généré :**
- Code généré par IA : statut juridique flou
- Responsabilité du développeur qui utilise le code
- Vérification recommandée pour éviter la copie de code propriétaire

**Bonnes pratiques :**
```
✅ Toujours réviser et adapter le code généré
✅ Ajouter ses propres commentaires et modifications
✅ Tester la fonctionnalité avant usage
✅ Documenter l'usage de l'IA dans le projet
❌ Copier-coller sans compréhension
❌ Réutiliser du code sans vérification de licence
```

#### Biais et discrimination

**Biais dans les modèles d'IA :**
- Reproduction de stéréotypes présents dans les données d'entraînement
- Choix technologiques orientés par les biais du modèle
- Importance de la diversité dans les équipes de développement

**Exemples pratiques :**
- Formulaires avec genres binaires uniquement
- Algorithmes de tri/classement biaisés
- Interfaces non accessibles aux handicaps

#### Transparence et responsabilité

**Disclosure de l'usage d'IA :**
```markdown
<!-- Exemple de documentation transparente -->
## Développement assisté par IA

Ce projet a été développé avec l'assistance de Claude/Cursor pour :
- Génération de la structure de base
- Optimisation des algorithmes
- Création des tests unitaires
- Rédaction de la documentation

Le code a été entièrement révisé et testé par l'équipe.
```

## 🎓 Notes formateur

### Adaptation selon le contexte

**Entreprise sensible à la sécurité :**
- Approfondir les aspects de sécurité
- Présenter les outils d'audit automatisé
- Insister sur les processus de validation

**Contexte environnemental :**
- Détailler l'impact carbone
- Présenter les alternatives locales
- Encourager l'optimisation des prompts

**Secteur réglementé :**
- Mentionner RGPD, compliance
- Aborder la traçabilité du code
- Présenter les bonnes pratiques documentaires

### Tonalité de présentation

**Éviter :**
- Le catastrophisme ou la peur
- La culpabilisation excessive
- Les interdictions sans alternatives

**Privilégier :**
- L'information factuelle
- Les solutions pratiques
- La responsabilisation progressive

### Messages clés

1. **"L'IA est un outil puissant qui demande de la responsabilité"**
2. **"La vigilance fait partie des compétences du vibe coding"**
3. **"Transparence et éthique renforcent la confiance"**
4. **"Un développeur responsable = meilleur développeur"**

### Transition vers le bilan

**Si le groupe est réceptif :**
- Encourager les questions et discussions
- Proposer des ressources pour approfondir
- Intégrer ces considérations dans les projets futurs

**Si le temps est serré :**
- Résumer en 3 points essentiels
- Fournir une checklist de sécurité
- Promettre des ressources complémentaires

## ✅ Critères de réussite
- [ ] Les participants connaissent les principaux risques
- [ ] Les bonnes pratiques de sécurité sont comprises
- [ ] La sensibilisation éthique est établie
- [ ] Un cadre d'usage responsable est posé

## 🔧 Ressources pratiques

### Checklist de sécurité rapide

```
🔒 SÉCURITÉ
□ Validation des entrées utilisateur
□ Pas de secrets hardcodés
□ Gestion d'erreurs sécurisée
□ Protection XSS/injection
□ HTTPS en production

🌱 ÉCO-RESPONSABILITÉ
□ Prompts optimisés
□ Pas de requêtes répétitives
□ Usage proportionnel à la tâche
□ Documentation de l'usage IA

⚖️ ÉTHIQUE
□ Code révisé et compris
□ Transparence sur l'usage IA
□ Vérification des biais
□ Respect de la propriété intellectuelle
```

### Ressources pour approfondir

**Sécurité :**
- OWASP Top 10 for AI
- Security checklist for AI-generated code
- Automated security scanning tools

**Green IT :**
- Carbon footprint calculators for AI
- Local AI alternatives
- Energy-efficient coding practices

**Éthique :**
- IEEE Standards for AI Ethics
- Partnership on AI best practices
- Algorithmic bias detection tools

### Prompts pour audit de sécurité

**Audit rapide :**
```
Analyse ce code pour identifier les vulnérabilités de sécurité :
- Injection (SQL, XSS, code)
- Gestion des données sensibles
- Validation des entrées
- Gestion d'erreurs
Fournis des corrections sécurisées.
```

**Vérification RGPD :**
```
Vérifie la conformité RGPD de ce code :
- Collecte de données personnelles
- Consentement utilisateur
- Droit à l'effacement
- Sécurisation des données
Propose les améliorations nécessaires.
```