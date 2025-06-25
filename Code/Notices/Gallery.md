## Bugs introduits :

### Bug CSS (lignes 69-72) :

`css.gallery-item:hover {
    /* ... */
    z-index: 9999; /* ⚠️ BUG: z-index trop élevé */
}`

### Bug JavaScript (ligne 107) :

javascript// BUG: condition inversée - devrait être === 0
`if (imagesToShow.length > 0) {`

### 🎯 Comment ces bugs interagissent :

- Le bug CSS : Le z-index: 9999 sur les items en hover les place au-dessus de la modal (z-index: 1000), créant des problèmes visuels
- Le bug JS : La condition inversée fait que la galerie ne s'affiche que quand il n'y a PAS d'images à montrer
Combinés, ces bugs créent une expérience frustrante où la galerie semble vide et les interactions sont perturbées

## 📚 Objectifs pédagogiques :

- Comprendre l'importance du z-index en CSS
- Déboguer la logique conditionnelle en JavaScript
- Analyser l'interaction entre CSS et JS
- Utiliser les outils de développement du navigateur
- Apprendre à tester systématiquement les fonctionnalités

## 🔧 Solutions :

* CSS : Réduire le z-index à une valeur raisonnable (ex: z-index: 10)
* JS : Corriger la condition en if (imagesToShow.length === 0)