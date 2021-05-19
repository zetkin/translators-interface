import { Translation } from '../global.types'
import joinTranslations from './joinTranslations'

// English translations
const translations = [
  {
    dotpath: 'h1',
  },
  {
    dotpath: 'h2',
  },
  {
    dotpath: 'h3',
  },
  {
    dotpath: 'h4',
  },
  {
    dotpath: 'h5',
  },
]

describe('joinTranslations()', () => {
  it('Joins matching lists of translations', () => {
    const translationsCopy = [...translations]

    const joinedTranslations = joinTranslations(
      // @ts-ignore
      translations,
      // @ts-ignore
      translationsCopy
    )

    expect(joinedTranslations.length).toEqual(5)

    joinedTranslations.forEach((joinedTranslation) => {
      expect(joinedTranslation.english.dotpath).toEqual(
        joinedTranslation.selected.dotpath
      )
    })
  })

  it('Joins lists of translations with more english translations', () => {
    const longerTranslations = [
      { dotpath: 'homePage.title' },
      { dotpath: 'homePage.subtitle' },
      { dotpath: 'homePage.tooltip' },
      ...translations,
    ]

    const joinedTranslations = joinTranslations(
      // @ts-ignore
      longerTranslations,
      // @ts-ignore
      translations
    )

    console.log(joinedTranslations)

    expect(joinedTranslations.length).toEqual(8)

    joinedTranslations.forEach((joinedTranslation, index) => {
      if (index < 3) expect(joinedTranslation.selected).toBeNull()
      else
        expect(joinedTranslation.english.dotpath).toEqual(
          joinedTranslation.selected.dotpath
        )
    })
  })
})
