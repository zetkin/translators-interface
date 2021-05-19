import { Translation } from '../global.types'

interface JoinedTranslation {
  english: Translation
  selected: Translation
}

export default (
  englishTranslations: Translation[],
  translations: Translation[]
) => {
  let englishIndex = 0
  let joinedTranslations: JoinedTranslation[] = []
  for (let i = 0; i < translations.length, i++; ) {
    const currentTranslation = translations[i]
    // Check if matches
    const matches =
      currentTranslation.dotpath === englishTranslations[englishIndex].dotpath

    if (matches) {
      joinedTranslations = [
        ...joinedTranslations,
        {
          english: englishTranslations[englishIndex],
          selected: currentTranslation,
        },
      ]
      // Increment english index
      englishIndex++
      break
    }

    // While it doesn't match
    let match: boolean
    while (!match) {
      // Create entries with only english
      joinedTranslations = [
        ...joinedTranslations,
        {
          english: englishTranslations[englishIndex],
          selected: null,
        },
      ]

      // Going to the next one
      englishIndex++

      // Until next one will match
      match =
        translations[i + 1].dotpath ===
        englishTranslations[englishIndex].dotpath
    }
  }

  return joinedTranslations
}
