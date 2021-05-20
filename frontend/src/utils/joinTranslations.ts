import { Translation } from '../global.types'

export interface JoinedTranslation {
  english: Translation
  selected: Translation
}

export default (
  englishTranslations: Translation[],
  selectedTranslations: Translation[]
) => {
  const joinedTranslations = englishTranslations.map((englishTranslation) => {
    // For every english translation, look for matching one
    const matchingTranslation = selectedTranslations.find(
      (selectedTranslation) =>
        selectedTranslation.dotpath === englishTranslation.dotpath
    )

    return {
      english: englishTranslation,
      selected: matchingTranslation ?? null,
    }
  })

  return joinedTranslations
}
