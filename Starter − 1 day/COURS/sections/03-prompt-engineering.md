# 3. Prompt Engineering Pratique (10h15 - 11h00)

## 🎯 Objectifs de cette tranche
- Maîtriser les principes fondamentaux du prompt engineering
- Appliquer le template de prompt universel
- Transformer un prompt inefficace en prompt performant
- Expérimenter collectivement l'amélioration de prompts

## 📝 Contenu

### Principes fondamentaux du prompt engineering (15 minutes)

#### Les 6 piliers d'un prompt efficace

**1. CONTEXTE** - Situer le projet
```
❌ Mauvais : "Crée une API"
✅ Bon : "Je développe une application de gestion de bibliothèque universitaire"
```

**2. RÔLE** - Définir l'expertise
```
❌ Mauvais : "Tu es un développeur"
✅ Bon : "Tu es un architecte backend spécialisé en Node.js et MongoDB"
```

**3. TÂCHE** - Action précise
```
❌ Mauvais : "Aide-moi avec l'authentification"
✅ Bon : "Crée un système d'authentification JWT avec middleware Express"
```

**4. CONTRAINTES** - Technologies et standards
```
❌ Mauvais : (pas de contraintes)
✅ Bon : "Utilise Express.js, bcrypt pour le hashing, respect du RGPD"
```

**5. FORMAT** - Structure de sortie
```
❌ Mauvais : (format libre)
✅ Bon : "Fournis le code avec tests unitaires et documentation API"
```

**6. EXEMPLES** - Cas concrets
```
❌ Mauvais : (pas d'exemples)
✅ Bon : "Comme un système login/logout similaire à celui de GitHub"
```

### Template de prompt universel (15 minutes)

#### Structure recommandée

```markdown
**CONTEXTE :**
[Description du projet, environnement technique, objectifs]

**RÔLE :**
Tu es [expertise spécifique] spécialisé en [technologies/domaine]

**TÂCHE :**
[Action précise à réaliser]

**CONTRAINTES :**
- Technologies : [stack technique]
- Standards : [conventions, bonnes pratiques]
- Performance : [exigences spécifiques]
- Sécurité : [considérations]

**FORMAT :**
- [Structure du code attendu]
- [Documentation nécessaire]
- [Tests requis]

**EXEMPLES :**
[Références ou cas similaires]
```

#### Exemple concret appliqué

**Prompt inefficace :**
> "Crée-moi un site web de e-commerce"

**Prompt optimisé avec le template :**

```markdown
**CONTEXTE :**
Je développe une boutique en ligne pour vendre des produits artisanaux locaux.
L'audience cible est constituée de particuliers soucieux de consommer local.
Budget limité, besoin d'une solution simple et efficace.

**RÔLE :**
Tu es un développeur full-stack expert en solutions e-commerce,
spécialisé dans les applications web performantes et accessibles.

**TÂCHE :**
Crée la structure complète d'un site e-commerce avec catalogue produits,
panier d'achat et système de commande simple.

**CONTRAINTES :**
- Technologies : HTML5, CSS3, JavaScript vanilla (pas de framework lourd)
- Responsive design obligatoire
- Accessibilité WCAG 2.1 niveau AA
- Chargement < 3 secondes
- Compatible IE11+

**FORMAT :**
- Code organisé en fichiers séparés (HTML/CSS/JS)
- Commentaires explicatifs dans le code
- Documentation README pour l'installation
- Exemples de données de test

**EXEMPLES :**
Interface inspirée de Etsy mais plus simple, avec un panier comme Amazon
mais sans système de paiement complexe.
```

### Exercice collectif d'amélioration (15 minutes)

#### Prompt de départ (volontairement inefficace)

> "Aide-moi à faire une app mobile pour gérer mes finances"

#### Étapes de l'exercice

**Étape 1 : Identification des problèmes (5 min)**
- Les participants identifient ce qui manque
- Noter les réponses au tableau

**Étape 2 : Construction collective (7 min)**
- Appliquer le template ensemble
- Chaque participant propose un élément

**Étape 3 : Test et résultat (3 min)**
- Soumission du prompt amélioré à l'IA
- Comparaison avec le résultat du prompt initial

#### Résultat attendu de l'exercice

```markdown
**CONTEXTE :**
Application mobile de gestion financière personnelle pour jeunes actifs (25-35 ans)
qui veulent suivre leurs dépenses et économiser pour des projets spécifiques.

**RÔLE :**
Tu es un développeur mobile senior spécialisé en React Native et en UX/UI
pour applications financières.

**TÂCHE :**
Crée une application mobile complète de gestion de budget personnel avec
tracking des dépenses, catégorisation automatique et objectifs d'épargne.

**CONTRAINTES :**
- React Native (iOS + Android)
- Stockage local (AsyncStorage)
- Design Material Design / iOS HIG
- Accessible et sécurisé (pas de données cloud)
- Performance 60fps

**FORMAT :**
- Architecture modulaire avec composants réutilisables
- Navigation stack claire
- Tests unitaires pour la logique métier
- Documentation des composants

**EXEMPLES :**
UX similaire à Mint mais plus simple, tracking comme Bankin mais sans
connexion bancaire, objectifs comme YNAB.
```

## 🎓 Notes formateur

### Préparation
- **Exemples variés** : Préparer 3-4 domaines différents (web, mobile, API, data)
- **Tableau/écran** : Pour noter les améliorations collectives
- **Timing strict** : Chronomètre chaque partie pour respecter les 45 minutes

### Animation de l'exercice collectif
- **Participation active** : Faire parler tous les participants
- **Bienveillance** : Toutes les suggestions sont bonnes
- **Guidage** : Orienter sans imposer les réponses

### Points clés à insister
1. **"Un bon prompt = un bon brief client"**
2. **"Plus de contexte = meilleur résultat"**
3. **"L'IA ne devine pas, elle interprète"**

### Erreurs fréquentes à corriger
- **Prompts trop vagues** : "Crée une app"
- **Pas de contraintes** : L'IA choisit arbitrairement
- **Oubli du rôle** : Résultat générique au lieu de spécialisé
- **Pas d'exemples** : L'IA ne comprend pas le style attendu

### Transition vers le module suivant
"Maintenant que vous maîtrisez l'art du prompt, nous allons développer ensemble un projet réel. Vous allez voir votre nouveau superpouvoir en action !"

## ✅ Critères de réussite
- [ ] Les 6 piliers sont compris et mémorisés
- [ ] Le template est appliqué correctement
- [ ] L'exercice collectif montre une amélioration notable
- [ ] Les participants se sentent confiants pour prompter

## 🔧 Ressources pratiques

### Checklist de relecture de prompt
```
□ Contexte suffisamment détaillé ?
□ Rôle spécialisé défini ?
□ Tâche actionnable et précise ?
□ Contraintes techniques listées ?
□ Format de sortie spécifié ?
□ Exemples pertinents fournis ?
```

### Exemples de prompts transformés

**Domain: API REST**
```
Avant: "Crée une API"
Après: "Tu es un architecte backend. Crée une API REST Node.js/Express
pour un système de réservation d'hôtel avec endpoints CRUD,
middleware d'auth JWT, validation Joi, et documentation Swagger."
```

**Domain: Interface utilisateur**
```
Avant: "Design d'interface"
Après: "Tu es un UX/UI designer. Crée l'interface d'un dashboard
analytics en HTML/CSS avec design system Material, accessibilité
WCAG, responsive mobile-first, et animations CSS subtiles."
```